"""Skill: openai."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("openai")


_SKILLS: dict[str, dict] = {
    'installing-a-skill': {
        "description": 'Skills in [`.',
        "guidance": 'Skills in [`.system`](skills/.system/) are automatically installed in the latest version of Codex.\n\nTo install [curated](skills/.curated/) or [experimental](skills/.experimental/) skills, you can use the `$skill-installer` inside Codex.\n\nCurated skills can be installed by name (defaults to `skills/.curated`):\n\n```\n$skill-installer gh-address-comments\n```\n\nFor experimental skills, specify the skill folder. For example:\n\n```\n$skill-installer install the create-plan skill from the .experimental folder\n```\n\nOr provide the GitHub directory URL:\n\n```\n$skill-installer install https://github.com/openai/skills/tree/main/skills/.experimental/create-plan\n```\n\nAfter installing a skill, restart Codex to pick up new skills.',
    },
    'license': {
        "description": "The license of an individual skill can be found directly inside the skill's directory inside the `LICENSE.",
        "guidance": "The license of an individual skill can be found directly inside the skill's directory inside the `LICENSE.txt` file.",
    },
}


@mcp.tool()
def list_openai_skills() -> dict:
    """List all available openai skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_openai_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific openai skill."""
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
    hint = get_presentation_hint('openai', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@openai",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'openai',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
