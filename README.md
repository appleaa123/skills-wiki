# Skills Wiki — Local AI Skills Manager

An open-source, fully local AI skills manager. Connect 128+ community-built skill packs to Claude, ChatGPT, or Gemini — all running on your own machine, no accounts, subscriptions, or cloud services required.

Browse skills, enable what you need, copy your local connection URL, and start working smarter in minutes.

---

## Table of Contents

1. [How It Works](#1-how-it-works)
2. [Tech Stack & Project Structure](#2-tech-stack--project-structure)
3. [Getting Started](#3-getting-started)
4. [Dashboard Walkthrough](#4-dashboard-walkthrough)
5. [Connecting Your AI Assistant](#5-connecting-your-ai-assistant)
6. [Using the Active Skills Panel](#6-using-the-active-skills-panel)
7. [Adding New Skills](#7-adding-new-skills)
8. [Per-Skill Configuration](#8-per-skill-configuration)
9. [Connecting External Services](#9-connecting-external-services)
10. [Environment Variables](#10-environment-variables)
11. [Skill Library](#11-skill-library)
12. [License](#12-license)

---

## 1. How It Works

Skills Wiki runs two processes on your machine:

```
Your AI Assistant (Claude / ChatGPT / Gemini)
             │
             │  MCP protocol or OpenAPI
             ▼
  Python MCP Server — http://localhost:8000
  (FastMCP, mounts all enabled skills)
             │
             │  reads config
             ▼
  data/local_config.json
  (enabled skills, connections, per-skill settings)
             ▲
             │  manages via UI
  Next.js Dashboard — http://localhost:3000
```

- **The Python server** (`main.py`) loads every skill in `skills_library/` at startup and exposes them over the MCP protocol at `localhost:8000/mcp` and as an OpenAPI schema at `localhost:8000/openapi.json`.
- **The dashboard** (`dashboard/`) is a Next.js app for browsing skills, toggling what's active, copying connection URLs, running skill tools, and managing connected services.
- **`data/local_config.json`** is the single source of truth — no database, no cloud.

Everything runs locally. Your data never leaves your machine.

---

## 2. Tech Stack & Project Structure

### Tech Stack

#### Frontend Dashboard (Next.js)
- **Next.js 15** — React 19, App Router, server components
- **TypeScript 5** — strict mode enabled
- **Tailwind CSS 3** — utility-first styling with custom v4 design tokens
- **shadcn/ui** — accessible UI components
- **JetBrains Mono** — monospace font for the terminal-style UI

#### Backend MCP Server (Python)
- **FastMCP** — Model Context Protocol SDK; each skill is a mounted namespace
- **Python 3.10+** — async throughout
- **python-dotenv** — environment variable management

#### Storage
- **`data/local_config.json`** — all state in one JSON file: enabled skills, connections, per-skill configs, and auto-generated credentials

---

### Project Structure

```
skills_wiki_opensource/
├── main.py                        # FastMCP server entry point
├── requirements.txt               # Python dependencies
├── .env.example                   # Environment variable template
├── package.json                   # Root scripts (setup, dev, etc.)
│
├── data/
│   └── local_config.json          # All runtime state (auto-created on first run)
│
├── core/                          # Python server utilities
│   ├── config.py                  # Reads enabled_skills from local_config.json
│   ├── db.py                      # JSON read/write helpers
│   ├── skill_config.py            # Per-skill presentation hints
│   ├── skill_runtime.py           # Skill execution helpers
│   └── credentials.py             # Service credential resolution
│
├── skills_library/                # 128+ MCP skill packs
│   ├── marketing_skills/          # Example skill
│   │   ├── main.py                #   FastMCP tool definitions
│   │   ├── skill_meta.json        #   Metadata: displayName, description, theme
│   │   └── __init__.py
│   └── ... (128+ skill folders)
│
├── scripts/
│   └── add_skill.py               # Install a skill from a GitHub repo
│
└── dashboard/                     # Next.js frontend
    ├── app/
    │   ├── dashboard/             # Main control center
    │   ├── marketplace/           # Browse & enable skills
    │   ├── connections/           # Manage third-party service credentials
    │   ├── config/                # Per-skill customization
    │   ├── setup/                 # Platform connection guides
    │   └── api/                   # Next.js API routes
    │       ├── skills/            # PATCH — update enabled skills
    │       ├── skill-tools/       # GET  — list tools for a skill
    │       ├── tool-run/          # POST — run a skill tool
    │       ├── connections/       # GET/POST/DELETE — manage services
    │       └── config/            # GET/POST/DELETE — per-skill settings
    ├── components/
    │   ├── DashboardClient.tsx    # Active skills panel + credentials panel
    │   ├── CredentialsPopup.tsx   # Copyable CLIENT_ID, API_KEY, URLs
    │   └── ...
    └── lib/
        ├── skills.ts              # Skill registry (500+ skills, 40+ themes)
        ├── local-db.ts            # JSON config read/write
        └── utils.ts               # URL helpers, key masking
```

---

## 3. Getting Started

### Prerequisites

- Python 3.10 or higher
- Node.js 18 or higher
- A Gemini API key *(optional — only needed to install new skills from GitHub)*

### Install & Run

```bash
# 1. Clone the repo
git clone https://github.com/your-org/skills-wiki.git
cd skills-wiki

# 2. Copy the environment file (add your Gemini key if you plan to add skills)
cp .env.example .env

# 3. Install all dependencies (Python + Node)
npm run setup

# 4. Start both servers
npm run dev
```

Open **http://localhost:3000** in your browser.

The MCP server starts at **http://localhost:8000**. Your credentials and connection URLs are generated automatically on first launch and shown on the dashboard.

### What `npm run dev` starts

| Process | URL | Purpose |
|---------|-----|---------|
| Python FastMCP server | http://localhost:8000 | Serves skills over MCP and OpenAPI |
| Next.js dashboard | http://localhost:3000 | Management UI |

Both processes run concurrently. Stop them with `Ctrl+C`.

---

## 4. Dashboard Walkthrough

Navigate to **http://localhost:3000/dashboard** after starting the app.

### Command Line Strip

At the top of the page, a status bar shows:
```
$ skills-wiki status --verbose          ● gateway: live    ● plan: local
```

### Plan Strip

```
plan = "local"   // running fully local — no cloud required
```

### Two-Column Grid

The main section splits into two panels side by side:

#### Left — `active_skills[]`

Lists all your currently enabled skills. Each skill shows as a card with its name and function count.

- **Click a card** → expands to show all tools/functions inside that skill with checkboxes
- **Check tools** → select the ones you want to run
- **`▶ run`** → executes selected tools and displays the output as formatted markdown
- **`copy`** → copies the markdown output to clipboard so you can paste it into any AI chat

This is the **core workflow**: expand a skill, select a function, run it, copy the result, paste it into Claude or ChatGPT to give the AI detailed context for that topic.

- **`--edit` button** → switches to edit mode with toggle switches; enable or disable individual skills
- **`--save`** → persists changes to `data/local_config.json`
- **`+ install more from ./marketplace`** → opens the marketplace to add more skills

#### Right — `gateway_credentials`

Shows all the information you need to connect your AI assistant:

| Field | Value |
|-------|-------|
| `CLIENT_ID` | Auto-generated UUID (stored in `local_config.json`) |
| `API_KEY` | Auto-generated bearer token — masked by default, click `[show]` to reveal |
| `CLAUDE_URL` | `http://localhost:8000/mcp` — use this for Claude Desktop and Claude.ai |
| `CHATGPT_URL` | `http://localhost:8000/openapi.json` — use this for ChatGPT Custom GPTs |
| `GEMINI_URL` | `http://localhost:8000/mcp` — use this for Gemini |

Every field has a copy button. Click `cat ./setup_guide →` for step-by-step platform instructions.

### Danger Zone

The `rm -rf ./connection` button clears all active skills and connections from your local config. This is irreversible.

---

## 5. Connecting Your AI Assistant

Navigate to **http://localhost:3000/setup** for per-platform guides. A summary:

### Claude Desktop

Open `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) and add:

```json
{
  "mcpServers": {
    "skills-wiki": {
      "type": "http",
      "url": "http://localhost:8000/mcp"
    }
  }
}
```

Restart Claude Desktop. Your enabled skills appear as tools.

> **Note:** Claude Desktop must be able to reach `localhost:8000`. Ensure the Python server is running before opening Claude Desktop.

### Claude.ai (Remote MCP)

Claude.ai requires a publicly accessible MCP URL. For local use, expose your server with a tunnel tool:

```bash
# Example using ngrok
ngrok http 8000
```

Then use the HTTPS URL ngrok provides in Claude.ai → Settings → Connectors → Add Custom Connector.

### ChatGPT Custom GPT

1. Go to `chatgpt.com` → Explore GPTs → Create → Configure → Actions → **Add action**
2. Import from URL: `http://localhost:8000/openapi.json` *(or your ngrok URL for remote access)*
3. Set Authentication → API Key → paste the `API_KEY` value from the dashboard
4. Save the Custom GPT

### Gemini

Gemini supports MCP via the same URL as Claude: `http://localhost:8000/mcp`.

---

## 6. Using the Active Skills Panel

This panel is the primary way to interact with skills before connecting them to an AI assistant. It lets you preview what a skill does, get its guidance text, and copy it to paste directly into any AI chat — no formal MCP connection needed.

### Step-by-step flow

1. **Go to the dashboard** → `http://localhost:3000/dashboard`
2. **Expand a skill card** — click the `▶` arrow next to any skill name
3. **Wait for tools to load** — the panel fetches all available functions from `main.py` (shows `// loading tools…` briefly)
4. **Check one or more tools** — each checkbox represents a skill function (e.g., `cold-email`, `product-marketing-context`)
5. **Click `▶ run (N selected)`** — the panel runs the selected tools and displays formatted markdown output
6. **Click `copy`** — the button changes to `✓ tools are copied`
7. **Paste into your AI chat** — open Claude, ChatGPT, or Gemini and paste. The AI now has the full skill context to follow

### What does "run" actually do?

When you run a tool:
1. The dashboard calls `POST /api/tool-run` with the skill name and selected tool
2. It first tries to call the Python MCP server at `localhost:8000/mcp` using JSON-RPC
3. If the server isn't reachable, it falls back to reading the guidance text directly from `skills_library/{skill}/main.py`
4. The result — typically detailed markdown with instructions, frameworks, or structured guidance — appears in the panel

This means the run feature works even when the Python server isn't running, as long as the skill has guidance text embedded in its `main.py`.

---

## 7. Adding New Skills

### From the UI

Go to **http://localhost:3000/config**, then **Link a Skill from GitHub**. Paste any public GitHub repo URL that contains FastMCP skill definitions. The skill is installed to `skills_library/` and activated immediately.

Requires `GEMINI_API_KEY` in your `.env` for AI-assisted skill generation.

### From the command line

```bash
# Add a skill from a public GitHub repo
python3 scripts/add_skill.py --url https://github.com/org/repo --name my_skill

# Force the entire repo to be treated as one skill (no auto-split)
python3 scripts/add_skill.py --url https://github.com/org/repo --name my_skill --no-split

# Add only a specific subdirectory
python3 scripts/add_skill.py \
  --url https://github.com/org/repo \
  --name my_skill \
  --subdir "skills/marketing"

# Add from a local file or folder
python3 scripts/add_skill.py --file ~/path/to/tools.py --name my_skill
python3 scripts/add_skill.py --file ~/path/to/skill-folder/ --name my_skill
```

After adding a skill, enable it from the dashboard marketplace. Then restart the Python server so it picks up the new skill:

```bash
# Stop the running server (Ctrl+C), then restart
npm run dev
```

### Skill format

Each skill in `skills_library/` is a folder with at minimum:
- `main.py` — defines a `FastMCP` instance named `mcp` with tool functions
- `skill_meta.json` — metadata: `display_name`, `description`, `theme`, `source_repo`
- `__init__.py` — empty file (required for Python module loading)

Example `skill_meta.json`:
```json
{
  "display_name": "Marketing Skills",
  "description": "Conversion, content, SEO, and growth skills.",
  "source_repo": "https://github.com/coreyhaines31/marketingskills",
  "theme": "marketing"
}
```

Example `main.py` structure:
```python
from fastmcp import FastMCP

mcp = FastMCP("my-skill")

_SKILLS = {
  "my-tool": {
    "description": "Does something useful.",
    "guidance": """# My Tool\n\nDetailed instructions here...""",
  }
}

@mcp.tool()
def get_my_skill(skill_name: str) -> str:
    """Returns guidance for the requested skill."""
    skill = _SKILLS.get(skill_name)
    if not skill:
        return f"Unknown skill: {skill_name}"
    return skill["guidance"]
```

---

## 8. Per-Skill Configuration

Go to **http://localhost:3000/config** to customize how each skill behaves.

For each installed skill you can set:

| Setting | Options |
|---------|---------|
| **Tone** | Formal, Casual, Technical |
| **Format** | Prose, Bullet points, Table |
| **Response Length** | Brief, Standard, Detailed |
| **Language** | Any (e.g., "Spanish", "French") |
| **Custom Instructions** | Free-text override appended to every response |

Settings are stored in `data/local_config.json` under `skill_configs`.

---

## 9. Connecting External Services

Go to **http://localhost:3000/connections** to add credentials for third-party services your skills need (GitHub tokens, Notion API keys, custom HTTP endpoints, etc.).

Credentials are stored in plaintext in `data/local_config.json`. Treat this file like a `.env` file — do not commit it to version control.

Skills that need external services read credentials from this store at runtime via `core/credentials.py`.

---

## 10. Environment Variables

Copy `.env.example` to `.env` and fill in what you need:

```bash
cp .env.example .env
```

| Variable | Required | Purpose |
|----------|----------|---------|
| `GEMINI_API_KEY` | Optional | AI-assisted skill generation when adding skills from GitHub |
| `NEXT_PUBLIC_GATEWAY_BASE_URL` | Optional | Override the MCP server URL (default: `http://localhost:8000`) |

The dashboard reads `NEXT_PUBLIC_GATEWAY_BASE_URL` to construct the `CLAUDE_URL`, `CHATGPT_URL`, and `GEMINI_URL` values shown in the credentials panel. Set this if you expose your server over a tunnel or run the server on a non-default port.

---

## 11. Skill Library

All 128 skills are included out of the box. Each folder in `skills_library/` is one skill pack.

| Skill | Source |
|-------|--------|
| activity_log | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) |
| addy_coding | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) |
| agency_agents | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) |
| agent_scan | [snyk/agent-scan](https://github.com/snyk/agent-scan) |
| agent_toolkit | [sanity-io/agent-toolkit](https://github.com/sanity-io/agent-toolkit) |
| ai_coding_skills | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) |
| algorithmic_art | [anthropics/skills](https://github.com/anthropics/skills) |
| amazon_skills | [nexscope-ai/Amazon-Skills](https://github.com/nexscope-ai/Amazon-Skills) |
| anthropic_cybersecurity_skills | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) |
| anthropics_official | [anthropics/skills](https://github.com/anthropics/skills) |
| app_preflight | [truongduy2611/app-store-preflight-skills](https://github.com/truongduy2611/app-store-preflight-skills) |
| app_store_cli | [rorkai/app-store-connect-cli-skills](https://github.com/rorkai/app-store-connect-cli-skills) |
| apple_bridge | [more-io/claude-apple-bridges](https://github.com/more-io/claude-apple-bridges) |
| aso_skills | [Eronred/aso-skills](https://github.com/Eronred/aso-skills) |
| auto_claude_code_research_in_sleep | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) |
| awesome_claude_skills | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) |
| better_auth | [better-auth/skills](https://github.com/better-auth/skills) |
| book_translator | [deusyu/translate-book](https://github.com/deusyu/translate-book) |
| bootstrap | [alinaqi/claude-bootstrap](https://github.com/alinaqi/claude-bootstrap) |
| brave | [brave/brave-search-skills](https://github.com/brave/brave-search-skills) |
| brian_wagner | [BrianRWagner/ai-marketing-claude-code-skills](https://github.com/BrianRWagner/ai-marketing-claude-code-skills) |
| charlie_cfo | [EveryInc/charlie-cfo-skill](https://github.com/EveryInc/charlie-cfo-skill) |
| claude_apple_bridges | [more-io/claude-apple-bridges](https://github.com/more-io/claude-apple-bridges) |
| claude_bootstrap | [alinaqi/claude-bootstrap](https://github.com/alinaqi/claude-bootstrap) |
| claude_code_startup | [rameerez/claude-code-startup-skills](https://github.com/rameerez/claude-code-startup-skills) |
| claude_ecom | [takechanman1228/claude-ecom](https://github.com/takechanman1228/claude-ecom) |
| claude_for_legal | [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal) |
| claude_memory | [hanfang/claude-memory-skill](https://github.com/hanfang/claude-memory-skill) |
| claude_seo | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) |
| claude_speed_reader | [SeanZoR/claude-speed-reader](https://github.com/SeanZoR/claude-speed-reader) |
| clickhouse | [ClickHouse/agent-skills](https://github.com/ClickHouse/agent-skills) |
| coderabbit | [coderabbitai/skills](https://github.com/coderabbitai/skills) |
| codex_collab | [Kevin7Qi/codex-collab](https://github.com/Kevin7Qi/codex-collab) |
| coinbase | [coinbase/agentic-wallet-skills](https://github.com/coinbase/agentic-wallet-skills) |
| composiohq | [ComposioHQ/skills](https://github.com/ComposioHQ/skills) |
| context_eng | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) |
| creative_director | [smixs/creative-director-skill](https://github.com/smixs/creative-director-skill) |
| cybersecurity | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) |
| data_structures | [k-kolomeitsev/data-structure-protocol](https://github.com/k-kolomeitsev/data-structure-protocol) |
| dev_agent | [fvadicamo/dev-agent-skills](https://github.com/fvadicamo/dev-agent-skills) |
| duckdb | [duckdb/duckdb-skills](https://github.com/duckdb/duckdb-skills) |
| ecommerce_skills | [nexscope-ai/eCommerce-Skills](https://github.com/nexscope-ai/eCommerce-Skills) |
| email_marketing | [CosmoBlk/email-marketing-bible](https://github.com/CosmoBlk/email-marketing-bible) |
| figma | [figma/mcp-server-guide](https://github.com/figma/mcp-server-guide) |
| firebase | [firebase/agent-skills](https://github.com/firebase/agent-skills) |
| founder_skills | [ognjengt/founder-skills](https://github.com/ognjengt/founder-skills) |
| frontend_slides | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) |
| gemini_official | [google-gemini/gemini-skills](https://github.com/google-gemini/gemini-skills) |
| general_skills | [sanjay3290/ai-skills](https://github.com/sanjay3290/ai-skills) |
| graphify | [safishamsi/graphify](https://github.com/safishamsi/graphify) |
| gstack | [garrytan/gstack](https://github.com/garrytan/gstack) |
| health | [huifer/WellAlly-health](https://github.com/huifer/WellAlly-health) |
| home_assistant | [komal-SkyNET/claude-skill-homeassistant](https://github.com/komal-SkyNET/claude-skill-homeassistant) |
| huggingface | [huggingface/skills](https://github.com/huggingface/skills) |
| humanizer | [blader/humanizer](https://github.com/blader/humanizer) |
| industry_expert | [voidborne-d/master-skill](https://github.com/voidborne-d/master-skill) |
| ios_simulator | [conorluddy/ios-simulator-skill](https://github.com/conorluddy/ios-simulator-skill) |
| kicad_happy | [aklofas/kicad-happy](https://github.com/aklofas/kicad-happy) |
| lambdatest | [LambdaTest/agent-skills](https://github.com/LambdaTest/agent-skills) |
| last30days | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) |
| linear_claude | [wrsmith108/linear-claude-skill](https://github.com/wrsmith108/linear-claude-skill) |
| marketing_skills | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) |
| materials_sim | [HeshamFS/materials-simulation-skills](https://github.com/HeshamFS/materials-simulation-skills) |
| mattpocock_skill | [mattpocock/skills](https://github.com/mattpocock/skills) |
| mcollina | [mcollina/skills](https://github.com/mcollina/skills) |
| memory_kit | [awrshift/claude-memory-kit](https://github.com/awrshift/claude-memory-kit) |
| model_hierarchy | [zscole/model-hierarchy-skill](https://github.com/zscole/model-hierarchy-skill) |
| mongodb | [mongodb/agent-skills](https://github.com/mongodb/agent-skills) |
| neondatabase | [neondatabase/agent-skills](https://github.com/neondatabase/agent-skills) |
| nodejs_skill | [mcollina/skills](https://github.com/mcollina/skills) |
| notebooklm | [PleasePrompto/notebooklm-skill](https://github.com/PleasePrompto/notebooklm-skill) |
| notion_cookbook | [makenotion/notion-cookbook](https://github.com/makenotion/notion-cookbook) |
| notion_official | [makenotion/skills](https://github.com/makenotion/skills) |
| opc_skills | [ReScienceLab/opc-skills](https://github.com/ReScienceLab/opc-skills) |
| openai | [openai/skills](https://github.com/openai/skills) |
| optimizer | [hqhq1025/skill-optimizer](https://github.com/hqhq1025/skill-optimizer) |
| pixelle_video | [AIDC-AI/Pixelle-Video](https://github.com/AIDC-AI/Pixelle-Video) |
| platform_design | [ehmo/platform-design-skills](https://github.com/ehmo/platform-design-skills) |
| playwright | [lackeyjb/playwright-skill](https://github.com/lackeyjb/playwright-skill) |
| product_manager_skills | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) |
| property_management | [appleaa123/property-management-skills](https://github.com/appleaa123/property-management-skills) |
| property_staging | [appleaa123/property-staging-skill](https://github.com/appleaa123/property-staging-skill) |
| qdrant | [qdrant/skills](https://github.com/qdrant/skills) |
| recursive_decomp | [massimodeluisa/recursive-decomposition-skill](https://github.com/massimodeluisa/recursive-decomposition-skill) |
| rednote_bootstrap | [CopeeeTang/rednote-mind-skills](https://github.com/CopeeeTang/rednote-mind-skills) |
| resend | [resend/resend-skills](https://github.com/resend/resend-skills) |
| resume_skills | [Paramchoudhary/ResumeSkills](https://github.com/Paramchoudhary/ResumeSkills) |
| rootly_mcp | [Rootly-AI-Labs/rootly-mcp-server](https://github.com/Rootly-AI-Labs/rootly-mcp-server) |
| scientific_agent | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) |
| seo_geo | [aaron-he-zhu/seo-geo-claude-skills](https://github.com/aaron-he-zhu/seo-geo-claude-skills) |
| shpigford | [Shpigford/skills](https://github.com/Shpigford/skills) |
| skill_seekers | [yusufkaraaslan/Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) |
| sleep_research | [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) |
| snyk_scan | [snyk/agent-scan](https://github.com/snyk/agent-scan) |
| speed_reader | [SeanZoR/claude-speed-reader](https://github.com/SeanZoR/claude-speed-reader) |
| startup_code | [rameerez/claude-code-startup-skills](https://github.com/rameerez/claude-code-startup-skills) |
| supabase | [supabase/agent-skills](https://github.com/supabase/agent-skills) |
| superpowers | [obra/superpowers](https://github.com/obra/superpowers) |
| superpowers_lab | [obra/superpowers-lab](https://github.com/obra/superpowers-lab) |
| swift_patterns | [efremidze/swift-patterns-skill](https://github.com/efremidze/swift-patterns-skill) |
| swiftui_agent | [AvdLee/SwiftUI-Agent-Skill](https://github.com/AvdLee/SwiftUI-Agent-Skill) |
| taste_skill | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) |
| tinybird | [tinybirdco/tinybird-agent-skills](https://github.com/tinybirdco/tinybird-agent-skills) |
| tutor_skills | [bevibing/tutor-skills](https://github.com/bevibing/tutor-skills) |
| tvc_director | [Ethanxwang/tvc-director](https://github.com/Ethanxwang/tvc-director) |
| tweetclaw | [Xquik-dev/tweetclaw](https://github.com/Xquik-dev/tweetclaw) |
| ui_skills | [ibelick/ui-skills](https://github.com/ibelick/ui-skills) |
| ui_ux_pro | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) |
| understand_code | [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) |
| varlock | [wrsmith108/varlock-claude-skill](https://github.com/wrsmith108/varlock-claude-skill) |
| vercel | [vercel-labs/skills](https://github.com/vercel-labs/skills) |
| vexor | [scarletkc/vexor](https://github.com/scarletkc/vexor) |
| vibesec | [BehiSecc/VibeSec-Skill](https://github.com/BehiSecc/VibeSec-Skill) |
| video_db | [video-db/skills](https://github.com/video-db/skills) |
| volt_agent | [VoltAgent/skills](https://github.com/VoltAgent/skills) |
| web_quality | [addyosmani/web-quality-skills](https://github.com/addyosmani/web-quality-skills) |
| wonda | [degausai/wonda](https://github.com/degausai/wonda) |
| wordpress | [WordPress/agent-skills](https://github.com/WordPress/agent-skills) |
| x_publisher | [wshuyi/x-article-publisher-skill](https://github.com/wshuyi/x-article-publisher-skill) |
| youtube_clipper | [op7418/Youtube-clipper-skill](https://github.com/op7418/Youtube-clipper-skill) |

---

## 12. License

MIT
