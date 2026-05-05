"""Skill: model_hierarchy_skill."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("model-hierarchy-skill")


_SKILLS: dict[str, dict] = {
    'the-problem': {
        "description": 'Most AI agents run everything on expensive models.',
        "guidance": "Most AI agents run everything on expensive models. But 80% of agent tasks are routine: file reads, status checks, formatting, simple Q&A. You're paying $15-75/M tokens for work that $0.14/M tokens handles fine.",
    },
    'the-solution': {
        "description": 'A skill that teaches agents to classify tasks and route them to the cheapest model that can handle them:\n\n| Task Type | Model Tier | Cost | Examples |\n|-----------|------------|------|----------|\n| Ro',
        "guidance": 'A skill that teaches agents to classify tasks and route them to the cheapest model that can handle them:\n\n| Task Type | Model Tier | Cost | Examples |\n|-----------|------------|------|----------|\n| Routine (80%) | Cheap | $0.14-0.50/M | File ops, status checks, formatting |\n| Moderate (15%) | Mid | $1-5/M | Code gen, summaries, drafts |\n| Complex (5%) | Premium | $10-75/M | Debugging, architecture, novel problems |\n\n**Result: ~10x cost reduction** with equivalent quality on the tasks that matter.',
    },
    'quick-start': {
        "description": '### OpenClaw\n\n```bash\n# Copy SKILL.',
        "guidance": '### OpenClaw\n\n```bash\n# Copy SKILL.md to your skills directory\ncp SKILL.md ~/.openclaw/skills/model-hierarchy/SKILL.md\n\n# Restart gateway to pick up the skill\nopenclaw gateway restart\n```\n\n### Claude Code / Codex\n\nAdd to your `CLAUDE.md` or project instructions:\n\n```markdown',
    },
    'model-routing': {
        "description": 'Before executing tasks, classify complexity:\n- ROUTINE (file ops, lookups, formatting) → Use cheapest model\n- MODERATE (code, summaries, analysis) → Use mid-tier model  \n- COMPLEX (debugging, architec',
        "guidance": 'Before executing tasks, classify complexity:\n- ROUTINE (file ops, lookups, formatting) → Use cheapest model\n- MODERATE (code, summaries, analysis) → Use mid-tier model  \n- COMPLEX (debugging, architecture, failures) → Use premium model\n\nWhen spawning sub-agents, default to cheap models unless task requires more.\n```\n\n### Other Agent Systems\n\nSee [SKILL.md](SKILL.md) for the full classification rules and integration examples.',
    },
    'cost-math': {
        "description": 'Assuming 100K tokens/day:\n\n| Strategy | Monthly Cost |\n|----------|--------------|\n| Pure Opus | ~$225 |\n| Pure Sonnet | ~$45 |\n| Hierarchy (80/15/5) | ~$19 |.',
        "guidance": 'Assuming 100K tokens/day:\n\n| Strategy | Monthly Cost |\n|----------|--------------|\n| Pure Opus | ~$225 |\n| Pure Sonnet | ~$45 |\n| Hierarchy (80/15/5) | ~$19 |',
    },
    'testing': {
        "description": '```bash\n# Run classification tests\npython -m pytest tests/ -v\n\n# Test specific scenarios\npython tests/test_classification.',
        "guidance": '```bash\n# Run classification tests\npython -m pytest tests/ -v\n\n# Test specific scenarios\npython tests/test_classification.py\n```',
    },
    'files': {
        "description": '```\nmodel-hierarchy-skill/\n├── SKILL.',
        "guidance": "```\nmodel-hierarchy-skill/\n├── SKILL.md          # The skill (install this)\n├── README.md         # You're here\n├── tests/\n│   ├── test_classification.py\n│   └── scenarios.json\n└── examples/\n    ├── openclaw.md\n    └── claude-code.md\n```",
    },
    'license': {
        "description": 'MIT.',
        "guidance": 'MIT',
    },
}


@mcp.tool()
def list_model_hierarchy_skill_skills() -> dict:
    """List all available model_hierarchy_skill skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_model_hierarchy_skill_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific model_hierarchy_skill skill."""
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
    hint = get_presentation_hint('model_hierarchy_skill', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@model_hierarchy_skill",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'model_hierarchy_skill',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
