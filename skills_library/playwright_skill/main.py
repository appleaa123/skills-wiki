"""Skill: playwright_skill."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("playwright-skill")


_SKILLS: dict[str, dict] = {
    'features': {
        "description": '- **Any Automation Task** - Claude writes custom code for your specific request, not limited to pre-built scripts\n- **Visible Browser by Default** - See automation in real-time with `headless: false`\n',
        "guidance": '- **Any Automation Task** - Claude writes custom code for your specific request, not limited to pre-built scripts\n- **Visible Browser by Default** - See automation in real-time with `headless: false`\n- **Zero Module Resolution Errors** - Universal executor ensures proper module access\n- **Progressive Disclosure** - Concise SKILL.md with full API reference loaded only when needed\n- **Safe Cleanup** - Smart temp file management without race conditions\n- **Comprehensive Helpers** - Optional utility functions for common tasks',
    },
    'installation': {
        "description": 'This repository is structured as a [Claude Code Plugin](https://docs.',
        "guidance": 'This repository is structured as a [Claude Code Plugin](https://docs.claude.com/en/docs/claude-code/plugins) containing a skill. You can install it as either a **plugin** (recommended) or extract it as a **standalone skill**.\n\n### Understanding the Structure\n\nThis repository uses the plugin format with a nested structure:\n\n```\nplaywright-skill/              # Plugin root\n├── .claude-plugin/           # Plugin metadata\n└── skills/\n    └── playwright-skill/     # The actual skill\n        └── SKILL.md\n```\n\nClaude Code expects skills to be directly in folders under `.claude/skills/`, so manual installation requires extracting the nested skill folder.\n\n---\n\n### Option 1: Plugin Installation (Recommended)\n\nInstall via Claude Code\'s plugin system for automatic updates and team distribution:\n\n```bash\n# Add this repository as a marketplace\n/plugin marketplace add lackeyjb/playwright-skill\n\n# Install the plugin\n/plugin install playwright-skill@playwright-skill\n\n# Navigate to the skill directory and run setup\ncd ~/.claude/plugins/marketplaces/playwright-skill/skills/playwright-skill\nnpm run setup\n```\n\nVerify installation by running `/help` to confirm the skill is available.\n\n---\n\n### Option 2: Standalone Skill Installation\n\nTo install as a standalone skill (without the plugin system), extract only the skill folder:\n\n**Global Installation (Available Everywhere):**\n\n```bash\n# Clone to a temporary location\ngit clone https://github.com/lackeyjb/playwright-skill.git /tmp/playwright-skill-temp\n\n# Copy only the skill folder to your global skills directory\nmkdir -p ~/.claude/skills\ncp -r /tmp/playwright-skill-temp/skills/playwright-skill ~/.claude/skills/\n\n# Navigate to the skill and run setup\ncd ~/.claude/skills/playwright-skill\nnpm run setup\n\n# Clean up temporary files\nrm -rf /tmp/playwright-skill-temp\n```\n\n**Project-Specific Installation:**\n\n```bash\n# Clone to a temporary location\ngit clone https://github.com/lackeyjb/playwright-skill.git /tmp/playwright-skill-temp\n\n# Copy only the skill folder to your project\nmkdir -p .claude/skills\ncp -r /tmp/playwright-skill-temp/skills/playwright-skill .claude/skills/\n\n# Navigate to the skill and run setup\ncd .claude/skills/playwright-skill\nnpm run setup\n\n# Clean up temporary files\nrm -rf /tmp/playwright-skill-temp\n```\n\n**Why this structure?** The plugin format requires the `skills/` directory for organizing multiple skills within a plugin. When installing as a standalone skill, you only need the inner `skills/playwright-skill/` folder contents.\n\n---\n\n### Option 3: Download Release\n\n1. Download and extract the latest release from [GitHub Releases](https://github.com/lackeyjb/playwright-skill/releases)\n2. Copy only the `skills/playwright-skill/` folder to:\n   - Global: `~/.claude/skills/playwright-skill`\n   - Project: `/path/to/your/project/.claude/skills/playwright-skill`\n3. Navigate to the skill directory and run setup:\n   ```bash\n   cd ~/.claude/skills/playwright-skill  # or your project path\n   npm run setup\n   ```\n\n---\n\n### Verify Installation\n\nRun `/help` to confirm the skill is loaded, then ask Claude to perform a simple browser task like "Test if google.com loads".',
    },
    'quick-start': {
        "description": 'After installation, simply ask Claude to test or automate any browser task.',
        "guidance": 'After installation, simply ask Claude to test or automate any browser task. Claude will write custom Playwright code, execute it, and return results with screenshots and console output.',
    },
    'usage-examples': {
        "description": '### Test Any Page\n\n```\n"Test the homepage"\n"Check if the contact form works"\n"Verify the signup flow"\n```\n\n### Visual Testing\n\n```\n"Take screenshots of the dashboard in mobile and desktop"\n"Test respo',
        "guidance": '### Test Any Page\n\n```\n"Test the homepage"\n"Check if the contact form works"\n"Verify the signup flow"\n```\n\n### Visual Testing\n\n```\n"Take screenshots of the dashboard in mobile and desktop"\n"Test responsive design across different viewports"\n```\n\n### Interaction Testing\n\n```\n"Fill out the registration form and submit it"\n"Click through the main navigation"\n"Test the search functionality"\n```\n\n### Validation\n\n```\n"Check for broken links"\n"Verify all images load"\n"Test form validation"\n```',
    },
    'how-it-works': {
        "description": '1.',
        "guidance": '1. Describe what you want to test or automate\n2. Claude writes custom Playwright code for the task\n3. The universal executor (run.js) runs it with proper module resolution\n4. Browser opens (visible by default) and automation executes\n5. Results are displayed with console output and screenshots',
    },
    'configuration': {
        "description": 'Default settings:\n\n- **Headless:** `false` (browser visible unless explicitly requested otherwise)\n- **Slow Motion:** `100ms` for visibility\n- **Timeout:** `30s`\n- **Screenshots:** Saved to `/tmp/`.',
        "guidance": 'Default settings:\n\n- **Headless:** `false` (browser visible unless explicitly requested otherwise)\n- **Slow Motion:** `100ms` for visibility\n- **Timeout:** `30s`\n- **Screenshots:** Saved to `/tmp/`',
    },
    'project-structure': {
        "description": '```\nplaywright-skill/\n├──.',
        "guidance": '```\nplaywright-skill/\n├── .claude-plugin/\n│   ├── plugin.json          # Plugin metadata for distribution\n│   └── marketplace.json     # Marketplace configuration\n├── skills/\n│   └── playwright-skill/    # The actual skill (Claude discovers this)\n│       ├── SKILL.md         # What Claude reads\n│       ├── run.js           # Universal executor (proper module resolution)\n│       ├── package.json     # Dependencies & setup scripts\n│       └── lib/\n│           └── helpers.js   # Optional utility functions\n│       └── API_REFERENCE.md # Full Playwright API reference\n├── README.md                # This file - user documentation\n├── CONTRIBUTING.md          # Contribution guidelines\n└── LICENSE                  # MIT License\n```',
    },
    'advanced-usage': {
        "description": 'Claude will automatically load `API_REFERENCE.',
        "guidance": 'Claude will automatically load `API_REFERENCE.md` when needed for comprehensive documentation on selectors, network interception, authentication, visual regression testing, mobile emulation, performance testing, and debugging.',
    },
    'dependencies': {
        "description": '- Node.',
        "guidance": '- Node.js\n- Playwright (installed via `npm run setup`)\n- Chromium (installed via `npm run setup`)',
    },
    'troubleshooting': {
        "description": '**Playwright not installed?**\nNavigate to the skill directory and run `npm run setup`.',
        "guidance": "**Playwright not installed?**\nNavigate to the skill directory and run `npm run setup`.\n\n**Module not found errors?**\nEnsure automation runs via `run.js`, which handles module resolution.\n\n**Browser doesn't open?**\nVerify `headless: false` is set. The skill defaults to visible browser unless headless mode is requested.\n\n**Install all browsers?**\nRun `npm run install-all-browsers` from the skill directory.",
    },
    'what-is-a-skill': {
        "description": '[Agent Skills](https://agentskills.',
        "guidance": '[Agent Skills](https://agentskills.io) are folders of instructions, scripts, and resources that agents can discover and use to do things more accurately and efficiently. When you ask Claude to test a webpage or automate browser interactions, Claude discovers this skill, loads the necessary instructions, executes custom Playwright code, and returns results with screenshots and console output.\n\nThis Playwright skill implements the [open Agent Skills specification](https://agentskills.io), making it compatible across agent platforms.',
    },
    'contributing': {
        "description": 'Contributions are welcome.',
        "guidance": 'Contributions are welcome. Fork the repository, create a feature branch, make your changes, and submit a pull request. See [CONTRIBUTING.md](CONTRIBUTING.md) for details.',
    },
    'learn-more': {
        "description": '- [Agent Skills Specification](https://agentskills.',
        "guidance": '- [Agent Skills Specification](https://agentskills.io) - Open specification for agent skills\n- [Claude Code Skills Documentation](https://docs.claude.com/en/docs/claude-code/skills)\n- [Claude Code Plugins Documentation](https://docs.claude.com/en/docs/claude-code/plugins)\n- [Plugin Marketplaces](https://docs.claude.com/en/docs/claude-code/plugin-marketplaces)\n- [API_REFERENCE.md](skills/playwright-skill/API_REFERENCE.md) - Full Playwright documentation\n- [GitHub Issues](https://github.com/lackeyjb/playwright-skill/issues)',
    },
    'license': {
        "description": 'MIT License - see [LICENSE](LICENSE) file for details.',
        "guidance": 'MIT License - see [LICENSE](LICENSE) file for details.',
    },
}


@mcp.tool()
def list_playwright_skill_skills() -> dict:
    """List all available playwright_skill skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_playwright_skill_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific playwright_skill skill."""
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
    hint = get_presentation_hint('playwright_skill', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@playwright_skill",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'playwright_skill',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
