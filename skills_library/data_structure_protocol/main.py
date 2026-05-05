"""Skill: data_structure_protocol."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("data-structure-protocol")


_SKILLS: dict[str, dict] = {
    'the-problem': {
        "description": 'Your agent re-reads the same codebase every session.',
        "guidance": 'Your agent re-reads the same codebase every session. **DSP fixes that.**\n\nEvery time you start a new task, your AI coding agent spends the first 5–15 minutes "getting oriented" — scanning files, tracing imports, figuring out what depends on what. On large projects this becomes a constant tax on tokens and attention. Context is rebuilt from scratch, every single time.\n\nDSP is a graph-based long-term structural memory stored in `.dsp/`. It gives agents a persistent, versionable map of your codebase — entities, dependencies, public APIs, and the *reasons* behind every connection — so they can pick up exactly where they left off.\n\n> **DSP is not another workflow framework.** It\'s the persistent structural memory layer that\'s missing from every AI coding workflow.\n\n---',
    },
    'install': {
        "description": '**macOS / Linux:**\n\n```bash\ncurl -fsSL https://raw.',
        "guidance": '**macOS / Linux:**\n\n```bash\ncurl -fsSL https://raw.githubusercontent.com/k-kolomeitsev/data-structure-protocol/main/install.sh | bash\n```\n\n**Windows:**\n\n```powershell\nirm https://raw.githubusercontent.com/k-kolomeitsev/data-structure-protocol/main/install.ps1 | iex\n```\n\n**Codex:**\n\n```\n$skill-installer install https://github.com/k-kolomeitsev/data-structure-protocol/tree/main/skills/data-structure-protocol\n```\n\n---',
    },
    'what-you-get': {
        "description": '- **Agent stops re-learning your project every session** — structural context persists across tasks, sessions, and even team members\n- **Dependency discovery in seconds, not minutes** — graph traversa',
        "guidance": '- **Agent stops re-learning your project every session** — structural context persists across tasks, sessions, and even team members\n- **Dependency discovery in seconds, not minutes** — graph traversal replaces full-repo scanning\n- **Impact analysis before refactors** — know what breaks before you touch it\n- **Safer changes on brownfield codebases** — hidden couplings become visible edges in the graph\n- **Works with Claude Code, Cursor, Codex — no lock-in** — DSP is an agent skill, not a platform\n- **Git-native and versionable** — `.dsp/` is plain text, diffs cleanly, reviews like code\n\n> **Honest trade-off:** bootstrapping DSP on a large project takes real effort (time, tokens, discipline). It pays back over the project lifetime through lower per-task token usage, faster discovery, and more predictable agent behavior.\n\n---',
    },
    'how-it-works': {
        "description": '```\n┌──────────────────────┐\n│      Codebase        │\n│  (files + assets)    │\n└──────────┬───────────┘\n           │  create/update graph as you work\n           ▼\n┌──────────────────────┐\n│   DSP Buil',
        "guidance": '```\n┌──────────────────────┐\n│      Codebase        │\n│  (files + assets)    │\n└──────────┬───────────┘\n           │  create/update graph as you work\n           ▼\n┌──────────────────────┐\n│   DSP Builder / CLI  │\n│   (dsp-cli.py)       │\n└──────────┬───────────┘\n           │  writes\n           ▼\n┌──────────────────────┐\n│        .dsp/         │\n│ entity graph + whys  │\n└──────────┬───────────┘\n           │  reads/searches/traverses\n           ▼\n┌──────────────────────┐\n│   LLM Orchestrator   │\n│ (your agent + skill) │\n└──────────────────────┘\n```\n\nAs you work, DSP builds a lightweight graph of your codebase: modules, functions, dependencies, and public APIs. Each connection carries a `why` — the reason it exists. Your agent reads this graph instead of re-scanning the repo, navigates structure through graph traversal, and keeps the graph updated as code evolves.\n\nThe graph lives in `.dsp/` — plain text files that commit, diff, and merge like any other source artifact.\n\n---',
    },
    'quick-start': {
        "description": '### Option A: Start from the boilerplate (fastest)\n\n[**dsp-boilerplate**](https://github.',
        "guidance": '### Option A: Start from the boilerplate (fastest)\n\n[**dsp-boilerplate**](https://github.com/k-kolomeitsev/dsp-boilerplate) is a production-ready fullstack starter — **NestJS 11 + React 19 + Vite 7** in Docker Compose, with a **fully initialized DSP graph**, pre-configured skills for all agents, Cursor rules, git hooks, and CI.\n\n```bash\ngit clone https://github.com/k-kolomeitsev/dsp-boilerplate.git my-project\ncd my-project\ndocker-compose up -d\n```\n\nEverything is wired: `.dsp/` graph with two roots (backend + frontend), `@dsp` markers in all source files, DSP skills for Cursor, Claude Code, and Codex. You can start coding and the agent already knows the entire project structure.\n\n### Option B: Add DSP to any project\n\n#### 1. Initialize\n\n```bash\npython dsp-cli.py --root . init\n```\n\n#### 2. Create entities\n\n```bash\npython dsp-cli.py --root . create-object "src/app.ts" "Main application entrypoint"\n# → obj-a1b2c3d4\n\npython dsp-cli.py --root . create-function "src/app.ts#start" "Starts the HTTP server" --owner obj-a1b2c3d4\n# → func-7f3a9c12\n\npython dsp-cli.py --root . add-import obj-a1b2c3d4 obj-deadbeef "HTTP routing"\n```\n\n#### 3. Navigate\n\n```bash\npython dsp-cli.py --root . search "authentication"\npython dsp-cli.py --root . find-by-source "src/auth/index.ts"\npython dsp-cli.py --root . get-children obj-a1b2c3d4 --depth 2\n```\n\n#### 4. Impact analysis\n\n```bash\npython dsp-cli.py --root . get-parents obj-a1b2c3d4 --depth inf\npython dsp-cli.py --root . get-recipients obj-a1b2c3d4\n```\n\n> Before any refactor, run `get-parents` or `get-recipients` to see everything that depends on the entity you\'re about to change.\n\n---',
    },
    'supported-agents': {
        "description": 'DSP installs as a skill for your agent.',
        "guidance": "DSP installs as a skill for your agent. Pick your agent and scope.\n\nDon't have a coding agent yet? Install one first:\n\n| Agent | Install |\n|---|---|\n| **Claude Code** | `npm i -g @anthropic-ai/claude-code` — [docs](https://docs.anthropic.com/en/docs/claude-code/setup) |\n| **Cursor** | [cursor.com/downloads](https://www.cursor.com/downloads) — [docs](https://docs.cursor.com) |\n| **Codex CLI** | `npm i -g @openai/codex` — [docs](https://developers.openai.com/codex/cli) \\| [github](https://github.com/openai/codex) |\n\n### macOS / Linux\n\n| Agent | Project Install | Global Install |\n|---|---|---|\n| **Cursor** | `curl -fsSL https://raw.githubusercontent.com/k-kolomeitsev/data-structure-protocol/main/install.sh \\| bash -s -- cursor` | `curl -fsSL https://raw.githubusercontent.com/k-kolomeitsev/data-structure-protocol/main/install.sh \\| bash -s -- --global cursor` |\n| **Claude Code** | `curl -fsSL https://raw.githubusercontent.com/k-kolomeitsev/data-structure-protocol/main/install.sh \\| bash -s -- claude` | `curl -fsSL https://raw.githubusercontent.com/k-kolomeitsev/data-structure-protocol/main/install.sh \\| bash -s -- --global claude` |\n| **Codex** | `curl -fsSL https://raw.githubusercontent.com/k-kolomeitsev/data-structure-protocol/main/install.sh \\| bash -s -- codex` | `curl -fsSL https://raw.githubusercontent.com/k-kolomeitsev/data-structure-protocol/main/install.sh \\| bash -s -- --global codex` |\n\n### Windows\n\n```powershell\n# Project-level (current directory)\nirm https://raw.githubusercontent.com/k-kolomeitsev/data-structure-protocol/main/install.ps1 | iex\n\n# With specific agent\npowershell -ExecutionPolicy Bypass -File install.ps1 -Agent cursor\npowershell -ExecutionPolicy Bypass -File install.ps1 -Agent claude\npowershell -ExecutionPolicy Bypass -File install.ps1 -Agent codex\n\n# Global (user-level)\npowershell -ExecutionPolicy Bypass -File install.ps1 -Agent cursor -Global\n```\n\n### Codex (alternative)\n\n```\n$skill-installer install https://github.com/k-kolomeitsev/data-structure-protocol/tree/main/skills/data-structure-protocol\n```\n\n> **Project install** puts the skill in your repo (`.cursor/skills/`, `.claude/skills/`, `.codex/skills/`).\n> **Global install** puts it in your home directory so it's available across all projects.\n\n---",
    },
    'dsp-vs-alternatives': {
        "description": 'Modern agents already know how to plan, write tests, verify, and ship.',
        "guidance": "Modern agents already know how to plan, write tests, verify, and ship. They don't need process wrappers. What they lack is **memory**.\n\n| | **DSP** | **GSD** | **Superpowers** |\n|---|---|---|---|\n| **Core idea** | Persistent structural memory | Process/confidence wrapper | Engineering discipline (TDD) |\n| **What it solves** | Agent has no memory of project between sessions | Agent doesn't follow structured workflow | Agent might skip tests/planning |\n| **Is the problem real?** | Yes — no model has built-in project memory | Diminishing — modern models plan and verify natively | Diminishing — modern models know TDD when prompted |\n| **Persistent memory** | Full graph across sessions | None | None |\n| **Impact analysis** | Built-in (graph traversal) | No | No |\n| **Brownfield** | First-class | One-time scan | No explicit support |\n| **Overhead** | Low | Medium | Medium |\n\n> Modern agents are smarter than most mid-level engineers. They plan, they test, they verify. They just can't remember your project. DSP is the fix. [Detailed comparison with GSD](./docs/comparisons/dsp-vs-gsd.md) | [Detailed comparison with Superpowers](./docs/comparisons/dsp-vs-superpowers.md)\n\n---",
    },
    'core-concepts': {
        "description": '| Concept | What it is |\n|---|---|\n| **Entity** | A node in the graph.',
        "guidance": '| Concept | What it is |\n|---|---|\n| **Entity** | A node in the graph. Either an **Object** (module/file/class/config/external dep) or a **Function** (function/method/handler) |\n| **UID** | Stable identifier (`obj-<8hex>`, `func-<8hex>`). File paths are attributes, not identity — entities survive renames and moves |\n| **imports** | Outgoing edges — what this entity uses, with a `why` for each connection |\n| **shared** | Public API of an object — what it exposes to consumers |\n| **exports/** | Reverse index — who imports this entity and why (incoming edges) |\n| **TOC** | Per-entrypoint table of contents listing all reachable entities from a root |\n\nUID markers anchor identity in source code:\n\n```ts\n// @dsp func-7f3a9c12\nexport function calculateTotal(items: Item[]): number { /* ... */ }\n```\n\n```python\n# @dsp func-3c19ab8e\ndef process_payment(order):\n    ...\n```\n\n---',
    },
    'storage-format': {
        "description": '`.',
        "guidance": '`.dsp/` is plain text in a deterministic directory layout:\n\n```\n.dsp/\n├── TOC                        # Table of contents (single root)\n├── TOC-<rootUid>              # One TOC per root (multi-root projects)\n├── obj-a1b2c3d4/              # Object entity\n│   ├── description            # source, kind, purpose\n│   ├── imports                # imported UIDs (one per line)\n│   ├── shared                 # exported/shared UIDs (one per line)\n│   └── exports/               # reverse index\n│       ├── <importer_uid>     # why the whole object is imported\n│       └── <shared_uid>/      # per shared entity\n│           ├── description    # what is exported\n│           └── <importer_uid> # why this shared is imported\n└── func-7f3a9c12/             # Function entity\n    ├── description\n    ├── imports\n    └── exports/\n        └── <owner_uid>        # ownership link\n```\n\nFull specification: [`ARCHITECTURE.md`](./ARCHITECTURE.md)\n\n---',
    },
    'git-hooks-ci': {
        "description": 'DSP ships with hooks that keep the graph in sync with your code:\n\n| Hook | What it does | LLM required |\n|---|---|---|\n| **pre-commit** | Checks staged files against DSP graph — flags new files withou',
        "guidance": 'DSP ships with hooks that keep the graph in sync with your code:\n\n| Hook | What it does | LLM required |\n|---|---|---|\n| **pre-commit** | Checks staged files against DSP graph — flags new files without entities, deleted files still referenced, orphans | No |\n| **pre-push** | Full graph integrity — orphan detection, cycle detection, stats summary | No |\n| **Agent-assisted review** | Deep semantic analysis of changes against DSP entities, dependency impact | Yes |\n\nInstall hooks:\n\n```bash\n./hooks/install-hooks.sh          # macOS/Linux\n.\\hooks\\install-hooks.ps1         # Windows\n```\n\nSee [`hooks/`](./hooks/) for configuration, standalone scripts, and GitHub Actions integration.\n\n---',
    },
    'integration-packs': {
        "description": 'Ready-made configurations for each supported agent:\n\n| Agent | Skill location |\n|---|---|\n| **Cursor** | `.',
        "guidance": 'Ready-made configurations for each supported agent:\n\n| Agent | Skill location |\n|---|---|\n| **Cursor** | `.cursor/skills/data-structure-protocol/` |\n| **Claude Code** | `.claude/skills/data-structure-protocol/` |\n| **Codex** | `.codex/skills/data-structure-protocol/` |\n\nEach integration includes the skill instructions (`SKILL.md`), CLI (`dsp-cli.py`), and reference docs. See [`integrations/`](./integrations/) for agent-specific setup guides.\n\n---',
    },
    'documentation': {
        "description": '| Document | Description |\n|---|---|\n| [**dsp-boilerplate**](https://github.',
        "guidance": '| Document | Description |\n|---|---|\n| [**dsp-boilerplate**](https://github.com/k-kolomeitsev/dsp-boilerplate) | Fullstack boilerplate (NestJS + React + Docker Compose) with DSP pre-initialized — the fastest way to start |\n| [**GETTING_STARTED.md**](./GETTING_STARTED.md) | Step-by-step guide from install to first impact analysis |\n| [**ARCHITECTURE.md**](./ARCHITECTURE.md) | Full protocol specification — entity model, storage format, operations |\n| [**docs/comparisons/**](./docs/comparisons/) | Detailed comparisons with GSD, Superpowers, and other tools |\n| [**docs/workflows/**](./docs/workflows/) | Workflow guides — bootstrap, brownfield adoption, team usage |\n| [**integrations/**](./integrations/) | Agent-specific integration guides and configurations |\n\n---',
    },
    'contributing': {
        "description": 'Contributions are welcome.',
        "guidance": 'Contributions are welcome. Areas where help is most valuable:\n\n- **Architecture spec** — improving [`ARCHITECTURE.md`](./ARCHITECTURE.md)\n- **CLI** — keeping `dsp-cli.py` aligned with the spec\n- **Skill instructions** — refining [`SKILL.md`](./skills/data-structure-protocol/SKILL.md) for agent clarity\n- **New integrations** — adding support for more agents and editors\n- **Documentation** — examples, workflow guides, comparisons\n\nPlease keep changes minimal, explicit, and consistent with the "minimal sufficient context" philosophy.\n\n---',
    },
    'license': {
        "description": 'Apache License 2.',
        "guidance": 'Apache License 2.0 — see [`LICENSE`](./LICENSE).',
    },
}


@mcp.tool()
def list_data_structure_protocol_skills() -> dict:
    """List all available data_structure_protocol skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_data_structure_protocol_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific data_structure_protocol skill."""
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
    hint = get_presentation_hint('data_structure_protocol', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@data_structure_protocol",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'data_structure_protocol',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
