"""Skill: invoice_organizer."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("invoice-organizer")


_SKILLS: dict[str, dict] = {
    'invoice-organizer': {
        "description": 'invoice_organizer skill.',
        "guidance": '',
    },
}


@mcp.tool()
def list_invoice_organizer_skills() -> dict:
    """List all available invoice_organizer skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_invoice_organizer_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific invoice_organizer skill."""
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
    hint = get_presentation_hint('invoice_organizer', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@invoice_organizer",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'invoice_organizer',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
