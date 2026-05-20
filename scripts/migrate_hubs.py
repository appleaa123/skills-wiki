#!/usr/bin/env python3
"""Migrate hub skill folders into individual skill folders.

Hub folders bundle multiple unrelated skills into one FastMCP instance.
This script splits them into individual folders, one per sub-skill, then
writes an initial themes.json grouping them by their source hub.

Usage:
    python scripts/migrate_hubs.py --dry-run   # preview without making changes
    python scripts/migrate_hubs.py             # apply all migrations
    python scripts/migrate_hubs.py --hub amazon_skills  # migrate one hub only
"""

import argparse
import ast
import json
import re
import sys
import textwrap
from pathlib import Path

_REPO_ROOT = Path(__file__).parent.parent
_SKILLS_DIR = _REPO_ROOT / "skills_library"
_CLIENTS_JSON = _REPO_ROOT / "clients.json"
_DASHBOARD_SKILLS_TS = _REPO_ROOT / "dashboard" / "lib" / "skills.ts"
_THEMES_JSON = _SKILLS_DIR / "themes.json"

# Hubs that contain multiple unrelated skills and should be split.
# Single-purpose skills (colleague_skill, feedback_skill, etc.) are skipped.
HUBS: dict[str, dict] = {
    "amazon_skills": {
        "type": "skills",
        "var": "_SKILLS",
        "source_repo": "https://github.com/nexscope-ai/Amazon-Skills",
        "theme": "amazon",
        "theme_name": "Amazon Selling",
        "theme_description": "Amazon FBA, keyword research, PPC, listing optimization, and profit calculation.",
    },
    "marketing_skills": {
        "type": "skills",
        "var": "_SKILLS",
        "source_repo": "https://github.com/coreyhaines31/marketingskills",
        "theme": "marketing",
        "theme_name": "Marketing",
        "theme_description": "Conversion copywriting, content strategy, email, paid ads, SEO, and growth.",
    },
    "seo_geo": {
        "type": "skills",
        "var": "_SKILLS",
        "source_repo": "https://github.com/aaron-he-zhu/seo-geo-claude-skills",
        "theme": "seo",
        "theme_name": "SEO & Search",
        "theme_description": "Keyword research, on-page SEO, technical SEO, link building, and geo-targeting.",
    },
    "ecommerce_skills": {
        "type": "skills",
        "var": "_SKILLS",
        "source_repo": "https://github.com/nexscope-ai/eCommerce-Skills",
        "theme": "ecommerce",
        "theme_name": "E-Commerce",
        "theme_description": "Shopify, Amazon, Etsy, TikTok Shop: listings, ads, pricing, and operations.",
    },
    "agency_agents": {
        "type": "agents",
        "var": "_AGENTS",
        "source_repo": "https://github.com/msitarzewski/agency-agents",
        "theme": "agency_agents",
        "theme_name": "Agency Agents",
        "theme_description": "144+ AI agent personas across 12 professional divisions.",
    },
}


