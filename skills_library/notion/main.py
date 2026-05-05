"""Skill: notion."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("notion")


_SKILLS: dict[str, dict] = {
    'what-s-inside': {
        "description": "### Examples\n\nReady-to-run code samples showing how to integrate with Notion's API:\n\n- **[JavaScript examples](examples/javascript/)**: Integrations built with Notion's official JavaScript SDK, from b",
        "guidance": "### Examples\n\nReady-to-run code samples showing how to integrate with Notion's API:\n\n- **[JavaScript examples](examples/javascript/)**: Integrations built with Notion's official JavaScript SDK, from basic API calls to full web applications\n\nFuture additions will include examples for other languages and frameworks.\n\n### Skills\n\nAI-powered workflows for common Notion tasks:\n\n- **[Claude skills](skills/claude/)**: Skills that use Claude with Notion MCP to automate documentation, meeting prep, research, and more\n\nAs the AI ecosystem grows, we'll add skills for other providers.\n\n### Documentation\n\nThe `docs/` directory is reserved for Notion's core developer documentation, which will be migrated here in the future. For now, visit [developers.notion.com](https://developers.notion.com) for API references and guides.",
    },
    'getting-started': {
        "description": '### Running examples\n\nEach example includes its own README with setup instructions.',
        "guidance": "### Running examples\n\nEach example includes its own README with setup instructions. In general:\n\n1. Clone this repository\n2. Navigate to the example you want to try\n3. Install dependencies with `npm install`\n4. Follow the example's README for configuration and usage\n\n### Using skills\n\nSkills are designed to work with Claude and the Notion MCP server. See the [skills documentation](skills/README.md) for setup instructions.",
    },
    'contributing': {
        "description": 'We welcome contributions from the community.',
        "guidance": 'We welcome contributions from the community. Whether you want to add a new example, improve documentation, or share a useful skill, check out [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.',
    },
    'resources': {
        "description": '- [Notion API documentation](https://developers.',
        "guidance": '- [Notion API documentation](https://developers.notion.com)\n- [Notion Developers Slack](https://join.slack.com/t/notiondevs/shared_invite/zt-20b5996xv-DzJdLiympy6jP0GGzu3AMg)\n- [Stack Overflow](https://stackoverflow.com/questions/tagged/notion-api)',
    },
    'license': {
        "description": 'This project is licensed under the [MIT License](LICENSE).',
        "guidance": 'This project is licensed under the [MIT License](LICENSE).',
    },
}


@mcp.tool()
def list_notion_skills() -> dict:
    """List all available notion skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_notion_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific notion skill."""
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
    hint = get_presentation_hint('notion', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@notion",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'notion',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
