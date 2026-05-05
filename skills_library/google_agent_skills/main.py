"""Skill: google_agent_skills."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("google-agent-skills")


_SKILLS: dict[str, dict] = {
    'installation': {
        "description": '```bash\nnpx skills add google/skills\n```\n\nFrom the `npx install` command, you can select the specific skills from this\nrepo to install.',
        "guidance": '```bash\nnpx skills add google/skills\n```\n\nFrom the `npx install` command, you can select the specific skills from this\nrepo to install.',
    },
    'available-skills': {
        "description": '- [**Gemini API in Agent Platform**](.',
        "guidance": '- [**Gemini API in Agent Platform**](./skills/cloud/gemini-api)\n- [**AlloyDB Basics**](./skills/cloud/alloydb-basics)\n- [**BigQuery Basics**](./skills/cloud/bigquery-basics)\n- [**Cloud Run Basics**](./skills/cloud/cloud-run-basics)\n- [**Cloud SQL Basics**](./skills/cloud/cloud-sql-basics)\n- [**Firebase Basics**](./skills/cloud/firebase-basics)\n- [**Kubernetes Engine (GKE) Basics**](./skills/cloud/gke-basics)\n- [**Recipe: Onboarding to Google Cloud**](./skills/cloud/google-cloud-recipe-onboarding)\n- [**Recipe: Authenticating to Google Cloud**](./skills/cloud/google-cloud-recipe-auth)\n- [**Recipe: Google Cloud Network Observability**](./skills/cloud/google-cloud-networking-observability)\n- [**Google Cloud Well-Architected Framework: Security**](./skills/cloud/google-cloud-waf-security)\n- [**Google Cloud Well-Architected Framework: Reliability**](./skills/cloud/google-cloud-waf-reliability)\n- [**Google Cloud Well-Architected Framework: Cost Optimization**](./skills/cloud/google-cloud-waf-cost-optimization)',
    },
    'support': {
        "description": 'If you need help or encounter issues with these skills, search for existing issues or open a new one in the [GitHub Issue Tracker](https://github.',
        "guidance": 'If you need help or encounter issues with these skills, search for existing issues or open a new one in the [GitHub Issue Tracker](https://github.com/google/skills/issues).',
    },
    'contributing': {
        "description": 'We welcome contributions to improve our skills.',
        "guidance": 'We welcome contributions to improve our skills. You can help by:\n\n*   [Reporting bugs or inaccuracies](https://github.com/google/skills/issues) in the skill Markdown files.\n*   Suggesting new skills to add to this repository (for example, Google technologies or recipes) by filing a feature request.',
    },
    'license': {
        "description": 'You are free to copy, modify, and distribute these skills under the terms of the\nApache 2.',
        "guidance": 'You are free to copy, modify, and distribute these skills under the terms of the\nApache 2.0 license. See the `LICENSE` file for details.',
    },
}


@mcp.tool()
def list_google_agent_skills_skills() -> dict:
    """List all available google_agent_skills skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_google_agent_skills_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific google_agent_skills skill."""
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
    hint = get_presentation_hint('google_agent_skills', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@google_agent_skills",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'google_agent_skills',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