def _to_snake(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")


def _extract_ast_var(source: str, var_name: str) -> dict | None:
    """Return the dict literal assigned to var_name in source, or None.

    Handles both plain assignments (_SKILLS = {...}) and annotated assignments
    (_SKILLS: dict[str, dict] = {...}).
    """
    try:
        tree = ast.parse(source)
    except SyntaxError as e:
        print(f"  [warn] AST parse error: {e}", file=sys.stderr)
        return None

    for node in tree.body:
        value_node = None

        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == var_name:
                    value_node = node.value
                    break

        elif isinstance(node, ast.AnnAssign):
            if isinstance(node.target, ast.Name) and node.target.id == var_name:
                value_node = node.value

        if value_node is not None:
            try:
                return ast.literal_eval(value_node)
            except Exception as exc:
                print(f"  [warn] Could not eval {var_name}: {exc}", file=sys.stderr)
                return None

    return None


def _extract_source_block(source: str, start_pattern: str, end_line_before: str | None = None) -> str:
    """Extract lines from start_pattern to either end_line_before or EOF."""
    lines = source.splitlines()
    capturing = False
    result: list[str] = []
    for line in lines:
        if not capturing and re.search(start_pattern, line):
            capturing = True
        if capturing:
            if end_line_before and re.search(end_line_before, line) and result:
                break
            result.append(line)
    return "\n".join(result)


def _generate_guidance_main(
    slug: str,
    data: dict,
    source_repo: str,
    hub_display_name: str,
) -> str:
    """Generate main.py for a guidance-only skill (description + guidance text)."""
    snake = _to_snake(slug)
    display = data.get("display_name") or slug.replace("-", " ").title()
    description = data.get("description", "")
    guidance = data.get("guidance", "")

    guidance_dict: dict = {"display_name": display, "description": description}
    if guidance:
        guidance_dict["guidance"] = guidance

    # Carry over any extra metadata fields
    for key in ("status", "category", "phase", "platforms"):
        if key in data:
            guidance_dict[key] = data[key]

    guidance_repr = repr(guidance_dict)

    return textwrap.dedent(f'''\
        """{display} — {description[:80]}

        Source: {source_repo}
        """

        from fastmcp import FastMCP

        mcp = FastMCP("{slug}")

        _GUIDANCE = {guidance_repr}


        @mcp.tool()
        def get_guidance() -> dict:
            """Get the full guidance for this skill: {display}."""
            return _GUIDANCE
        ''')


def _generate_agents_main(
    division_slug: str,
    agents: dict[str, str],
    source_repo: str,
) -> str:
    """Generate main.py for an agent division (list + persona getter)."""
    snake = _to_snake(division_slug)
    display = division_slug.replace("-", " ").title() + " Agents"
    agents_repr = repr(agents)

    return textwrap.dedent(f'''\
        """{display} — agent personas for the {division_slug} division.

        Source: {source_repo}
        """

        from fastmcp import FastMCP

        mcp = FastMCP("{division_slug}-agents")

        _AGENTS: dict[str, str] = {agents_repr}


        @mcp.tool()
        def list_agents() -> dict:
            """List all agent personas in the {division_slug} division."""
            return _AGENTS


        @mcp.tool()
        def get_agent_persona(role: str) -> dict:
            """Get the full persona description for a specific agent role.

            Args:
                role: Agent role slug (e.g. 'frontend-developer', 'backend-architect').
            """
            role = role.lower().strip()
            if role not in _AGENTS:
                return {{"error": f"Unknown role '{{role}}'", "available": list(_AGENTS.keys())}}
            return {{"role": role, "division": "{division_slug}", "persona": _AGENTS[role]}}
        ''')


def _generate_amazon_fba_main(amazon_source: str, source_repo: str) -> str:
    """Extract the FBA calculator logic from amazon_skills/main.py using AST."""
    try:
        tree = ast.parse(amazon_source)
    except SyntaxError:
        return ""

    lines = amazon_source.splitlines()

    # Collect: data variables (_FBA_SIZE_TIERS, _REFERRAL_RATES, _STORAGE_RATES)
    # and functions (_classify_size_tier, calculate_fba_fees)
    keep_names = {"_FBA_SIZE_TIERS", "_REFERRAL_RATES", "_STORAGE_RATES", "_classify_size_tier", "calculate_fba_fees"}
    chunks: list[str] = []

    for node in tree.body:
        name = None
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name) and t.id in keep_names:
                    name = t.id
                    break
        elif isinstance(node, ast.AnnAssign):
            if isinstance(node.target, ast.Name) and node.target.id in keep_names:
                name = node.target.id
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if node.name in keep_names:
                name = node.name

        if name:
            chunk_lines = lines[node.lineno - 1 : node.end_lineno]
            # For calculate_fba_fees, also add the @mcp.tool() decorator
            # by looking at the line before
            if name == "calculate_fba_fees" and node.lineno > 1:
                prev = lines[node.lineno - 2].strip()
                if prev.startswith("@mcp.tool"):
                    chunk_lines = [lines[node.lineno - 2]] + chunk_lines
            # Remove any references to get_presentation_hint and _SKILL_NAME
            chunk_lines = [
                ln for ln in chunk_lines
                if "get_presentation_hint" not in ln and "_SKILL_NAME" not in ln
            ]
            chunks.append("\n".join(chunk_lines))

    body = "\n\n\n".join(chunks)

    return (
        f'"""Amazon FBA Calculator — complete fee breakdown and profit analysis (2024 US rates).\n\n'
        f"Source: {source_repo}\n"
        f'"""\n\n'
        f"from fastmcp import FastMCP\n\n"
        f'mcp = FastMCP("amazon-fba-calculator")\n\n\n'
        f"{body}\n"
    )


def _write_skill_meta(skill_dir: Path, data: dict, source_repo: str, theme: str, dry_run: bool) -> None:
    meta = {
        "display_name": data.get("display_name") or data.get("slug", "").replace("-", " ").title(),
        "description": data.get("description", ""),
        "source_repo": source_repo,
        "theme": theme,
    }
    if not dry_run:
        (skill_dir / "skill_meta.json").write_text(json.dumps(meta, indent=2) + "\n")


