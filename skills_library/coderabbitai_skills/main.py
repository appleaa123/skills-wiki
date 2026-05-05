"""Skill: coderabbitai_skills."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("coderabbitai-skills")


_SKILLS: dict[str, dict] = {
    'quickstart': {
        "description": 'Install the CodeRabbit CLI via the [CLI docs](https://docs.',
        "guidance": 'Install the CodeRabbit CLI via the [CLI docs](https://docs.coderabbit.ai/cli),\nthen authenticate:\n\n```bash\ncoderabbit auth login\n```\n\nThen tell your agent: **“Review my code.”**',
    },
    'installation': {
        "description": '### 1.',
        "guidance": '### 1. Install the CodeRabbit CLI\n\nUse the [CLI docs](https://docs.coderabbit.ai/cli) for the primary install path.\nThey cover Homebrew, the install script, authentication, and CLI usage.\n\n### 2. Install the agent integration\n\nChoose the path that matches your coding agent.\n\n#### Skills installer\n\nFor agents that support portable `SKILL.md` files, use the\n[skills docs](https://docs.coderabbit.ai/cli/skills).\n\n```bash\nnpx skills add coderabbitai/skills\n```\n\nInstallation options for the skills installer:\n\n| Flag           | Purpose                                          |\n| -------------- | ------------------------------------------------ |\n| `-g, --global` | Install to user directory instead of project     |\n| `-a, --agent`  | Target specific agents (for example `claude-code`) |\n| `-s, --skill`  | Install particular skills by name                |\n| `--all`        | Install all skills to all agents without prompts |\n\n#### Claude Code Plugin\n\nClaude Code users can also install this as a plugin directly from the official marketplace:\n\n```text\n/plugin marketplace update\n/plugin install coderabbit\n```\n\nFor the full setup flow, see the\n[Claude Code integration guide](https://docs.coderabbit.ai/cli/claude-code-integration).\n\n#### Cursor Plugin\n\nThis repository now includes Cursor marketplace metadata in\n[`/.cursor-plugin/plugin.json`](.cursor-plugin/plugin.json).\n\nAfter publication, Cursor marketplace installs use:\n\n```text\n/add-plugin coderabbit\n```\n\nFor the current recommended setup, see the\n[Cursor integration guide](https://docs.coderabbit.ai/cli/cursor-integration).\n\n#### Codex App\n\nCodex users can install the official CodeRabbit plugin by following the\n[Codex app integration guide](https://docs.coderabbit.ai/cli/codex-integration#codex-app).\n\nFor an at-a-glance inventory of active and repo-packaged distribution paths, see\n[DISTRIBUTION_CHANNELS.md](DISTRIBUTION_CHANNELS.md).',
    },
    'what-lives-here': {
        "description": '| Path | Purpose |\n| --- | --- |\n| `skills/` | Portable CodeRabbit skills for agents that support `SKILL.',
        "guidance": '| Path | Purpose |\n| --- | --- |\n| `skills/` | Portable CodeRabbit skills for agents that support `SKILL.md`. |\n| `.claude-plugin/` | Claude Code plugin marketplace metadata. |\n| `commands/` | Claude Code slash commands shipped by the plugin. |\n| `agents/` | Claude Code subagents shipped by the plugin. |\n| `.cursor-plugin/` | Cursor marketplace metadata. |\n| `assets/` | Shared marketplace and brand assets. |\n| `DISTRIBUTION_CHANNELS.md` | Maintainer inventory of live, packaged, and in-development channels. |',
    },
    'usage': {
        "description": "Once installed, just ask your agent:\n\n```text\nReview my code\nCheck for security issues\nWhat's wrong with my changes?\nRun a code review\nReview my PR\n```\n\nThe agent will automatically:\n\n1.",
        "guidance": "Once installed, just ask your agent:\n\n```text\nReview my code\nCheck for security issues\nWhat's wrong with my changes?\nRun a code review\nReview my PR\n```\n\nThe agent will automatically:\n\n1. Check if CodeRabbit CLI is installed and authenticated\n2. Run the review on your changes\n3. Present findings grouped by severity\n4. Optionally fix issues and re-review",
    },
    'supported-agents': {
        "description": 'CodeRabbit supports 35+ coding agents.',
        "guidance": 'CodeRabbit supports 35+ coding agents.\n\n| Agent              | Project Path           | Global Path                            |\n| ------------------ | ---------------------- | -------------------------------------- |\n| Amp, Kimi Code CLI | `.agents/skills/`      | `~/.config/agents/skills/`             |\n| Antigravity        | `.agent/skills/`       | `~/.gemini/antigravity/global_skills/` |\n| Claude Code        | `.claude/skills/`      | `~/.claude/skills/`                    |\n| Cline              | `.cline/skills/`       | `~/.cline/skills/`                     |\n| CodeBuddy          | `.codebuddy/skills/`   | `~/.codebuddy/skills/`                 |\n| Codex              | `.codex/skills/`       | `~/.codex/skills/`                     |\n| Command Code       | `.commandcode/skills/` | `~/.commandcode/skills/`               |\n| Continue           | `.continue/skills/`    | `~/.continue/skills/`                  |\n| Crush              | `.crush/skills/`       | `~/.config/crush/skills/`              |\n| Cursor             | `.cursor/skills/`      | `~/.cursor/skills/`                    |\n| Droid              | `.factory/skills/`     | `~/.factory/skills/`                   |\n| Gemini CLI         | `.gemini/skills/`      | `~/.gemini/skills/`                    |\n| GitHub Copilot     | `.github/skills/`      | `~/.copilot/skills/`                   |\n| Goose              | `.goose/skills/`       | `~/.config/goose/skills/`              |\n| Junie              | `.junie/skills/`       | `~/.junie/skills/`                     |\n| Kilo Code          | `.kilocode/skills/`    | `~/.kilocode/skills/`                  |\n| Kiro CLI           | `.kiro/skills/`        | `~/.kiro/skills/`                      |\n| Kode               | `.kode/skills/`        | `~/.kode/skills/`                      |\n| MCPJam             | `.mcpjam/skills/`      | `~/.mcpjam/skills/`                    |\n| Moltbot            | `skills/`              | `~/.moltbot/skills/`                   |\n| Mux                | `.mux/skills/`         | `~/.mux/skills/`                       |\n| Neovate            | `.neovate/skills/`     | `~/.neovate/skills/`                   |\n| OpenClaude IDE     | `.openclaude/skills/`  | `~/.openclaude/skills/`                |\n| OpenCode           | `.opencode/skills/`    | `~/.config/opencode/skills/`           |\n| OpenHands          | `.openhands/skills/`   | `~/.openhands/skills/`                 |\n| Pi                 | `.pi/skills/`          | `~/.pi/agent/skills/`                  |\n| Pochi              | `.pochi/skills/`       | `~/.pochi/skills/`                     |\n| Qoder              | `.qoder/skills/`       | `~/.qoder/skills/`                     |\n| Qwen Code          | `.qwen/skills/`        | `~/.qwen/skills/`                      |\n| Replit             | `.agent/skills/`       | N/A (project-only)                     |\n| Roo Code           | `.roo/skills/`         | `~/.roo/skills/`                       |\n| Trae               | `.trae/skills/`        | `~/.trae/skills/`                      |\n| Trae CN            | `.trae/skills/`        | `~/.trae-cn/skills/`                   |\n| Windsurf           | `.windsurf/skills/`    | `~/.codeium/windsurf/skills/`          |\n| Zencoder           | `.zencoder/skills/`    | `~/.zencoder/skills/`                  |',
    },
    'available-skills': {
        "description": '### [code-review](skills/code-review/SKILL.',
        "guidance": '### [code-review](skills/code-review/SKILL.md)\n\nAI-powered code review that finds bugs, security issues, and suggests improvements using CodeRabbit.\n\n**Use when:**\n\n- You want to review code changes before committing or merging\n- Checking for bugs, security vulnerabilities, or anti-patterns\n- Getting PR feedback or suggestions for improvements\n- Running automated code quality checks\n\n**Categories covered:** Bug detection, security analysis, code quality, performance issues, best practices\n\n**Triggers:** "review my code", "check for bugs", "security review", "PR feedback", "run coderabbit"\n\n**Capabilities:**\n\n- Analyzes code changes for bugs, security issues, and anti-patterns\n- Groups findings by severity (critical, warning, info)\n- Supports autonomous fix-review cycles\n- Works with staged, committed, or all changes\n\n### [autofix](skills/autofix/SKILL.md)\n\nSafe fix workflow for unresolved CodeRabbit GitHub PR review threads, with per-issue review and approval.\n\n**Use when:**\n\n- You already have an open GitHub PR reviewed by CodeRabbit\n- You want to apply suggested fixes from unresolved current CodeRabbit review threads\n- You want guided fixes with explicit approval for each change\n\n**Categories covered:** Review-thread extraction, issue prioritization, guarded fixes, consolidated commit and PR summary\n\n**Triggers:** "coderabbit autofix", "fix coderabbit", "cr fix"\n\n**Capabilities:**\n\n- Fetches unresolved current CodeRabbit review threads for the current PR\n- Parses and prioritizes issues by severity\n- Applies fixes only after validating the issue and getting approval\n- Produces a single consolidated commit and posts a PR summary comment',
    },
    'plugin-components': {
        "description": '### Claude Code\n\n- Slash command: `/coderabbit:review`\n- Subagent: `code-reviewer`\n- Marketplace manifest: `.',
        "guidance": '### Claude Code\n\n- Slash command: `/coderabbit:review`\n- Subagent: `code-reviewer`\n- Marketplace manifest: `.claude-plugin/plugin.json`\n\nThe `code-review` skill also remains available for natural-language triggering\ninside compatible agents.\n\n### Cursor\n\n- Marketplace manifest: `.cursor-plugin/plugin.json`\n- Skills source: `skills/`',
    },
    'resources': {
        "description": '- [CodeRabbit Documentation](https://coderabbit.',
        "guidance": '- [CodeRabbit Documentation](https://coderabbit.ai/docs)\n- [CodeRabbit CLI Guide](https://docs.coderabbit.ai/cli)\n- [Vercel Skills CLI](https://github.com/vercel-labs/skills)\n- [Agent Skills Specification](https://agentskills.io/specification)',
    },
    'license': {
        "description": 'MIT.',
        "guidance": 'MIT',
    },
}


@mcp.tool()
def list_coderabbitai_skills_skills() -> dict:
    """List all available coderabbitai_skills skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_coderabbitai_skills_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific coderabbitai_skills skill."""
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
    hint = get_presentation_hint('coderabbitai_skills', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@coderabbitai_skills",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'coderabbitai_skills',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
