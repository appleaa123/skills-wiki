"""Skill: wordpress."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("wordpress")


_SKILLS: dict[str, dict] = {
    'why-agent-skills': {
        "description": 'AI coding assistants are powerful, but they often:\n- Generate outdated WordPress patterns (pre-Gutenberg, pre-block themes)\n- Miss critical security considerations in plugin development\n- Skip proper ',
        "guidance": 'AI coding assistants are powerful, but they often:\n- Generate outdated WordPress patterns (pre-Gutenberg, pre-block themes)\n- Miss critical security considerations in plugin development\n- Skip proper block deprecations, causing "Invalid block" errors\n- Ignore existing tooling in your repo\n\nAgent Skills solve this by giving AI assistants **expert-level WordPress knowledge** in a format they can actually use.',
    },
    'available-skills': {
        "description": '| Skill | What it teaches |\n|-------|-----------------|\n| **wordpress-router** | Classifies WordPress repos and routes to the right workflow |\n| **wp-project-triage** | Detects project type, tooling, ',
        "guidance": '| Skill | What it teaches |\n|-------|-----------------|\n| **wordpress-router** | Classifies WordPress repos and routes to the right workflow |\n| **wp-project-triage** | Detects project type, tooling, and versions automatically |\n| **wp-block-development** | Gutenberg blocks: `block.json`, attributes, rendering, deprecations |\n| **wp-block-themes** | Block themes: `theme.json`, templates, patterns, style variations |\n| **wp-plugin-development** | Plugin architecture, hooks, settings API, security |\n| **wp-rest-api** | REST API routes/endpoints, schema, auth, and response shaping |\n| **wp-interactivity-api** | Frontend interactivity with `data-wp-*` directives and stores |\n| **wp-abilities-api** | Capability-based permissions and REST API authentication |\n| **wp-wpcli-and-ops** | WP-CLI commands, automation, multisite, search-replace |\n| **wp-performance** | Profiling, caching, database optimization, Server-Timing |\n| **wp-phpstan** | PHPStan static analysis for WordPress projects (config, baselines, WP-specific typing) |\n| **wp-playground** | WordPress Playground for instant local environments |\n| **wpds** | WordPress Design System |\n| **wp-plugin-directory-guidelines** | WordPress Plugin Directory Guidelines |\n| **blueprint** | WordPress Playground Blueprints for declarative Playground environment setup |',
    },
    'quick-start': {
        "description": '### Install globally for Claude Code\n\n```bash\n# Clone agent-skills\ngit clone https://github.',
        "guidance": "### Install globally for Claude Code\n\n```bash\n# Clone agent-skills\ngit clone https://github.com/WordPress/agent-skills.git\ncd agent-skills\n\n# Build the distribution\nnode shared/scripts/skillpack-build.mjs --clean\n\n# Install all skills globally (available across all projects)\nnode shared/scripts/skillpack-install.mjs --global\n\n# Or install specific skills only\nnode shared/scripts/skillpack-install.mjs --global --skills=wp-playground,wp-block-development\n```\n\nThis installs skills to `~/.claude/skills/` where Claude Code will automatically discover them.\n\n### Install into your repo\n\n```bash\n# Clone agent-skills\ngit clone https://github.com/WordPress/agent-skills.git\ncd agent-skills\n\n# Build the distribution\nnode shared/scripts/skillpack-build.mjs --clean\n\n# Install into your WordPress project\nnode shared/scripts/skillpack-install.mjs --dest=../your-wp-project --targets=codex,vscode,claude,cursor\n```\n\nThis copies skills into:\n- `.codex/skills/` for OpenAI Codex\n- `.github/skills/` for VS Code / GitHub Copilot\n- `.claude/skills/` for Claude Code (project-level)\n- `.cursor/skills/` for Cursor (project-level)\n\n### Install globally for Cursor\n\n```bash\nnode shared/scripts/skillpack-install.mjs --targets=cursor-global\n```\n\nThis installs skills to `~/.cursor/skills/` where Cursor will discover them.\n\n### Available options\n\n```bash\n# List available skills\nnode shared/scripts/skillpack-install.mjs --list\n\n# Dry run (preview without installing)\nnode shared/scripts/skillpack-install.mjs --global --dry-run\n\n# Install specific skills to a project (e.g. Claude + Cursor)\nnode shared/scripts/skillpack-install.mjs --dest=../my-repo --targets=claude,cursor --skills=wp-wpcli-and-ops\n```\n\n### Manual installation\n\nCopy any skill folder from `skills/` into your project's instructions directory for your AI assistant.",
    },
    'how-it-works': {
        "description": 'Each skill contains:\n\n```\nskills/wp-block-development/\n├── SKILL.',
        "guidance": 'Each skill contains:\n\n```\nskills/wp-block-development/\n├── SKILL.md              # Main instructions (when to use, procedure, verification)\n├── references/           # Deep-dive docs on specific topics\n│   ├── block-json.md\n│   ├── deprecations.md\n│   └── ...\n└── scripts/              # Deterministic helpers (detection, validation)\n    └── list_blocks.mjs\n```\n\nWhen you ask your AI assistant to work on WordPress code, it reads these skills and follows the documented procedures rather than guessing.',
    },
    'compatibility': {
        "description": '- **WordPress 6.',
        "guidance": '- **WordPress 6.9+** (PHP 7.2.24+)\n- Works with any AI assistant that supports project-level instructions',
    },
    'contributing': {
        "description": "**We welcome contributions!** This project is a great way to share your WordPress expertise—you don't need to be a coding wizard.",
        "guidance": '**We welcome contributions!** This project is a great way to share your WordPress expertise—you don\'t need to be a coding wizard. Most skills are written in Markdown, focusing on clear procedures and best practices.\n\nSee [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to get started.\n\nQuick commands:\n\n```bash\n# Scaffold a new skill\nnode shared/scripts/scaffold-skill.mjs <skill-name> "<description>"\n\n# Validate skills\nnode eval/harness/run.mjs\n```',
    },
    'documentation': {
        "description": '- [Authoring Guide](docs/authoring-guide.',
        "guidance": '- [Authoring Guide](docs/authoring-guide.md) - How to create and improve skills\n- [Principles](docs/principles.md) - Design philosophy\n- [Packaging](docs/packaging.md) - Build and distribution\n- [Compatibility Policy](docs/compatibility-policy.md) - Version targeting',
    },
    'license': {
        "description": 'GPL-2.',
        "guidance": 'GPL-2.0-or-later',
    },
}


@mcp.tool()
def list_wordpress_skills() -> dict:
    """List all available wordpress skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_wordpress_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific wordpress skill."""
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
    hint = get_presentation_hint('wordpress', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@wordpress",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'wordpress',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
