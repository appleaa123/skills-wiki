"""Skill: opc_skills."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("opc-skills")


_SKILLS: dict[str, dict] = {
    'what-are-skills': {
        "description": 'Skills are folders of instructions, scripts, and resources that AI agents load dynamically to improve performance on specialized tasks.',
        "guidance": 'Skills are folders of instructions, scripts, and resources that AI agents load dynamically to improve performance on specialized tasks. Each skill is self-contained with a `SKILL.md` file containing instructions and metadata.\n\nFor more information about the Agent Skills standard, see [agentskills.io](http://agentskills.io).',
    },
    'included-skills': {
        "description": '| | Skill | Description |\n|:---:|-------|-------------|\n| <img src=".',
        "guidance": '| | Skill | Description |\n|:---:|-------|-------------|\n| <img src="./skill-logos/seo-geo.svg" width="24"> | [seo-geo](./skills/seo-geo) | SEO & GEO optimization for AI search engines (ChatGPT, Perplexity, Google) |\n| <img src="./skill-logos/requesthunt.svg" width="24"> | [requesthunt](./skills/requesthunt) | Research user demand from Reddit, X, and GitHub |\n| <img src="./skill-logos/domain-hunter.svg" width="24"> | [domain-hunter](./skills/domain-hunter) | Find domains, compare registrar prices, and discover promo codes |\n| <img src="./skill-logos/logo-creator.svg" width="24"> | [logo-creator](./skills/logo-creator) | Create logos with AI, crop, remove background, export as SVG |\n| <img src="./skill-logos/banner-creator.svg" width="24"> | [banner-creator](./skills/banner-creator) | Create banners for GitHub, Twitter, LinkedIn, etc. |\n| <img src="./skill-logos/nanobanana.svg" width="24"> | [nanobanana](./skills/nanobanana) | Generate images using Gemini 3 Pro Image (Nano Banana Pro) |\n| <img src="./skill-logos/reddit.svg" width="24"> | [reddit](./skills/reddit) | Search and retrieve content from Reddit via the public JSON API |\n| <img src="./skill-logos/twitter.svg" width="24"> | [twitter](./skills/twitter) | Search and retrieve content from Twitter/X via twitterapi.io |\n| <img src="./skill-logos/producthunt.svg" width="24"> | [producthunt](./skills/producthunt) | Search Product Hunt posts, topics, users, and collections |\n| <img src="./skill-logos/archive.svg" width="24"> | [archive](./skills/archive) | Archive session learnings and debugging solutions with indexed markdown |',
    },
    'quick-install': {
        "description": "### Claude Code Plugin Marketplace\n\nInstall directly from Claude Code's plugin marketplace:\n\n```bash\n# Add the OPC Skills marketplace\n/plugin marketplace add ReScienceLab/opc-skills\n\n# Install specifi",
        "guidance": "### Claude Code Plugin Marketplace\n\nInstall directly from Claude Code's plugin marketplace:\n\n```bash\n# Add the OPC Skills marketplace\n/plugin marketplace add ReScienceLab/opc-skills\n\n# Install specific skills\n/plugin install requesthunt@opc-skills\n/plugin install domain-hunter@opc-skills\n/plugin install seo-geo@opc-skills\n\n# List all available skills\n/plugin marketplace list opc-skills\n```\n\n### Universal Installation (16+ AI Tools)\n\nInstall with one command - works with Claude Code, Cursor, Windsurf, Droid, and 12+ other AI tools:\n\n```bash\n# Install all skills\nnpx skills add ReScienceLab/opc-skills\n\n# Install specific skill\nnpx skills add ReScienceLab/opc-skills --skill reddit\n\n# Install to specific agent\nnpx skills add ReScienceLab/opc-skills -a droid\n```\n\nBrowse and discover skills at **[skills.sh](https://skills.sh/ReScienceLab/opc-skills)** 🎯\n\n### Skills with Dependencies\n\nSome skills require other skills to function properly:\n\n- **domain-hunter** → requires `twitter` and `reddit`\n- **logo-creator** → requires `nanobanana`\n- **banner-creator** → requires `nanobanana`\n\nInstall them together:\n\n```bash\nnpx skills add ReScienceLab/opc-skills --skill reddit --skill twitter --skill domain-hunter\n```\n\n---",
    },
    'supported-ai-tools': {
        "description": 'OPC Skills work with 16+ AI coding agents via `npx skills add`:\n\n- **Claude Code** - Desktop app for AI-assisted coding\n- **Cursor** - AI-first code editor\n- **Factory Droid** - AI software engineerin',
        "guidance": 'OPC Skills work with 16+ AI coding agents via `npx skills add`:\n\n- **Claude Code** - Desktop app for AI-assisted coding\n- **Cursor** - AI-first code editor\n- **Factory Droid** - AI software engineering agent\n- **Windsurf** - AI-powered IDE\n- **OpenCode** - Open-source AI coding assistant\n- **Codex** - AI code generation tool\n- **GitHub Copilot** - AI pair programmer\n- **Gemini CLI** - Command-line AI assistant\n- **Goose** - Terminal-based AI agent\n- **Kilo Code** - Lightweight AI coding tool\n- **Roo Code** - AI code assistant\n- **Trae** - AI development companion\n- **And more...**\n\nSee the [full compatibility list](https://github.com/vercel-labs/add-skill#available-agents) for all supported tools.\n\n---',
    },
    'documentation-resources': {
        "description": 'Explore OPC Skills through multiple channels:\n\n- **[DeepWiki](https://deepwiki.',
        "guidance": 'Explore OPC Skills through multiple channels:\n\n- **[DeepWiki](https://deepwiki.com/ReScienceLab/opc-skills)** - AI-powered interactive documentation with code exploration and Q&A\n- **[Skills Browser](https://skills.sh/ReScienceLab/opc-skills)** - Browse and discover all available skills\n- **[Official Website](https://opc.dev)** - Guides, tutorials, and usage examples\n- **[Agent Skills Standard](https://agentskills.io/)** - Learn about the skills specification\n\n### Using DeepWiki\n\nDeepWiki provides an AI assistant that can answer questions about the codebase:\n- Ask: "How does the domain-hunter skill work?"\n- Ask: "Show me the dependencies between skills"\n- Ask: "Explain the skill installation process"\n\nThe documentation auto-syncs with the repository, so it\'s always up to date.\n\n---',
    },
    'creating-new-skills': {
        "description": 'See the template in `.',
        "guidance": 'See the template in `./template/` directory for the basic structure:\n\n1. Create a folder in `skills/` with your skill name\n2. Add a `SKILL.md` file with YAML frontmatter\n3. (Optional) Add scripts, examples, or other resources\n\n**Required fields in SKILL.md:**\n```yaml\n---\nname: my-skill-name\ndescription: A clear description of what this skill does and when to use it\n---\n```\n\nFor detailed guidance, check out existing skills or visit the [Agent Skills specification](https://agentskills.io/).',
    },
    'star-history': {
        "description": '[![Star History Chart](https://api.',
        "guidance": '[![Star History Chart](https://api.star-history.com/svg?repos=ReScienceLab/opc-skills&type=Date)](https://star-history.com/#ReScienceLab/opc-skills&Date)',
    },
    'contributing': {
        "description": '1.',
        "guidance": '1. Fork this repository\n2. Create a new skill folder in `skills/`\n3. Add a `SKILL.md` with proper frontmatter\n4. Submit a pull request',
    },
    'license': {
        "description": 'Apache 2.',
        "guidance": 'Apache 2.0',
    },
}


@mcp.tool()
def list_opc_skills_skills() -> dict:
    """List all available opc_skills skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_opc_skills_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific opc_skills skill."""
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
    hint = get_presentation_hint('opc_skills', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@opc_skills",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'opc_skills',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
