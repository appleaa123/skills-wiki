"""Skill: mongodb_skills."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("mongodb-skills")


_SKILLS: dict[str, dict] = {
    'installation': {
        "description": '### Claude\n\nInstall the plugin from the [Claude marketplace](https://claude.',
        "guidance": "### Claude\n\nInstall the plugin from the [Claude marketplace](https://claude.com/plugins/mongodb), or run the following command from a Claude session:\n\n1. Install the plugin:\n\n   ```bash\n   /plugin install mongodb\n   ```\n\n2. Follow the prompts to complete the installation, then run `/reload-plugins` to activate it.\n\n### Cursor\n\nInstall the plugin from the [Cursor marketplace](https://cursor.com/marketplace/mongodb), or run the following command from a Cursor session:\n\n1. Install the plugin:\n\n   ```bash\n   /add-plugin mongodb\n   ```\n\n2. Follow the prompts to complete the installation.\n\n### Codex\n\nInstall the plugin by running the following command from a Codex session:\n\n```bash\ncodex plugin marketplace add mongodb/agent-skills\n```\n\nFollow the prompts to complete the installation.\n\n### Gemini\n\nInstall the extension from the [Gemini marketplace](https://geminicli.com/extensions/?name=mongodbagent-skills), or run the following command from Gemini CLI:\n\n1. Install the extension:\n\n   ```bash\n   gemini extensions install https://github.com/mongodb/agent-skills\n   ```\n\n2. Follow the prompts to complete the installation.\n\n\n### Copilot CLI\n\nInstall the plugin from the GitHub repository: `/plugin install https://github.com/mongodb/agent-skills.git`. Then restart Copilot CLI to activate the MCP server.\n\n### Install using Vercel's Agent Skills Directory\n\nhttps://skills.sh/ is a popular directory and a CLI that automates the installation of skills.\n\n1. Add the skills you want to your agent:\n\n   ```bash\n   npx skills add mongodb/agent-skills\n   ```\n\n2. Install the MCP server: `npx mongodb-mcp-server@1 setup` and follow the instructions.\n\n### Local install from repository\n\n1. Clone the repository:\n\n   ```bash\n   git clone https://github.com/mongodb/agent-skills.git\n   ```\n\n2. Install the skills for your platform:\n\n   Copy the `skills/` directory to the location where your coding agent\n   reads its skills or context files. Refer to your agent's documentation\n   for the correct path.\n\n3. Install the MCP server: `npx mongodb-mcp-server@1 setup` and follow the instructions.",
    },
    'configuration': {
        "description": 'Using the MCP Server to connect to MongoDB requires authentication - you can use the `mongodb-mcp-setup` skill to guide you through the process.',
        "guidance": 'Using the MCP Server to connect to MongoDB requires authentication - you can use the `mongodb-mcp-setup` skill to guide you through the process. Alternatively, refer to the [MongoDB MCP server documentation](https://www.mongodb.com/docs/mcp-server/configuration/options/) for a full list of configuration options.',
    },
}


@mcp.tool()
def list_mongodb_skills_skills() -> dict:
    """List all available mongodb_skills skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_mongodb_skills_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific mongodb_skills skill."""
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
    hint = get_presentation_hint('mongodb_skills', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@mongodb_skills",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'mongodb_skills',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
