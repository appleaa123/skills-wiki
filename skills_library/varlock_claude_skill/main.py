"""Skill: varlock_claude_skill."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("varlock-claude-skill")


_SKILLS: dict[str, dict] = {
    'why-this-skill': {
        "description": "When working with Claude Code, secrets can accidentally leak into:\n- Terminal output\n- Claude's input/output context\n- Log files or traces\n- Git commits or diffs\n\nThis skill wraps [Varlock](https://va",
        "guidance": "When working with Claude Code, secrets can accidentally leak into:\n- Terminal output\n- Claude's input/output context\n- Log files or traces\n- Git commits or diffs\n\nThis skill wraps [Varlock](https://varlock.dev) to enforce secure patterns and prevent accidental exposure.",
    },
    'installation': {
        "description": '### Option A: One-liner (Recommended)\n\n```bash\nmkdir -p ~/.',
        "guidance": '### Option A: One-liner (Recommended)\n\n```bash\nmkdir -p ~/.claude/skills/varlock && curl -sSL https://raw.githubusercontent.com/wrsmith108/varlock-claude-skill/main/skills/varlock/SKILL.md -o ~/.claude/skills/varlock/SKILL.md\n```\n\n### Option B: Manual\n\n```bash\ngit clone https://github.com/wrsmith108/varlock-claude-skill /tmp/varlock-skill\ncp -r /tmp/varlock-skill/skills/varlock ~/.claude/skills/\nrm -rf /tmp/varlock-skill\n```',
    },
    'prerequisites': {
        "description": 'Install the Varlock CLI:\n\n```bash\ncurl -sSfL https://varlock.',
        "guidance": 'Install the Varlock CLI:\n\n```bash\ncurl -sSfL https://varlock.dev/install.sh | sh -s -- --force-no-brew\nexport PATH="$HOME/.varlock/bin:$PATH"\n```',
    },
    'core-principle': {
        "description": "**Secrets must NEVER appear in Claude's context.",
        "guidance": "**Secrets must NEVER appear in Claude's context.**\n\n| Never Do | Safe Alternative |\n|----------|------------------|\n| `cat .env` | `cat .env.schema` |\n| `echo $SECRET` | `varlock load` |\n| `printenv \\| grep API` | `varlock load \\| grep API` |",
    },
    'quick-reference': {
        "description": '```bash\n# Validate all secrets (shows masked values)\nvarlock load\n\n# Quiet validation (no output on success)\nvarlock load --quiet\n\n# Run command with secrets injected\nvarlock run -- npm start\n\n# View ',
        "guidance": '```bash\n# Validate all secrets (shows masked values)\nvarlock load\n\n# Quiet validation (no output on success)\nvarlock load --quiet\n\n# Run command with secrets injected\nvarlock run -- npm start\n\n# View schema (safe - no values)\ncat .env.schema\n```',
    },
    'schema-file': {
        "description": 'Create `.',
        "guidance": 'Create `.env.schema` to define variable types and sensitivity:\n\n```bash\n# Global defaults\n# @defaultSensitive=true @defaultRequired=infer\n\n# Public config\n# @type=enum(development,staging,production) @sensitive=false\nNODE_ENV=development\n\n# Sensitive secrets\n# @type=string(startsWith=sk_) @required @sensitive\nSTRIPE_SECRET_KEY=\n\n# @type=url @required @sensitive\nDATABASE_URL=\n```\n\n### Annotations\n\n| Annotation | Effect |\n|------------|--------|\n| `@sensitive` | Value masked in all output |\n| `@sensitive=false` | Value shown (for public keys) |\n| `@required` | Must be present |\n| `@type=string(startsWith=X)` | Prefix validation |',
    },
    'handling-secret-requests': {
        "description": 'When users ask Claude to:\n\n- **"Check if API key is set"** → `varlock load | grep API_KEY`\n- **"Debug authentication"** → `varlock load` (validates all)\n- **"Update a secret"** → Decline; ask user to ',
        "guidance": 'When users ask Claude to:\n\n- **"Check if API key is set"** → `varlock load | grep API_KEY`\n- **"Debug authentication"** → `varlock load` (validates all)\n- **"Update a secret"** → Decline; ask user to update manually\n- **"Show me .env"** → `cat .env.schema` instead',
    },
    'credits': {
        "description": 'This skill wraps [Varlock](https://github.',
        "guidance": 'This skill wraps [Varlock](https://github.com/dmno-dev/varlock) by [DMNO](https://dmno.dev).',
    },
    'license': {
        "description": 'MIT.',
        "guidance": 'MIT',
    },
}


@mcp.tool()
def list_varlock_claude_skill_skills() -> dict:
    """List all available varlock_claude_skill skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_varlock_claude_skill_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific varlock_claude_skill skill."""
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
    hint = get_presentation_hint('varlock_claude_skill', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@varlock_claude_skill",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'varlock_claude_skill',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
