#!/usr/bin/env python3
"""Organize individual skill folders into themes.

Three modes:
  --propose   Use Gemini to group skills into themes → writes themes_proposed.json
  --approve   CLI diff walkthrough to accept/reject/reassign proposed changes
  --assign    Manually assign a skill to a theme (--assign <skill> <theme>)

Usage:
    python scripts/organize_themes.py --propose
    python scripts/organize_themes.py --approve
    python scripts/organize_themes.py --assign keyword_research seo
    python scripts/organize_themes.py --list     # show current themes
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

_REPO_ROOT = Path(__file__).parent.parent
_SKILLS_DIR = _REPO_ROOT / "skills_library"
_THEMES_JSON = _SKILLS_DIR / "themes.json"
_PROPOSED_JSON = _SKILLS_DIR / "themes_proposed.json"


def _to_snake(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")


# ── Skill discovery ────────────────────────────────────────────────────────────

def get_all_skills() -> dict[str, dict]:
    """Return {folder_name: meta_dict} for all individual skill folders."""
    skills: dict[str, dict] = {}
    for d in sorted(_SKILLS_DIR.iterdir()):
        if not d.is_dir() or not (d / "main.py").exists():
            continue
        meta_path = d / "skill_meta.json"
        if meta_path.exists():
            try:
                meta = json.loads(meta_path.read_text())
                skills[d.name] = meta
                continue
            except Exception:
                pass
        # Fallback: read description from main.py docstring
        source = (d / "main.py").read_text(errors="replace")
        lines = source.splitlines()
        desc = ""
        if lines and lines[0].startswith('"""'):
            for line in lines[1:]:
                if line.strip().startswith('"""') or line.strip() == "":
                    break
                desc = line.strip()
                break
        skills[d.name] = {"display_name": d.name.replace("_", " ").title(), "description": desc}
    return skills


def load_themes() -> dict:
    """Load themes.json, or return empty structure if not present."""
    if not _THEMES_JSON.exists():
        return {"_unthemed": {"name": "Uncategorized", "description": "", "skills": []}}
    return json.loads(_THEMES_JSON.read_text())


def save_themes(themes: dict) -> None:
    _THEMES_JSON.write_text(json.dumps(themes, indent=2) + "\n")


def update_skill_meta_theme(skill_name: str, theme_slug: str) -> None:
    """Update the theme field in a skill's skill_meta.json."""
    meta_path = _SKILLS_DIR / skill_name / "skill_meta.json"
    if meta_path.exists():
        try:
            meta = json.loads(meta_path.read_text())
            meta["theme"] = theme_slug
            meta_path.write_text(json.dumps(meta, indent=2) + "\n")
        except Exception:
            pass
    else:
        meta_path.write_text(json.dumps({"theme": theme_slug}, indent=2) + "\n")


# ── Propose mode ───────────────────────────────────────────────────────────────

_PROPOSE_PROMPT = """\
You are organizing a library of AI skills into themes for a SaaS product.

Below is a list of skill folder names and their descriptions.
Group them into 5-15 meaningful themes (e.g. "Amazon Selling", "SEO & Search", "Marketing").

Rules:
- Every skill must belong to exactly one theme.
- Theme slugs must be lowercase snake_case (e.g. "amazon", "seo", "content_creation").
- Use an existing theme name where it clearly fits.
- Create a new theme only when no existing one fits.
- Output ONLY valid JSON — no markdown fences, no commentary.

Existing themes (reuse slugs where possible):
{existing_themes}

Skills to organize:
{skills_list}

Output format (JSON only):
{{
  "theme_slug": {{
    "name": "Human-readable Theme Name",
    "description": "One sentence description.",
    "skills": ["skill_folder_name", ...]
  }},
  ...
}}
"""


