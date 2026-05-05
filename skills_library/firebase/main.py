"""Skill: firebase."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("firebase")


_SKILLS: dict[str, dict] = {
    'installation': {
        "description": '### Option 1: Agent Skills CLI \n\nFor most popular AI-assistive tools, you can use the `skills` CLI to install Firebase agent skills:\n\n```bash\nnpx skills add firebase/skills\n```\n\n### Option 2: Gemini C',
        "guidance": '### Option 1: Agent Skills CLI \n\nFor most popular AI-assistive tools, you can use the `skills` CLI to install Firebase agent skills:\n\n```bash\nnpx skills add firebase/skills\n```\n\n### Option 2: Gemini CLI Extension\n\nThis repository is configured as a Gemini CLI extension. You can add it using the Gemini CLI:\n\n```bash\ngemini extensions install https://github.com/firebase/skills\n```\n\n### Option 3: Claude Plugin\n\n1. Add the Firebase marketplace for Claude plugins:\n\n```bash\nclaude plugin marketplace add firebase/skills\n```\n\nInstall the Claude plugin for Firebase:\n\n```bash\nclaude plugin install firebase@firebase\n```\n\nVerify the installation:\n\n```bash\nclaude plugin marketplace list\n```\n\n### Option 4: Manual Set Up\n\n1. Clone this repository:\n\n```bash\ngit clone https://github.com/firebase/skills.git\n```\n\n2. Copy the contents of the `skills` directory to the appropriate location for your AI tool. Common locations include:\n   - **Cursor**: `.cursor/rules/`\n   - **Windsurf**: `.windsurfrules/`\n   - **GitHub Copilot**: `.github/copilot-instructions.md` (or project-specific instruction files)\n\n### Option 5: Local Path via Agent Skills CLI\n\nThe `skills` CLI also supports installing skills from a local directory. If you have cloned this repository, you can add skills by pointing the CLI to your local folder:\n\n```bash\nnpx skills add /path/to/your/local/firebase-skills/skills\n```\n\nIf you make changes to the local skills repository and want to update your project with the new changes, you can update them by running:\n\n```bash\nnpx skills experimental_install\n```\n\n### Option 6: Local Development (Live Symlinking)\n\nIf you are actively contributing to or developing these skills, using `npx skills add` or copying files means you have to manually update them every time you make a change. Instead, use a symlink so that changes in your local clone are immediately reflected in your test project.\n\nFor example, to test with Cursor:\n\n```bash\nln -s /path/to/firebase-skills/skills /path/to/your/test-project/.cursor/rules\n```',
    },
    'contributing': {
        "description": '1.',
        "guidance": "1. Fork the repository\n2. Create a feature branch: `git checkout -b feature/amazing-feature`\n3. Commit changes: `git commit -m 'Add amazing feature'`\n4. Push to branch: `git push origin feature/amazing-feature`\n5. Open a Pull Request (PR)",
    },
    'license': {
        "description": 'This project is licensed under the Apache 2 License - see the [LICENSE](LICENSE) file for details.',
        "guidance": 'This project is licensed under the Apache 2 License - see the [LICENSE](LICENSE) file for details.\n\n**Made with ❤️ from Firebase for the AI community**',
    },
}


@mcp.tool()
def list_firebase_skills() -> dict:
    """List all available firebase skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_firebase_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific firebase skill."""
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
    hint = get_presentation_hint('firebase', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@firebase",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'firebase',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
