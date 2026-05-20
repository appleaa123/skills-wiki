#!/usr/bin/env python3
"""Export all skills in skills_library/ to a bulk-upload CSV.

The output CSV uses the exact same format accepted by:
    python3 scripts/add_skill.py --bulk FILE

Columns:
    url         — source GitHub repo (from skill_meta.json; blank if added from local file)
    name        — skill folder name
    plan        — lowest plan tier that includes this skill (basic / pro / enterprise)
    split       — always "no-split" (re-import replaces existing folder without re-splitting)
    theme       — from skill_meta.json
    description — from skill_meta.json
    subdir      — from skill_meta.json (blank if whole-repo import)

Usage:
    python3 scripts/export_skills.py
    python3 scripts/export_skills.py --output my_skills.csv
    python3 scripts/export_skills.py --filter-url https://github.com/some/repo
"""

import argparse
import ast
import csv
import json
import re
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).parent.parent
_SKILLS_DIR = _REPO_ROOT / "skills_library"
_PROVISION_PY = _REPO_ROOT / "scripts" / "provision.py"


def _load_plan_skills() -> dict[str, list[str]]:
    """Parse _PLAN_SKILLS from provision.py without importing it."""
    content = _PROVISION_PY.read_text()
    match = re.search(r"_PLAN_SKILLS\s*:[^=]+=\s*(\{.*?\})", content, re.DOTALL)
    if not match:
        return {}
    try:
        return ast.literal_eval(match.group(1))
    except Exception:
        return {}


def _lowest_tier(skill_name: str, plan_skills: dict[str, list[str]]) -> str:
    """Return the most restrictive tier that includes this skill."""
    for tier in ("basic", "pro", "enterprise"):
        if skill_name in plan_skills.get(tier, []):
            return tier
    return "pro"


def export(output: Path, filter_url: str | None = None) -> list[dict]:
    plan_skills = _load_plan_skills()

    rows: list[dict] = []
    skipped = 0

    for skill_dir in sorted(_SKILLS_DIR.iterdir()):
        if not skill_dir.is_dir():
            continue
        if skill_dir.name.startswith("."):
            continue
        if not (skill_dir / "main.py").exists():
            continue

        meta: dict = {}
        meta_path = skill_dir / "skill_meta.json"
        if meta_path.exists():
            try:
                meta = json.loads(meta_path.read_text())
            except Exception:
                pass

        url = meta.get("source_repo", "").strip()
        if filter_url:
            normalized_filter = filter_url.rstrip("/").removesuffix(".git")
            normalized_url = url.rstrip("/").removesuffix(".git")
            if normalized_url != normalized_filter:
                skipped += 1
                continue

        rows.append({
            "url": url,
            "name": skill_dir.name,
            "plan": _lowest_tier(skill_dir.name, plan_skills),
            "split": "no-split",
            "theme": meta.get("theme", "_unthemed") or "_unthemed",
            "description": meta.get("description", "").strip(),
            "subdir": meta.get("subdir", "").strip(),
        })

    return rows, skipped


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Export skills_library/ skills to a bulk-upload CSV."
    )
    parser.add_argument(
        "--output", "-o",
        default="skills_export.csv",
        metavar="FILE",
        help="Output CSV path (default: skills_export.csv)",
    )
    parser.add_argument(
        "--filter-url",
        metavar="URL",
        default=None,
        help="Only export skills whose source_repo matches this GitHub URL",
    )
    args = parser.parse_args()

    output = Path(args.output)
    rows, skipped = export(output, filter_url=args.filter_url)

    if not rows:
        print("[export] No skills found matching the given criteria.", file=sys.stderr)
        sys.exit(1)

    fieldnames = ["url", "name", "plan", "split", "theme", "description", "subdir"]
    with output.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Exported {len(rows)} skill(s) → {output}")
    if skipped:
        print(f"  (skipped {skipped} skill(s) that didn't match --filter-url)")
    print(f"\nEdit {output} as needed, then re-import with:")
    print(f"  python3 scripts/add_skill.py --bulk {output}")


if __name__ == "__main__":
    main()
