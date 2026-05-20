"""Migration script to overhaul all community skill get_*_skill tools for:
1. Multi-tenancy (client_id via X-Client-ID HTTP header).
2. Robust null handling (skill_name="null" support).
3. Marketplace/Functional structure (wrapped results with id, status, interface).

Idempotent — re-running a patched file is a no-op (or an upgrade to the latest pattern).

Usage:
    python scripts/patch_skill_hints.py [--dry-run]
"""

import argparse
import re
import sys
from pathlib import Path

SKILLS_DIR = Path(__file__).parent.parent / "skills_library"

IMPORT_LINE = "from core.skill_config import get_presentation_hint\n"

# Matches: def get_<anything>_skill(skill_name[: str][ = None][, metadata: dict = None])
GET_SKILL_SIG_RE = re.compile(r"def (get_\w+_skill)\(skill_name(?::\s*str)?(?:\s*=\s*None)?(?:,\s*metadata(?::\s*dict)?(?:\s*=\s*None)?)?\)")


def _build_replacement(indent: str, skill_folder: str) -> str:
    return (
        f"{indent}if not skill_name or str(skill_name).lower() in [\"null\", \"none\"]:\n"
        f"{indent}    skill_name = \"start-here\" if \"start-here\" in _SKILLS else next(iter(_SKILLS))\n"
        f"{indent}skill_data = _SKILLS.get(skill_name, {{\"error\": f\"Unknown skill: {{skill_name}}\"}})\n"
        f"{indent}try:\n"
        f"{indent}    from fastmcp.server.dependencies import get_http_request\n"
        f"{indent}    client_id = get_http_request().headers.get(\"x-client-id\")\n"
        f"{indent}except Exception:\n"
        f"{indent}    client_id = None\n"
        f"{indent}if not client_id:\n"
        f"{indent}    from core.config import get_client_id\n"
        f"{indent}    client_id = get_client_id()\n"
        f"{indent}hint = get_presentation_hint({skill_folder!r}, client_id=client_id)\n"
        f"{indent}if hint:\n"
        f"{indent}    skill_data = {{**skill_data, \"_presentation_hint\": hint}}\n"
        f"{indent}return {{\n"
        f"{indent}    \"id\": f\"{{skill_name}}@{skill_folder}\",\n"
        f"{indent}    \"skill_name\": skill_name,\n"
        f"{indent}    \"status\": skill_data.get(\"status\", \"production\"),\n"
        f"{indent}    \"metadata\": {{\n"
        f"{indent}        \"folder\": {skill_folder!r},\n"
        f"{indent}        \"client_id\": client_id,\n"
        f"{indent}        \"source\": \"community-library\"\n"
        f"{indent}    }},\n"
        f"{indent}    \"interface\": {{\n"
        f"{indent}        \"commands\": [f\"/{{skill_name}}\"]\n"
        f"{indent}    }},\n"
        f"{indent}    \"content\": skill_data\n"
        f"{indent}}}"
    )


def patch_file(path: Path, dry_run: bool) -> str:
    """Patch a single skill main.py. Returns a status string."""
    source = path.read_text(encoding="utf-8")
    skill_folder = path.parent.name

    # 1. Check if it's a get_*_skill tool
    sig_match = GET_SKILL_SIG_RE.search(source)
    if not sig_match:
        return "SKIP (no get_*_skill tool)"

    # 2. Check if we already have the NEWEST pattern
    if "get_http_request().headers.get(\"x-client-id\")" in source and "skill_name.lower() in [\"null\", \"none\"]" in source:
        return "SKIP (already has newest http-header pattern)"

    func_name = sig_match.group(1)
    new_sig = f"def {func_name}(skill_name: str = None)"
    
    # Update signature
    patched = GET_SKILL_SIG_RE.sub(new_sig, source, count=1)

    # 3. Find and replace the function body logic
    lines = patched.splitlines()
    func_line_idx = -1
    for i, line in enumerate(lines):
        if line.strip().startswith(f"def {func_name}"):
            func_line_idx = i
            break

    if func_line_idx == -1:
        return "WARN (signature line not found)"

    # Find where the body starts (skip docstring)
    body_start_idx = func_line_idx + 1
    if body_start_idx < len(lines) and '"""' in lines[body_start_idx]:
        if lines[body_start_idx].strip().count('"""') == 2:
            # Single line docstring
            body_start_idx += 1
        else:
            # Multi-line docstring
            body_start_idx += 1
            while body_start_idx < len(lines) and '"""' not in lines[body_start_idx]:
                body_start_idx += 1
            body_start_idx += 1 
    
    # Find the end of the current function body
    body_end_idx = len(lines)
    for i in range(body_start_idx, len(lines)):
        if lines[i].strip().startswith("@mcp.tool") or lines[i].strip().startswith("def "):
            body_end_idx = i
            break
        if not lines[i].strip() and i + 1 < len(lines) and lines[i+1] and not lines[i+1].startswith(" "):
             body_end_idx = i
             break

    # Reconstruct the function with the new body
    indent = "    "
    new_body = _build_replacement(indent, skill_folder).splitlines()
    
    final_lines = lines[:body_start_idx] + new_body + lines[body_end_idx:]
    patched = "\n".join(final_lines) + "\n"

    # 4. Add import if missing
    if "from core.skill_config import get_presentation_hint" not in patched:
        if "from fastmcp import FastMCP\n" in patched:
            patched = patched.replace(
                "from fastmcp import FastMCP\n",
                "from fastmcp import FastMCP\n" + IMPORT_LINE,
                1,
            )
        else:
            # Fallback
            patched = IMPORT_LINE + patched

    if not dry_run:
        path.write_text(patched, encoding="utf-8")

    return "OVERHAULED" + (" (dry-run)" if dry_run else "")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="Print changes without writing files")
    args = parser.parse_args()

    results: dict[str, list[str]] = {}

    for skill_dir in sorted(SKILLS_DIR.iterdir()):
        main_py = skill_dir / "main.py"
        if not skill_dir.is_dir() or not main_py.exists():
            continue
        status = patch_file(main_py, args.dry_run)
        category = status.split()[0]
        results.setdefault(category, []).append(skill_dir.name)
        print(f"[{status:<30}] {skill_dir.name}")

    print()
    print("Summary:")
    for cat, items in results.items():
        print(f"  {cat:<10}: {len(items)}")

    if results.get("WARN"):
        print("\nManual review required:")
        for name in results["WARN"]:
            print(f"  skills_library/{name}/main.py")
        sys.exit(1)


if __name__ == "__main__":
    main()
