"""Skill: common_tasks_agent_skills."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("common-tasks-agent-skills")


_SKILLS: dict[str, dict] = {
    'installation': {
        "description": '```bash\nnpx skills add Shpigford/skills\n```\n\nOr manually:\n\n```bash\ngit clone https://github.',
        "guidance": '```bash\nnpx skills add Shpigford/skills\n```\n\nOr manually:\n\n```bash\ngit clone https://github.com/Shpigford/skills.git ~/.skills/shpigford\n```',
    },
    'available-skills': {
        "description": '| Skill | Description |\n|-------|-------------|\n| [build](#build) | Feature development pipeline with research, planning, and phased implementation |\n| [but-for-real](#but-for-real) | Skeptical self-r',
        "guidance": '| Skill | Description |\n|-------|-------------|\n| [build](#build) | Feature development pipeline with research, planning, and phased implementation |\n| [but-for-real](#but-for-real) | Skeptical self-review that forces verification before declaring victory |\n| [chat-widget](#chat-widget) | Real-time support chat system with user widget and admin dashboard |\n| [conductor-setup](#conductor-setup) | Configure a Rails project for Conductor parallel coding agents |\n| [favicon](#favicon) | Generate a complete favicon set from a source image |\n| [feature-image](#feature-image) | Generate branded social media images for feature announcements |\n| [issues](#issues) | Create, list, and view GitHub issues via the gh CLI |\n| [learnings](#learnings) | Pre-commit sweep for session insights worth codifying in CLAUDE.md or README.md |\n| [new-rails-project](#new-rails-project) | Scaffold a new Rails 8 project with Inertia, React, and Vite |\n| [research](#research) | Deep research before planning — parallel agents search docs, web, and codebase |\n| [readme](#readme) | Generate absurdly thorough README documentation for any project |\n| [screenshots](#screenshots) | Capture retina-quality marketing screenshots with Playwright |\n\n---\n\n### build\n\nA 4-phase feature development pipeline that walks you through research, implementation planning, progress tracking, and phased execution. Each phase produces documented artifacts (RESEARCH.md, IMPLEMENTATION.md, PROGRESS.md) and uses deep research including web search, documentation lookup, and codebase exploration before writing code.\n\n- Subcommands: `research`, `implementation`, `progress`, `phase`, `status`\n\n```bash\n/build research chat-interface\n/build implementation chat-interface\n/build phase 1 chat-interface\n```\n\n---\n\n### but-for-real\n\nForces a ruthless self-review of your own work. Reads the git diff, checks every changed line, hunts for forgotten tests, missed edge cases, dead code, and logic errors. Then actually runs the code to verify it works instead of pattern-matching to "looks correct."\n\n```bash\n/but-for-real\n```\n\n---\n\n### chat-widget\n\nBuilds a complete real-time support chat system: a floating widget for end users and an admin dashboard for support staff. Covers data models, WebSocket channels, REST APIs, frontend components (React, Vue, Rails), email notifications, and message deduplication. Includes framework-specific guidance for Rails, React, Next.js, Laravel, and Vue.\n\n```bash\n/chat-widget\n```\n\n---\n\n### conductor-setup\n\nConfigures a Rails project to work with Conductor, the Mac app for parallel coding agents. Creates `conductor.json`, setup scripts, and a port-aware server script. Updates Redis configuration across Sidekiq, ActionCable, caching, and Rack::Attack to use environment variables for workspace isolation.\n\n```bash\n/conductor-setup\n```\n\n---\n\n### favicon\n\nGenerates a complete set of favicons (ICO, PNG, Apple Touch Icon, web manifest icons) from a single source image using ImageMagick. Auto-detects the project framework to place files in the correct static directory and updates the HTML layout with proper link tags.\n\nRequires: ImageMagick v7+\n\n```bash\n/favicon path/to/logo.svg\n```\n\n---\n\n### feature-image\n\nGenerates branded social media announcement images by analyzing your git history to detect what changed, extracting your brand\'s colors/fonts/visual patterns from the codebase, building a styled HTML page, and screenshotting it with Playwright. Supports stylized mockup, screenshot+overlay, and abstract styles.\n\nRequires: Playwright\n\n```bash\n/feature-image dark mode support\n```\n\n---\n\n### issues\n\nInteractive GitHub issue management. Create issues with guided title/body/label prompts, list issues with filters (assignee, author, label), or view issue details. Enforces short, scannable titles and detailed bodies.\n\nRequires: `gh` CLI\n\n```bash\n/issues\n```\n\n---\n\n### learnings\n\nPre-commit sweep that reviews the current session\'s code changes, user corrections, and discoveries to identify anything worth codifying in CLAUDE.md or README.md. Applies a high bar — most sessions produce nothing worth adding, and that\'s a valid outcome. Proposes edits but never writes to load-bearing files without approval.\n\nTriggers: "anything learned?", "anything to note?", "should we update CLAUDE.md?"\n\n```bash\n/learnings\n```\n\n---\n\n### new-rails-project\n\nScaffolds a new Rails 8 project with a full modern stack: Inertia.js + React + Vite + Tailwind CSS + Sidekiq + Redis. Configures UUID primary keys, timestamptz columns, minitest, and RuboCop. Verifies the boilerplate runs via Playwright.\n\n```bash\n/new-rails-project my-app\n```\n\n---\n\n### research\n\nDeep research skill that runs before planning or implementation. Clarifies ambiguities with the user first, then launches parallel sub-agents to search the codebase, official docs (via Context7), and the web. Synthesizes findings into a structured output with evidence, sources, downsides, and a recommendation — then flows into Plan mode.\n\n- Agents: codebase, docs, web, dependencies, UI, UX, delight (matched to problem complexity)\n\n```bash\n/research how should we handle webhook retries\n/research why is the dashboard slow on mobile\n```\n\n---\n\n### readme\n\nGenerates comprehensive README documentation by deeply exploring the codebase first. Covers local setup, architecture (directory structure, request lifecycle, data flow), environment variables, available scripts, testing, deployment (auto-detected platform), and troubleshooting. Writes directly to README.md.\n\n```bash\n/readme\n```\n\n---\n\n### screenshots\n\nCaptures retina-quality (2x) marketing screenshots using Playwright. Analyzes routes and components to discover screenshottable features, handles authentication with smart form detection, and produces consistently sized HiDPI images ready for Product Hunt, social media, or landing pages.\n\nRequires: Playwright\n\n```bash\n/screenshots http://localhost:3000\n```\n\n---',
    },
    'compatibility': {
        "description": 'These skills work with any Agent Skills Standard-compatible tool:\n\n- Claude Code (Anthropic)\n- Cursor\n- Gemini Code Assist (Google)\n- GitHub Copilot (Microsoft).',
        "guidance": 'These skills work with any Agent Skills Standard-compatible tool:\n\n- Claude Code (Anthropic)\n- Cursor\n- Gemini Code Assist (Google)\n- GitHub Copilot (Microsoft)',
    },
    'license': {
        "description": 'MIT.',
        "guidance": 'MIT',
    },
}


@mcp.tool()
def list_common_tasks_agent_skills_skills() -> dict:
    """List all available common_tasks_agent_skills skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_common_tasks_agent_skills_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific common_tasks_agent_skills skill."""
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
    hint = get_presentation_hint('common_tasks_agent_skills', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@common_tasks_agent_skills",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'common_tasks_agent_skills',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
