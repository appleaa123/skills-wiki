"""Skill: claude_code_startup."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("claude-code-startup")


_SKILLS: dict[str, dict] = {
    'install': {
        "description": '```bash\n/plugin marketplace add rameerez/claude-code-startup-skills\n/plugin install startup@rameerez-claude-code-startup-skills\n```\n\nDone.',
        "guidance": '```bash\n/plugin marketplace add rameerez/claude-code-startup-skills\n/plugin install startup@rameerez-claude-code-startup-skills\n```\n\nDone. Now you have access to all skills below.',
    },
    'skills': {
        "description": '| Skill | What it does |\n|-------|--------------|\n| `/startup:compress-images` | Compress images to WebP for blazing fast page loads |\n| `/startup:customer-empathy` | Deep-dive into customer empathy a',
        "guidance": '| Skill | What it does |\n|-------|--------------|\n| `/startup:compress-images` | Compress images to WebP for blazing fast page loads |\n| `/startup:customer-empathy` | Deep-dive into customer empathy and user journey thinking |\n| `/startup:download-video` | Download videos from X, YouTube, TikTok, Instagram, etc. |\n| `/startup:transcribe-video` | Generate subtitles and transcripts from video/audio |\n| `/startup:x-post` | Post to X (Twitter) — text, images, and video |',
    },
    'usage': {
        "description": '```\n/startup:compress-images.',
        "guidance": '```\n/startup:compress-images ./images/\n/startup:download-video https://x.com/user/status/123\n/startup:transcribe-video ./video.mp4\n/startup:x-post "Just shipped a new feature!"\n/startup:customer-empathy\n```',
    },
    'contributing': {
        "description": 'PRs welcome! Add your skill to `skills/<skill-name>/SKILL.',
        "guidance": 'PRs welcome! Add your skill to `skills/<skill-name>/SKILL.md`.',
    },
    'license': {
        "description": 'MIT.',
        "guidance": 'MIT',
    },
}


@mcp.tool()
def list_claude_code_startup_skills() -> dict:
    """List all available claude_code_startup skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_claude_code_startup_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific claude_code_startup skill."""
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
    hint = get_presentation_hint('claude_code_startup', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@claude_code_startup",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'claude_code_startup',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
