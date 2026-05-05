"""Skill: duckdb_skills."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("duckdb-skills")


_SKILLS: dict[str, dict] = {
    'installation': {
        "description": '### From the Discover tab (coming soon)\n\nWe are working on submitting this plugin to the official Anthropic marketplace.',
        "guidance": '### From the Discover tab (coming soon)\n\nWe are working on submitting this plugin to the official Anthropic marketplace. Once listed, it will appear in the **Discover** tab when you run `/plugin` inside Claude Code.\n\n### From GitHub (available now)\n\nAdd the repository as a plugin source and install:\n\n```\n/plugin marketplace add duckdb/duckdb-skills\n```\n```\n/plugin install duckdb-skills@duckdb-skills\n```\n\nThis registers the GitHub repo as a marketplace and installs the plugin. Skills will be available as `/duckdb-skills:<skill-name>` in all future sessions.\n\n### Updating\n\nTo pull the latest version, update the marketplace first and then the plugin:\n\n```\n/plugin marketplace update duckdb-skills\n/plugin update duckdb-skills@duckdb-skills\n```',
    },
    'skills': {
        "description": '### `attach-db`\nAttach a DuckDB database file for interactive querying.',
        "guidance": '### `attach-db`\nAttach a DuckDB database file for interactive querying. Explores the schema (tables, columns, row counts) and writes a SQL state file so all other skills can restore the session automatically. You can choose to store state in the project directory (`.duckdb-skills/state.sql`) or in your home directory (`~/.duckdb-skills/<project>/state.sql`).\n\n```\n/duckdb-skills:attach-db my_analytics.duckdb\n```\n\nSupports multiple databases — running `attach-db` again can append to the existing state file.\n\n### `query`\nRun SQL queries against attached databases or ad-hoc against files. Accepts raw SQL or natural language questions. Uses DuckDB\'s Friendly SQL dialect. Automatically picks up session state from `attach-db`.\n\n```\n/duckdb-skills:query FROM sales LIMIT 10\n/duckdb-skills:query "what are the top 5 customers by revenue?"\n/duckdb-skills:query FROM \'exports.csv\' WHERE amount > 100\n```\n\n### `read-file`\nRead and explore any data file — CSV, JSON, Parquet, Avro, Excel, spatial, SQLite, Jupyter notebooks, and more — locally or from remote storage (S3, GCS, Azure, HTTPS). Auto-detects the format by file extension using a built-in `read_any` table macro. Suggests `query` for further exploration.\n\n```\n/duckdb-skills:read-file variants.parquet what columns does it have?\n/duckdb-skills:read-file s3://my-bucket/data.parquet describe the schema\n/duckdb-skills:read-file https://example.com/data.csv how many rows?\n```\n\n### `duckdb-docs`\nSearch DuckDB and DuckLake documentation and blog posts using full-text search against the hosted search indexes. No local setup required — queries run over HTTPS by default, with an option to cache the index locally for faster offline searches.\n\n```\n/duckdb-skills:duckdb-docs window functions\n/duckdb-skills:duckdb-docs "how do I read a CSV with custom delimiters?"\n```\n\n### `read-memories`\nSearch past Claude Code session logs to recover context from previous conversations — decisions made, patterns established, open TODOs. Offloads large result sets to a temporary DuckDB file for interactive drill-down.\n\n```\n/duckdb-skills:read-memories duckdb --here\n```\n\n### `install-duckdb`\nInstall or update DuckDB extensions. Supports `name@repo` syntax for community extensions and a `--update` flag that also checks whether your DuckDB CLI is on the latest stable version.\n\n```\n/duckdb-skills:install-duckdb spatial httpfs\n/duckdb-skills:install-duckdb gcs@community\n/duckdb-skills:install-duckdb --update\n```',
    },
    'session-state': {
        "description": 'All skills share a single `state.',
        "guidance": "All skills share a single `state.sql` file per project — a plain SQL file containing ATTACH/USE/LOAD statements, secrets, and macros. When state is first needed, you'll be asked where to store it:\n\n1. **In the project directory** (`.duckdb-skills/state.sql`) — colocated with the project, optionally gitignored\n2. **In your home directory** (`~/.duckdb-skills/<project>/state.sql`) — keeps the repo clean\n\nThe file is append-only and idempotent. Any skill restores the session via `duckdb -init state.sql`.",
    },
    'local-development': {
        "description": 'To test skills locally from a clone of this repo:\n\n```bash\n# 1.',
        "guidance": "To test skills locally from a clone of this repo:\n\n```bash\n# 1. Clone the repo\ngit clone https://github.com/duckdb/duckdb-skills.git\ncd duckdb-skills\n\n# 2. Launch Claude Code with the local plugin directory\nclaude --plugin-dir .\n```\n\nThis loads the plugin from disk instead of the marketplace, so any edits to `skills/*/SKILL.md` take effect immediately — just start a new conversation (or re-run the slash command) to pick up changes.\n\nYou can test individual skills directly:\n\n```\n/duckdb-skills:read-file some_local_file.parquet\n/duckdb-skills:duckdb-docs pivot unpivot\n/duckdb-skills:query SELECT 42\n```\n\n**Prerequisites:** DuckDB CLI must be installed. If it isn't, the skills will offer to install it via `/duckdb-skills:install-duckdb`.",
    },
    'how-the-skills-work-together': {
        "description": 'Skills reference each other where it makes sense:\n\n- `read-file` suggests `query` for follow-up exploration and `attach-db` for persisting large files\n- `query`, `read-file`, and `read-memories` all u',
        "guidance": 'Skills reference each other where it makes sense:\n\n- `read-file` suggests `query` for follow-up exploration and `attach-db` for persisting large files\n- `query`, `read-file`, and `read-memories` all use `duckdb-docs` to troubleshoot DuckDB errors automatically\n- All skills share the same `state.sql` — secrets and macros set up by `read-file` are reused by `query`, and databases attached by `attach-db` are available everywhere',
    },
    'platform-support': {
        "description": 'These skills have been tested on **macOS** and **Linux**.',
        "guidance": 'These skills have been tested on **macOS** and **Linux**. Windows is not yet fully supported — some shell commands and path handling may not work as expected. We plan to improve Windows compatibility in a future release.',
    },
    'reporting-issues-suggestions': {
        "description": 'Found a bug or have an idea for improvement? Open an issue at:\n\n**https://github.',
        "guidance": 'Found a bug or have an idea for improvement? Open an issue at:\n\n**https://github.com/duckdb/duckdb-skills/issues**\n\nFor DuckDB-specific bugs (extension loading, SQL errors), please include the DuckDB version (`duckdb --version`) and the full error message.',
    },
}


@mcp.tool()
def list_duckdb_skills_skills() -> dict:
    """List all available duckdb_skills skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_duckdb_skills_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific duckdb_skills skill."""
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
    hint = get_presentation_hint('duckdb_skills', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@duckdb_skills",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'duckdb_skills',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
