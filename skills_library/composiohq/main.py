"""Skill: composiohq."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("composiohq")


_SKILLS: dict[str, dict] = {
    'quick-start': {
        "description": 'Add Composio skills to your AI assistant:\n\n```bash\nnpx skills add composiohq/skills\n```\n\nThis command installs the Composio agent skills, giving your AI assistant access to:\n- **Tool Router best pract',
        "guidance": 'Add Composio skills to your AI assistant:\n\n```bash\nnpx skills add composiohq/skills\n```\n\nThis command installs the Composio agent skills, giving your AI assistant access to:\n- **Tool Router best practices** - Session management, authentication, and framework integration\n- **Triggers & Events** - Real-time webhooks and event handling\n- **Production patterns** - Security, error handling, and deployment guides\n\nYour AI assistant can now reference these skills when helping you build with Composio!',
    },
    'overview': {
        "description": 'This skills repository provides comprehensive guides and best practices for building AI agents with Composio, organized as markdown files that AI assistants can easily reference.',
        "guidance": 'This skills repository provides comprehensive guides and best practices for building AI agents with Composio, organized as markdown files that AI assistants can easily reference.',
    },
    'structure': {
        "description": '```\nskills/\n└── composio/\n    ├── SKILL.',
        "guidance": '```\nskills/\n└── composio/\n    ├── SKILL.md           # Main skill overview with rule references\n    ├── AGENTS.md          # Consolidated single-file version (auto-generated)\n    └── rules/             # Individual rule files\n        ├── tr-*.md        # Tool Router rules\n        └── triggers-*.md  # Trigger rules\n```',
    },
    'available-skills': {
        "description": '### 1.',
        "guidance": '### 1. Tool Router (Building Agents)\n- User ID best practices for security\n- Creating and managing sessions\n- Session lifecycle patterns\n- Native tools vs MCP integration\n- Framework integration (Vercel, OpenAI Agents, LangChain, Claude, CrewAI)\n\n### 2. Authentication\n- Auto authentication in chat\n- Manual authorization flows\n- Connection management\n\n### 3. Toolkits & Connection Status\n- Querying toolkit availability\n- Building connection UIs\n\n### 4. Advanced Features (Triggers & Events)\n- Creating triggers for real-time events\n- Subscribing to events (development only)\n- Webhook verification (production recommended)\n- Managing trigger lifecycle',
    },
    'usage': {
        "description": '### For AI Assistants\n\nRead either:\n- **SKILL.',
        "guidance": '### For AI Assistants\n\nRead either:\n- **SKILL.md** - Main file with links to individual rules (faster to navigate)\n- **AGENTS.md** - Single consolidated file with all content (easier to consume)\n\n### For Developers\n\n#### Build AGENTS.md\n\nAutomatically generate the consolidated AGENTS.md file from all rule files:\n\n```bash\nnpm run build:agents\n```\n\nThis script:\n- Reads SKILL.md for structure\n- Extracts all rule references\n- Combines individual rule files\n- Generates table of contents\n- Outputs AGENTS.md with proper formatting\n\n#### Watch Mode\n\nAuto-rebuild AGENTS.md when any file changes:\n\n```bash\nnpm run watch:agents\n```\n\nThis watches:\n- `SKILL.md` for structure changes\n- `rules/*.md` for content changes\n- Auto-rebuilds on any modification',
    },
    'contributing': {
        "description": '### Adding a New Rule\n\n1.',
        "guidance": '### Adding a New Rule\n\n1. Create a new markdown file in `skills/composio/rules/`\n2. Use the naming convention:\n   - `tr-*.md` for Tool Router rules\n   - `triggers-*.md` for Trigger rules\n3. Include frontmatter:\n\n```markdown\n---\ntitle: Your Rule Title\nimpact: CRITICAL|HIGH|MEDIUM|LOW\ndescription: Brief description of what this rule covers\ntags: [tool-router, triggers, etc]\n---\n\n# Your Rule Title\n\nContent with ❌ Incorrect and ✅ Correct examples...\n```\n\n4. Add reference to `SKILL.md` in the appropriate section\n5. Run `npm run build:agents` to regenerate AGENTS.md\n6. Commit all changes (rule file, SKILL.md, and AGENTS.md)\n\n### Rule Format\n\nEach rule should include:\n- **Frontmatter** with metadata\n- **❌ Incorrect examples** showing what not to do\n- **✅ Correct examples** showing best practices\n- **Explanations** of why each approach is better\n- **Code examples** in both TypeScript and Python (when applicable)\n- **References** to official documentation',
    },
    'build-scripts': {
        "description": 'The repository includes two scripts in `scripts/`:\n\n### build-agents.',
        "guidance": 'The repository includes two scripts in `scripts/`:\n\n### build-agents.cjs\n\nGenerates the consolidated AGENTS.md file:\n- Parses SKILL.md for structure\n- Reads all rule files\n- Combines content with proper formatting\n- Generates table of contents\n- Adds impact badges and descriptions\n\n### watch-agents.cjs\n\nWatches for file changes and auto-rebuilds:\n- Monitors SKILL.md and rules/ directory\n- Triggers rebuild on any .md file change\n- Shows real-time build status',
    },
    'file-statistics': {
        "description": 'Current repository stats:\n- **14+ rules** covering Tool Router and Triggers\n- **150+ KB** of consolidated documentation\n- **Both TypeScript and Python** examples throughout\n- **Production-ready** patt',
        "guidance": 'Current repository stats:\n- **14+ rules** covering Tool Router and Triggers\n- **150+ KB** of consolidated documentation\n- **Both TypeScript and Python** examples throughout\n- **Production-ready** patterns and best practices',
    },
    'key-features': {
        "description": '### Tool Router Coverage\n- Session management and lifecycle\n- User isolation patterns\n- Native tools vs MCP comparison\n- Framework integration guides\n- Connection management\n- Authentication flows\n\n##',
        "guidance": '### Tool Router Coverage\n- Session management and lifecycle\n- User isolation patterns\n- Native tools vs MCP comparison\n- Framework integration guides\n- Connection management\n- Authentication flows\n\n### Triggers Coverage\n- Creating trigger instances\n- Real-time event subscription\n- Webhook verification and security\n- Trigger lifecycle management\n- Production deployment patterns',
    },
    'license': {
        "description": 'MIT.',
        "guidance": 'MIT',
    },
    'links': {
        "description": '- [Composio Documentation](https://docs.',
        "guidance": '- [Composio Documentation](https://docs.composio.dev)\n- [Tool Router API](https://docs.composio.dev/sdk/typescript/api/tool-router)\n- [Triggers API](https://docs.composio.dev/sdk/typescript/api/triggers)\n- [GitHub Repository](https://github.com/composiohq/skills)',
    },
}


@mcp.tool()
def list_composiohq_skills() -> dict:
    """List all available composiohq skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_composiohq_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific composiohq skill."""
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
    hint = get_presentation_hint('composiohq', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@composiohq",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'composiohq',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
