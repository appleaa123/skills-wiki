"""Skill: understand_anything."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("understand-anything")


_SKILLS: dict[str, dict] = {
    'features': {
        "description": '> [!NOTE]\n> **Want to skip the reading?** Try the [live demo](https://understand-anything.',
        "guidance": '> [!NOTE]\n> **Want to skip the reading?** Try the [live demo](https://understand-anything.com/demo/) in our [homepage](https://understand-anything.com/) — a fully interactive dashboard you can pan, zoom, search, and explore right in your browser.\n\n### Explore the structural graph\n\nNavigate your codebase as an interactive knowledge graph — every file, function, and class is a node you can click, search, and explore. Select any node to see plain-English summaries, relationships, and guided tours.\n\n<p align="center">\n  <img src="assets/overview-structural.gif" alt="Structural graph — explore files, functions, classes and their relationships" width="750" />\n</p>\n\n### Understand business logic\n\nSwitch to the domain view and see how your code maps to real business processes — domains, flows, and steps laid out as a horizontal graph.\n\n<p align="center">\n  <img src="assets/overview-domain.gif" alt="Domain graph — business domains, flows, and process steps" width="750" />\n</p>\n\n### Analyze knowledge bases\n\nPoint `/understand-knowledge` at a [Karpathy-pattern LLM wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) and get a force-directed knowledge graph with community clustering. The deterministic parser extracts wikilinks and categories from `index.md`, then LLM agents discover implicit relationships, extract entities, and surface claims — turning your wiki into a navigable graph of interconnected ideas.\n\n<table>\n  <tr>\n    <td width="50%" valign="top">\n      <h3>🧭 Guided Tours</h3>\n      <p>Auto-generated walkthroughs of the architecture, ordered by dependency. Learn the codebase in the right order.</p>\n    </td>\n    <td width="50%" valign="top">\n      <h3>🔍 Fuzzy & Semantic Search</h3>\n      <p>Find anything by name or by meaning. Search "which parts handle auth?" and get relevant results across the graph.</p>\n    </td>\n  </tr>\n  <tr>\n    <td width="50%" valign="top">\n      <h3>📊 Diff Impact Analysis</h3>\n      <p>See which parts of the system your changes affect before you commit. Understand ripple effects across the codebase.</p>\n    </td>\n    <td width="50%" valign="top">\n      <h3>🎭 Persona-Adaptive UI</h3>\n      <p>The dashboard adjusts its detail level based on who you are — junior dev, PM, or power user.</p>\n    </td>\n  </tr>\n  <tr>\n    <td width="50%" valign="top">\n      <h3>🏗️ Layer Visualization</h3>\n      <p>Automatic grouping by architectural layer — API, Service, Data, UI, Utility — with color-coded legend.</p>\n    </td>\n    <td width="50%" valign="top">\n      <h3>📚 Language Concepts</h3>\n      <p>12 programming patterns (generics, closures, decorators, etc.) explained in context wherever they appear.</p>\n    </td>\n  </tr>\n</table>\n\n---',
    },
    'quick-start': {
        "description": '### 1.',
        "guidance": '### 1. Install the plugin\n\n```bash\n/plugin marketplace add Lum1104/Understand-Anything\n/plugin install understand-anything\n```\n\n### 2. Analyze your codebase\n\n```bash\n/understand\n```\n\nA multi-agent pipeline scans your project, extracts every file, function, class, and dependency, then builds a knowledge graph saved to `.understand-anything/knowledge-graph.json`.\n\n### 3. Explore the dashboard\n\n```bash\n/understand-dashboard\n```\n\nAn interactive web dashboard opens with your codebase visualized as a graph — color-coded by architectural layer, searchable, and clickable. Select any node to see its code, relationships, and a plain-English explanation.\n\n### 4. Keep learning\n\n```bash\n# Ask anything about the codebase\n/understand-chat How does the payment flow work?\n\n# Analyze impact of your current changes\n/understand-diff\n\n# Deep-dive into a specific file or function\n/understand-explain src/auth/login.ts\n\n# Generate an onboarding guide for new team members\n/understand-onboard\n\n# Extract business domain knowledge (domains, flows, steps)\n/understand-domain\n\n# Analyze a Karpathy-pattern LLM wiki knowledge base\n/understand-knowledge ~/path/to/wiki\n```\n\n---',
    },
    'multi-platform-installation': {
        "description": 'Understand-Anything works across multiple AI coding platforms.',
        "guidance": 'Understand-Anything works across multiple AI coding platforms.\n\n### Claude Code (Native)\n\n```bash\n/plugin marketplace add Lum1104/Understand-Anything\n/plugin install understand-anything\n```\n\n### Codex\n\nTell Codex:\n```\nFetch and follow instructions from https://raw.githubusercontent.com/Lum1104/Understand-Anything/refs/heads/main/.codex/INSTALL.md\n```\n\n### OpenCode\n\nTell OpenCode:\n```\nFetch and follow instructions from https://raw.githubusercontent.com/Lum1104/Understand-Anything/refs/heads/main/.opencode/INSTALL.md\n```\n\n### OpenClaw\n\nTell OpenClaw:\n```\nFetch and follow instructions from https://raw.githubusercontent.com/Lum1104/Understand-Anything/refs/heads/main/.openclaw/INSTALL.md\n```\n\n### Cursor\n\nCursor auto-discovers the plugin via `.cursor-plugin/plugin.json` when this repo is cloned. No manual installation needed — just clone and open in Cursor.\n\n### VS Code + GitHub Copilot\n\nVS Code with GitHub Copilot (v1.108+) auto-discovers the plugin via `.copilot-plugin/plugin.json` when this repo is cloned. No manual installation needed — just clone and open in VS Code.\n\nFor personal skills (available across all projects), tell GitHub Copilot:\n```text\nFetch and follow instructions from https://raw.githubusercontent.com/Lum1104/Understand-Anything/refs/heads/main/.vscode/INSTALL.md\n```\n\n### Copilot CLI\n\n```bash\ncopilot plugin install Lum1104/Understand-Anything:understand-anything-plugin\n```\n\n### Antigravity\n\nTell Antigravity:\n```text\nFetch and follow instructions from https://raw.githubusercontent.com/Lum1104/Understand-Anything/refs/heads/main/.antigravity/INSTALL.md\n```\n\n### Gemini CLI\n\nTell Gemini CLI:\n```text\nFetch and follow instructions from https://raw.githubusercontent.com/Lum1104/Understand-Anything/refs/heads/main/.gemini/INSTALL.md\n```\n\n### Pi Agent\n\nTell Pi Agent:\n```text\nFetch and follow instructions from https://raw.githubusercontent.com/Lum1104/Understand-Anything/refs/heads/main/.pi/INSTALL.md\n```\n\n### Platform Compatibility\n\n| Platform | Status | Install Method |\n|----------|--------|----------------|\n| Claude Code | ✅ Native | Plugin marketplace |\n| Codex | ✅ Supported | AI-driven install |\n| OpenCode | ✅ Supported | AI-driven install |\n| OpenClaw | ✅ Supported | AI-driven install |\n| Cursor | ✅ Supported | Auto-discovery |\n| VS Code + GitHub Copilot | ✅ Supported | Auto-discovery |\n| Copilot CLI | ✅ Supported | Plugin install |\n| Antigravity | ✅ Supported | AI-driven install |\n| Gemini CLI | ✅ Supported | AI-driven install |\n| Pi Agent | ✅ Supported | AI-driven install |\n\n---',
    },
    'share-the-graph-with-your-team': {
        "description": 'The graph is just JSON — **commit it once, and teammates skip the pipeline**.',
        "guidance": 'The graph is just JSON — **commit it once, and teammates skip the pipeline**. Good for onboarding, PR reviews, and docs-as-code.\n\n> **Example:** [GoogleCloudPlatform/microservices-demo (fork)](https://github.com/Lum1104/microservices-demo) — Go / Java / Python / Node reference with a committed graph.\n\n**What to commit:** everything in `.understand-anything/` *except* `intermediate/` and `diff-overlay.json` (those are local scratch).\n\n```gitignore\n.understand-anything/intermediate/\n.understand-anything/diff-overlay.json\n```\n\n**Keep it fresh:** enable `/understand --auto-update` — a post-commit hook incrementally patches the graph so each commit lands with a matching graph. Or re-run `/understand` manually before releases.\n\n**Large graphs (10 MB+):** track with **git-lfs**.\n\n```bash\ngit lfs install\ngit lfs track ".understand-anything/*.json"\ngit add .gitattributes .understand-anything/\n```\n\n---',
    },
    'under-the-hood': {
        "description": '### Multi-Agent Pipeline\n\nThe `/understand` command orchestrates 5 specialized agents, and `/understand-domain` adds a 6th:\n\n| Agent | Role |\n|-------|------|\n| `project-scanner` | Discover files, det',
        "guidance": '### Multi-Agent Pipeline\n\nThe `/understand` command orchestrates 5 specialized agents, and `/understand-domain` adds a 6th:\n\n| Agent | Role |\n|-------|------|\n| `project-scanner` | Discover files, detect languages and frameworks |\n| `file-analyzer` | Extract functions, classes, imports; produce graph nodes and edges |\n| `architecture-analyzer` | Identify architectural layers |\n| `tour-builder` | Generate guided learning tours |\n| `graph-reviewer` | Validate graph completeness and referential integrity (runs inline by default; use `--review` for full LLM review) |\n| `domain-analyzer` | Extract business domains, flows, and process steps (used by `/understand-domain`) |\n| `article-analyzer` | Extract entities, claims, and implicit relationships from wiki articles (used by `/understand-knowledge`) |\n\nFile analyzers run in parallel (up to 5 concurrent, 20-30 files per batch). Supports incremental updates — only re-analyzes files that changed since the last run.\n\n---',
    },
    'contributing': {
        "description": "Contributions are welcome! Here's how to get started:\n\n1.",
        "guidance": 'Contributions are welcome! Here\'s how to get started:\n\n1. Fork the repository\n2. Create a feature branch (`git checkout -b feature/my-feature`)\n3. Run the tests (`pnpm --filter @understand-anything/core test`)\n4. Commit your changes and open a pull request\n\nPlease open an issue first for major changes so we can discuss the approach.\n\n---\n\n<p align="center">\n  <strong>Stop reading code blind. Start understanding everything.</strong>\n</p>',
    },
    'star-history': {
        "description": '<a href="https://www.',
        "guidance": '<a href="https://www.star-history.com/?repos=Lum1104%2FUnderstand-Anything&type=date&legend=top-left">\n <picture>\n   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/image?repos=Lum1104/Understand-Anything&type=date&theme=dark&legend=top-left" />\n   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/image?repos=Lum1104/Understand-Anything&type=date&legend=top-left" />\n   <img alt="Star History Chart" src="https://api.star-history.com/image?repos=Lum1104/Understand-Anything&type=date&legend=top-left" />\n </picture>\n</a>\n\n<p align="center">\n  MIT License &copy; <a href="https://github.com/Lum1104">Lum1104</a>\n</p>',
    },
}


@mcp.tool()
def list_understand_anything_skills() -> dict:
    """List all available understand_anything skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_understand_anything_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific understand_anything skill."""
    if not skill_name or str(skill_name).lower() in ["null", "none"]:
        skill_name = "start-here" if "start-here" in _SKILLS else next(iter(_SKILLS))
    skill_data = _SKILLS.get(skill_name, {"error": f"Unknown skill: {skill_name}"})
    try:
        from fastmcp.server.dependencies import get_http_request
        client_id = get_http_request().headers.get("x-client-id")
    except Exception:
        client_id = None
    if not client_id:
        from core.config import get_client_id
        client_id = get_client_id()
    hint = get_presentation_hint('understand_anything', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@understand_anything",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'understand_anything',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
