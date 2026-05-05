"""Skill: property_staging_skill."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("property-staging-skill")


_SKILLS: dict[str, dict] = {
    'property-staging-skill': {
        "description": 'property_staging_skill skill.',
        "guidance": '',
    },
}


@mcp.tool()
def list_property_staging_skill_skills() -> dict:
    """List all available property_staging_skill skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_property_staging_skill_skill(skill_name: str) -> dict:
    """Get full guidance for a specific property_staging_skill skill."""
    result = _SKILLS.get(skill_name, {"error": f"Unknown skill: {skill_name}"})
    hint = get_presentation_hint('property_staging_skill')
    if hint:
        result = {**result, "_presentation_hint": hint}
    return result
