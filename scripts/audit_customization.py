"""Audit all skills for customization (get_presentation_hint) compliance.

Usage:
    python scripts/audit_customization.py
"""

import re
import sys
from pathlib import Path

SKILLS_DIR = Path(__file__).parent.parent / "skills_library"

GET_SKILL_RE = re.compile(r"def get_\w+_skill\(skill_name")


def audit_file(path: Path) -> tuple[str, str]:
    """Return (status, note) for a skill main.py."""
    source = path.read_text(encoding="utf-8")
    has_tool = bool(GET_SKILL_RE.search(source))
    has_hint = "get_presentation_hint" in source

    if not has_tool:
        return "SKIP", "no get_*_skill tool"
    if has_hint:
        return "PASS", "calls get_presentation_hint"
    return "WARN", "get_*_skill tool but no hint — run patch_skill_hints.py"


def main() -> None:
    rows: list[tuple[str, str, str]] = []

    for skill_dir in sorted(SKILLS_DIR.iterdir()):
        main_py = skill_dir / "main.py"
        if not skill_dir.is_dir() or not main_py.exists():
            continue
        status, note = audit_file(main_py)
        rows.append((skill_dir.name, status, note))

    col_w = max(len(r[0]) for r in rows) + 2
    print(f"{'skill':<{col_w}} {'status':<8} note")
    print("-" * (col_w + 50))

    warn_count = 0
    for name, status, note in rows:
        print(f"{name:<{col_w}} {status:<8} {note}")
        if status == "WARN":
            warn_count += 1

    total = len(rows)
    passed = sum(1 for _, s, _ in rows if s == "PASS")
    skipped = sum(1 for _, s, _ in rows if s == "SKIP")

    print()
    print(f"Total: {total}  PASS: {passed}  WARN: {warn_count}  SKIP: {skipped}")

    if warn_count:
        print(f"\n{warn_count} skill(s) missing customization hook.")
        print("Run: python scripts/patch_skill_hints.py")
        sys.exit(1)


if __name__ == "__main__":
    main()