def propose(interactive: bool = True) -> None:
    """Call Gemini to propose a new themes grouping."""
    try:
        import google.generativeai as genai
    except ImportError:
        print("[propose] google-generativeai not installed. Run: pip install google-generativeai", file=sys.stderr)
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("[propose] GEMINI_API_KEY is not set.", file=sys.stderr)
        sys.exit(1)

    genai.configure(api_key=api_key)

    skills = get_all_skills()
    current_themes = load_themes()

    existing_themes_text = "\n".join(
        f"  {slug}: {info.get('name', slug)}"
        for slug, info in current_themes.items()
        if slug != "_unthemed"
    )

    skills_list_text = "\n".join(
        f"  {name}: {meta.get('description', 'No description')[:100]}"
        for name, meta in skills.items()
    )

    prompt = _PROPOSE_PROMPT.format(
        existing_themes=existing_themes_text or "  (none yet)",
        skills_list=skills_list_text,
    )

    print(f"Calling Gemini Flash to propose themes for {len(skills)} skills...")
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    raw = response.text.strip()

    # Strip accidental markdown fences
    raw = re.sub(r"^```(?:json)?\n?", "", raw)
    raw = re.sub(r"\n?```$", "", raw)

    try:
        proposed = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"[propose] Could not parse Gemini response as JSON: {e}", file=sys.stderr)
        print("Raw response:", raw[:500], file=sys.stderr)
        sys.exit(1)

    # Validate: every skill should appear exactly once
    all_assigned: list[str] = [s for t in proposed.values() for s in t.get("skills", [])]
    missing = set(skills.keys()) - set(all_assigned)
    if missing:
        proposed.setdefault("_unthemed", {"name": "Uncategorized", "description": "", "skills": []})
        proposed["_unthemed"]["skills"].extend(sorted(missing))

    _PROPOSED_JSON.write_text(json.dumps(proposed, indent=2) + "\n")
    print(f"\n✓ Proposal written to {_PROPOSED_JSON.relative_to(_REPO_ROOT)}")
    print(f"  {len(proposed)} theme(s), {len(all_assigned)} skill(s) assigned")

    if interactive:
        answer = input("\nRun --approve now to review? [Y/n] ").strip().lower()
        if answer in ("", "y", "yes"):
            approve()


# ── Approve mode ───────────────────────────────────────────────────────────────

def _show_diff(current: dict, proposed: dict) -> None:
    """Print a compact diff between current and proposed themes."""
    current_map: dict[str, str] = {}
    for slug, info in current.items():
        for s in info.get("skills", []):
            current_map[s] = slug

    proposed_map: dict[str, str] = {}
    for slug, info in proposed.items():
        for s in info.get("skills", []):
            proposed_map[s] = slug

    moves = [(s, current_map.get(s, "(new)"), proposed_map[s]) for s in proposed_map if current_map.get(s) != proposed_map[s]]
    new_skills = [s for s in proposed_map if s not in current_map]
    removed = [s for s in current_map if s not in proposed_map]

    if not moves and not removed:
        print("  No changes between current and proposed themes.")
        return

    if moves:
        print(f"\n  {len(moves)} skill(s) would move:")
        for skill, old_t, new_t in sorted(moves):
            marker = "[NEW]" if skill in new_skills else "     "
            print(f"  {marker} {skill}: {old_t} → {new_t}")
    if removed:
        print(f"\n  {len(removed)} skill(s) removed from proposed (will keep in current):")
        for s in removed:
            print(f"       {s}")


def approve() -> None:
    """Interactive CLI to review and approve the proposed themes."""
    if not _PROPOSED_JSON.exists():
        print("[approve] No proposal found. Run --propose first.", file=sys.stderr)
        sys.exit(1)

    proposed: dict = json.loads(_PROPOSED_JSON.read_text())
    current: dict = load_themes()
    skills = get_all_skills()

    print("\n=== Proposed theme changes ===")
    _show_diff(current, proposed)

    print("\nTheme summary:")
    for slug, info in proposed.items():
        print(f"  {slug}: {info.get('name', slug)} ({len(info.get('skills', []))} skills)")

    print("\nOptions per skill group:")
    print("  [a] Accept all proposed changes")
    print("  [r] Reassign a skill to a different theme")
    print("  [n] Create a new theme and assign skills there")
    print("  [q] Quit without saving")

    choice = input("\nChoice [a/r/n/q]: ").strip().lower()

    if choice == "q":
        print("Aborted.")
        return

    if choice == "a":
        _apply_proposed(proposed, current)
        return

    if choice == "r":
        skill = input("Skill folder name to reassign: ").strip()
        if skill not in skills:
            print(f"[approve] Unknown skill: {skill}", file=sys.stderr)
            return
        theme = input("Assign to theme slug: ").strip()
        if theme not in proposed and theme not in current:
            theme_name = input(f"New theme '{theme}' — human-readable name: ").strip()
            theme_desc = input("Description (one line): ").strip()
            proposed[theme] = {"name": theme_name, "description": theme_desc, "skills": []}
        # Move skill
        for t in proposed.values():
            t["skills"] = [s for s in t["skills"] if s != skill]
        proposed.setdefault(theme, {"name": theme, "description": "", "skills": []})["skills"].append(skill)
        _PROPOSED_JSON.write_text(json.dumps(proposed, indent=2) + "\n")
        print(f"Updated proposal. Run --approve again to continue reviewing.")
        return

    if choice == "n":
        slug = _to_snake(input("New theme slug (snake_case): ").strip())
        name = input("Human-readable name: ").strip()
        desc = input("Description: ").strip()
        skills_input = input("Skill names to add (comma-separated): ").strip()
        skill_list = [s.strip() for s in skills_input.split(",") if s.strip()]
        for t in proposed.values():
            t["skills"] = [s for s in t["skills"] if s not in skill_list]
        proposed[slug] = {"name": name, "description": desc, "skills": skill_list}
        _PROPOSED_JSON.write_text(json.dumps(proposed, indent=2) + "\n")
        print(f"Updated proposal. Run --approve again to finalize.")
        return

    print("Unrecognized choice. Run --approve again.")


