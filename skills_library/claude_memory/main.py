"""Skill: claude_memory."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("claude-memory")


_SKILLS: dict[str, dict] = {
    'the-problem': {
        "description": 'Claude Code forgets everything between sessions.',
        "guidance": 'Claude Code forgets everything between sessions. Built-in auto-memory exists but:\n- It\'s opaque (Claude decides what\'s "meaningful")\n- Limited to 200 lines loaded at startup\n- Not tightly integrated into the agentic loop\n- No hierarchical organization (scales poorly)',
    },
    'the-solution': {
        "description": 'A skill-based memory protocol with:\n- **Hierarchical storage**: `core.',
        "guidance": "A skill-based memory protocol with:\n- **Hierarchical storage**: `core.md` summaries → `topics/<topic>.md` details\n- **Background agents**: Memory ops don't block the main agent\n- **Categorized entries**: No dumping ground, everything has a topic\n- **Filesystem-based**: Robust, inspectable, git-trackable",
    },
    'installation': {
        "description": '```bash\ncurl -fsSL https://raw.',
        "guidance": '```bash\ncurl -fsSL https://raw.githubusercontent.com/hanfang/claude-memory-skill/main/install.sh | bash\n```\n\nOr clone and run locally:\n\n```bash\ngit clone https://github.com/hanfang/claude-memory-skill.git\ncd claude-memory-skill\n./install.sh\n```',
    },
    'what-gets-installed': {
        "description": '```\n~/.',
        "guidance": '```\n~/.claude/\n├── CLAUDE.md              # Hook added (or created)\n├── commands/\n│   └── mem.md             # The memory skill\n└── memory/\n    ├── core.md            # Summaries + pointers (always loaded)\n    ├── me.md              # About you (always loaded)\n    ├── topics/            # Detailed entries by topic\n    │   └── <topic>.md\n    └── projects/          # Project-specific memories\n        └── <project>.md\n```',
    },
    'architecture': {
        "description": "```\n┌─────────────────────────────────────────────────────┐\n│  Main Agent                                         │\n│  - Focuses on user's task                           │\n│  - Spawns memory agent whe",
        "guidance": "```\n┌─────────────────────────────────────────────────────┐\n│  Main Agent                                         │\n│  - Focuses on user's task                           │\n│  - Spawns memory agent when needed                  │\n│  - Doesn't wait (background)                        │\n└─────────────────────┬───────────────────────────────┘\n                      │ spawn (background)\n                      ▼\n┌─────────────────────────────────────────────────────┐\n│  Memory Agent                                       │\n│  - Reads core.md + relevant topics                  │\n│  - Writes to topic files                            │\n│  - Updates core.md summaries                        │\n└─────────────────────────────────────────────────────┘\n```",
    },
    'how-it-works': {
        "description": "### Agent-Initiated (Automatic)\n\nThese run automatically — you don't invoke them:\n\n| Action | When | Blocking |\n|--------|------|----------|\n| `load` | Session start | No |\n| `save` | Claude learns so",
        "guidance": '### Agent-Initiated (Automatic)\n\nThese run automatically — you don\'t invoke them:\n\n| Action | When | Blocking |\n|--------|------|----------|\n| `load` | Session start | No |\n| `save` | Claude learns something useful | No |\n| `recall` | Claude needs context | No |\n\n### User-Initiated (Manual)\n\nThese are for you to inspect and manage memory:\n\n| Command | Description |\n|---------|-------------|\n| `/mem show` | Display memory structure and contents |\n| `/mem forget <topic>` | Remove a topic or specific entries |\n\n### Tell Claude What to Remember\n\nJust say it naturally:\n- "Remember that we use pnpm, not npm"\n- "Save that the API requires auth headers"\n- "Note that tests need Redis running"\n\n### Fill In Your Profile\n\nEdit `~/.claude/memory/me.md` with facts about yourself:\n\n```markdown\n# About the User\n\n- AI researcher, focus on agents and RL\n- Prefer explicit code over clever abstractions\n- Python, PyTorch, JAX\n```\n\n### Hierarchical Memory\n\n**core.md** (always loaded):\n```markdown\n# Core Memory',
    },
    'debugging': {
        "description": 'Mostly async/timing issues.',
        "guidance": 'Mostly async/timing issues. Prefer explicit logging.\n→ topics/debugging.md',
    },
    'rl-research': {
        "description": 'PPO tuning, reward shaping experiments.',
        "guidance": 'PPO tuning, reward shaping experiments.\n→ topics/rl.md\n```\n\n**topics/debugging.md** (loaded on demand):\n```markdown',
    },
    'async-race-condition-fix-2024-01-15': {
        "description": 'Added explicit locks around shared state access.',
        "guidance": 'Added explicit locks around shared state access.',
    },
    'redis-timeout-debugging-2024-01-10': {
        "description": 'Default timeout was too short for large payloads.',
        "guidance": 'Default timeout was too short for large payloads.\n```\n\n### Write Flow\n\n1. Learn something → spawn background memory agent\n2. Agent categorizes → finds or creates topic file\n3. Agent appends entry with timestamp\n4. If significant, agent updates core.md summary\n\n### Read Flow\n\n1. Session start → agent reads core.md + me.md in background\n2. When stuck → agent follows pointers to relevant topics\n3. Returns context to main agent',
    },
    'design-principles': {
        "description": "- **Background ops**: Memory doesn't block the main agent\n- **Hierarchical**: Summaries in core.",
        "guidance": "- **Background ops**: Memory doesn't block the main agent\n- **Hierarchical**: Summaries in core.md, details in topics\n- **Categorized**: Every entry belongs to a topic\n- **Atomic entries**: One `##` block = one memory\n- **No semantic search**: Deterministic, grep-based retrieval\n- **User editable**: Plain markdown, edit anytime",
    },
    'uninstall': {
        "description": '```bash\nrm -rf ~/.',
        "guidance": '```bash\nrm -rf ~/.claude/memory\nrm ~/.claude/commands/mem.md\n# Manually remove the memory hook from ~/.claude/CLAUDE.md\n```',
    },
    'license': {
        "description": 'MIT.',
        "guidance": 'MIT',
    },
}


@mcp.tool()
def list_claude_memory_skills() -> dict:
    """List all available claude_memory skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_claude_memory_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific claude_memory skill."""
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
    hint = get_presentation_hint('claude_memory', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@claude_memory",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'claude_memory',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
