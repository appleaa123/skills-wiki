"""Skill: tinybird."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("tinybird")


_SKILLS: dict[str, dict] = {
    'available-skills': {
        "description": '### Core project skills\n\nUse these for day-to-day Tinybird project work.',
        "guidance": '### Core project skills\n\nUse these for day-to-day Tinybird project work. They are safe defaults to keep enabled.\n\n#### tinybird-best-practices\n\nTinybird project guidelines from Tinybird Engineering. Contains 18 rule files covering datasources, pipes, endpoints, SQL, deployments, and testing.\n\n**Use when:**\n- Creating or updating Tinybird resources (.datasource, .pipe, .connection)\n- Working with queries, endpoints, or data exploration\n- Managing Tinybird deployments, secrets, or tests\n- Reviewing or refactoring Tinybird project files\n\n**Categories covered:**\n- Project structure and local development\n- Datasource, pipe, and endpoint files\n- SQL and query optimization\n- Build and deploy workflows\n- Testing and secrets management\n\n### CLI workflow skills\n\nUse these when operating Tinybird with the CLI (local dev, deployments, data ops) and the datafile (.pipe, .connection, .datasource) format\n\n#### tinybird-cli-guidelines\n\nTinybird CLI commands, workflows, and operations. Use when running `tb` commands, managing local development, deploying, or working with data operations.\n\n**Use when:**\n- Running any `tb` command\n- Local development with Tinybird Local\n- Building and deploying projects\n- Appending, replacing, or deleting data\n- Managing tokens and secrets via CLI\n- Generating mock data\n- Running tests\n\n### TypeScript SDK skills\n\nUse these when working with the `@tinybirdco/sdk` package and type-safe projects.\n\n#### tinybird-typescript-sdk-guidelines\n\nTinybird TypeScript SDK for defining datasources, pipes, and queries with full type inference. Use when working with @tinybirdco/sdk, TypeScript Tinybird projects, or type-safe data ingestion and queries.\n\n**Use when:**\n- Installing or configuring @tinybirdco/sdk\n- Defining datasources or pipes in TypeScript\n- Creating typed Tinybird clients\n- Using type-safe ingestion or queries\n- Running tinybird dev/build/deploy commands for TypeScript projects\n- Migrating from legacy .datasource/.pipe files to TypeScript\n\n### Python SDK skills\n\nUse these when working with the `tinybird-sdk` package and Python projects.\n\n#### tinybird-python-sdk-guidelines\n\nTinybird Python SDK for defining datasources, pipes, and queries in Python. Use when working with tinybird-sdk, Python Tinybird projects, or data ingestion and queries in Python.\n\n**Use when:**\n- Installing or configuring tinybird-sdk\n- Defining datasources, pipes, or endpoints in Python\n- Creating Tinybird clients in Python\n- Using data ingestion or queries in Python\n- Running tinybird dev/build/deploy commands for Python projects\n- Migrating from legacy .datasource/.pipe files to Python\n- Defining connections (Kafka, S3, GCS)\n- Creating materialized views, copy pipes, or sink pipes',
    },
    'usage': {
        "description": 'Skills are automatically available once installed.',
        "guidance": 'Skills are automatically available once installed. The agent will use them when relevant tasks are detected. You can use the agent cli to check, e.g., `amp skill list`, or directly ask the agent to tell you what skills are available.\n\n**Recommended defaults:**\n- Always enable `tinybird-best-practices` for general Tinybird project work.\n- Add `tinybird-cli-guidelines` whenever you plan to run `tb` commands.\n- Add `tinybird-typescript-sdk-guidelines` for TypeScript SDK projects.\n- Add `tinybird-python-sdk-guidelines` for Python SDK projects.\n\n**Examples:**\n- "Create a datasource for user events"\n- "Optimize this endpoint for low latency"\n- "Set up tests for my endpoints"',
    },
    'skill-structure': {
        "description": 'Each skill contains:\n- `SKILL.',
        "guidance": 'Each skill contains:\n- `SKILL.md` - Instructions for the agent\n- `rules/` - Individual guidance files',
    },
}


@mcp.tool()
def list_tinybird_skills() -> dict:
    """List all available tinybird skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_tinybird_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific tinybird skill."""
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
    hint = get_presentation_hint('tinybird', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@tinybird",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'tinybird',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
