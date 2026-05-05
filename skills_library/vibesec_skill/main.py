"""Skill: vibesec_skill."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("vibesec-skill")


_SKILLS: dict[str, dict] = {
    'introduction': {
        "description": 'Vibe coding is fun until your app ends up on social media for all the wrong reasons.',
        "guidance": "Vibe coding is fun until your app ends up on social media for all the wrong reasons.\n\nWe have all seen the posts/memes:\n\n* API keys hardcoded in JavaScript bundles\n* IDOR vulnerabilities allowing user data dumps\n* No authentication for sensitive pages\n* Weak passwords for admin panels\n\nSecurity gaps aren't obvious until someone exploits them. Without the right guidance, AI will confidently ship vulnerable patterns alongside your features.\n\nVibeSec is an AI Skill that acts as a security-first co-pilot. It teaches your selected model to approach your code from a bug hunter's perspective, catching vulnerabilities before they ship.",
    },
    'table-of-contents': {
        "description": '- [VibeSec-Skill](#VibeSec-Skill)\n  - [📥 Installation](#-installation)\n  - [🛡️ Covered Vulnerabilities](#️-covered-vulnerabilities)\n  - [🚀 Quick Start](#-quick-start)\n  - [🤝 Contribution](#-contributi',
        "guidance": '- [VibeSec-Skill](#VibeSec-Skill)\n  - [📥 Installation](#-installation)\n  - [🛡️ Covered Vulnerabilities](#️-covered-vulnerabilities)\n  - [🚀 Quick Start](#-quick-start)\n  - [🤝 Contribution](#-contribution)\n  - [📬 Contact](#-contact)\n\n\n>[!Tip]\n>This skill already covers 60-70% of the common vulnerabilities. However, if you need a more robust version with more vulnerability coverage, please visit [vibesec.sh](https://vibesec.sh/)',
    },
    'installation': {
        "description": '- <details><summary>Claude Code</summary>\n\n  * Clone this repository: `git clone https://github.',
        "guidance": '- <details><summary>Claude Code</summary>\n\n  * Clone this repository: `git clone https://github.com/BehiSecc/VibeSec-Skill`\n\n  * Add it to `~/.claude/skills` (global) or `.claude/skills` in your project directory (project-only).\n</details>\n\n- <details><summary>Cursor</summary>\n\n  * Clone this repository: `git clone https://github.com/BehiSecc/VibeSec-Skill`\n\n  * Add it to `~/.cursor/skills` (global) or `.cursor/skills` in your project directory (project-only).\n</details>\n\n- <details><summary>Codex</summary>\n\n  * Clone this repository: `git clone https://github.com/BehiSecc/VibeSec-Skill`\n\n  * Add it to `~/.agents/skills` (global) or `.agents/skills` in your project directory (project-only).\n\n</details>\n\n- <details><summary>Github Copilot</summary>\n\n  * Clone this repository: `git clone https://github.com/BehiSecc/VibeSec-Skill`\n\n  * Add it to `~/.copilot/skills` (global) or `.github/skills` in your project directory (project-only).\n\n</details>\n\n- <details><summary>Antigravity</summary>\n\n  * Clone this repository: `git clone https://github.com/BehiSecc/VibeSec-Skill`\n\n  * Add it to `~/.gemini/antigravity/skills/` (global) or `.agent/skills/` in your project directory (project-only).\n\n</details>',
    },
    'covered-vulnerabilities': {
        "description": 'VibeSec provides comprehensive protection against:\n\n| Category | Covered Vulnerabilities |\n|----------|-----------------|\n| **Access Control** | IDOR, Privilege Escalation, Horizontal/Vertical Access,',
        "guidance": 'VibeSec provides comprehensive protection against:\n\n| Category | Covered Vulnerabilities |\n|----------|-----------------|\n| **Access Control** | IDOR, Privilege Escalation, Horizontal/Vertical Access, Mass Assignment, Token Revocation |\n| **Client-Side** | XSS (Stored, Reflected, DOM), CSRF, Secret Key Exposure, Open Redirect |\n| **Server-Side** | SSRF, SQL Injection, XXE, Path Traversal, Insecure File Upload |\n| **Authentication** | Weak Passwords, Session Management, Account Lifecycle, JWT Security |\n| **API Security** | Mass Assignment, GraphQL Security |\n\n\n### Deep Coverage Includes:\n\n- ✅ **Bypass techniques** - Not just "sanitize input" but specific bypasses attackers use\n- ✅ **Edge cases** - URL fragments, DNS rebinding, polyglot files, Unicode tricks\n- ✅ **Framework-aware** - Patterns for React, Vue, Node.js, Python, Java, .NET\n- ✅ **Cloud-aware** - Metadata endpoint protection for AWS, GCP, Azure\n- ✅ **Checklists** - Actionable verification steps for each vulnerability class',
    },
    'quick-start': {
        "description": '```markdown\n# Add the skill to your project dir:\n\n"I\'m building a [web app description].',
        "guidance": '```markdown\n# Add the skill to your project dir:\n\n"I\'m building a [web app description]. Please follow secure coding practices."\n\n# Claude/Codex/etc will now automatically:\n# - Implement proper access controls  \n# - Add security headers\n# - Validate and sanitize all inputs\n# - Flag potential security issues\n```',
    },
    'contribution': {
        "description": 'If you have suggestions, improvements, or new resources to add:\n\n1.',
        "guidance": 'If you have suggestions, improvements, or new resources to add:\n\n1. Fork this repo\n2. Make your changes\n3. Submit a Pull Request\n\nYou can also open an **Issue** 🐛 if you spot something that needs fixing.',
    },
    'contact': {
        "description": 'If you want to contact me, you can reach me on [X](https://x.',
        "guidance": 'If you want to contact me, you can reach me on [X](https://x.com/Behi_Sec).',
    },
}


@mcp.tool()
def list_vibesec_skill_skills() -> dict:
    """List all available vibesec_skill skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_vibesec_skill_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific vibesec_skill skill."""
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
    hint = get_presentation_hint('vibesec_skill', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@vibesec_skill",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'vibesec_skill',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
