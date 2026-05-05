"""Skill: superpowers."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("superpowers")


_SKILLS: dict[str, dict] = {
    'how-it-works': {
        "description": 'It starts from the moment you fire up your coding agent.',
        "guidance": 'It starts from the moment you fire up your coding agent. As soon as it sees that you\'re building something, it *doesn\'t* just jump into trying to write code. Instead, it steps back and asks you what you\'re really trying to do. \n\nOnce it\'s teased a spec out of the conversation, it shows it to you in chunks short enough to actually read and digest. \n\nAfter you\'ve signed off on the design, your agent puts together an implementation plan that\'s clear enough for an enthusiastic junior engineer with poor taste, no judgement, no project context, and an aversion to testing to follow. It emphasizes true red/green TDD, YAGNI (You Aren\'t Gonna Need It), and DRY. \n\nNext up, once you say "go", it launches a *subagent-driven-development* process, having agents work through each engineering task, inspecting and reviewing their work, and continuing forward. It\'s not uncommon for Claude to be able to work autonomously for a couple hours at a time without deviating from the plan you put together.\n\nThere\'s a bunch more to it, but that\'s the core of the system. And because the skills trigger automatically, you don\'t need to do anything special. Your coding agent just has Superpowers.',
    },
    'sponsorship': {
        "description": "If Superpowers has helped you do stuff that makes money and you are so inclined, I'd greatly appreciate it if you'd consider [sponsoring my opensource work](https://github.",
        "guidance": "If Superpowers has helped you do stuff that makes money and you are so inclined, I'd greatly appreciate it if you'd consider [sponsoring my opensource work](https://github.com/sponsors/obra).\n\nThanks! \n\n- Jesse",
    },
    'installation': {
        "description": '**Note:** Installation differs by platform.',
        "guidance": '**Note:** Installation differs by platform. \n\n### Claude Code Official Marketplace\n\nSuperpowers is available via the [official Claude plugin marketplace](https://claude.com/plugins/superpowers)\n\nInstall the plugin from Anthropic\'s official marketplace:\n\n```bash\n/plugin install superpowers@claude-plugins-official\n```\n\n### Claude Code (Superpowers Marketplace)\n\nThe Superpowers marketplace provides Superpowers and some other related plugins for Claude Code.\n\nIn Claude Code, register the marketplace first:\n\n```bash\n/plugin marketplace add obra/superpowers-marketplace\n```\n\nThen install the plugin from this marketplace:\n\n```bash\n/plugin install superpowers@superpowers-marketplace\n```\n\n### OpenAI Codex CLI\n\n- Open plugin search interface\n\n```bash\n/plugins\n```\n\nSearch for Superpowers\n\n```bash\nsuperpowers\n```\n\nSelect `Install Plugin`\n\n### OpenAI Codex App\n\n- In the Codex app, click on Plugins in the sidebar.\n- You should see `Superpowers` in the Coding section. \n- Click the `+` next to Superpowers and follow the prompts.\n\n\n### Cursor (via Plugin Marketplace)\n\nIn Cursor Agent chat, install from marketplace:\n\n```text\n/add-plugin superpowers\n```\n\nor search for "superpowers" in the plugin marketplace.\n\n### OpenCode\n\nTell OpenCode:\n\n```\nFetch and follow instructions from https://raw.githubusercontent.com/obra/superpowers/refs/heads/main/.opencode/INSTALL.md\n```\n\n**Detailed docs:** [docs/README.opencode.md](docs/README.opencode.md)\n\n### GitHub Copilot CLI\n\n```bash\ncopilot plugin marketplace add obra/superpowers-marketplace\ncopilot plugin install superpowers@superpowers-marketplace\n```\n\n### Gemini CLI\n\n```bash\ngemini extensions install https://github.com/obra/superpowers\n```\n\nTo update:\n\n```bash\ngemini extensions update superpowers\n```',
    },
    'the-basic-workflow': {
        "description": '1.',
        "guidance": '1. **brainstorming** - Activates before writing code. Refines rough ideas through questions, explores alternatives, presents design in sections for validation. Saves design document.\n\n2. **using-git-worktrees** - Activates after design approval. Creates isolated workspace on new branch, runs project setup, verifies clean test baseline.\n\n3. **writing-plans** - Activates with approved design. Breaks work into bite-sized tasks (2-5 minutes each). Every task has exact file paths, complete code, verification steps.\n\n4. **subagent-driven-development** or **executing-plans** - Activates with plan. Dispatches fresh subagent per task with two-stage review (spec compliance, then code quality), or executes in batches with human checkpoints.\n\n5. **test-driven-development** - Activates during implementation. Enforces RED-GREEN-REFACTOR: write failing test, watch it fail, write minimal code, watch it pass, commit. Deletes code written before tests.\n\n6. **requesting-code-review** - Activates between tasks. Reviews against plan, reports issues by severity. Critical issues block progress.\n\n7. **finishing-a-development-branch** - Activates when tasks complete. Verifies tests, presents options (merge/PR/keep/discard), cleans up worktree.\n\n**The agent checks for relevant skills before any task.** Mandatory workflows, not suggestions.',
    },
    'what-s-inside': {
        "description": '### Skills Library\n\n**Testing**\n- **test-driven-development** - RED-GREEN-REFACTOR cycle (includes testing anti-patterns reference)\n\n**Debugging**\n- **systematic-debugging** - 4-phase root cause proce',
        "guidance": "### Skills Library\n\n**Testing**\n- **test-driven-development** - RED-GREEN-REFACTOR cycle (includes testing anti-patterns reference)\n\n**Debugging**\n- **systematic-debugging** - 4-phase root cause process (includes root-cause-tracing, defense-in-depth, condition-based-waiting techniques)\n- **verification-before-completion** - Ensure it's actually fixed\n\n**Collaboration** \n- **brainstorming** - Socratic design refinement\n- **writing-plans** - Detailed implementation plans\n- **executing-plans** - Batch execution with checkpoints\n- **dispatching-parallel-agents** - Concurrent subagent workflows\n- **requesting-code-review** - Pre-review checklist\n- **receiving-code-review** - Responding to feedback\n- **using-git-worktrees** - Parallel development branches\n- **finishing-a-development-branch** - Merge/PR decision workflow\n- **subagent-driven-development** - Fast iteration with two-stage review (spec compliance, then code quality)\n\n**Meta**\n- **writing-skills** - Create new skills following best practices (includes testing methodology)\n- **using-superpowers** - Introduction to the skills system",
    },
    'philosophy': {
        "description": '- **Test-Driven Development** - Write tests first, always\n- **Systematic over ad-hoc** - Process over guessing\n- **Complexity reduction** - Simplicity as primary goal\n- **Evidence over claims** - Veri',
        "guidance": '- **Test-Driven Development** - Write tests first, always\n- **Systematic over ad-hoc** - Process over guessing\n- **Complexity reduction** - Simplicity as primary goal\n- **Evidence over claims** - Verify before declaring success\n\nRead [the original release announcement](https://blog.fsck.com/2025/10/09/superpowers/).',
    },
    'contributing': {
        "description": 'The general contribution process for Superpowers is below.',
        "guidance": "The general contribution process for Superpowers is below. Keep in mind that we don't generally accept contributions of new skills and that any updates to skills must work across all of the coding agents we support.\n\n1. Fork the repository\n2. Switch to the 'dev' branch\n3. Create a branch for your work\n4. Follow the `writing-skills` skill for creating and testing new and modified skills\n5. Submit a PR, being sure to fill in the pull request template.\n\nSee `skills/writing-skills/SKILL.md` for the complete guide.",
    },
    'updating': {
        "description": 'Superpowers updates are somewhat coding-agent dependent, but are often automatic.',
        "guidance": 'Superpowers updates are somewhat coding-agent dependent, but are often automatic.',
    },
    'license': {
        "description": 'MIT License - see LICENSE file for details.',
        "guidance": 'MIT License - see LICENSE file for details',
    },
    'community': {
        "description": 'Superpowers is built by [Jesse Vincent](https://blog.',
        "guidance": "Superpowers is built by [Jesse Vincent](https://blog.fsck.com) and the rest of the folks at [Prime Radiant](https://primeradiant.com).\n\n- **Discord**: [Join us](https://discord.gg/35wsABTejz) for community support, questions, and sharing what you're building with Superpowers\n- **Issues**: https://github.com/obra/superpowers/issues\n- **Release announcements**: [Sign up](https://primeradiant.com/superpowers/) to get notified about new versions",
    },
}


@mcp.tool()
def list_superpowers_skills() -> dict:
    """List all available superpowers skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_superpowers_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific superpowers skill."""
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
    hint = get_presentation_hint('superpowers', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@superpowers",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'superpowers',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
