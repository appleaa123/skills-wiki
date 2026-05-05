"""Skill: claude_speed_reader."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("claude-speed-reader")


_SKILLS: dict[str, dict] = {
    'what-is-this': {
        "description": 'A Claude Code skill that lets you speed-read any response.',
        "guidance": 'A Claude Code skill that lets you speed-read any response. Uses **Rapid Serial Visual Presentation (RSVP)** — displaying one word at a time with the **Optimal Recognition Point (ORP)** highlighted in red. Your eyes stay fixed while your brain processes text at 2-3x normal reading speed.',
    },
    'install': {
        "description": '```bash\n# Clone to your Claude skills directory\ngit clone https://github.',
        "guidance": '```bash\n# Clone to your Claude skills directory\ngit clone https://github.com/SeanZoR/claude-speed-reader.git ~/.claude/skills/speed\n```\n\nOr manually copy the `.claude/` folder contents to your `~/.claude/` directory.',
    },
    'usage': {
        "description": "In Claude Code, after any response:\n\n```\n/speed\n```\n\nThat's it.",
        "guidance": 'In Claude Code, after any response:\n\n```\n/speed\n```\n\nThat\'s it. Opens a minimal dark reader with the last response loaded.\n\n**Custom text:**\n```\n/speed "Your text here"\n```',
    },
    'controls': {
        "description": '| Key | Action |\n|-----|--------|\n| `Space` | Play / Pause |\n| `←` `→` | Adjust speed (±50 WPM) |\n| `R` | Restart |\n| `V` | Paste new text |\n\nClick anywhere to toggle play/pause.',
        "guidance": '| Key | Action |\n|-----|--------|\n| `Space` | Play / Pause |\n| `←` `→` | Adjust speed (±50 WPM) |\n| `R` | Restart |\n| `V` | Paste new text |\n\nClick anywhere to toggle play/pause. Drag & drop text files supported.',
    },
    'how-orp-works': {
        "description": 'The red highlighted letter is the **Optimal Recognition Point** — positioned ~1/3 into each word where your brain naturally focuses.',
        "guidance": 'The red highlighted letter is the **Optimal Recognition Point** — positioned ~1/3 into each word where your brain naturally focuses. By keeping this point fixed on screen, you eliminate eye movement (saccades) that consume 80% of reading time.\n\n```\n    th[e] quick br[o]wn fox ju[m]ps\n       ↑         ↑         ↑\n      ORP       ORP       ORP\n```',
    },
    'customization': {
        "description": 'Edit `~/.',
        "guidance": 'Edit `~/.claude/skills/speed/data/reader.html` to customize:\n- Default WPM (currently 600)\n- Colors and fonts\n- Timing multipliers for punctuation',
    },
    'requirements': {
        "description": '- Claude Code\n- macOS (uses `open` command).',
        "guidance": '- Claude Code\n- macOS (uses `open` command)',
    },
    'license': {
        "description": "MIT\n\n---\n\nBuilt for humans who want to read Claude's novels faster.",
        "guidance": "MIT\n\n---\n\nBuilt for humans who want to read Claude's novels faster.",
    },
}


@mcp.tool()
def list_claude_speed_reader_skills() -> dict:
    """List all available claude_speed_reader skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_claude_speed_reader_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific claude_speed_reader skill."""
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
    hint = get_presentation_hint('claude_speed_reader', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@claude_speed_reader",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'claude_speed_reader',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
