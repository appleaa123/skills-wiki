"""Skill: supabase_supabase_agent_skills."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("supabase-supabase-agent-skills")


_SKILLS: dict[str, dict] = {
    'installation': {
        "description": 'See the [Supabase AI Skills documentation](https://supabase.',
        "guidance": 'See the [Supabase AI Skills documentation](https://supabase.com/docs/guides/getting-started/ai-skills)\nfor detailed installation instructions.\n\n### Install all skills\n\n```bash\nnpx skills add supabase/agent-skills\n```\n\n### Install a specific skill\n\n```bash\nnpx skills add supabase/agent-skills --skill supabase\nnpx skills add supabase/agent-skills --skill supabase-postgres-best-practices\n```\n\n### Claude Code Plugin\n\nYou can also install the skills as Claude Code plugins:\n\n```bash\n# 1. Install supabase/agent-skill marketplace\nclaude plugin marketplace add supabase/agent-skills\n\n# 2. Install the plugin that you want \nclaude plugin install supabase@supabase-agent-skills\nclaude plugin install postgres-best-practices@supabase-agent-skills\n```',
    },
    'available-skills': {
        "description": '<details>\n<summary><strong>supabase</strong></summary>\n\nComprehensive Supabase development skill covering all Supabase products and\nintegrations.',
        "guidance": '<details>\n<summary><strong>supabase</strong></summary>\n\nComprehensive Supabase development skill covering all Supabase products and\nintegrations.\n\n**Use when:**\n\n- Working with any Supabase product (Database, Auth, Edge Functions, Realtime,\n  Storage, Vectors, Cron, Queues)\n- Using client libraries and SSR integrations (supabase-js, @supabase/ssr) in\n  Next.js, React, SvelteKit, Astro, Remix\n- Troubleshooting auth issues (login, logout, sessions, JWT, cookies, getSession,\n  getUser, getClaims, RLS)\n- Using the Supabase CLI or MCP server\n- Working with schema changes, migrations, security audits, or Postgres extensions\n  (pg_graphql, pg_cron, pg_vector)\n\n</details>\n\n<details>\n<summary><strong>supabase-postgres-best-practices</strong></summary>\n\nPostgres performance optimization guidelines from Supabase. Contains references\nacross 8 categories, prioritized by impact.\n\n**Use when:**\n\n- Writing SQL queries or designing schemas\n- Implementing indexes or query optimization\n- Reviewing database performance issues\n- Configuring connection pooling or scaling\n- Working with Row-Level Security (RLS)\n\n**Categories covered:**\n\n- Query Performance (Critical)\n- Connection Management (Critical)\n- Schema Design (High)\n- Concurrency & Locking (Medium-High)\n- Security & RLS (Critical)\n- Data Access Patterns (Medium)\n- Monitoring & Diagnostics (Low-Medium)\n- Advanced Features (Low)\n\n</details>',
    },
    'usage': {
        "description": 'Skills are automatically available once installed.',
        "guidance": 'Skills are automatically available once installed. The agent will use them when\nrelevant tasks are detected.\n\n**Examples:**\n\n```\nOptimize this Postgres query\n```\n\n```\nReview my schema for performance issues\n```\n\n```\nHelp me set up Supabase Auth with Next.js\n```\n\n```\nHelp me add proper indexes to this table\n```',
    },
    'skill-structure': {
        "description": 'Each skill follows the [Agent Skills Open Standard](https://agentskills.',
        "guidance": 'Each skill follows the [Agent Skills Open Standard](https://agentskills.io/):\n\n- `SKILL.md` - Required skill manifest with frontmatter (name, description, metadata)\n- `references/` - (Optional) Reference files for detailed documentation',
    },
}


@mcp.tool()
def list_supabase_supabase_agent_skills_skills() -> dict:
    """List all available supabase_supabase_agent_skills skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_supabase_supabase_agent_skills_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific supabase_supabase_agent_skills skill."""
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
    hint = get_presentation_hint('supabase_supabase_agent_skills', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@supabase_supabase_agent_skills",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'supabase_supabase_agent_skills',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
