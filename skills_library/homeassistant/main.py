"""Skill: homeassistant."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("homeassistant")


_SKILLS: dict[str, dict] = {
    'see-it-in-action': {
        "description": '### Quick Skill Check\nVerify Claude can see and use this skill:\n\nhttps://github.',
        "guidance": '### Quick Skill Check\nVerify Claude can see and use this skill:\n\nhttps://github.com/user-attachments/assets/a215df83-ce84-4ed2-bb93-f3a3ee0c43e8\n\n*Shows Claude recognizing the skill and loading Home Assistant expertise*\n\n### Full Workflow Demo\nWatch the complete workflow in action - end to end (3x speed):\n\n\nhttps://github.com/user-attachments/assets/eab53b18-ae2b-4d43-b1e4-e45bf9357099\n\n*Complete automation development cycle including deployment, testing, log analysis, and git workflow*',
    },
    'what-this-skill-does': {
        "description": 'This Claude Code skill transforms Claude into a **Home Assistant expert** that helps you:\n\n### Configuration Management\n- **Rapid Development Workflow**: Deploy changes via `scp` for instant testing, ',
        "guidance": 'This Claude Code skill transforms Claude into a **Home Assistant expert** that helps you:\n\n### Configuration Management\n- **Rapid Development Workflow**: Deploy changes via `scp` for instant testing, commit to git when stable\n- **Smart Reload vs Restart**: Automatically determines whether to reload or restart based on change type\n- **Configuration Validation**: Always validates before applying changes to prevent downtime\n- **Remote CLI Access**: Seamlessly manages HA instances via SSH and `hass-cli`\n\n### Automation Development\n- **Complete Verification Protocol**: Automatically tests automations by triggering manually and checking logs\n- **Error Detection**: Identifies template errors, type mismatches, and execution failures\n- **Log Analysis Patterns**: Knows what success and error indicators to look for\n- **Iterative Fix Workflow**: Guides through debugging and re-testing cycles\n\n### Lovelace Dashboard Development\n- **Tablet Optimization**: Creates touch-friendly dashboards optimized for specific screen sizes (7", 11", 13")\n- **Card Type Expertise**: Knows when to use Mushroom cards, Tile cards, Panel vs Sections views\n- **Template Patterns**: Provides ready-to-use Jinja2 templates for common use cases:\n  - Door/window counting with color coding\n  - Conditional display based on time/state\n  - Multi-condition status indicators\n- **Common Pitfall Solutions**: Solves dashboard registration, auto-entities failures, template type errors\n- **Real-World Examples**: Includes working examples from production tablet dashboards\n\n### Workflow Optimization\n- **Git + scp Hybrid**: Uses git for version control, scp for rapid iteration\n- **No Restart for Dashboards**: Deploys dashboard changes with just browser refresh\n- **Context7 Integration**: Leverages official HA documentation via MCP when available\n- **Deployment Decision Tree**: Guides through the optimal workflow based on change type',
    },
    'installation': {
        "description": '### Prerequisites\n\n1.',
        "guidance": '### Prerequisites\n\n1. **Claude Code** installed and configured\n2. **Home Assistant** instance with:\n   - SSH access enabled\n   - Git repository connected to `/config` directory\n3. **Local tools**:\n   - `hass-cli` installed (`pipx install homeassistant-cli`)\n   - SSH key authentication configured\n   - Environment variables set: `HASS_SERVER`, `HASS_TOKEN`\n\n### Install the Skill\n\n#### Option 1: Clone into your Home Assistant config repository\n\n```bash\ncd /path/to/your/homeassistant/config\nmkdir -p .claude/skills\ncd .claude/skills\ngit clone git@github.com:komal-SkyNET/claude-skill-homeassistant.git home-assistant-manager\n```\n\n#### Option 2: Download and extract\n\n```bash\ncd /path/to/your/homeassistant/config\nmkdir -p .claude/skills/home-assistant-manager\ncd .claude/skills/home-assistant-manager\ncurl -L https://github.com/komal-SkyNET/claude-skill-homeassistant/archive/main.tar.gz | tar xz --strip-components=1\n```\n\n### Verify Installation\n\nThe skill should appear when you start Claude Code in your Home Assistant repository. Claude will automatically load the skill and apply the expertise.',
    },
    'usage-examples': {
        "description": '### Example 1: Create a New Automation\n\n```\nUser: "Create an automation that sends a notification when the front door\n       is left open for more than 5 minutes"\n\nClaude: [Uses skill to]:\n1.',
        "guidance": '### Example 1: Create a New Automation\n\n```\nUser: "Create an automation that sends a notification when the front door\n       is left open for more than 5 minutes"\n\nClaude: [Uses skill to]:\n1. Create automation YAML with proper syntax\n2. Deploy via scp for testing\n3. Reload automations (no restart needed)\n4. Manually trigger to test\n5. Check logs for execution\n6. Verify notification received\n7. Commit to git when working\n```\n\n### Example 2: Build a Tablet Dashboard\n\n```\nUser: "Create a dashboard for my 11-inch tablet in the living room\n       with lights, thermostat, and door status"\n\nClaude: [Uses skill to]:\n1. Create new dashboard file in .storage/\n2. Register in lovelace_dashboards\n3. Use 3-column grid layout (optimal for 11")\n4. Add Mushroom cards for touch-friendly controls\n5. Create template card with door counting\n6. Deploy via scp for instant preview\n7. Iterate on layout based on feedback\n8. Commit when finalized\n```\n\n### Example 3: Debug a Template Error\n\n```\nUser: "My automation has a TypeError about comparing str and int"\n\nClaude: [Uses skill to]:\n1. Check logs for exact error message\n2. Identify template needs | int filter\n3. Fix the template syntax\n4. Deploy via scp\n5. Trigger manually to verify\n6. Check logs confirm no errors\n7. Commit the fix\n```',
    },
    'skill-architecture': {
        "description": 'This skill provides expertise in three core areas:\n\n### 1.',
        "guidance": 'This skill provides expertise in three core areas:\n\n### 1. Remote Access Patterns\n- `hass-cli` commands with environment variables\n- SSH-based `ha` CLI commands\n- Log analysis and error detection\n- State verification\n\n### 2. Deployment Workflows\n- **Git workflow**: For final, tested changes\n- **scp workflow**: For rapid iteration (dashboards, testing)\n- **Reload vs Restart**: Smart decision making\n- **Verification protocols**: Always check outcomes\n\n### 3. Dashboard Development\n- **View types**: Panel (full-screen) vs Sections (organized)\n- **Card types**: Mushroom, Tile, Template, Auto-entities\n- **Template patterns**: Jinja2 snippets for common use cases\n- **Debugging**: JSON validation, template testing, entity verification',
    },
    'contributing': {
        "description": 'We welcome contributions from the Home Assistant community! This skill has been developed through real-world usage and we want to keep improving it.',
        "guidance": 'We welcome contributions from the Home Assistant community! This skill has been developed through real-world usage and we want to keep improving it.\n\n### What to Contribute\n\n**🎯 Focus on Home Assistant-specific expertise:**\n\n✅ **GOOD contributions:**\n- New template patterns for common use cases\n- Solutions to specific HA configuration pitfalls\n- Dashboard card examples for different devices\n- Integration-specific deployment workflows\n- Automation verification patterns\n- Log analysis patterns for specific errors\n\n❌ **AVOID generic contributions:**\n- General git workflows (unless HA-specific)\n- Generic Python/YAML best practices\n- Non-HA development workflows\n\n### Contribution Guidelines\n\n#### 1. Template Pattern Contributions\n\nAdd to the "Common Template Patterns" section:\n\n```markdown\n**Your Pattern Name:**\n```jinja2\n{% set entities = [...] %}\n{{ your_template_logic }}\n```\n\n**Use case:** Explain when to use this\n**Example output:** Show what it produces\n```\n\n#### 2. Dashboard Card Examples\n\nAdd to "Real-World Examples":\n\n```markdown\n### Your Card Name\n```json\n{\n  "type": "...",\n  ...\n}\n```\n\n**Best for:** Device type, use case\n**Features:** What makes this example useful\n```\n\n#### 3. Pitfall Solutions\n\nAdd to "Common Pitfalls":\n\n```markdown\n**Problem X: Brief description**\n- **Symptom:** What the user sees\n- **Cause:** Root cause explanation\n- **Fix:** Step-by-step solution\n```\n\n#### 4. Workflow Improvements\n\nIf proposing workflow changes:\n- Explain the problem with current workflow\n- Provide specific HA scenario where it applies\n- Show before/after comparison\n- Include verification steps\n\n### How to Submit\n\n1. **Fork the repository**\n2. **Create a feature branch**: `git checkout -b feature/your-contribution-name`\n3. **Make your changes** to `SKILL.md`\n4. **Test thoroughly** in your own HA environment\n5. **Update README.md** if adding new capabilities\n6. **Submit a Pull Request** with:\n   - Clear description of what you\'re adding\n   - Example usage scenario\n   - Verification that it works in real HA setup\n\n### Contribution Review Process\n\nPRs are reviewed for:\n- ✅ **HA-specific value**: Does it solve a real HA problem?\n- ✅ **Accuracy**: Is the information correct and up-to-date?\n- ✅ **Clarity**: Is it well-documented and easy to understand?\n- ✅ **Tested**: Has it been verified in a real HA environment?',
    },
    'skill-structure': {
        "description": '```\nhome-assistant-manager/\n├── SKILL.',
        "guidance": '```\nhome-assistant-manager/\n├── SKILL.md          # Main skill content with YAML frontmatter\n├── README.md         # This file\n└── LICENSE           # MIT License\n```\n\nThe skill follows the [official Claude skills specification](https://github.com/anthropics/skills):\n- `SKILL.md` contains YAML frontmatter with `name` and `description`\n- Content organized in logical sections\n- Includes examples, patterns, and workflows\n- Focused on actionable expertise',
    },
    'environment-setup': {
        "description": 'For the skill to work optimally, ensure your environment has:\n\n### SSH Access\n```bash\n# Test SSH access\nssh root@homeassistant.',
        "guidance": 'For the skill to work optimally, ensure your environment has:\n\n### SSH Access\n```bash\n# Test SSH access\nssh root@homeassistant.local "ha core info"\n```\n\n### hass-cli Setup\n```bash\n# Install hass-cli\npipx install homeassistant-cli\n\n# Set environment variables (add to ~/.bashrc or ~/.zshrc)\nexport HASS_SERVER=http://homeassistant.local:8123\nexport HASS_TOKEN=your_long_lived_access_token\n\n# Test hass-cli\nhass-cli state list\n```\n\n### Git Repository\n```bash\n# Your HA config should be a git repository\ncd /config\ngit init\ngit remote add origin your-repo-url\n\n# Claude should be run from this directory\n```\n\n### Context7 MCP (Optional but Recommended)\n```bash\n# Add Context7 for official HA documentation\nclaude mcp add --transport http context7 https://mcp.context7.com/mcp \\\n  --header "CONTEXT7_API_KEY: your_api_key"\n```',
    },
    'use-cases': {
        "description": '### DevOps & Configuration Management\n- Rapid automation development and testing\n- Safe configuration changes with validation\n- Remote HA instance management\n- Git-based version control workflow\n\n### ',
        "guidance": '### DevOps & Configuration Management\n- Rapid automation development and testing\n- Safe configuration changes with validation\n- Remote HA instance management\n- Git-based version control workflow\n\n### Dashboard Development\n- Tablet-optimized control panels\n- Wall-mounted dashboard displays\n- Mobile-responsive layouts\n- Touch-friendly interface design\n\n### Template Development\n- Jinja2 template creation and debugging\n- Dynamic sensor calculations\n- Conditional automation logic\n- Custom card configurations\n\n### Troubleshooting\n- Log analysis and error detection\n- Template type error resolution\n- Dashboard debugging\n- Integration configuration issues',
    },
    'related-resources': {
        "description": '- [Official Claude Skills Repository](https://github.',
        "guidance": '- [Official Claude Skills Repository](https://github.com/anthropics/skills)\n- [Home Assistant Documentation](https://www.home-assistant.io/docs/)\n- [Lovelace UI Documentation](https://www.home-assistant.io/lovelace/)\n- [Home Assistant Community](https://community.home-assistant.io/)',
    },
    'license': {
        "description": 'MIT License - See [LICENSE](LICENSE) file for details.',
        "guidance": 'MIT License - See [LICENSE](LICENSE) file for details.',
    },
    'author': {
        "description": '**Komal Venkatesh Ganesan**\n\nIf you find this skill helpful for managing your Home Assistant setup, consider supporting its development:\n\n<a href="https://www.',
        "guidance": '**Komal Venkatesh Ganesan**\n\nIf you find this skill helpful for managing your Home Assistant setup, consider supporting its development:\n\n<a href="https://www.buymeacoffee.com/komalvenkag" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" height="50"></a>',
    },
    'support-discussion': {
        "description": '- **Issues**: [GitHub Issues](https://github.',
        "guidance": '- **Issues**: [GitHub Issues](https://github.com/komal-SkyNET/claude-skill-homeassistant/issues)\n- **Discussions**: [GitHub Discussions](https://github.com/komal-SkyNET/claude-skill-homeassistant/discussions)\n- **Home Assistant Community**: Tag contributions with `claude-skill`\n\n---\n\n**Made with ❤️ for the Home Assistant community**',
    },
}


@mcp.tool()
def list_homeassistant_skills() -> dict:
    """List all available homeassistant skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_homeassistant_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific homeassistant skill."""
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
    hint = get_presentation_hint('homeassistant', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@homeassistant",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'homeassistant',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
