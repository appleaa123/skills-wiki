#!/usr/bin/env python3
"""
Sync skill_meta.json → dashboard/lib/skills.ts

Reads description, source_repo (→githubUrl), and theme from each
skill_meta.json and updates the corresponding skill entry in skills.ts.
Skills whose theme has changed are moved to the correct theme bucket.

Usage:
    python scripts/sync_skills_ts.py          # apply changes
    python scripts/sync_skills_ts.py --dry-run # report without writing
"""

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
SKILLS_LIBRARY_DIR = REPO_ROOT / "skills_library"
SKILLS_TS_PATH = REPO_ROOT / "dashboard" / "lib" / "skills.ts"
THEMES_JSON_PATH = SKILLS_LIBRARY_DIR / "themes.json"


# ─── Data loading ─────────────────────────────────────────────────────────────

def load_skill_metas() -> dict:
    metas = {}
    for path in sorted(SKILLS_LIBRARY_DIR.glob("*/skill_meta.json")):
        skill_name = path.parent.name
        try:
            with open(path) as f:
                metas[skill_name] = json.load(f)
        except (json.JSONDecodeError, OSError) as e:
            print(f"Warning: skipping {path}: {e}", file=sys.stderr)
    return metas


def load_themes_json() -> dict:
    if not THEMES_JSON_PATH.exists():
        return {}
    with open(THEMES_JSON_PATH) as f:
        return json.load(f)


def build_name_to_slug(themes_json: dict) -> dict:
    """Map theme display name (lowercase) → slug."""
    return {data.get("name", "").lower(): slug for slug, data in themes_json.items()}


# ─── skills.ts parsing ────────────────────────────────────────────────────────

def find_matching_bracket(text: str, open_pos: int, open_ch: str, close_ch: str) -> int:
    """Return the index of the bracket that closes the one at open_pos."""
    depth = 1
    i = open_pos + 1
    while i < len(text) and depth > 0:
        if text[i] == open_ch:
            depth += 1
        elif text[i] == close_ch:
            depth -= 1
        i += 1
    return i - 1  # position of closing bracket


def split_top_level_objects(text: str) -> list[str]:
    """Return a list of top-level {...} blocks in text."""
    blocks = []
    i = 0
    while i < len(text):
        if text[i] == "{":
            end = find_matching_bracket(text, i, "{", "}")
            blocks.append(text[i : end + 1])
            i = end + 1
        else:
            i += 1
    return blocks


def extract_field_str(block: str, field: str) -> str:
    """Extract a string field value from a skill/theme block."""
    m = re.search(rf'{field}:\s*"((?:[^"\\]|\\.)*)"', block)
    return m.group(1) if m else ""


def extract_field_array(block: str, field: str) -> list[str]:
    """Extract a simple string-array field value."""
    m = re.search(rf'{field}:\s*\[', block)
    if not m:
        return []
    start = m.end()
    end = find_matching_bracket(block, start - 1, "[", "]")
    inner = block[start:end]
    return [s.strip().strip('"') for s in inner.split(",") if s.strip().strip('"')]


def parse_skill_block(block: str) -> dict | None:
    name = extract_field_str(block, "name")
    if not name:
        return None
    skill: dict = {
        "name": name,
        "displayName": extract_field_str(block, "displayName"),
        "description": extract_field_str(block, "description"),
        "tools": extract_field_array(block, "tools"),
        "theme": extract_field_str(block, "theme"),
    }
    github = extract_field_str(block, "githubUrl")
    if github:
        skill["githubUrl"] = github
    return skill


def parse_theme_block(block: str) -> dict | None:
    slug = extract_field_str(block, "slug")
    if not slug:
        return None

    # Find the skills array using bracket matching
    skills_m = re.search(r'skills:\s*\[', block)
    skills = []
    if skills_m:
        arr_start = skills_m.end() - 1  # position of '['
        arr_end = find_matching_bracket(block, arr_start, "[", "]")
        skills_body = block[arr_start + 1 : arr_end]
        for sb in split_top_level_objects(skills_body):
            skill = parse_skill_block(sb)
            if skill:
                skills.append(skill)

    return {
        "slug": slug,
        "name": extract_field_str(block, "name"),
        "description": extract_field_str(block, "description"),
        "skills": skills,
    }


def parse_skills_ts(content: str) -> tuple[str, list[dict], str]:
    """
    Split skills.ts into:
    - header: text up to and including 'export const THEMES: Theme[] = [\n'
    - themes: parsed list of theme dicts
    - footer: text from closing ]; onward
    """
    marker = "export const THEMES: Theme[] = ["
    themes_start = content.index(marker)
    header_end = themes_start + len(marker) + 1  # include the newline
    header = content[:header_end]

    # Find the matching ] for the THEMES array
    arr_open = content.index("[", themes_start + len(marker) - 1)
    arr_close = find_matching_bracket(content, arr_open, "[", "]")
    body = content[arr_open + 1 : arr_close]
    footer = content[arr_close + 1 :]

    themes = []
    for tb in split_top_level_objects(body):
        theme = parse_theme_block(tb)
        if theme:
            themes.append(theme)

    return header, themes, footer


