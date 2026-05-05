"""Skill: voltagent_voltagent_skills."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("voltagent-voltagent-skills")


_SKILLS: dict[str, dict] = {
    'install': {
        "description": 'If your agent supports add-skill:\n\n```bash\nnpx skills add VoltAgent/skills\n```.',
        "guidance": 'If your agent supports add-skill:\n\n```bash\nnpx skills add VoltAgent/skills\n```',
    },
    'skill-list': {
        "description": '- create-voltagent: Project setup guide with CLI and manual steps.',
        "guidance": '- create-voltagent: Project setup guide with CLI and manual steps.\n- voltagent-best-practices: Architecture and usage patterns for agents, workflows, memory, and servers.\n- voltagent-core-reference: Reference for the VoltAgent class options and lifecycle methods.\n- voltagent-docs-bundle: Lookup embedded docs from @voltagent/core/docs for version-matched documentation.',
    },
    'manual-install': {
        "description": '```bash\ngit clone https://github.',
        "guidance": '```bash\ngit clone https://github.com/VoltAgent/skills.git\n```\n\nThen configure your coding agent to load skills from the cloned directory.',
    },
    'links': {
        "description": '- https://voltagent.',
        "guidance": '- https://voltagent.dev/docs\n- https://github.com/voltagent/voltagent\n- https://agentskills.io',
    },
    'license': {
        "description": 'MIT - see LICENSE.',
        "guidance": 'MIT - see LICENSE.',
    },
}


@mcp.tool()
def list_voltagent_voltagent_skills_skills() -> dict:
    """List all available voltagent_voltagent_skills skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_voltagent_voltagent_skills_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific voltagent_voltagent_skills skill."""
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
    hint = get_presentation_hint('voltagent_voltagent_skills', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@voltagent_voltagent_skills",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'voltagent_voltagent_skills',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
