"""Skill: qdrant_skills."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("qdrant-skills")


_SKILLS: dict[str, dict] = {
    'philosophy': {
        "description": 'Skills are not documentation.',
        "guidance": 'Skills are not documentation. Qdrant already has docs in markdown. Skills\nanswer "when?" and "why?", not "how?"\n\nThey are structured as the handbook of a Solutions Architect working on Qdrant:\ngiven a problem, navigate to the exact place in the documentation where the\nanswer lives. No tutorials, no concept explanations. Only references and\nminimal snippets where absolutely necessary.',
    },
    'disclaimer': {
        "description": 'These skills are under active development.',
        "guidance": 'These skills are under active development. Skill content and structure may change between versions as Qdrant evolves.',
    },
    'installation': {
        "description": '### npx skills\n\nInstall using the [`npx skills`](https://skills.',
        "guidance": '### npx skills\n\nInstall using the [`npx skills`](https://skills.sh) CLI:\n\n```bash\nnpx skills add qdrant/skills\n```\n\n### Claude Code\n\nAdd the marketplace, then install all Qdrant skills:\n\n```\n/plugin marketplace add qdrant/skills\n/plugin install qdrant@qdrant\n```\n\n### Cursor\n\nInstall from the Cursor Marketplace or add manually via **Settings > Rules > Add Rule > Remote Rule (GitHub)** with `qdrant/skills`.\n\n### Clone / Copy\n\nClone this repo and copy the skill folders into the appropriate directory for your agent:\n\n| Agent | Skill Directory | Docs |\n|-------|-----------------|------|\n| Claude Code | `~/.claude/skills/` | [docs](https://code.claude.com/docs/en/skills) |\n| Cursor | `.cursor/skills/` | [docs](https://docs.cursor.com/context/skills) |\n| OpenCode | `~/.config/opencode/skill/` | [docs](https://opencode.ai/docs/skills/) |\n| OpenAI Codex | `~/.codex/skills/` | [docs](https://developers.openai.com/codex/skills/) |\n| Pi | `~/.pi/agent/skills/` | [docs](https://github.com/badlogic/pi-mono/tree/main/packages/coding-agent#skills) |',
    },
    'quick-start': {
        "description": 'After installing, just ask your agent about Qdrant.',
        "guidance": 'After installing, just ask your agent about Qdrant. Skills are triggered automatically when your question matches their description.\n\n```\n"I have 50M vectors on a single node and search is slow, should I add more nodes?"\n→ qdrant-scaling skill activates, recommends quantization and vertical scaling before adding nodes\n\n"My search results are returning irrelevant matches"\n→ qdrant-search-quality skill activates, walks through diagnosis and search strategy options\n\n"How do I switch from OpenAI embeddings to Cohere without downtime?"\n→ qdrant-model-migration skill activates, guides zero-downtime migration with dual vectors\n```',
    },
    'skills': {
        "description": 'Skills are triggered automatically when your question matches their description.',
        "guidance": 'Skills are triggered automatically when your question matches their description.\n\n| Skill | Useful for |\n|-------|------------|\n| qdrant-clients-sdk | SDK setup, code examples, snippet search across Python, TypeScript, Rust, Go, .NET, Java |\n| qdrant-scaling | Scaling decisions: data volume, QPS, latency, query volume, horizontal vs vertical |\n| qdrant-performance-optimization | Search speed, memory usage, indexing performance |\n| qdrant-search-quality | Diagnosing bad results, search strategies, hybrid search |\n| qdrant-monitoring | Metrics, health checks, debugging optimizer and cluster issues |\n| qdrant-deployment-options | Choosing between local, self-hosted, cloud, and hybrid |\n| qdrant-model-migration | Switching embedding models without downtime |\n| qdrant-version-upgrade | Safe upgrade paths, compatibility guarantees, rolling upgrades |',
    },
    'mcp-servers': {
        "description": 'For additional Qdrant context, pair skills with these MCP servers:\n\n| Server | Purpose |\n|--------|---------|\n| [mcp-code-snippets](https://github.',
        "guidance": 'For additional Qdrant context, pair skills with these MCP servers:\n\n| Server | Purpose |\n|--------|---------|\n| [mcp-code-snippets](https://github.com/qdrant/mcp-code-snippets) | Search Qdrant docs and code examples across all SDKs |\n| [mcp-server-qdrant](https://github.com/qdrant/mcp-server-qdrant) | Store and retrieve memories, manage collections directly |',
    },
    'getting-help': {
        "description": 'Found a bug or wrong advice in a skill? [Open an issue](https://github.',
        "guidance": 'Found a bug or wrong advice in a skill? [Open an issue](https://github.com/qdrant/skills/issues/new) on GitHub and include:\n\n- The skill name\n- The prompt you gave your agent\n- What the agent said vs what it should have said',
    },
    'contributing': {
        "description": 'If you are interested in contributing, follow the instructions in [CONTRIBUTING.',
        "guidance": 'If you are interested in contributing, follow the instructions in [CONTRIBUTING.md](./CONTRIBUTING.md).',
    },
}


@mcp.tool()
def list_qdrant_skills_skills() -> dict:
    """List all available qdrant_skills skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_qdrant_skills_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific qdrant_skills skill."""
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
    hint = get_presentation_hint('qdrant_skills', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@qdrant_skills",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'qdrant_skills',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
