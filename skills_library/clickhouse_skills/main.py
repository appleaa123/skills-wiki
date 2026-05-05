"""Skill: clickhouse_skills."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("clickhouse-skills")


_SKILLS: dict[str, dict] = {
    'installation': {
        "description": '### npx\n\n```bash\nnpx skills add clickhouse/agent-skills\n```\nThe CLI auto-detects installed agents and prompts you to select where to install.',
        "guidance": '### npx\n\n```bash\nnpx skills add clickhouse/agent-skills\n```\nThe CLI auto-detects installed agents and prompts you to select where to install.\n\n### clickhousectl\n\nUse the ClickHouse CLI [`clickhousectl`](https://github.com/ClickHouse/clickhousectl) to install the agent skills:\n\n```bash\nclickhousectl skills\n```',
    },
    'what-is-this': {
        "description": 'Agent Skills are packaged instructions that extend AI coding agents (Claude Code, Cursor, Copilot, etc.',
        "guidance": 'Agent Skills are packaged instructions that extend AI coding agents (Claude Code, Cursor, Copilot, etc.) with domain-specific expertise. This repository provides skills for ClickHouse databases and chdb — covering schema design, query optimization, data ingestion patterns, and in-process analytics with Python.\n\nWhen an agent loads these skills, it gains knowledge of ClickHouse best practices and chdb APIs, and can apply them while helping you design tables, write queries, analyze data, or troubleshoot performance issues.\n\nSkills follow the open specification at [agentskills.io](https://agentskills.io).',
    },
    'available-skills': {
        "description": '### ClickHouse Best Practices\n\n**28 rules** covering schema design, query optimization, and data ingestion—prioritized by impact.',
        "guidance": '### ClickHouse Best Practices\n\n**28 rules** covering schema design, query optimization, and data ingestion—prioritized by impact.\n\n| Category | Rules | Impact |\n|----------|-------|--------|\n| Primary Key Selection | 4 | CRITICAL |\n| Data Type Selection | 5 | CRITICAL |\n| JOIN Optimization | 5 | CRITICAL |\n| Insert Batching | 1 | CRITICAL |\n| Mutation Avoidance | 2 | CRITICAL |\n| Partitioning Strategy | 4 | HIGH |\n| Skipping Indices | 1 | HIGH |\n| Materialized Views | 2 | HIGH |\n| Async Inserts | 2 | HIGH |\n| OPTIMIZE Avoidance | 1 | HIGH |\n| JSON Usage | 1 | MEDIUM |\n\n**Location:** [`skills/clickhouse-best-practices/`](./skills/clickhouse-best-practices/)\n\n**For humans:** Read [SKILL.md](./skills/clickhouse-best-practices/SKILL.md) for an overview, or [AGENTS.md](./skills/clickhouse-best-practices/AGENTS.md) for the complete compiled guide.\n\n**For agents:** The skill activates automatically when you work with ClickHouse—creating tables, writing queries, or designing data pipelines.\n\n### ClickHouse Architecture Advisor\n\n**5 decision frameworks** covering workload-aware architecture decisions for real-time ClickHouse deployments.\n\n| Decision Area | Impact |\n|---------------|--------|\n| Ingestion Strategy | CRITICAL |\n| Join & Enrichment Patterns | CRITICAL |\n| Late-Arriving Data & Upserts | CRITICAL |\n| Time-Series Partitioning | HIGH |\n| Real-Time Pre-Aggregation | HIGH |\n\nComplements `clickhouse-best-practices` by answering *when*, *why*, and *how* — not just *what*. All recommendations are explicitly classified as `official`, `derived`, or `field` guidance.\n\n**Location:** [`skills/clickhouse-architecture-advisor/`](./skills/clickhouse-architecture-advisor/)\n\n**For humans:** Read [SKILL.md](./skills/clickhouse-architecture-advisor/SKILL.md) for an overview, or [AGENTS.md](./skills/clickhouse-architecture-advisor/AGENTS.md) for the compiled guide.\n\n**For agents:** The skill activates during architecture design sessions — when choosing ingestion patterns, designing time-series schemas, selecting enrichment strategies, or handling mutable state.\n\n### chdb DataStore\n\n**Pandas-compatible API** for chdb — drop-in pandas replacement backed by ClickHouse. Write `import chdb.datastore as pd` and use the same pandas API, 10-100x faster. Supports 16+ data sources (MySQL, PostgreSQL, S3, MongoDB, Iceberg, Delta Lake, etc.) with cross-source joins.\n\n**Location:** [`skills/chdb-datastore/`](./skills/chdb-datastore/)\n\n**For agents:** The skill activates when you analyze data with pandas-style syntax, speed up slow pandas code, query remote databases as DataFrames, or join data across different sources.\n\n### chdb SQL\n\n**In-process ClickHouse SQL** for Python — run SQL queries on local files, remote databases, and cloud storage without a server. Covers `chdb.query()`, Session, DB-API 2.0, parametrized queries, UDFs, streaming, and all ClickHouse table functions.\n\n**Location:** [`skills/chdb-sql/`](./skills/chdb-sql/)\n\n**For agents:** The skill activates when you write SQL queries against files, use ClickHouse table functions, build stateful analytical pipelines, or use advanced ClickHouse SQL features.',
    },
    'quick-start': {
        "description": 'After installation, your AI agent will reference these skills when:\n\n- Creating new tables with `CREATE TABLE`\n- Choosing `ORDER BY` / `PRIMARY KEY` columns\n- Selecting data types for columns\n- Optimi',
        "guidance": 'After installation, your AI agent will reference these skills when:\n\n- Creating new tables with `CREATE TABLE`\n- Choosing `ORDER BY` / `PRIMARY KEY` columns\n- Selecting data types for columns\n- Optimizing slow queries\n- Writing or tuning JOINs\n- Designing data ingestion pipelines\n- Handling updates or deletes\n- Analyzing data with pandas-style DataStore API\n- Querying files or databases with chdb SQL\n- Joining data across different sources (MySQL + S3 + local files)\n\nExample prompts:\n> "Create a table for storing user events with fields for user_id, event_type, properties (JSON), and timestamp"\n\nThe agent will apply relevant ClickHouse best practices rules.\n\n> "Load this Parquet file and group by country, show top 10 by revenue"\n\nThe agent will use chdb DataStore or SQL to query the file directly.\n\n> "Join my MySQL customers table with this local orders.parquet file"\n\nThe agent will use chdb\'s cross-source join capabilities.',
    },
    'supported-agents': {
        "description": 'Skills are **agent-agnostic**—the same skill works across all supported AI coding assistants:\n\n| Agent | Config Directory |\n|-------|------------------|\n| [Claude Code](https://claude.',
        "guidance": "Skills are **agent-agnostic**—the same skill works across all supported AI coding assistants:\n\n| Agent | Config Directory |\n|-------|------------------|\n| [Claude Code](https://claude.ai/code) | `.claude/skills/` |\n| [Cursor](https://cursor.sh) | `.cursor/skills/` |\n| [Windsurf](https://codeium.com/windsurf) | `.windsurf/skills/` |\n| [GitHub Copilot](https://github.com/features/copilot) | `.github/skills/` |\n| [Gemini CLI](https://github.com/google-gemini/gemini-cli) | `.gemini/skills/` |\n| [Cline](https://github.com/cline/cline) | `.cline/skills/` |\n| [Codex](https://openai.com/codex) | `.codex/skills/` |\n| [Goose](https://github.com/block/goose) | `.goose/skills/` |\n| [Roo Code](https://roo.ai) | `.roo/skills/` |\n| [OpenHands](https://github.com/All-Hands-AI/OpenHands) | `.openhands/skills/` |\n\nAnd 13 more including Amp, Kiro CLI, Trae, Zencoder, and others.\n\nThe installer detects which agents you have by checking for their configuration directories. If an agent isn't listed, either install it first or create its config directory manually (e.g., `mkdir -p ~/.cursor`).",
    },
    'license': {
        "description": 'Apache 2.',
        "guidance": 'Apache 2.0 — see [LICENSE](./LICENSE) for details.',
    },
}


@mcp.tool()
def list_clickhouse_skills_skills() -> dict:
    """List all available clickhouse_skills skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_clickhouse_skills_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific clickhouse_skills skill."""
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
    hint = get_presentation_hint('clickhouse_skills', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@clickhouse_skills",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'clickhouse_skills',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
