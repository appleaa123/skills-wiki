"""Skill: charlie_cfo_skill."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("charlie-cfo-skill")


_SKILLS: dict[str, dict] = {
    'what-it-does': {
        "description": 'Charlie provides financial frameworks for bootstrapped, high-growth startups:\n\n- **Cash management** — Runway calculations, reserve structures, burn analysis\n- **Unit economics** — LTV:CAC ratios, CAC',
        "guidance": 'Charlie provides financial frameworks for bootstrapped, high-growth startups:\n\n- **Cash management** — Runway calculations, reserve structures, burn analysis\n- **Unit economics** — LTV:CAC ratios, CAC payback, gross margin targets\n- **Capital allocation** — Hiring ROI, Rule of 40, investment payback periods\n- **Working capital** — Cash conversion cycle, AR/AP optimization, prepay strategies\n- **Forecasting** — Driver-based planning, scenario modeling, 13-week cash flow',
    },
    'installation': {
        "description": '```bash\nnpx skills add EveryInc/charlie-cfo-skill\n```.',
        "guidance": '```bash\nnpx skills add EveryInc/charlie-cfo-skill\n```',
    },
    'usage': {
        "description": 'Once installed, Charlie activates automatically when you ask financial questions:\n\n- "Should we make this hire?"\n- "How much runway do we need?"\n- "What metrics should I track?"\n- "How do I forecast r',
        "guidance": 'Once installed, Charlie activates automatically when you ask financial questions:\n\n- "Should we make this hire?"\n- "How much runway do we need?"\n- "What metrics should I track?"\n- "How do I forecast revenue?"\n- "What\'s a healthy LTV:CAC ratio?"',
    },
    'philosophy': {
        "description": '**Profit is a constraint, not a goal.',
        "guidance": '**Profit is a constraint, not a goal.** Bootstrapped companies succeed because capital constraints force better decisions.\n\nKey principles:\n- Unit economics are survival requirements, not nice-to-haves\n- Revenue per employee matters more than headcount\n- Runway targets: 24-36 months minimum\n- Every investment needs a <12 month payback period',
    },
    'references': {
        "description": 'The skill includes detailed reference docs:\n\n- `references/metrics-benchmarks.',
        "guidance": 'The skill includes detailed reference docs:\n\n- `references/metrics-benchmarks.md` — Formulas and industry benchmarks\n- `references/case-studies.md` — Examples from Mailchimp, Zapier, Basecamp, ConvertKit, Zoho',
    },
    'about-every': {
        "description": 'Every is the only subscription you need to stay at the edge of AI—ideas, apps, and training all in one bundle.',
        "guidance": 'Every is the only subscription you need to stay at the edge of AI—ideas, apps, and training all in one bundle.\n\nStart your free trial: https://every.to/subscribe',
    },
    'license': {
        "description": 'MIT.',
        "guidance": 'MIT',
    },
}


@mcp.tool()
def list_charlie_cfo_skill_skills() -> dict:
    """List all available charlie_cfo_skill skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_charlie_cfo_skill_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific charlie_cfo_skill skill."""
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
    hint = get_presentation_hint('charlie_cfo_skill', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@charlie_cfo_skill",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'charlie_cfo_skill',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