def _apply_proposed(proposed: dict, current: dict) -> None:
    """Merge proposed into current, write themes.json and update skill_meta.json files."""
    # Preserve theme metadata from current for unchanged themes
    merged: dict = {}
    for slug, info in proposed.items():
        merged[slug] = {
            "name": info.get("name") or current.get(slug, {}).get("name", slug.replace("_", " ").title()),
            "description": info.get("description") or current.get(slug, {}).get("description", ""),
            "skills": info.get("skills", []),
        }

    save_themes(merged)

    # Update skill_meta.json for each skill
    for slug, info in merged.items():
        for skill in info.get("skills", []):
            update_skill_meta_theme(skill, slug)

    # Clean up proposal file
    _PROPOSED_JSON.unlink(missing_ok=True)

    total = sum(len(t["skills"]) for t in merged.values())
    print(f"\n✓ Saved themes.json: {len(merged)} theme(s), {total} skill(s)")
    print(f"  Updated skill_meta.json for all assigned skills.")


# ── Assign mode ────────────────────────────────────────────────────────────────

def assign(skill_name: str, theme_slug: str) -> None:
    """Manually assign a single skill to a theme."""
    skill_dir = _SKILLS_DIR / skill_name
    if not skill_dir.exists():
        print(f"[assign] Skill folder not found: {skill_name}", file=sys.stderr)
        sys.exit(1)

    themes = load_themes()

    if theme_slug not in themes:
        name = input(f"New theme '{theme_slug}' — human-readable name: ").strip()
        desc = input("Description: ").strip()
        themes[theme_slug] = {"name": name, "description": desc, "skills": []}

    # Remove from current theme
    for t in themes.values():
        t["skills"] = [s for s in t.get("skills", []) if s != skill_name]

    # Add to target theme
    themes[theme_slug]["skills"].append(skill_name)

    # Clean up empty themes (but keep _unthemed)
    themes = {k: v for k, v in themes.items() if v["skills"] or k == "_unthemed"}

    save_themes(themes)
    update_skill_meta_theme(skill_name, theme_slug)
    print(f"✓ Assigned '{skill_name}' to theme '{theme_slug}'")


# ── List mode ──────────────────────────────────────────────────────────────────

def list_themes() -> None:
    """Print current themes and their skills."""
    themes = load_themes()
    all_skills = get_all_skills()

    print(f"\nCurrent themes ({len(themes)} total, {len(all_skills)} individual skills):\n")
    for slug, info in themes.items():
        skills = info.get("skills", [])
        print(f"  [{slug}] {info.get('name', slug)}  ({len(skills)} skills)")
        for s in skills[:5]:
            print(f"    • {s}")
        if len(skills) > 5:
            print(f"    ... and {len(skills) - 5} more")
        print()

    # Skills not in any theme
    themed = {s for t in themes.values() for s in t.get("skills", [])}
    orphans = [s for s in all_skills if s not in themed]
    if orphans:
        print(f"  Orphaned skills (not in themes.json): {', '.join(orphans)}")


# ── Main ───────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(description="Organize skill folders into themes.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--propose", action="store_true", help="Use Gemini to propose theme groupings")
    group.add_argument("--approve", action="store_true", help="CLI review of proposed changes")
    group.add_argument("--assign", nargs=2, metavar=("SKILL", "THEME"), help="Assign a skill to a theme")
    group.add_argument("--list", action="store_true", help="List current themes and skills")
    args = parser.parse_args()

    if args.propose:
        propose(interactive=True)
    elif args.approve:
        approve()
    elif args.assign:
        assign(args.assign[0], args.assign[1])
    elif args.list:
        list_themes()


if __name__ == "__main__":
    main()
