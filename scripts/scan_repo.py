#!/usr/bin/env python3
"""Scan a GitHub repo and generate a bulk CSV for add_skill.py.

Clones the repo once, discovers category dirs inside each specified container
(e.g. skills/, plugins/), and writes a bulk_scan.csv that can be fed directly
to add_skill.py --bulk. Optionally runs the import immediately with --run.

Usage:
    python3 scripts/scan_repo.py --url URL [options]

Examples:
    # Generate CSV only (review before importing)
    python3 scripts/scan_repo.py \\
        --url https://github.com/jeremylongshore/claude-code-plugins-plus-skills.git \\
        --containers skills plugins \\
        --output bulk_jeremy.csv

    # Generate and run immediately
    python3 scripts/scan_repo.py \\
        --url https://github.com/jeremylongshore/claude-code-plugins-plus-skills.git \\
        --containers skills plugins \\
        --no-split --plan pro --run
"""

import argparse
import csv
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

_REPO_ROOT = Path(__file__).parent.parent
_NON_SKILL_DIRS = frozenset({
    "node_modules", ".git", "__pycache__", "dist", "build",
    "test", "tests", "docs", "examples", ".github", ".vscode",
})


def _to_snake(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")


def _strip_leading_number(name: str) -> str:
    """'01-devops-basics' → 'devops-basics'"""
    return re.sub(r"^\d+[-_]", "", name)


def _clone_repo(url: str) -> Path:
    tmp = Path(tempfile.mkdtemp())
    print(f"Cloning {url} ...")
    result = subprocess.run(
        ["git", "clone", "--depth", "1", url, str(tmp)],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"[scan_repo] git clone failed:\n{result.stderr}", file=sys.stderr)
        shutil.rmtree(tmp, ignore_errors=True)
        sys.exit(1)
    return tmp


def _is_category_dir(d: Path) -> bool:
    return (
        d.is_dir()
        and not d.name.startswith(".")
        and d.name not in _NON_SKILL_DIRS
    )


def _count_skill_files(d: Path) -> int:
    """Count SKILL.md files recursively in a directory."""
    return sum(1 for _ in d.rglob("SKILL.md"))


def scan(url: str, containers: list[str], plan: str, split_mode: str, output: Path) -> list[dict]:
    """Clone the repo and generate one CSV entry per category dir per container."""
    tmp = _clone_repo(url)
    entries: list[dict] = []

    try:
        for container in containers:
            container_path = tmp / container
            if not container_path.exists():
                print(f"  [skip] '{container}/' not found in repo")
                continue

            category_dirs = sorted(
                d for d in container_path.iterdir() if _is_category_dir(d)
            )
            if not category_dirs:
                print(f"  [skip] '{container}/' has no subdirectories")
                continue

            print(f"  Found {len(category_dirs)} category dir(s) in {container}/")
            for cat_dir in category_dirs:
                clean = _strip_leading_number(cat_dir.name)
                slug = _to_snake(clean)

                # Prefix non-skill containers to avoid name collisions
                # e.g. skills → "devops_basics", plugins → "plugin_devops_basics"
                container_prefix = container.rstrip("s")  # "skills"→"skill", "plugins"→"plugin"
                if container_prefix == "skill":
                    name = slug
                else:
                    name = f"{container_prefix}_{slug}"

                skill_count = _count_skill_files(cat_dir)
                entries.append({
                    "url": url,
                    "name": name,
                    "plan": plan,
                    "split": split_mode,
                    "theme": "_unthemed",
                    "description": "",
                    "subdir": f"{container}/{cat_dir.name}",
                    # informational only — not read by add_skill.py
                    "_skill_count": str(skill_count),
                })
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    return entries


def write_csv(entries: list[dict], output: Path) -> None:
    fieldnames = ["url", "name", "plan", "split", "theme", "description", "subdir"]
    with output.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(entries)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Scan a GitHub repo and generate a bulk CSV for add_skill.py."
    )
    parser.add_argument("--url", required=True, help="GitHub repository URL to scan")
    parser.add_argument(
        "--containers",
        nargs="+",
        default=["skills", "plugins"],
        metavar="DIR",
        help="Top-level dirs to scan (default: skills plugins)",
    )
    parser.add_argument(
        "--plan",
        choices=["basic", "pro", "enterprise", "all"],
        default="pro",
        help="Plan tier for all generated entries (default: pro)",
    )

    split_group = parser.add_mutually_exclusive_group()
    split_group.add_argument(
        "--split",
        dest="split_mode",
        action="store_const",
        const="split",
        help="Force split: one skill folder per individual skill inside each category",
    )
    split_group.add_argument(
        "--no-split",
        dest="split_mode",
        action="store_const",
        const="no-split",
        help="No split: one skill folder per category (recommended for large repos)",
    )
    parser.set_defaults(split_mode="no-split")

    parser.add_argument(
        "--output",
        default="bulk_scan.csv",
        metavar="FILE",
        help="Output CSV path (default: bulk_scan.csv)",
    )
    parser.add_argument(
        "--run",
        action="store_true",
        help="After writing the CSV, immediately run: python3 scripts/add_skill.py --bulk <output>",
    )

    args = parser.parse_args()
    output = Path(args.output)

    entries = scan(args.url, args.containers, args.plan, args.split_mode, output)

    if not entries:
        print("[scan_repo] No entries found — check --containers match dirs in the repo.", file=sys.stderr)
        sys.exit(1)

    write_csv(entries, output)

    # Print a summary table
    print(f"\nGenerated {output} with {len(entries)} entries:")
    print(f"  {'name':<40} {'subdir':<45} {'skills'}")
    print(f"  {'-'*40} {'-'*45} {'-'*6}")
    for e in entries:
        print(f"  {e['name']:<40} {e['subdir']:<45} {e.get('_skill_count', '?'):>6}")

    print(f"\nReview {output} and edit names/themes/plans as needed, then run:")
    print(f"  python3 scripts/add_skill.py --bulk {output}")

    if args.run:
        print(f"\nRunning bulk import ...")
        result = subprocess.run(
            [sys.executable, str(_REPO_ROOT / "scripts" / "add_skill.py"), "--bulk", str(output)],
            cwd=str(_REPO_ROOT),
        )
        sys.exit(result.returncode)


if __name__ == "__main__":
    main()
