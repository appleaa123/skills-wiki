"""Skill: nodejs_skill."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("nodejs-skill")


_SKILLS: dict[str, dict] = {
    'available-skills': {
        "description": '| Skill | Description |\n|-------|-------------|\n| `documentation` | Technical writer specializing in the Diátaxis documentation framework |\n| `fastify` | Comprehensive best practices for Fastify devel',
        "guidance": '| Skill | Description |\n|-------|-------------|\n| `documentation` | Technical writer specializing in the Diátaxis documentation framework |\n| `fastify` | Comprehensive best practices for Fastify development |\n| `init` | Creates and maintains high-signal AGENTS.md guidance for repositories |\n| `linting-neostandard-eslint9` | Linting workflows with neostandard and ESLint v9 flat config |\n| `node` | Best practices for Node.js development |\n| `nodejs-core` | Deep Node.js internals expertise including C++ addons, V8, libuv, and build systems |\n| `oauth` | OAuth 2.0/2.1 specification expert with deep RFC knowledge and Fastify integration patterns |\n| `octocat` | Git and GitHub wizard using gh CLI for all git operations and GitHub interactions |\n| `skill-optimizer` | Improves skill activation, benchmark outcomes, and regression resistance across models |\n| `snipgrapher` | Configure and use snipgrapher to generate polished code snippet images |\n| `typescript-magician` | TypeScript wizard specializing in advanced type systems, complex generics, and eliminating any types |',
    },
    'usage': {
        "description": 'This package contains best practices and skills for AI-assisted development.',
        "guidance": 'This package contains best practices and skills for AI-assisted development.',
    },
    'benchmarking': {
        "description": '- [Cross-model skill benchmarking workflow](docs/skill-benchmarking.',
        "guidance": '- [Cross-model skill benchmarking workflow](docs/skill-benchmarking.md)\n- [Benchmark run history](docs/skill-benchmark-runs.md)',
    },
}


@mcp.tool()
def list_nodejs_skill_skills() -> dict:
    """List all available nodejs_skill skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_nodejs_skill_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific nodejs_skill skill."""
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
    hint = get_presentation_hint('nodejs_skill', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@nodejs_skill",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'nodejs_skill',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