def migrate_hub(hub_name: str, hub_cfg: dict, dry_run: bool) -> list[str]:
    """Migrate one hub. Returns list of created skill folder names."""
    hub_dir = _SKILLS_DIR / hub_name
    if not hub_dir.exists():
        print(f"  [skip] {hub_name}/ not found")
        return []

    source = (hub_dir / "main.py").read_text()
    source_repo = hub_cfg["source_repo"]
    theme = hub_cfg["theme"]
    created: list[str] = []

    if hub_cfg["type"] == "skills":
        skills_data = _extract_ast_var(source, hub_cfg["var"])
        if not skills_data:
            print(f"  [error] Could not extract {hub_cfg['var']} from {hub_name}/main.py")
            return []

        # For amazon_skills, skip the stub entry for amazon-fba-calculator
        # because we generate a real calculator skill from the function code below.
        fba_stubs = {"amazon-fba-calculator"} if hub_name == "amazon_skills" else set()

        for slug, data in skills_data.items():
            if not isinstance(data, dict):
                continue
            if slug in fba_stubs:
                continue
            folder_name = _to_snake(slug)
            skill_dir = _SKILLS_DIR / folder_name

            if skill_dir.exists():
                print(f"  [skip]  {folder_name}/ already exists")
                continue

            data_with_slug = dict(data)
            data_with_slug["display_name"] = slug.replace("-", " ").title()
            main_py = _generate_guidance_main(slug, data_with_slug, source_repo, hub_name)

            print(f"  [create] {folder_name}/  ({slug})")
            if not dry_run:
                skill_dir.mkdir()
                (skill_dir / "__init__.py").write_text("")
                (skill_dir / "main.py").write_text(main_py)
                _write_skill_meta(skill_dir, data_with_slug, source_repo, theme, dry_run)
            created.append(folder_name)

        # Special case: amazon FBA calculator with real computation
        if hub_name == "amazon_skills":
            fba_dir = _SKILLS_DIR / "amazon_fba_calculator"
            if not fba_dir.exists():
                fba_main = _generate_amazon_fba_main(source, source_repo)
                if fba_main:
                    print(f"  [create] amazon_fba_calculator/  (calculate_fba_fees tool)")
                    if not dry_run:
                        fba_dir.mkdir()
                        (fba_dir / "__init__.py").write_text("")
                        (fba_dir / "main.py").write_text(fba_main)
                        fba_meta = {
                            "display_name": "Amazon FBA Calculator",
                            "description": "Complete FBA fee breakdown and profit analysis with 2024 rates.",
                            "source_repo": source_repo,
                            "theme": theme,
                        }
                        (fba_dir / "skill_meta.json").write_text(json.dumps(fba_meta, indent=2) + "\n")
                    created.append("amazon_fba_calculator")

    elif hub_cfg["type"] == "agents":
        agents_data = _extract_ast_var(source, hub_cfg["var"])
        if not agents_data:
            print(f"  [error] Could not extract {hub_cfg['var']} from {hub_name}/main.py")
            return []

        for division, agents in agents_data.items():
            if not isinstance(agents, dict):
                continue
            folder_name = f"agents_{_to_snake(division)}"
            skill_dir = _SKILLS_DIR / folder_name

            if skill_dir.exists():
                print(f"  [skip]  {folder_name}/ already exists")
                continue

            main_py = _generate_agents_main(division, agents, source_repo)
            print(f"  [create] {folder_name}/  ({len(agents)} agent personas)")
            if not dry_run:
                skill_dir.mkdir()
                (skill_dir / "__init__.py").write_text("")
                (skill_dir / "main.py").write_text(main_py)
                meta = {
                    "display_name": division.replace("-", " ").title() + " Agents",
                    "description": f"Agent personas for the {division} division.",
                    "source_repo": source_repo,
                    "theme": theme,
                }
                (skill_dir / "skill_meta.json").write_text(json.dumps(meta, indent=2) + "\n")
            created.append(folder_name)

    return created


def update_clients_json(hub_to_skills: dict[str, list[str]], dry_run: bool) -> None:
    """Replace hub names with individual skill names in clients.json."""
    if not _CLIENTS_JSON.exists():
        return

    data: dict = json.loads(_CLIENTS_JSON.read_text())
    changed = False

    for client_id, client in data.items():
        old_skills: list[str] = client.get("enabled_skills", [])
        new_skills: list[str] = []
        for skill in old_skills:
            if skill in hub_to_skills:
                new_skills.extend(hub_to_skills[skill])
                changed = True
            else:
                new_skills.append(skill)
        client["enabled_skills"] = new_skills

    if changed:
        print("\n[clients.json] Updated enabled_skills to use individual skill names")
        if not dry_run:
            _CLIENTS_JSON.write_text(json.dumps(data, indent=2) + "\n")
    else:
        print("\n[clients.json] No changes needed")


