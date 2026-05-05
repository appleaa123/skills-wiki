"""Skill: google_gemini_skills."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("google-gemini-skills")


_SKILLS: dict[str, dict] = {
    'about': {
        "description": 'LLMs have fixed knowledge, being trained at a specific point in time.',
        "guidance": "LLMs have fixed knowledge, being trained at a specific point in time. Software\ndev is fast paced and changes often, where new libraries are launched every day\nand best practices evolve quickly.\n\nThis leaves a knowledge gap that language models can't solve on their own. For\nexample, models don't know about themselves when they're trained, and they\naren't necessarily aware of subtle changes in best practices (like [thought\ncirculation](https://ai.google.dev/gemini-api/docs/thought-signatures)) or SDK\nchanges.\n\n[Skills](https://agentskills.io/) are a lightweight technique for adding\nrelevant context to your agents. This repo contains skills related to building\napps powered by the Gemini API.\n\n### Performance\n\nOur evaluations found that adding this skill improved an agent's ability to\ngenerate correct API code following best practices to 87% with Gemini 3 Flash\nand 96% with Gemini 3 Pro.",
    },
    'skills-in-this-repo': {
        "description": '| Skill | Description |\n| :--- | :--- |\n| [`gemini-api-dev`](skills/gemini-api-dev) | Skill for developing Gemini-powered apps.',
        "guidance": '| Skill | Description |\n| :--- | :--- |\n| [`gemini-api-dev`](skills/gemini-api-dev) | Skill for developing Gemini-powered apps. Provides the best practices for building apps that use the Gemini API. |\n| [`vertex-ai-api-dev`](skills/vertex-ai-api-dev) | Skill for developing Gemini-powered apps on Google Cloud Vertex AI using the Gen AI SDK. Covers tools, multimodal generation, caching, and batch prediction. |\n| [`gemini-live-api-dev`](skills/gemini-live-api-dev) | Skill for building real-time, bidirectional streaming apps with the Gemini Live API. Covers WebSocket-based audio/video/text streaming, voice activity detection, native audio features, function calling, and session management. |\n| [`gemini-interactions-api`](skills/gemini-interactions-api) | Skill for building apps with the [Gemini Interactions API](https://ai.google.dev/gemini-api/docs/interactions?ua=chat). Covers text generation, multi-turn chat, streaming, function calling, structured output, image generation, Deep Research agents, deprecated model guardrails, and both Python and TypeScript SDKs. |',
    },
    'installation': {
        "description": 'You can browse and install skills using either the [Vercel skills CLI](https://skills.',
        "guidance": 'You can browse and install skills using either the [Vercel skills CLI](https://skills.sh) or the [Context7 skills CLI](https://context7.com).\n\n### Using [Vercel skills CLI](https://skills.sh)\n\n```sh\n# Interactively browse and install skills.\nnpx skills add google-gemini/gemini-skills --list\n\n# Install a specific skill (e.g., gemini-api-dev).\nnpx skills add google-gemini/gemini-skills --skill gemini-api-dev --global\n```\n\n### Using [Context7 skills CLI](https://context7.com)\n\n```sh\n# Interactively browse and install skills.\nnpx ctx7 skills install /google-gemini/gemini-skills\n\n# Install a specific skill (e.g., vertex-ai-api-dev).\nnpx ctx7 skills install /google-gemini/gemini-skills vertex-ai-api-dev\n```',
    },
    'gemini-api-docs-mcp': {
        "description": 'A public Model Context Protocol (MCP) server for the Gemini API is available at\n`https://gemini-api-docs-mcp.',
        "guidance": 'A public Model Context Protocol (MCP) server for the Gemini API is available at\n`https://gemini-api-docs-mcp.dev`. Connecting your coding agent to this server ensures that\nall queries have access to the latest APIs, code updates, and optimal configuration examples.\n\nRun the following command in your agent\'s terminal or project root to install\nthe server:\n\n    npx add-mcp "https://gemini-api-docs-mcp.dev"\n\nThis server adds a `search_docs` tool that your agent can use to\nretrieve real-time API definitions and integration patterns from the official\nGemini API documentation.\n\nNote that the `gemini-api-dev` skill works with or without the MCP server, so\nwe recommend installing them both.',
    },
    'more-info': {
        "description": 'You can find additional information about setting up your coding assistant with\nGemini API MCP and Skills in [the docs](https://ai.',
        "guidance": 'You can find additional information about setting up your coding assistant with\nGemini API MCP and Skills in [the docs](https://ai.google.dev/gemini-api/docs/coding-agents).',
    },
    'disclaimer': {
        "description": 'This is not an officially supported Google product.',
        "guidance": 'This is not an officially supported Google product. This project is not\neligible for the [Google Open Source Software Vulnerability Rewards\nProgram](https://bughunters.google.com/open-source-security).',
    },
}


@mcp.tool()
def list_google_gemini_skills_skills() -> dict:
    """List all available google_gemini_skills skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_google_gemini_skills_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific google_gemini_skills skill."""
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
    hint = get_presentation_hint('google_gemini_skills', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@google_gemini_skills",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'google_gemini_skills',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
