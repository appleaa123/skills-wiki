#!/usr/bin/env python3
"""Add a new skill to skills_library/ from a GitHub URL or local file.

Usage:
    python scripts/add_skill.py --url https://github.com/org/repo --name my_skill
    python scripts/add_skill.py --file ~/tools.py --name my_skill
    python scripts/add_skill.py --url ... --name ... --plan basic|pro|enterprise|all
    python scripts/add_skill.py --url ... --name ... --llm
    python scripts/add_skill.py --url ... --name ... --split      # force split into individual skills
    python scripts/add_skill.py --url ... --name ... --no-split   # force keep as one skill
    python scripts/add_skill.py --url ... --name ... --auto       # LLM detects hub vs single (default)
"""

import argparse
import ast
import json
import os
import py_compile
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

_REPO_ROOT = Path(__file__).parent.parent
_SKILLS_DIR = _REPO_ROOT / "skills_library"
_PROVISION_PY = _REPO_ROOT / "scripts" / "provision.py"
_CLIENTS_JSON = _REPO_ROOT / "clients.json"

_MAX_CHARS = 200_000
_SKILLS_TS = _REPO_ROOT / "dashboard" / "lib" / "skills.ts"

# Higher-tier plans are supersets: adding to "pro" also adds to "enterprise"
_TIER_INCLUSIONS: dict[str, list[str]] = {
    "basic": ["basic", "pro", "enterprise"],
    "pro": ["pro", "enterprise"],
    "enterprise": ["enterprise"],
    "all": ["basic", "pro", "enterprise"],
}


# ── Step 1: Collect source content ─────────────────────────────────────────

def _read_dir(path: Path) -> str:
    parts: list[str] = []
    total = 0

    for readme_name in ("README.md", "readme.md", "README.rst"):
        readme = path / readme_name
        if readme.exists():
            text = readme.read_text(errors="replace")
            parts.append(f"=== {readme_name} ===\n{text}")
            total += len(text)
            break

    # Collect all SKILL.md files recursively — these are the actual skill specifications
    for skill_md in sorted(path.rglob("SKILL.md")):
        if total >= _MAX_CHARS:
            break
        rel = skill_md.relative_to(path)
        if any(part in _NON_SKILL_DIRS for part in rel.parts):
            continue
        text = skill_md.read_text(errors="replace")
        remaining = _MAX_CHARS - total
        parts.append(f"=== {rel} ===\n{text[:remaining]}")
        total += len(text)

    for py_file in sorted(path.glob("*.py")):
        if total >= _MAX_CHARS:
            break
        text = py_file.read_text(errors="replace")
        remaining = _MAX_CHARS - total
        parts.append(f"=== {py_file.name} ===\n{text[:remaining]}")
        total += len(text)

    return "\n\n".join(parts)