def build_initial_themes(hub_to_skills: dict[str, list[str]]) -> dict:
    """Build themes.json by scanning skill_meta.json files in all skill folders.

    Falls back to hub_to_skills for skills created in this run that don't
    have skill_meta.json on disk yet (dry-run scenario).
    """
    # theme_slug -> list of skill folder names
    theme_skills: dict[str, list[str]] = {}
    themed: set[str] = set()

    # Scan existing skill folders for skill_meta.json
    for skill_dir in sorted(_SKILLS_DIR.iterdir()):
        if not skill_dir.is_dir() or not (skill_dir / "main.py").exists():
            continue
        if skill_dir.name in HUBS:
            continue  # skip old hub folders
        meta_path = skill_dir / "skill_meta.json"
        if meta_path.exists():
            try:
                meta = json.loads(meta_path.read_text())
                theme = meta.get("theme", "_unthemed")
                theme_skills.setdefault(theme, []).append(skill_dir.name)
                themed.add(skill_dir.name)
            except Exception:
                pass

    # Add skills from current run that may not have meta on disk yet (dry-run)
    for hub_name, created in hub_to_skills.items():
        theme = HUBS[hub_name]["theme"]
        for s in created:
            if s not in themed:
                theme_skills.setdefault(theme, []).append(s)
                themed.add(s)

    # Build structured themes dict preserving HUBS order then unthemed last
    themes: dict = {}
    seen_themes: set[str] = set()

    for hub_cfg in HUBS.values():
        t = hub_cfg["theme"]
        if t in theme_skills and t not in seen_themes:
            themes[t] = {
                "name": hub_cfg["theme_name"],
                "description": hub_cfg["theme_description"],
                "skills": theme_skills[t],
            }
            seen_themes.add(t)

    # Any themes not in HUBS (custom themes from previous organize runs)
    for t, skills in theme_skills.items():
        if t not in seen_themes and t != "_unthemed":
            themes[t] = {"name": t.replace("_", " ").title(), "description": "", "skills": skills}

    # Unthemed: skill folders with no skill_meta.json and not in any theme
    all_themed_skills = {s for t in themes.values() for s in t["skills"]}
    unthemed: list[str] = []
    for skill_dir in sorted(_SKILLS_DIR.iterdir()):
        if not skill_dir.is_dir() or not (skill_dir / "main.py").exists():
            continue
        if skill_dir.name in HUBS:
            continue
        if skill_dir.name not in all_themed_skills:
            unthemed.append(skill_dir.name)

    if theme_skills.get("_unthemed"):
        unthemed.extend(s for s in theme_skills["_unthemed"] if s not in unthemed)

    if unthemed:
        themes["_unthemed"] = {
            "name": "Uncategorized",
            "description": "Skills not yet assigned to a theme.",
            "skills": sorted(set(unthemed)),
        }

    return themes


def main() -> None:
    parser = argparse.ArgumentParser(description="Migrate hub skill folders into individual skills.")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without writing files")
    parser.add_argument("--hub", help="Migrate only this hub (e.g. amazon_skills)")
    args = parser.parse_args()

    if args.dry_run:
        print("=== DRY RUN — no files will be written ===\n")

    hubs_to_run = {args.hub: HUBS[args.hub]} if args.hub and args.hub in HUBS else HUBS

    if args.hub and args.hub not in HUBS:
        print(f"[error] Unknown hub '{args.hub}'. Known hubs: {', '.join(HUBS)}", file=sys.stderr)
        sys.exit(1)

    hub_to_skills: dict[str, list[str]] = {}

    for hub_name, hub_cfg in hubs_to_run.items():
        print(f"\n--- Migrating {hub_name} ---")
        created = migrate_hub(hub_name, hub_cfg, args.dry_run)
        hub_to_skills[hub_name] = created
        print(f"  → {len(created)} skill(s) {'would be ' if args.dry_run else ''}created")

    update_clients_json(hub_to_skills, args.dry_run)

    # Build and write themes.json
    themes = build_initial_themes(hub_to_skills)
    total_themed = sum(len(t["skills"]) for t in themes.values())
    print(f"\n[themes.json] {len(themes)} theme(s), {total_themed} skill(s) total")

    if not args.dry_run:
        _THEMES_JSON.write_text(json.dumps(themes, indent=2) + "\n")
        print(f"  Written to {_THEMES_JSON.relative_to(_REPO_ROOT)}")
    else:
        print("  (dry run — themes.json not written)")
        print(json.dumps(themes, indent=2))

    if args.dry_run:
        print("\n=== Re-run without --dry-run to apply changes ===")
    else:
        print("\n✓ Migration complete.")
        print("  Old hub folders are preserved. Remove them manually once verified.")
        print("  Next: python scripts/organize_themes.py --propose")


if __name__ == "__main__":
    main()
