"""Skill: superpowers_lab."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("superpowers-lab")


_SKILLS: dict[str, dict] = {
    'what-is-this': {
        "description": "This plugin contains experimental skills that extend Claude Code's capabilities with new techniques that are still being refined and tested.",
        "guidance": "This plugin contains experimental skills that extend Claude Code's capabilities with new techniques that are still being refined and tested. These skills are functional but may evolve based on real-world usage and feedback.",
    },
    'current-skills': {
        "description": '### finding-duplicate-functions\n\nDetect semantic code duplication in LLM-generated codebases.',
        "guidance": '### finding-duplicate-functions\n\nDetect semantic code duplication in LLM-generated codebases. Unlike traditional copy-paste detectors that find syntactic duplicates, this skill identifies functions with the same intent but different implementations.\n\n**Use cases:**\n- Audit codebases that have grown organically with multiple contributors\n- Identify utility functions that have been reimplemented multiple times\n- Find consolidation opportunities before major refactoring\n- Complement jscpd after syntactic duplicates are handled\n\n**How it works:** Two-phase approach using classical function extraction followed by LLM-powered intent clustering. Haiku categorizes functions by domain, then Opus analyzes each category to find semantic duplicates.\n\nSee [skills/finding-duplicate-functions/SKILL.md](skills/finding-duplicate-functions/SKILL.md) for full documentation.\n\n### mcp-cli\n\nUse MCP servers on-demand via the `mcp` CLI tool. Discover and invoke tools, resources, and prompts without polluting context with pre-loaded MCP integrations.\n\n**Use cases:**\n- Query MCP servers without permanent configuration\n- Explore available tools before deciding to integrate\n- One-off MCP tool invocations\n\nSee [skills/mcp-cli/SKILL.md](skills/mcp-cli/SKILL.md) for full documentation.\n\n### using-tmux-for-interactive-commands\n\nEnables Claude Code to control interactive CLI tools (vim, git rebase -i, menuconfig, REPLs, etc.) through tmux sessions.\n\n**Use cases:**\n- Interactive text editors (vim, nano)\n- Terminal UI tools (menuconfig, htop)\n- Interactive REPLs (Python, Node, etc.)\n- Interactive git operations (rebase -i, add -p)\n- Any tool requiring keyboard navigation and real-time interaction\n\n**How it works:** Creates detached tmux sessions, sends keystrokes programmatically, and captures terminal output to enable automation of traditionally manual workflows.\n\nSee [skills/using-tmux-for-interactive-commands/SKILL.md](skills/using-tmux-for-interactive-commands/SKILL.md) for full documentation.\n\n### windows-vm\n\nCreate, manage, or connect to a headless Windows 11 VM running in Docker with KVM acceleration and SSH access — no RDP or GUI required.\n\n**Use cases:**\n- Spin up a Windows environment for testing or development\n- Run Claude Code on Windows via SSH\n- Test cross-platform behavior without leaving the terminal\n\n**How it works:** Uses [dockur/windows](https://github.com/dockur/windows) to run Windows 11 in a Docker container with KVM acceleration. Manages the full lifecycle: create, start, stop, restart, SSH, and status checks. Includes automated setup of OpenSSH Server, Node.js, and Claude Code inside the VM.\n\nSee [skills/windows-vm/SKILL.md](skills/windows-vm/SKILL.md) for full documentation.',
    },
    'installation': {
        "description": '```bash\n# Install the plugin\nclaude-code plugin install https://github.',
        "guidance": '```bash\n# Install the plugin\nclaude-code plugin install https://github.com/obra/superpowers-lab\n\n# Or add to your claude.json\n{\n  "plugins": [\n    "https://github.com/obra/superpowers-lab"\n  ]\n}\n```',
    },
    'requirements': {
        "description": '- tmux must be installed on your system\n- Skills are tested on Linux/macOS (tmux required).',
        "guidance": '- tmux must be installed on your system\n- Skills are tested on Linux/macOS (tmux required)',
    },
    'experimental-status': {
        "description": 'Skills in this plugin are:\n- ✅ Functional and tested\n- 🧪 Under active refinement\n- 📝 May evolve based on usage\n- 🔬 Open to feedback and improvements.',
        "guidance": 'Skills in this plugin are:\n- ✅ Functional and tested\n- 🧪 Under active refinement\n- 📝 May evolve based on usage\n- 🔬 Open to feedback and improvements',
    },
    'contributing': {
        "description": 'Found a bug or have an improvement? Please open an issue or PR!.',
        "guidance": 'Found a bug or have an improvement? Please open an issue or PR!',
    },
    'related-projects': {
        "description": '- [superpowers](https://github.',
        "guidance": '- [superpowers](https://github.com/obra/superpowers) - Core skills library for Claude Code\n- [superpowers-chrome](https://github.com/obra/superpowers-chrome) - Browser automation skills',
    },
    'license': {
        "description": 'MIT License - see [LICENSE](LICENSE) for details.',
        "guidance": 'MIT License - see [LICENSE](LICENSE) for details',
    },
}


@mcp.tool()
def list_superpowers_lab_skills() -> dict:
    """List all available superpowers_lab skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_superpowers_lab_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific superpowers_lab skill."""
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
    hint = get_presentation_hint('superpowers_lab', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@superpowers_lab",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'superpowers_lab',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