def collect_content(args: argparse.Namespace) -> tuple[str, Path | None]:
    """Return (raw_content, temp_dir_to_cleanup | None)."""
    if args.url:
        tmp = Path(tempfile.mkdtemp())
        print(f"Cloning {args.url} ...")
        result = subprocess.run(
            ["git", "clone", "--depth", "1", args.url, str(tmp)],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            print(f"[add_skill] git clone failed:\n{result.stderr}", file=sys.stderr)
            shutil.rmtree(tmp, ignore_errors=True)
            sys.exit(1)
        return _read_dir(tmp), tmp

    src = Path(args.file).expanduser().resolve()
    if not src.exists():
        print(f"[add_skill] Not found: {src}", file=sys.stderr)
        sys.exit(1)

    if src.suffix == ".zip":
        tmp = Path(tempfile.mkdtemp())
        with zipfile.ZipFile(src) as zf:
            zf.extractall(tmp)
        return _read_dir(tmp), tmp

    if src.is_dir():
        return _read_dir(src), None

    return src.read_text(errors="replace")[:_MAX_CHARS], None


# ── Step 2a: Template generation ───────────────────────────────────────────

def _to_snake(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")


def _to_kebab(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def _extract_functions(source: str) -> list[tuple[str, str]]:
    """Return list of (func_name, func_source) for public top-level defs."""
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return []

    lines = source.splitlines()
    results = []
    for node in tree.body:
        if not isinstance(node, ast.FunctionDef):
            continue
        if node.name.startswith("_"):
            continue
        func_lines = lines[node.lineno - 1 : node.end_lineno]
        results.append((node.name, "\n".join(func_lines)))
    return results


def _parse_readme_sections(content: str) -> list[tuple[str, str, str]]:
    """Return list of (slug, description, guidance) from ## headings."""
    sections: list[tuple[str, str, str]] = []
    current_heading: str | None = None
    current_lines: list[str] = []

    def _flush() -> None:
        if current_heading and current_lines:
            body = "\n".join(current_lines).strip()
            first_sentence = body.split(".")[0].strip() + "." if body else current_heading
            sections.append((_to_kebab(current_heading), first_sentence[:200], body))

    for line in content.splitlines():
        if line.startswith("## "):
            _flush()
            current_heading = line[3:].strip()
            current_lines = []
        elif current_heading:
            current_lines.append(line)

    _flush()
    return sections


def _parse_skill_md_frontmatter(text: str) -> str:
    """Extract description from YAML frontmatter, or fall back to first content line."""
    m = re.match(r"^---\n(.+?)\n---", text, re.DOTALL)
    if m:
        for line in m.group(1).splitlines():
            if line.lower().startswith("description:"):
                return line.split(":", 1)[1].strip().strip('"\'')
    for line in text.splitlines():
        line = line.strip()
        if line and not line.startswith("#") and not line.startswith("---"):
            return line[:200]
    return ""


def _get_repo_branch(repo_dir: Path) -> str:
    """Return the current branch name of a cloned repo, defaulting to 'main'."""
    try:
        result = subprocess.run(
            ["git", "-C", str(repo_dir), "rev-parse", "--abbrev-ref", "HEAD"],
            capture_output=True, text=True,
        )
        branch = result.stdout.strip()
        return branch if branch and branch != "HEAD" else "main"
    except Exception:
        return "main"


def _build_raw_url(source_repo: str, branch: str, path: str) -> str:
    """Convert a GitHub repo URL + path to a raw.githubusercontent.com URL."""
    # Normalize: strip .git suffix, trailing slash
    repo = source_repo.rstrip("/")
    if repo.endswith(".git"):
        repo = repo[:-4]
    # https://github.com/owner/repo → https://raw.githubusercontent.com/owner/repo
    raw_base = repo.replace("https://github.com/", "https://raw.githubusercontent.com/", 1)
    path = path.lstrip("/")
    return f"{raw_base}/{branch}/{path}"


def _copy_skill_files(
    src_root: Path,
    skill_dir: Path,
    source_repo: str = "",
) -> list[tuple[str, str]]:
    """Index SKILL.md files from a cloned repo into skill_dir/skill_files/_index.json.

    Stores raw GitHub URLs instead of copying file content — no disk bloat.
    Content is fetched on demand at runtime with a TTL cache in skill_runtime.py.

    Args:
        src_root: Root of the cloned/extracted repository.
        skill_dir: Destination skill directory in skills_library/.
        source_repo: GitHub repo URL (e.g. https://github.com/owner/repo).

    Returns:
        List of (slug, description) tuples for each SKILL.md found.
    """
    skill_files_dir = skill_dir / "skill_files"
    index: dict[str, dict] = {}
    results: list[tuple[str, str]] = []

    branch = _get_repo_branch(src_root) if src_root.exists() else "main"

    for skill_md in sorted(src_root.rglob("SKILL.md")):
        rel = skill_md.relative_to(src_root)
        if any(part in _NON_SKILL_DIRS for part in rel.parts):
            continue

        # Slug = parent dir name; fall back to skill folder name for root-level SKILL.md
        raw_slug = rel.parent.name if str(rel.parent) != "." else skill_dir.name
        slug = _to_kebab(raw_slug)

        # Resolve slug collisions
        base_slug = slug
        i = 2
        while slug in index:
            slug = f"{base_slug}-{i}"
            i += 1

        text = skill_md.read_text(errors="replace")
        description = _parse_skill_md_frontmatter(text)

        entry: dict = {"original_path": str(rel), "size": skill_md.stat().st_size}
        if source_repo:
            entry["raw_url"] = _build_raw_url(source_repo, branch, str(rel))

        index[slug] = entry
        results.append((slug, description))

    if index:
        skill_files_dir.mkdir(parents=True, exist_ok=True)
        (skill_files_dir / "_index.json").write_text(json.dumps(index, indent=2) + "\n")
        print(f"  Indexed {len(results)} SKILL.md file(s) → skill_files/_index.json")

    return results


def generate_template(
    skill_name: str,
    content: str,
    skill_files: list[tuple[str, str]] | None = None,
) -> str:
    """Generate main.py using deterministic template (no LLM).

    Args:
        skill_name: Snake_case skill folder name.
        content: Raw source content (README + SKILL.md text) for README section parsing.
        skill_files: If provided, list of (slug, description) from _copy_skill_files().
            When non-empty, generates file-pointer mode with runtime SKILL.md loading and
            _connections injection. When empty/None, falls back to legacy inline-guidance mode.
    """
    kebab = _to_kebab(skill_name)
    snake = _to_snake(skill_name)

    # Try AST function extraction from any Python content found
    py_source = ""
    for block in re.split(r"=== .+? ===\n", content):
        if "def " in block:
            py_source += block + "\n"
    if not py_source and "def " in content:
        py_source = content

    functions = _extract_functions(py_source)

    if functions:
        # Sub-case A: wrap extracted Python functions as tools
        tool_blocks = [f"@mcp.tool()\n{src}" for _, src in functions]
        return (
            f'"""Skill: {skill_name}."""\n\n'
            f"from fastmcp import FastMCP\n\n"
            f'mcp = FastMCP("{kebab}")\n\n\n'
            + "\n\n\n".join(tool_blocks)
            + "\n"
        )

    # Sub-case B1: file-pointer mode — SKILL.md files were captured on disk
    if skill_files:
        skills_lines = ["_SKILLS: dict[str, dict] = {"]
        for slug, desc in skill_files:
            skills_lines.append(f"    {repr(slug)}: {{")
            skills_lines.append(f"        \"description\": {repr(desc)},")
            skills_lines.append(f"        \"file\": {repr(slug + '.md')},")
            skills_lines.append("    },")
        skills_lines.append("}")
        skills_block = "\n".join(skills_lines)

        return (
            f'"""Skill: {skill_name}."""\n\n'
            f"from fastmcp import FastMCP\n"
            f"from core.skill_config import get_presentation_hint\n\n"
            f'mcp = FastMCP("{kebab}")\n\n\n'
            f"{skills_block}\n\n\n"
            f"@mcp.tool()\n"
            f"def list_{snake}_skills() -> dict:\n"
            f'    """List all available {skill_name} skills."""\n'
            f'    return {{k: v["description"] for k, v in _SKILLS.items()}}\n\n\n'
            f"@mcp.tool()\n"
            f"def get_{snake}_skill(skill_name: str) -> dict:\n"
            f'    """Get full guidance for a specific {skill_name} skill."""\n'
            f'    from core.skill_runtime import read_skill_file, list_client_connections\n'
            f'    entry = _SKILLS.get(skill_name)\n'
            f'    if not entry:\n'
            f'        return {{"error": f"Unknown skill: {{skill_name}}"}}\n'
            f'    guidance = read_skill_file(__file__, entry.get("file", "")) or entry.get("guidance", "")\n'
            f'    result = {{\n'
            f'        "description": entry["description"],\n'
            f'        "guidance": guidance,\n'
            f'        "_connections": list_client_connections(),\n'
            f'    }}\n'
            f'    hint = get_presentation_hint({repr(snake)})\n'
            f'    if hint:\n'
            f'        result = {{**result, "_presentation_hint": hint}}\n'
            f'    return result\n'
        )

    # Sub-case B2: legacy inline-guidance mode — no SKILL.md files found
    sections = _parse_readme_sections(content)

    if not sections:
        sections = [(kebab, f"{skill_name} skill.", content[:4000])]

    skills_lines = ["_SKILLS: dict[str, dict] = {"]
    for slug, desc, guidance in sections:
        skills_lines.append(f"    {repr(slug)}: {{")
        skills_lines.append(f"        \"description\": {repr(desc)},")
        skills_lines.append(f"        \"guidance\": {repr(guidance)},")
        skills_lines.append("    },")
    skills_lines.append("}")
    skills_block = "\n".join(skills_lines)

    return (
        f'"""Skill: {skill_name}."""\n\n'
        f"from fastmcp import FastMCP\n"
        f"from core.skill_config import get_presentation_hint\n\n"
        f'mcp = FastMCP("{kebab}")\n\n\n'
        f"{skills_block}\n\n\n"
        f"@mcp.tool()\n"
        f"def list_{snake}_skills() -> dict:\n"
        f'    """List all available {skill_name} skills."""\n'
        f'    return {{k: v["description"] for k, v in _SKILLS.items()}}\n\n\n'
        f"@mcp.tool()\n"
        f"def get_{snake}_skill(skill_name: str) -> dict:\n"
        f'    """Get full guidance for a specific {skill_name} skill."""\n'
        f'    result = _SKILLS.get(skill_name, {{"error": f"Unknown skill: {{skill_name}}"}})\n'
        f'    hint = get_presentation_hint({repr(snake)})\n'
        f'    if hint:\n'
        f'        result = {{**result, "_presentation_hint": hint}}\n'
        f'    return result\n'
    )


# ── Step 2b: LLM generation ─────────────────────────────────────────────────

_LLM_EXAMPLE = """\
from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("example")

_SKILLS: dict[str, dict] = {
    "tool-name": {
        "description": "One-line description.",
        "guidance": "Full guidance markdown here.",
    },
}

@mcp.tool()
def list_example_skills() -> dict:
    \"\"\"List all available skills.\"\"\"
    return {k: v["description"] for k, v in _SKILLS.items()}

@mcp.tool()
def get_example_skill(skill_name: str) -> dict:
    \"\"\"Get full guidance for a specific skill.\"\"\"
    result = _SKILLS.get(skill_name, {"error": f"Unknown skill: {skill_name}"})
    hint = get_presentation_hint("example")
    if hint:
        result = {**result, "_presentation_hint": hint}
    return result
"""


def generate_llm(skill_name: str, content: str) -> str:
    """Call Gemini 1.5 Pro to generate a FastMCP main.py."""
    try:
        import google.generativeai as genai
    except ImportError:
        print("[add_skill] google-generativeai not installed. Run: pip install google-generativeai", file=sys.stderr)
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("[add_skill] GEMINI_API_KEY is not set.", file=sys.stderr)
        sys.exit(1)

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-pro")

    prompt = (
        f"Wrap this source into a FastMCP skill named '{skill_name}'.\n\n"
        f"Follow this exact pattern:\n```python\n{_LLM_EXAMPLE}\n```\n\n"
        f"SOURCE:\n{content}\n\n"
        "Rules:\n"
        "1. Must define `mcp = FastMCP(...)` at module level.\n"
        "2. Every tool must have `@mcp.tool()` and a docstring.\n"
        "3. Return ONLY valid Python — no markdown fences, no explanations."
    )

    print("Calling Gemini 1.5 Pro ...")
    text = model.generate_content(prompt).text.strip()
    # Strip accidental markdown fences if Gemini adds them
    text = re.sub(r"^```python\n?", "", text)
    text = re.sub(r"\n?```$", "", text)
    return text.strip()


# ── Step 3: Validate syntax ─────────────────────────────────────────────────

def validate_syntax(source: str) -> None:
    with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as f:
        f.write(source.encode())
        tmp_path = f.name
    try:
        py_compile.compile(tmp_path, doraise=True)
    except py_compile.PyCompileError as e:
        print(f"[add_skill] Syntax error in generated code:\n{e}", file=sys.stderr)
        sys.exit(1)
    finally:
        Path(tmp_path).unlink(missing_ok=True)


# ── Step 5: Register ────────────────────────────────────────────────────────

def register_in_provision(skill_name: str, tiers: list[str]) -> None:
    content = _PROVISION_PY.read_text()
    match = re.search(r"(_PLAN_SKILLS\s*:[^=]+=\s*)(\{.*?\})", content, re.DOTALL)
    if not match:
        print("[add_skill] Could not find _PLAN_SKILLS in provision.py — skipping.", file=sys.stderr)
        return

    current: dict[str, list[str]] = ast.literal_eval(match.group(2))
    changed = False
    for tier in tiers:
        if tier in current and skill_name not in current[tier]:
            current[tier].append(skill_name)
            changed = True

    if not changed:
        return

    lines = ["{\n"]
    for tier, skills in current.items():
        if len(skills) <= 3:
            inner = ", ".join(f'"{s}"' for s in skills)
            lines.append(f'    "{tier}": [{inner}],\n')
        else:
            lines.append(f'    "{tier}": [\n')
            for s in skills:
                lines.append(f'        "{s}",\n')
            lines.append("    ],\n")
    lines.append("}")

    new_content = content[: match.start(2)] + "".join(lines) + content[match.end(2) :]
    _PROVISION_PY.write_text(new_content)


def register_in_clients_json(skill_name: str) -> None:
    """Add skill to data/local_config.json enabled_skills."""
    config_path = _REPO_ROOT / "data" / "local_config.json"
    config_path.parent.mkdir(parents=True, exist_ok=True)
    if config_path.exists():
        data = json.loads(config_path.read_text())
    else:
        data = {"enabled_skills": [], "skill_configs": {}, "connections": {}}
    skills: list[str] = data.get("enabled_skills", [])
    if skill_name not in skills:
        skills.append(skill_name)
        data["enabled_skills"] = skills
        config_path.write_text(json.dumps(data, indent=2) + "\n")


# ── Step 4: Split detection ─────────────────────────────────────────────────

_SPLIT_DETECT_PROMPT = """\
You are deciding how to add a GitHub repository as skills for an AI assistant platform.

Two options:
A) SPLIT — the repo contains multiple UNRELATED skills from different domains (e.g. a collection of 50 skills across business, marketing, coding, cooking). Each skill should become a separate folder.
B) NO_SPLIT — the repo covers one cohesive topic (e.g. all Amazon seller tools, all SEO skills). Keep as one folder.

Respond with ONLY a JSON object:
{{
  "split": true or false,
  "reason": "one sentence explaining why",
  "suggested_skill_names": ["slug-one", "slug-two", ...]  // only if split=true, suggest snake_case folder names
}}

Repository content:
{content}
"""


_DOC_SECTIONS = {
    "contents", "table of contents", "toc",
    "license", "contributing", "installation", "usage",
    "getting started", "quick start", "prerequisites",
    "requirements", "setup", "faq", "changelog", "roadmap",
    "about", "acknowledgements", "references", "resources",
    "platforms", "contact",
}

_NON_SKILL_DIRS = frozenset({
    "node_modules", ".git", "__pycache__", "dist", "build",
    "test", "tests", "docs", "examples", ".github", ".vscode",
})


def _is_skill_dir(d: Path) -> bool:
    return (
        d.is_dir()
        and not d.name.startswith(".")
        and d.name not in _NON_SKILL_DIRS
        and any((d / f).exists() for f in ("SKILL.md", "main.py", "README.md", "readme.md"))
    )


def _find_skill_dirs(root: Path, subdir: str | None = None) -> list[Path]:
    """Find subdirectories that look like individual skill folders.

    When subdir is given, searches root/subdir recursively for dirs containing
    SKILL.md (handles 2-level hierarchies like skills/category/skill/SKILL.md).
    When subdir is None, uses the original container-then-root-level heuristic.
    """
    if subdir:
        search_root = root / subdir
        if not search_root.exists():
            print(f"[warn] '{subdir}' not found in repo — searching root instead")
            search_root = root
        skill_dirs = sorted({
            p.parent for p in search_root.rglob("SKILL.md")
            if not any(part in _NON_SKILL_DIRS for part in p.parts)
        })
        if skill_dirs:
            return skill_dirs
        return [d for d in sorted(search_root.iterdir()) if _is_skill_dir(d)]

    # Original logic (no --subdir): check container dirs, then root-level
    for container in ("skills", "plugins", "tools"):
        container_dir = root / container
        if container_dir.is_dir():
            nested = [d for d in sorted(container_dir.iterdir()) if _is_skill_dir(d)]
            if len(nested) > 1:
                return nested

    return [d for d in sorted(root.iterdir()) if _is_skill_dir(d)]


def detect_split_mode(content: str, tmp_dir: Path | None = None, subdir: str | None = None) -> tuple[bool, list[str]]:
    """Use Gemini to decide if a repo should be split into individual skills.

    Returns (should_split, suggested_skill_names).
    Falls back to heuristic if Gemini unavailable.
    """
    # Primary heuristic: presence of skill subdirectories is a stronger signal than README sections
    if tmp_dir:
        skill_dirs = _find_skill_dirs(tmp_dir, subdir=subdir)
        if len(skill_dirs) > 1:
            names = [_to_snake(d.name) for d in skill_dirs]
            api_key = os.environ.get("GEMINI_API_KEY")
            if not api_key:
                print(f"[detect] GEMINI_API_KEY not set — found {len(skill_dirs)} skill dirs → split=True")
                return True, names
            # Subdirs confirm split; still try Gemini for better slug names
            heuristic_split = True
        else:
            # No subdirs — fall back to README section count
            readme_sections = re.findall(r"^## (.+)$", content, re.MULTILINE)
            skill_sections = [s for s in readme_sections if s.lower().strip() not in _DOC_SECTIONS]
            heuristic_split = len(skill_sections) > 4
    else:
        readme_sections = re.findall(r"^## (.+)$", content, re.MULTILINE)
        skill_sections = [s for s in readme_sections if s.lower().strip() not in _DOC_SECTIONS]
        heuristic_split = len(skill_sections) > 4

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print(f"[detect] GEMINI_API_KEY not set — using heuristic (split={heuristic_split})")
        return heuristic_split, []

    try:
        import google.generativeai as genai
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-2.0-flash")
        prompt = _SPLIT_DETECT_PROMPT.format(content=content[:6000])
        raw = model.generate_content(prompt).text.strip()
        raw = re.sub(r"^```(?:json)?\n?", "", raw)
        raw = re.sub(r"\n?```$", "", raw)
        result = json.loads(raw)
        return bool(result.get("split")), result.get("suggested_skill_names", [])
    except Exception as e:
        print(f"[detect] Gemini detection failed ({e}), using heuristic (split={heuristic_split})")
        return heuristic_split, []


_SPLIT_GENERATE_PROMPT = """\
You are wrapping a GitHub repository into multiple individual FastMCP skills.

Each skill must follow this exact pattern:
```python
from fastmcp import FastMCP

mcp = FastMCP("skill-slug")

_GUIDANCE = {{
    "display_name": "Human Name",
    "description": "One sentence.",
    "guidance": "Full markdown guidance here.",
}}

@mcp.tool()
def get_guidance() -> dict:
    \"\"\"Get the full guidance for this skill.\"\"\"
    return _GUIDANCE
```

Source repository content:
{content}

Identify the distinct skills and generate one Python module per skill.

Return ONLY a JSON array (no markdown fences):
[
  {{
    "slug": "skill-slug",
    "folder_name": "skill_folder_name",
    "source": "python module source as string"
  }},
  ...
]
"""


def generate_split_skills(
    hub_name: str, content: str, suggested: list[str], tmp_dir: Path | None = None, subdir: str | None = None
) -> list[tuple[str, str]]:
    """Use Gemini to split a hub repo into individual skill (folder_name, main_py) pairs.

    Falls back to subdirectory structure, then README sections.
    """
    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key:
        try:
            import google.generativeai as genai
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel("gemini-2.0-flash")
            print("Calling Gemini to generate individual skills...")
            raw = model.generate_content(
                _SPLIT_GENERATE_PROMPT.format(content=content[:8000])
            ).text.strip()
            raw = re.sub(r"^```(?:json)?\n?", "", raw)
            raw = re.sub(r"\n?```$", "", raw)
            items = json.loads(raw)
            results: list[tuple[str, str]] = []
            for item in items:
                folder = _to_snake(item.get("folder_name") or item.get("slug", "skill"))
                source = item.get("source", "")
                if source:
                    results.append((folder, source))
            if results:
                return results
        except Exception as e:
            print(f"[split] Gemini generation failed ({e}), falling back to template")

    # Template fallback 1: use skill subdirectories if present
    if tmp_dir:
        skill_dirs = _find_skill_dirs(tmp_dir, subdir=subdir)
        if skill_dirs:
            print(f"[split] Using {len(skill_dirs)} skill subdirectories as source")
            results = []
            for skill_dir in skill_dirs:
                folder = _to_snake(skill_dir.name)
                subdir_content = _read_dir(skill_dir)
                source = generate_template(folder, subdir_content)
                results.append((folder, source))
            return results

    # Template fallback 2: one folder per README ## section
    sections = _parse_readme_sections(content)
    if not sections:
        sections = [(_to_kebab(hub_name), f"{hub_name} skill.", content[:4000])]

    results = []
    for slug, desc, guidance in sections:
        folder = _to_snake(slug)
        source = (
            f'"""Skill: {slug.replace("-", " ").title()}."""\n\n'
            f"from fastmcp import FastMCP\n\n"
            f'mcp = FastMCP("{slug}")\n\n\n'
            f"_GUIDANCE = {{'display_name': {repr(slug.replace('-', ' ').title())}, "
            f"'description': {repr(desc)}, 'guidance': {repr(guidance)}}}\n\n\n"
            f"@mcp.tool()\n"
            f"def get_guidance() -> dict:\n"
            f'    """Get the full guidance for this skill."""\n'
            f"    return _GUIDANCE\n"
        )
        results.append((folder, source))
    return results


def write_skill_meta(skill_dir: Path, folder_name: str, description: str, source_repo: str, theme: str = "_unthemed", subdir: str | None = None) -> None:
    """Write skill_meta.json for a newly created skill folder."""
    meta = {
        "display_name": folder_name.replace("_", " ").title(),
        "description": description,
        "source_repo": source_repo,
        "theme": theme,
    }
    if subdir:
        meta["subdir"] = subdir
    (skill_dir / "skill_meta.json").write_text(json.dumps(meta, indent=2) + "\n")


def _normalize_theme_slug(raw: str) -> str:
    """Convert a display-name theme to a snake_case slug. 'Data Analysis' → 'data_analysis'."""
    cleaned = raw.strip()
    if not cleaned or cleaned in ("_unthemed", "unthemed"):
        return "_unthemed"
    return re.sub(r"[^a-z0-9]+", "_", cleaned.lower()).strip("_") or "_unthemed"


def _theme_display_name(slug: str) -> str:
    """'data_analysis' → 'Data Analysis'"""
    return slug.replace("_", " ").title()


def add_to_themes_unthemed(skill_name: str) -> None:
    """Add a newly created skill to the _unthemed bucket in themes.json."""
    add_to_theme(skill_name, "_unthemed")


def add_to_theme(skill_name: str, theme_slug: str) -> None:
    """Add a skill to the specified theme bucket in themes.json, creating it if needed."""
    themes_path = _REPO_ROOT / "skills_library" / "themes.json"
    if not themes_path.exists():
        return
    theme_slug = _normalize_theme_slug(theme_slug)
    themes: dict = json.loads(themes_path.read_text())
    if theme_slug not in themes:
        themes[theme_slug] = {"name": _theme_display_name(theme_slug), "description": "", "skills": []}
    bucket = themes[theme_slug]
    if skill_name not in bucket["skills"]:
        bucket["skills"].append(skill_name)
    themes_path.write_text(json.dumps(themes, indent=2) + "\n")


def _ensure_theme_in_skills_ts(src: str, theme_slug: str) -> str:
    """Add a new THEMES entry to skills.ts if the slug doesn't exist. Returns updated src."""
    if f'slug: "{theme_slug}"' in src:
        return src
    display_name = _theme_display_name(theme_slug)
    new_theme = (
        f'  {{\n'
        f'    slug: "{theme_slug}",\n'
        f'    name: "{display_name}",\n'
        f'    description: "",\n'
        f'    skills: [\n'
        f'    ],\n'
        f'  }},'
    )
    # Insert before the closing `];` of THEMES
    return re.sub(r'(\n\];)', "\n" + new_theme + r'\1', src, count=1)


def _move_skill_in_skills_ts(src: str, skill_name: str, new_theme: str) -> str:
    """Move a skill entry from its current theme block to new_theme in skills.ts."""
    lines = src.splitlines(keepends=True)

    # Skill entries are at 6-space indent inside `skills: [`.
    # Track each opening `      {` as "pending"; if the very next name line matches
    # skill_name this is our entry, otherwise reset on closing `      },`.
    skill_start = None
    skill_end = None
    pending_open = None

    for i, line in enumerate(lines):
        stripped = line.rstrip("\n")

        if stripped == "      {":
            pending_open = i
        elif pending_open is not None and skill_start is None:
            if f'        name: "{skill_name}"' in line:
                skill_start = pending_open
            elif stripped in ("      },", "      }"):
                pending_open = None  # entry closed without matching name

        if skill_start is not None and i > skill_start:
            if stripped in ("      },", "      }"):
                skill_end = i
                break

    if skill_start is None or skill_end is None:
        return src

    skill_entry_lines = list(lines[skill_start : skill_end + 1])
    # Update the theme property inside the extracted entry
    skill_entry_lines = [
        re.sub(r'(theme:\s*")[^"]*(")', rf'\g<1>{new_theme}\2', ln)
        for ln in skill_entry_lines
    ]
    skill_entry = "".join(skill_entry_lines)
    # Ensure trailing newline so it joins cleanly
    if not skill_entry.endswith("\n"):
        skill_entry += "\n"

    # Remove from old location
    remaining = lines[: skill_start] + lines[skill_end + 1 :]
    src = "".join(remaining)

    # Ensure the target theme block exists
    src = _ensure_theme_in_skills_ts(src, new_theme)

    # Insert at the top of the target theme's skills array
    slug_pos = src.find(f'slug: "{new_theme}"')
    if slug_pos == -1:
        return src
    skills_open = src.find("skills: [", slug_pos)
    if skills_open == -1:
        return src
    insert_pos = src.find("\n", skills_open) + 1
    src = src[:insert_pos] + skill_entry + src[insert_pos:]
    return src


def register_in_skills_ts(skill_name: str, theme: str = "_unthemed") -> None:
    """Append a new skill entry to dashboard/lib/skills.ts."""
    if not _SKILLS_TS.exists():
        return
    src = _SKILLS_TS.read_text()
    if f'name: "{skill_name}"' in src:
        return

    skill_dir = _SKILLS_DIR / skill_name
    main_py = skill_dir / "main.py"
    if not main_py.exists():
        return

    main_src = main_py.read_text()
    tools = re.findall(r"@mcp\.tool\(\)\ndef ([a-z_]+)\(", main_src)

    display = skill_name.replace("_", " ").title()
    description = ""
    meta_path = skill_dir / "skill_meta.json"
    if meta_path.exists():
        try:
            meta = json.loads(meta_path.read_text())
            display = meta.get("display_name", display)
            description = meta.get("description", "") or ""
        except Exception:
            pass

    theme_slug = _normalize_theme_slug(theme)
    description = description.replace('"', '\\"')
    display = display.replace('"', '\\"')
    tools_ts = json.dumps(tools)
    new_entry = (
        f'      {{\n'
        f'        name: "{skill_name}",\n'
        f'        displayName: "{display}",\n'
        f'        description: "{description}",\n'
        f'        tools: {tools_ts},\n'
        f'        theme: "{theme_slug}",\n'
        f'      }},'
    )

    # Create the theme block in skills.ts if it doesn't exist yet
    src = _ensure_theme_in_skills_ts(src, theme_slug)

    slug_pos = src.find(f'slug: "{theme_slug}"')
    if slug_pos != -1:
        skills_open = src.find("skills: [", slug_pos)
        if skills_open != -1:
            close_match = re.search(r'\n    \],', src[skills_open:])
            if close_match:
                insert_pos = skills_open + close_match.start()
                src = src[:insert_pos] + "\n" + new_entry + src[insert_pos:]
                _SKILLS_TS.write_text(src)
                print(f"  Registered in skills.ts (theme: {theme_slug})")
                return

    # Fallback: insert before the THEMES closing `];`
    src = re.sub(r'(\n\];)', "\n" + new_entry + r'\1', src, count=1)
    _SKILLS_TS.write_text(src)
    print(f"  Registered in skills.ts (fallback)")


# ── Main ────────────────────────────────────────────────────────────────────

def _add_one_repo(
    url: str | None,
    file_path: str | None,
    name: str,
    plan: str = "pro",
    use_llm: bool = False,
    force_split: bool = False,
    force_no_split: bool = False,
    non_interactive: bool = False,
    theme: str = "_unthemed",
    description: str = "",
    subdir: str | None = None,
    pre_cloned_dir: Path | None = None,
) -> bool:
    """Add a single repo or file as skill(s). Returns True on success.

    pre_cloned_dir: if provided, use this already-cloned directory instead of
    cloning again. The caller owns the directory and is responsible for cleanup.
    """
    import types

    hub_name = _to_snake(name)
    tiers = _TIER_INCLUSIONS[plan]

    if pre_cloned_dir and pre_cloned_dir.exists():
        content = _read_dir(pre_cloned_dir)
        tmp_dir = None      # caller owns this dir — don't clean it up
        src_dir = pre_cloned_dir
    else:
        fake_args = types.SimpleNamespace(url=url, file=file_path)
        content, tmp_dir = collect_content(fake_args)
        src_dir = tmp_dir

    try:
        if force_no_split:
            do_split = False
            suggested: list[str] = []
        elif force_split:
            do_split = True
            suggested = []
        else:
            do_split, suggested = detect_split_mode(content, src_dir, subdir=subdir)
            if non_interactive:
                print(f"  [auto] split={do_split}" + (f", suggested: {suggested[:3]}" if suggested else ""))
            else:
                print(f"\n[auto-detect] split={do_split}" + (f", suggested: {suggested[:3]}" if suggested else ""))
                answer = input(f"Proceed with split={do_split}? [Y/n] ").strip().lower()
                if answer in ("n", "no"):
                    do_split = not do_split
                    print(f"  → Using split={do_split}")

        if do_split:
            _run_split(hub_name, content, suggested, tiers, src_dir, theme=theme, source_repo=url or "", description=description, subdir=subdir)
        else:
            _run_single(hub_name, content, use_llm, tiers, src_dir, theme=theme, source_repo=url or "", description=description, subdir=subdir)
        return True

    except SystemExit:
        return False
    finally:
        if tmp_dir and tmp_dir.exists():
            shutil.rmtree(tmp_dir, ignore_errors=True)


def _run_bulk(bulk_file: str, plan: str, use_llm: bool) -> None:
    """Add multiple skills from a CSV or JSON file.

    CSV format (with header row):  url,name,plan,split,theme,description
    JSON format:                   [{"url": "...", "name": "...", "plan": "pro", "split": "auto", "theme": "marketing", "description": "..."}, ...]
    CSV column headers are case-insensitive and leading/trailing whitespace is stripped.

    split values: auto (default) | split | no-split
    theme values: any slug from themes.json (default: _unthemed)
    """
    import csv

    path = Path(bulk_file).expanduser().resolve()
    if not path.exists():
        print(f"[bulk] File not found: {path}", file=sys.stderr)
        sys.exit(1)

    entries: list[dict] = []
    if path.suffix == ".json":
        entries = json.loads(path.read_text())
    else:
        with path.open(encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            entries = [{k.strip().lower(): v for k, v in row.items()} for row in reader]

    if not entries:
        print("[bulk] No entries found.", file=sys.stderr)
        sys.exit(1)

    # Clone each unique URL once and reuse the directory across all entries
    # that share the same URL. Without this, a 74-entry bulk CSV from one repo
    # would clone 74 times instead of 1.
    unique_urls = sorted({e.get("url", "").strip() for e in entries if e.get("url", "").strip()})
    url_clones: dict[str, Path] = {}
    if unique_urls:
        print(f"[bulk] Pre-cloning {len(unique_urls)} unique repo(s) ...")
        for repo_url in unique_urls:
            tmp = Path(tempfile.mkdtemp())
            result = subprocess.run(
                ["git", "clone", "--depth", "1", repo_url, str(tmp)],
                capture_output=True, text=True,
            )
            if result.returncode == 0:
                url_clones[repo_url] = tmp
                print(f"  ✓ {repo_url}")
            else:
                shutil.rmtree(tmp, ignore_errors=True)
                print(f"  ✗ {repo_url} (clone failed — will retry per-entry)")

    print(f"[bulk] Processing {len(entries)} repo(s) ...")
    succeeded: list[str] = []
    failed: list[str] = []
    has_unthemed = False

    try:
        for i, entry in enumerate(entries, 1):
            url = entry.get("url", "").strip()
            name = entry.get("name", "").strip()
            entry_plan = entry.get("plan", plan).strip() or plan
            split_flag = entry.get("split", "auto").strip().lower()
            entry_theme = entry.get("theme", "_unthemed").strip() or "_unthemed"
            entry_description = entry.get("description", "").strip()

            if not url or not name:
                print(f"  [{i}] SKIP — missing url or name: {entry}")
                failed.append(name or url or f"entry-{i}")
                continue

            force_split = split_flag == "split"
            force_no_split = split_flag in ("no-split", "no_split")
            entry_subdir = entry.get("subdir", "").strip() or None
            if entry_theme == "_unthemed":
                has_unthemed = True

            print(f"\n  [{i}/{len(entries)}] {name} ← {url}" + (f" (subdir: {entry_subdir})" if entry_subdir else ""))
            ok = _add_one_repo(
                url=url,
                file_path=None,
                name=name,
                plan=entry_plan,
                use_llm=use_llm,
                force_split=force_split,
                force_no_split=force_no_split,
                non_interactive=True,
                theme=entry_theme,
                description=entry_description,
                subdir=entry_subdir,
                pre_cloned_dir=url_clones.get(url),
            )
            (succeeded if ok else failed).append(name)
    finally:
        for tmp in url_clones.values():
            shutil.rmtree(tmp, ignore_errors=True)

    print(f"\n{'=' * 40}")
    print(f"[bulk] Done: {len(succeeded)} succeeded, {len(failed)} failed")
    if succeeded:
        print(f"  OK:   {', '.join(succeeded)}")
    if failed:
        print(f"  FAIL: {', '.join(failed)}")
    if succeeded and has_unthemed:
        print(f"\nNext: python scripts/organize_themes.py --propose")


def _read_skill_theme(skill_name: str) -> str:
    """Read the theme for a skill from skill_meta.json → normalized slug."""
    meta_path = _SKILLS_DIR / skill_name / "skill_meta.json"
    if meta_path.exists():
        try:
            meta = json.loads(meta_path.read_text())
            raw = meta.get("theme", "_unthemed") or "_unthemed"
            return _normalize_theme_slug(raw)
        except Exception:
            pass
    return "_unthemed"


def _find_skills_by_source_repo(source_repo: str, subdir: str | None = None) -> list[str]:
    """Return folder names of existing skills whose skill_meta.json matches source_repo.

    When subdir is given, only matches skills that were imported from the same
    subdir slice — preventing bulk imports of different subdirs from the same
    repo from deleting each other.
    """
    if not source_repo:
        return []
    normalized = source_repo.rstrip("/").removesuffix(".git")
    matches = []
    for skill_dir in sorted(_SKILLS_DIR.iterdir()):
        if not skill_dir.is_dir():
            continue
        meta_path = skill_dir / "skill_meta.json"
        if not meta_path.exists():
            continue
        try:
            meta = json.loads(meta_path.read_text())
            existing = meta.get("source_repo", "").rstrip("/").removesuffix(".git")
            if existing and existing == normalized:
                if subdir:
                    if meta.get("subdir", "") == subdir:
                        matches.append(skill_dir.name)
                else:
                    matches.append(skill_dir.name)
        except Exception:
            pass
    return matches


def _run_sync() -> None:
    """Backfill and fix-themes for every skill folder in skills_library/."""
    if not _SKILLS_TS.exists():
        print("[sync] dashboard/lib/skills.ts not found — nothing to do.", file=sys.stderr)
        return

    src = _SKILLS_TS.read_text()

    # name → which THEME BLOCK the skill is actually nested in (by slug: "..." line above)
    block_of: dict[str, str] = {}
    current_slug = None
    for line in src.splitlines():
        m = re.match(r'    slug:\s*"([^"]+)"', line)
        if m:
            current_slug = m.group(1)
        m2 = re.match(r'        name:\s*"([^"]+)"', line)
        if m2 and current_slug:
            block_of[m2.group(1)] = current_slug

    candidates = sorted(
        d.name for d in _SKILLS_DIR.iterdir()
        if d.is_dir() and (d / "main.py").exists() and not d.name.startswith(".")
    )

    missing = [c for c in candidates if c not in block_of]
    # wrong_theme: skill is nested in the wrong block (not matching skill_meta.json)
    wrong_theme = [
        c for c in candidates
        if c in block_of and block_of[c] != _read_skill_theme(c)
    ]

    if not missing and not wrong_theme:
        print("[sync] skills.ts is already up to date.")
        return

    if missing:
        print(f"[sync] Registering {len(missing)} missing skill(s) ...")
        for skill_name in missing:
            theme = _read_skill_theme(skill_name)
            add_to_theme(skill_name, theme)
            register_in_skills_ts(skill_name, theme)

    if wrong_theme:
        print(f"[sync] Fixing theme for {len(wrong_theme)} skill(s) ...")
        # Re-read src after potential inserts above
        src = _SKILLS_TS.read_text()
        for skill_name in wrong_theme:
            correct = _read_skill_theme(skill_name)
            old = block_of[skill_name]
            src = _move_skill_in_skills_ts(src, skill_name, correct)
            add_to_theme(skill_name, correct)
            print(f"  {skill_name}: {old} → {correct}")
        _SKILLS_TS.write_text(src)

    print(f"[sync] Done.")



def main() -> None:
    parser = argparse.ArgumentParser(
        description="Add a skill to skills_library/ from a GitHub URL or local file."
    )
    src = parser.add_mutually_exclusive_group(required=True)
    src.add_argument("--url", help="GitHub repository URL")
    src.add_argument("--file", help="Local .py file, .zip, or directory")
    src.add_argument("--bulk", metavar="FILE", help="CSV or JSON file with repos to add in bulk (non-interactive)")
    src.add_argument("--sync", action="store_true", help="Backfill dashboard/lib/skills.ts for all skills already in skills_library/")
    parser.add_argument("--name", help="Skill name (snake_case) — required unless --bulk")
    parser.add_argument(
        "--plan",
        choices=["basic", "pro", "enterprise", "all"],
        default="pro",
        help="Plan tier(s) to assign this skill to (default: pro)",
    )
    parser.add_argument("--llm", action="store_true", help="Use Gemini to generate the wrapper")

    split_group = parser.add_mutually_exclusive_group()
    split_group.add_argument("--split", action="store_true", help="Force split repo into individual skill folders")
    split_group.add_argument("--no-split", action="store_true", dest="no_split", help="Force keep repo as one skill folder")
    split_group.add_argument("--auto", action="store_true", default=True, help="LLM detects split vs single (default)")

    parser.add_argument(
        "--subdir",
        metavar="PATH",
        default=None,
        help=(
            "Process only this subdirectory of the repo "
            "(e.g. 'skills/01-devops-basics', 'plugins/devops'). "
            "Uses recursive SKILL.md search to handle deep-nested skill hierarchies."
        ),
    )

    args = parser.parse_args()

    if args.sync:
        _run_sync()
        return

    if args.bulk:
        _run_bulk(args.bulk, args.plan, args.llm)
        return

    if not args.name:
        parser.error("--name is required when not using --bulk")

    _add_one_repo(
        url=args.url,
        file_path=args.file,
        name=args.name,
        plan=args.plan,
        use_llm=args.llm,
        force_split=args.split,
        force_no_split=args.no_split,
        subdir=args.subdir,
    )


def _run_single(skill_name: str, content: str, use_llm: bool, tiers: list[str], tmp_dir: Path | None, theme: str = "_unthemed", source_repo: str = "", description: str = "", subdir: str | None = None) -> None:
    """Add the repo as a single skill folder (original behavior)."""
    # Remove any existing skills that came from the same source repo (may have a different folder name).
    # When subdir is set, only match skills from the same subdir so bulk imports of
    # multiple subdirs from one repo don't delete each other.
    for existing in _find_skills_by_source_repo(source_repo, subdir=subdir):
        existing_dir = _SKILLS_DIR / existing
        label = existing if existing == skill_name else f"{existing} (was {existing!r}, now {skill_name!r})"
        print(f"  [replace] '{label}' already exists — replacing contents ...")
        shutil.rmtree(existing_dir, ignore_errors=True)

    skill_dir = _SKILLS_DIR / skill_name
    if skill_dir.exists():
        print(f"  [replace] '{skill_name}' already exists — replacing contents ...")
        shutil.rmtree(skill_dir)

    try:
        skill_dir.mkdir(parents=True)
        (skill_dir / "__init__.py").write_text("")

        # Index SKILL.md files before generating template so slugs feed file-pointer mode
        skill_files: list[tuple[str, str]] = []
        if tmp_dir:
            skill_files = _copy_skill_files(tmp_dir, skill_dir, source_repo=source_repo)

        if use_llm:
            source = generate_llm(skill_name, content)
        else:
            source = generate_template(skill_name, content, skill_files=skill_files or None)
        validate_syntax(source)

        (skill_dir / "main.py").write_text(source)
        write_skill_meta(skill_dir, skill_name, description, source_repo, theme=theme, subdir=subdir)
        add_to_theme(skill_name, theme)
        register_in_skills_ts(skill_name, theme)

        register_in_clients_json(skill_name)

    except Exception:
        shutil.rmtree(skill_dir, ignore_errors=True)
        raise

    theme_note = f"Added to themes.json ({theme})"
    next_step = "" if theme != "_unthemed" else f"\nNext: python scripts/organize_themes.py --assign {skill_name} <theme>\n"
    print(
        f"\n  Created   skills_library/{skill_name}/main.py\n"
        f"  {theme_note}\n"
        f"  Added to data/local_config.json (enabled)\n"
        f"{next_step}"
    )


def _run_split(hub_name: str, content: str, suggested: list[str], tiers: list[str], tmp_dir: Path | None, theme: str = "_unthemed", source_repo: str = "", description: str = "", subdir: str | None = None) -> None:
    """Split repo into multiple individual skill folders."""
    skill_pairs = generate_split_skills(hub_name, content, suggested, tmp_dir, subdir=subdir)
    if not skill_pairs:
        print("[add_skill] Split generation returned no skills. Try --no-split.", file=sys.stderr)
        sys.exit(1)

    # Remove all existing skills from the same source repo (and same subdir, if given)
    # before creating new split folders.
    new_names = {folder for folder, _ in skill_pairs}
    for existing in _find_skills_by_source_repo(source_repo, subdir=subdir):
        if existing not in new_names:
            print(f"  [remove]   {existing}/ (previously from same source, no longer in split)")
        else:
            print(f"  [replace]  {existing}/ (replacing existing)")
        shutil.rmtree(_SKILLS_DIR / existing, ignore_errors=True)

    print(f"\n  Splitting into {len(skill_pairs)} individual skill(s):")
    created: list[str] = []
    failed: list[str] = []

    # Pre-build lookup: snake_case folder name → actual source path on disk.
    # This handles deep-nested repos (e.g. skills/category/skill-name/) where
    # the naive tmp_dir/folder_name lookup would miss the correct path.
    name_to_src: dict[str, Path] = {}
    if tmp_dir:
        for d in _find_skill_dirs(tmp_dir, subdir=subdir):
            name_to_src[_to_snake(d.name)] = d

    for folder_name, source in skill_pairs:
        skill_dir = _SKILLS_DIR / folder_name
        if skill_dir.exists():
            print(f"  [replace]  {folder_name}/ (replacing existing)")
            shutil.rmtree(skill_dir)

        try:
            validate_syntax(source)
            skill_dir.mkdir(parents=True)
            (skill_dir / "__init__.py").write_text("")
            (skill_dir / "main.py").write_text(source)

            # Locate the source dir for SKILL.md indexing
            if tmp_dir:
                src_path = name_to_src.get(folder_name)
                if src_path:
                    _copy_skill_files(src_path, skill_dir, source_repo=source_repo)
                else:
                    # Fallback for Gemini-generated names that differ from dir names
                    for container in ("skills", "tools", "plugins"):
                        candidate = tmp_dir / container / folder_name
                        if candidate.exists():
                            _copy_skill_files(candidate, skill_dir, source_repo=source_repo)
                            break
                    else:
                        _copy_skill_files(tmp_dir, skill_dir, source_repo=source_repo)

            write_skill_meta(skill_dir, folder_name, description, source_repo, theme=theme, subdir=subdir)
            add_to_theme(folder_name, theme)
            register_in_skills_ts(folder_name, theme)
            register_in_clients_json(folder_name)
            print(f"  [OK]    {folder_name}/")
            created.append(folder_name)
        except Exception as exc:
            print(f"  [FAIL]  {folder_name}/: {exc}")
            shutil.rmtree(skill_dir, ignore_errors=True)
            failed.append(folder_name)

    print(f"\n  Created {len(created)} skill(s), failed {len(failed)}")
    if created:
        print(f"  Added to themes.json ({theme})")
        if theme == "_unthemed":
            print(f"\nNext: python scripts/organize_themes.py --propose  # regroup all skills into themes")


if __name__ == "__main__":
    main()
