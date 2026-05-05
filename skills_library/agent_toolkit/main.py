"""Skill: agent_toolkit."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("agent-toolkit")


_SKILLS: dict[str, dict] = {
    'features': {
        "description": '- **MCP server:** Direct access to your Sanity projects (content, datasets, releases, schemas) and agent rules.',
        "guidance": '- **MCP server:** Direct access to your Sanity projects (content, datasets, releases, schemas) and agent rules.\n- **Agent skills:** Comprehensive best practices skills for Sanity development, content modeling, SEO/AEO, and experimentation. Includes 21 integration/topic guides and 26 focused best-practice rules.\n- **Claude Code plugin:** MCP server, agent skills, and slash commands for [Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview) users.\n- **Cursor plugin:** MCP server, agent skills, and commands for the [Cursor Marketplace](https://cursor.com/marketplace).\n\n---',
    },
    'get-started': {
        "description": 'Choose your path based on how you want agents to work with Sanity:\n\n1.',
        "guidance": 'Choose your path based on how you want agents to work with Sanity:\n\n1. **MCP server** — Give your agent always up-to-date rules and full access to your Sanity projects. No local files to maintain. Works with Cursor, VS Code, Claude Code, Lovable, v0, and other MCP-compatible clients.\n2. **Agent skills** — Install best practices skills for Sanity, content modeling, SEO/AEO, and experimentation. Works with Cursor, Claude Code, and any [Agent Skills](https://agentskills.io)-compatible agent.\n3. **Plugin** — Install the Sanity plugin for Cursor or Claude Code. Bundles MCP server, agent skills, and commands.\n4. **Manual installation** — Copy the skill references locally for offline use. You\'ll need to update them yourself.\n\n### Option 1: Install MCP server (recommended)\n\nGive agents direct access to Sanity projects and always up-to-date agent rules via the MCP server.\n\n#### Quick install via Sanity CLI\n\nRun in terminal to detect and configure MCP for Cursor, Claude Code and VS Code automatically:\n\n```bash\nnpx sanity@latest mcp configure\n```\n\nUses your logged-in CLI user for authentication — no manual tokens or OAuth needed.\n\n#### Client-specific instructions\n\n<details>\n<summary><strong>Cursor</strong></summary>\n\nOne-click install:<br>\n[![Install MCP Server](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/en-US/install-mcp?name=Sanity&config=eyJ0eXBlIjoiaHR0cCIsInVybCI6Imh0dHBzOi8vbWNwLnNhbml0eS5pbyJ9)\n\nOr manually: Open **Command Palette** (`Cmd+Shift+P` / `Ctrl+Shift+P`) → **View: Open MCP Settings** → **+ New MCP Server** → add to `mcp.json`:\n```json\n{\n  "mcpServers": {\n    "Sanity": {\n      "type": "http",\n      "url": "https://mcp.sanity.io"\n    }\n  }\n}\n```\n</details>\n\n<details>\n<summary><strong>Claude Code</strong></summary>\n\nRun in terminal. Authenticate with OAuth on next launch:\n```bash\nclaude mcp add Sanity -t http https://mcp.sanity.io --scope user\n```\n</details>\n\n<details>\n<summary><strong>VS Code</strong></summary>\n\nOpen **Command Palette** (`Cmd+Shift+P` / `Ctrl+Shift+P`) → **MCP: Open User Configuration** → add:\n```json\n{\n  "servers": {\n    "Sanity": {\n      "type": "http",\n      "url": "https://mcp.sanity.io"\n    }\n  }\n}\n```\n</details>\n\n<details>\n<summary><strong>Lovable</strong></summary>\n\n**Settings** → **Connectors** → **Personal connectors** → **New MCP server** → Enter `Sanity` as name and `https://mcp.sanity.io` as Server URL → **Add & authorize** → Authenticate with OAuth.\n</details>\n\n<details>\n<summary><strong>v0</strong></summary>\n\nIn the prompt input field, click **Prompt Tools** → **MCPs** → **Add New** → Select **Sanity** → **Authorize** → Authenticate with OAuth.\n</details>\n\n<details>\n<summary><strong>Replit</strong></summary>\n\nGo to [Integrations Page](https://replit.com/integrations) → scroll to **MCP Servers for Replit Agent** → **Add MCP server** → Enter `Sanity` as name and `https://mcp.sanity.io` as Server URL → **Test & Save** → Authenticate with OAuth.\n</details>\n\n<details>\n<summary><strong>OpenCode</strong></summary>\n\nAdd to your `opencode.json`:\n```json\n{\n  "$schema": "https://opencode.ai/config.json",\n  "mcp": {\n    "sanity": {\n      "type": "remote",\n      "url": "https://mcp.sanity.io",\n      "oauth": {}\n    }\n  }\n}\n```\nThen run: `opencode mcp auth sanity`\n</details>\n\n<details>\n<summary><strong>Other clients</strong></summary>\n\nFor any MCP-compatible client, add `https://mcp.sanity.io` as the server URL.\n\nIf your client doesn\'t support remote MCP servers, use a proxy like `mcp-remote`:\n```json\n{\n  "mcpServers": {\n    "Sanity": {\n      "command": "npx",\n      "args": ["mcp-remote", "https://mcp.sanity.io", "--transport", "http-only"]\n    }\n  }\n}\n```\n</details>\n\n<br />\n\nSee the [Sanity MCP docs](https://www.sanity.io/docs/compute-and-ai/mcp-server) for authorization options and troubleshooting.\n\n### Option 2: Install Agent Skills\n\nInstall best practices skills that work with any [Agent Skills](https://agentskills.io)-compatible agent.\n\n```bash\nnpx skills add sanity-io/agent-toolkit\n```\n\nSee [Option 3](#option-3-install-plugin) for plugin installation.\n\n### Option 3: Install plugin\n\nInstall the Sanity plugin to get MCP server, agent skills, and commands.\n\n#### Claude Code\n\n1. Add the Sanity marketplace:\n\n```\n/plugin marketplace add sanity-io/agent-toolkit\n```\n\n2. Install the plugin:\n\n```\n/plugin install sanity-plugin@sanity-agent-toolkit\n```\n\n3. Verify installation: Ask Claude Code: "which skills do you have access to?"\n\nYou should see the Sanity skills listed.\n\n4. Start using: Use natural language and skills activate automatically:\n\n> Help me create a blog post schema in Sanity\n\n> Review my GROQ query and Next.js Visual Editing setup\n\nOr run `/sanity` to explore all capabilities.\n\n#### Cursor\n\nIn Cursor chat, run:\n\n```\n/add-plugin sanity\n```\n\n### Option 4: Manual installation\n\nInstall the skill references locally to teach your editor Sanity best practices:\n\n1. Copy `skills/sanity-best-practices/` to your project.\n2. (Recommended) Copy `AGENTS.md` to your project root to act as a knowledge router.\n\n---',
    },
    'capabilities': {
        "description": '### MCP tools\n\nWith MCP connected, your AI can use tools like:\n- `query_documents` — run GROQ queries directly\n- `create_documents_from_json` / `create_documents_from_markdown` — create draft document',
        "guidance": '### MCP tools\n\nWith MCP connected, your AI can use tools like:\n- `query_documents` — run GROQ queries directly\n- `create_documents_from_json` / `create_documents_from_markdown` — create draft documents\n- `patch_document_from_json` / `patch_document_from_markdown` — surgical edits to existing documents\n- `publish_documents` / `unpublish_documents` — manage document lifecycle\n- `deploy_schema` / `get_schema` — deploy and inspect schemas\n- `create_version` — create version documents for releases\n- `generate_image` / `transform_image` — AI image generation and editing\n- `search_docs` / `read_docs` — search and read Sanity documentation\n- `list_sanity_rules` / `get_sanity_rules` — load agent rules on demand\n\nSee the [full list of available tools](https://www.sanity.io/docs/compute-and-ai/mcp-server#k4ae680bb2e88).\n\n### Agent skills\n\nBest practices skills that agents like Claude Code, Cursor, GitHub Copilot, etc. can discover and use automatically. Skills follow the [Agent Skills](https://agentskills.io) format. See [Option 2](#option-2-install-agent-skills) for installation.\n\n| Skill | Description |\n| :--- | :--- |\n| **sanity-best-practices** | GROQ performance, schema design, Visual Editing, images, Portable Text, Studio, TypeGen, localization, migrations, and framework integration guides |\n| **content-modeling-best-practices** | Structured content principles: separation of concerns, references vs embedding, content reuse |\n| **seo-aeo-best-practices** | SEO/AEO with EEAT principles, structured data (JSON-LD), technical SEO patterns |\n| **content-experimentation-best-practices** | A/B testing methodology, statistical foundations, experiment design |\n\n### Getting started flow\n\nThe onboarding guide follows three phases:\n\n1. **Studio & Schema** — Set up Sanity Studio and define your content model\n2. **Content** — Import existing content or generate placeholder content via MCP\n3. **Frontend** — Integrate with your application (framework-specific)\n\nJust say: "Get started with Sanity" to begin.\n\n### Slash commands (Claude Code)\n\n| Command | What it does |\n| :--- | :--- |\n| `/sanity` | List available skills and help topics |\n| `/review` | Review code for Sanity best practices |\n| `/typegen` | Run TypeGen and troubleshoot issues |\n| `/deploy-schema` | Deploy schema with verification |\n\n---',
    },
    'repository-structure': {
        "description": "> **Note:** The reference files in `skills/sanity-best-practices/references/` are the canonical content for the Sanity MCP server's `list_sanity_rules` / `get_sanity_rules` tools.",
        "guidance": "> **Note:** The reference files in `skills/sanity-best-practices/references/` are the canonical content for the Sanity MCP server's `list_sanity_rules` / `get_sanity_rules` tools. Each file must have valid `name` and `description` frontmatter — rule names are derived from filenames (e.g., `nextjs.md` → `nextjs`).\n\n```text\nsanity-io/agent-toolkit/\n├── AGENTS.md                      # Knowledge router & agent behavior\n├── README.md                      # This file\n├── .claude-plugin/                # Claude Code plugin configuration\n│   └── marketplace.json           # Plugin metadata and marketplace config\n├── .cursor-plugin/                # Cursor plugin configuration\n│   ├── marketplace.json           # Cursor marketplace metadata\n│   └── plugin.json                # Per-plugin manifest\n├── .mcp.json                      # MCP server configuration\n├── assets/                        # Plugin branding\n│   └── logo.svg                   # Sanity logo for marketplace display\n├── commands/                      # Agent commands\n│   ├── sanity.md                  # /sanity help\n│   ├── review.md                  # /review\n│   ├── typegen.md                 # /typegen\n│   └── deploy-schema.md           # /deploy-schema\n├── scripts/                       # Validation and CI scripts\n│   └── validate-cursor-plugin.mjs # Cursor plugin validator\n└── skills/                        # Agent skills (agentskills.io format)\n    ├── sanity-best-practices/     # Comprehensive Sanity skill\n    │   ├── SKILL.md               # Skill definition and quick reference\n    │   └── references/            # Canonical content (22 guides)\n    │       ├── get-started.md     # Onboarding guide\n    │       ├── nextjs.md          # Next.js integration\n    │       ├── groq.md            # GROQ patterns & performance\n    │       ├── schema.md          # Schema design & validation\n    │       └── ...                # See SKILL.md for full index\n    ├── content-modeling-best-practices/      # Modeling guidance + topic references\n    ├── seo-aeo-best-practices/               # SEO/AEO guidance + topic references\n    └── content-experimentation-best-practices/ # Experiment design + stats references\n```\n\nAll skills use `references/` for detailed content loaded on demand. The `sanity-best-practices` references are also the canonical source for the MCP server's Sanity rules.\n\n---",
    },
    'resources': {
        "description": '- [Create Sanity account](https://www.',
        "guidance": '- [Create Sanity account](https://www.sanity.io/get-started)\n- [Sanity documentation](https://www.sanity.io/docs)\n- [GROQ language reference](https://www.sanity.io/docs/groq)\n- [Visual Editing guide](https://www.sanity.io/docs/visual-editing)\n- [Sanity TypeGen](https://www.sanity.io/docs/sanity-typegen)\n- [MCP server docs](https://www.sanity.io/docs/compute-and-ai/mcp-server)\n- [Blueprints Infrastructure as Code](https://www.sanity.io/docs/compute-and-ai/blueprints)\n\n---',
    },
    'contributing': {
        "description": 'Found a better pattern? Missing a framework or best practice? Read the [contributing guide](CONTRIBUTING.',
        "guidance": 'Found a better pattern? Missing a framework or best practice? Read the [contributing guide](CONTRIBUTING.md) for how skills work and what makes a good contribution, then:\n\n1. Fork the repo.\n2. Install dependencies with `npm install`.\n3. Make your changes in `skills/<skill-name>/`.\n4. Run `npm run validate:all` to check skill and plugin validity.\n5. Submit a PR.\n\n---',
    },
    'support': {
        "description": '- [Sanity Community (Discord)](https://www.',
        "guidance": '- [Sanity Community (Discord)](https://www.sanity.io/community/join)\n- [GitHub issues](https://github.com/sanity-io/agent-toolkit/issues)\n\n---\n\n**License:** MIT',
    },
}


@mcp.tool()
def list_agent_toolkit_skills() -> dict:
    """List all available agent_toolkit skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_agent_toolkit_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific agent_toolkit skill."""
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
    hint = get_presentation_hint('agent_toolkit', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@agent_toolkit",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'agent_toolkit',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
