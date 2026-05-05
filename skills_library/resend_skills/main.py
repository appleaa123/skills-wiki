"""Skill: resend_skills."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("resend-skills")


_SKILLS: dict[str, dict] = {
    'install': {
        "description": '```bash\nnpx skills add resend/resend-skills\n```\nThen select the ones you wish to install.',
        "guidance": '```bash\nnpx skills add resend/resend-skills\n```\nThen select the ones you wish to install.',
    },
    'available-skills': {
        "description": '| Skill | Description | Source |\n|---|---|---|\n| [`resend`](.',
        "guidance": '| Skill | Description | Source |\n|---|---|---|\n| [`resend`](./skills/resend) | Resend email API | Authored here |\n| [`agent-email-inbox`](./skills/agent-email-inbox) | Secure email inbox for AI agents | Authored here |\n| [`resend-cli`](./skills/resend-cli) | Operate Resend from the terminal  | Synced from [resend/resend-cli](https://github.com/resend/resend-cli) |\n| [`react-email`](./skills/react-email) | Build HTML emails with React components | Synced from [resend/react-email](https://github.com/resend/react-email) |\n| [`email-best-practices`](./skills/email-best-practices) | Guidance for building deliverable, compliant, user-friendly emails | Synced from [resend/email-best-practices](https://github.com/resend/email-best-practices) |',
    },
    'mcp-server': {
        "description": 'The plugin includes the [Resend MCP server](https://github.',
        "guidance": 'The plugin includes the [Resend MCP server](https://github.com/resend/resend-mcp), giving agents tool access to the full Resend API.',
    },
    'plugins': {
        "description": 'This repo serves as a plugin for multiple platforms:\n\n- **Claude Code** — `.',
        "guidance": 'This repo serves as a plugin for multiple platforms:\n\n- **Claude Code** — `.claude-plugin/`\n- **Cursor** — `.cursor-plugin/`\n- **OpenAI Codex** — `.codex-plugin/`',
    },
    'editing-skills': {
        "description": 'Skills marked **"Authored here"** can be edited directly in this repo.',
        "guidance": 'Skills marked **"Authored here"** can be edited directly in this repo.\n\nSkills marked **"Synced from"** are automatically synced from their source repos. **Do not edit them here** — changes will be overwritten on the next sync. Edit in the source repo instead.',
    },
    'prerequisites': {
        "description": '- A Resend account with a verified domain\n- API key stored in `RESEND_API_KEY` environment variable\n\nGet your API key at [resend.',
        "guidance": '- A Resend account with a verified domain\n- API key stored in `RESEND_API_KEY` environment variable\n\nGet your API key at [resend.com/api-keys](https://resend.com/api-keys)',
    },
    'license': {
        "description": 'MIT.',
        "guidance": 'MIT',
    },
}


@mcp.tool()
def list_resend_skills_skills() -> dict:
    """List all available resend_skills skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_resend_skills_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific resend_skills skill."""
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
    hint = get_presentation_hint('resend_skills', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@resend_skills",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'resend_skills',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
