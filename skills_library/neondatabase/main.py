"""Skill: neondatabase."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("neondatabase")


_SKILLS: dict[str, dict] = {
    'what-are-agent-skills': {
        "description": 'Skills are folders of instructions, scripts, and resources that agents can discover and use to do things more accurately and efficiently.',
        "guidance": "Skills are folders of instructions, scripts, and resources that agents can discover and use to do things more accurately and efficiently. Once installed, skills are automatically invoked by the agent upon detection of relevant tasks.\n\nIt all starts with the `SKILL.md` file in the skill's directory. It's the entry point and allows agents to progressively discover information as needed.",
    },
    'available-skills': {
        "description": '### Neon Postgres\n\n[skills/neon-postgres](skills/neon-postgres/SKILL.',
        "guidance": '### Neon Postgres\n\n[skills/neon-postgres](skills/neon-postgres/SKILL.md)\n\nA comprehensive index of Neon Serverless Postgres documentation and best practices to set your agents up for success.\n\n### Claimable Postgres\n\n[skills/claimable-postgres](skills/claimable-postgres/SKILL.md)\n\nProvision instant temporary Postgres databases via Claimable Postgres by Neon ([neon.new](https://neon.new)) with no login, signup, or credit card. Supports REST API, CLI, and SDK.\n\n### Neon Postgres Egress Optimizer\n\n[skills/neon-postgres-egress-optimizer](skills/neon-postgres-egress-optimizer/SKILL.md)\n\nDiagnose and fix excessive Postgres egress (network data transfer) in a codebase. Use when investigating high database bills, unexpected data transfer costs, or query overfetching.',
    },
    'installation': {
        "description": '```bash\nnpx skills add neondatabase/agent-skills\n```\n\n### Claude Code Plugin\n\nYou can also install the skills as a Claude Code plugin, which bundles both the neon-postgres agent skill and the [Neon MC',
        "guidance": "```bash\nnpx skills add neondatabase/agent-skills\n```\n\n### Claude Code Plugin\n\nYou can also install the skills as a Claude Code plugin, which bundles both the neon-postgres agent skill and the [Neon MCP Server](https://mcp.neon.tech) for natural language database management:\n\n```\n/plugin marketplace add neondatabase/agent-skills\n/plugin install neon-postgres@neon\n```\n\nAfter installation, you'll be prompted to authenticate with Neon via OAuth when you first use MCP tools.\n\nThe top-level `skills/` directory remains the source of truth. Plugin folders symlink only the skill directories they expose.\n\n### Cursor Plugin\n\nThis repository also includes Cursor plugin packaging with the same scope as the Claude plugin (neon-postgres agent skill and Neon MCP Server)\n\nRun this command in chat:\n\n```text\n/add-plugin neon-postgres\n```",
    },
    'usage': {
        "description": 'Example prompts:\n\n```\nGet started with Neon\n```\n\n```\nRecommend a connection method for this project\n```\n\n```\nSet up Drizzle ORM with Neon\n```\n\n```\nSet up Neon Auth for my Next.',
        "guidance": 'Example prompts:\n\n```\nGet started with Neon\n```\n\n```\nRecommend a connection method for this project\n```\n\n```\nSet up Drizzle ORM with Neon\n```\n\n```\nSet up Neon Auth for my Next.js app\n```\n\n```\nQuery the database using neon-js\n```\n\n```\nCreate a new Neon branch using the API\n```\n\n```\nUse the serverless driver for edge functions\n```\n\n```\nGive me a quick temporary Postgres database\n```\n\n```\nWhy is my Neon bill so high?\n```',
    },
}


@mcp.tool()
def list_neondatabase_skills() -> dict:
    """List all available neondatabase skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_neondatabase_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific neondatabase skill."""
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
    hint = get_presentation_hint('neondatabase', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@neondatabase",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'neondatabase',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