# ─── skills.ts generation ─────────────────────────────────────────────────────

def esc(s: str) -> str:
    return s.replace("\\", "\\\\").replace('"', '\\"')


def render_skill(skill: dict, indent: str = "      ") -> str:
    i = indent
    lines = [f"{i}{{"]
    lines.append(f'{i}  name: "{esc(skill["name"])}",')
    lines.append(f'{i}  displayName: "{esc(skill["displayName"])}",')
    lines.append(f'{i}  description: "{esc(skill.get("description", ""))}",')
    tools = ", ".join(f'"{t}"' for t in skill.get("tools", []))
    lines.append(f"{i}  tools: [{tools}],")
    lines.append(f'{i}  theme: "{esc(skill["theme"])}",')
    if skill.get("githubUrl"):
        lines.append(f'{i}  githubUrl: "{esc(skill["githubUrl"])}",')
    lines.append(f"{i}}},")
    return "\n".join(lines)


def render_theme(theme: dict) -> str:
    lines = ["  {"]
    lines.append(f'    slug: "{esc(theme["slug"])}",')
    lines.append(f'    name: "{esc(theme["name"])}",')
    lines.append(f'    description: "{esc(theme.get("description", ""))}",')
    lines.append("    skills: [")
    for skill in theme["skills"]:
        lines.append(render_skill(skill))
    lines.append("    ],")
    lines.append("  },")
    return "\n".join(lines)


# ─── Main sync logic ──────────────────────────────────────────────────────────

def sync(dry_run: bool = False) -> None:
    content = SKILLS_TS_PATH.read_text()
    skill_metas = load_skill_metas()
    themes_json = load_themes_json()
    name_to_slug = build_name_to_slug(themes_json)

    header, themes, footer = parse_skills_ts(content)

    # Flat map: skill_name → skill dict (mutable)
    all_skills: dict[str, dict] = {}
    for theme in themes:
        for skill in theme["skills"]:
            all_skills[skill["name"]] = skill

    # Apply updates from skill_meta.json
    updated, moved = 0, 0
    for skill_name, meta in skill_metas.items():
        if skill_name not in all_skills:
            continue

        skill = all_skills[skill_name]
        changed = False

        new_desc = meta.get("description", "")
        if new_desc and skill.get("description") != new_desc:
            skill["description"] = new_desc
            changed = True

        new_url = meta.get("source_repo", "")
        if new_url and skill.get("githubUrl") != new_url:
            skill["githubUrl"] = new_url
            changed = True

        meta_theme_name = meta.get("theme", "")
        if meta_theme_name:
            slug = name_to_slug.get(meta_theme_name.lower())
            if not slug:
                slug = re.sub(r"[\s\-]+", "_", meta_theme_name).lower()
            if skill["theme"] != slug:
                skill["theme"] = slug
                moved += 1
                changed = True

        if changed:
            updated += 1
            if not dry_run:
                pass  # changes are in-place on the dict

    # Re-group skills by their (possibly updated) theme slug
    theme_slugs_seen = {t["slug"] for t in themes}

    # Create buckets for any new theme slugs referenced by skills
    for skill in all_skills.values():
        slug = skill["theme"]
        if slug not in theme_slugs_seen:
            tj = themes_json.get(slug, {})
            themes.append({
                "slug": slug,
                "name": tj.get("name", slug.replace("_", " ").title()),
                "description": tj.get("description", ""),
                "skills": [],
            })
            theme_slugs_seen.add(slug)

    # Clear existing skill lists, then fill from updated all_skills
    theme_map = {t["slug"]: t for t in themes}
    for t in themes:
        t["skills"] = []

    for skill in all_skills.values():
        target = skill["theme"]
        if target not in theme_map:
            target = "_unthemed"
        theme_map[target]["skills"].append(skill)

    # Move _unthemed to the end
    ordered = [t for t in themes if t["slug"] != "_unthemed"]
    if "_unthemed" in theme_map:
        ordered.append(theme_map["_unthemed"])

    # Drop empty theme buckets (except _unthemed which we always keep)
    final_themes = [t for t in ordered if t["skills"] or t["slug"] == "_unthemed"]

    if dry_run:
        print(f"[dry-run] {updated} skills would be updated ({moved} theme changes)")
        for skill_name, meta in skill_metas.items():
            if skill_name in all_skills:
                s = all_skills[skill_name]
                print(f"  {skill_name}: theme={s['theme']}, desc={bool(s.get('description'))}, url={bool(s.get('githubUrl'))}")
        return

    theme_blocks = "\n".join(render_theme(t) for t in final_themes) + "\n"
    new_content = header + theme_blocks + "];" + footer[footer.index(";") + 1 :]

    SKILLS_TS_PATH.write_text(new_content)
    print(f"Done: {updated} skills updated, {moved} moved to a new theme bucket")
    print(f"Wrote: {SKILLS_TS_PATH}")


if __name__ == "__main__":
    sync(dry_run="--dry-run" in sys.argv)
