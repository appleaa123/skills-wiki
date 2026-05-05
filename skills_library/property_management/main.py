"""Skill: property_management."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("property-management")


_SKILLS: dict[str, dict] = {
    'client-care-route': {
        "description": 'Daily geo-optimized property visit route. Query properties needing visits, send tenant confirmation requests, compile confirmed/unconfirmed lists, and deliver the final route to the manager.',
        "file": 'client-care-route.md',
    },
    'ltb-forms': {
        "description": 'Legal notice form workflow. Detects the required form based on jurisdiction and situation, gathers required data, drafts the form, and manages the approval/delivery process.',
        "file": 'ltb-forms.md',
    },
    'maintenance-triage': {
        "description": 'Handles inbound maintenance requests. Classifies the issue by trade, checks for emergency status, looks up the appropriate vendor, generates a work order, gets manager approval, and dispatches it.',
        "file": 'maintenance-triage.md',
    },
    'manager-persona': {
        "description": "Extracts the manager's communication style, urgency signals, and approval preferences to create a persona guide. Use this skill to ensure all AI-generated communications match the manager's unique voice and decision-making style.",
        "file": 'manager-persona.md',
    },
    'property-db': {
        "description": "Defines the conceptual data model for property management and the rules for accessing the user's database. Use this skill when you need to understand how properties, tenants, vendors, maintenance requests, and interaction histories relate to each other, and the safety rules (HITL) for reading or modifying this data.",
        "file": 'property-db.md',
    },
    'rent-adjustment': {
        "description": 'Lease review and rent increase advisory. Queries tenant/lease data to find upcoming lease anniversaries, researches local rent control laws, conducts market research, and drafts an advisory brief for the manager.',
        "file": 'rent-adjustment.md',
    },
}


@mcp.tool()
def list_property_management_skills() -> dict:
    """List all available property_management skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_property_management_skill(skill_name: str) -> dict:
    """Get full guidance for a specific property_management skill."""
    from core.skill_runtime import read_skill_file, fetch_referenced_files, list_client_connections
    entry = _SKILLS.get(skill_name)
    if not entry:
        return {"error": f"Unknown skill: {skill_name}"}
    guidance = read_skill_file(__file__, entry.get("file", "")) or entry.get("guidance", "")
    result = {
        "description": entry["description"],
        "guidance": guidance,
        "_connections": list_client_connections(),
    }
    if guidance:
        refs = fetch_referenced_files(__file__, guidance, skill_name)
        if refs:
            result["_references"] = refs
    hint = get_presentation_hint('property_management')
    if hint:
        result = {**result, "_presentation_hint": hint}
    return result
