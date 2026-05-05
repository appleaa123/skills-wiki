"""Skill: claude_seo."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("claude-seo")


_SKILLS: dict[str, dict] = {
    'table-of-contents': {
        "description": '- [Installation](#installation)\n- [Quick Start](#quick-start)\n- [Commands](#commands)\n- [Features](#features)\n- [Architecture](#architecture)\n- [Extensions](#extensions)\n- [Showcase](#showcase)\n- [Eco',
        "guidance": '- [Installation](#installation)\n- [Quick Start](#quick-start)\n- [Commands](#commands)\n- [Features](#features)\n- [Architecture](#architecture)\n- [Extensions](#extensions)\n- [Showcase](#showcase)\n- [Ecosystem](#ecosystem)\n- [Documentation](#documentation)\n- [Requirements](#requirements)\n- [Uninstall](#uninstall)\n- [Contributing](#contributing)',
    },
    'installation': {
        "description": '### Plugin Install (Claude Code 1.',
        "guidance": "### Plugin Install (Claude Code 1.0.33+)\n\n```bash\n# Add marketplace (one-time)\n/plugin marketplace add AgriciDaniel/claude-seo\n\n# Install plugin\n/plugin install claude-seo@AgriciDaniel-claude-seo\n```\n\n### Manual Install (Unix/macOS/Linux)\n\n```bash\ngit clone --depth 1 https://github.com/AgriciDaniel/claude-seo.git\nbash claude-seo/install.sh\n```\n\n<details>\n<summary>One-liner (curl)</summary>\n\n```bash\ncurl -fsSL https://raw.githubusercontent.com/AgriciDaniel/claude-seo/main/install.sh | bash\n```\n\nOr via [install.cat](https://install.cat):\n\n```bash\ncurl -fsSL install.cat/AgriciDaniel/claude-seo | bash\n```\n\nPrefer to review the script before running?\n\n```bash\ncurl -fsSL https://raw.githubusercontent.com/AgriciDaniel/claude-seo/main/install.sh > install.sh\ncat install.sh        # review\nbash install.sh       # run when satisfied\nrm install.sh\n```\n\n</details>\n\n### Windows (PowerShell)\n\n```powershell\ngit clone --depth 1 https://github.com/AgriciDaniel/claude-seo.git\npowershell -ExecutionPolicy Bypass -File claude-seo\\install.ps1\n```\n\n> **Why git clone instead of `irm | iex`?** Claude Code's own security guardrails flag `irm ... | iex` as a supply chain risk (downloading and executing remote code with no verification). The git clone approach lets you inspect the script at `claude-seo\\install.ps1` before running it.",
    },
    'quick-start': {
        "description": '```bash\n# Start Claude Code\nclaude\n\n# Run a full site audit\n/seo audit https://example.',
        "guidance": '```bash\n# Start Claude Code\nclaude\n\n# Run a full site audit\n/seo audit https://example.com\n\n# Analyze a single page\n/seo page https://example.com/about\n\n# Check schema markup\n/seo schema https://example.com\n\n# Generate a sitemap\n/seo sitemap generate\n\n# Optimize for AI search\n/seo geo https://example.com\n```\n### Demo:\n[Watch the full demo on YouTube](https://www.youtube.com/watch?v=COMnNlUakQk)\n\n**`/seo audit`: full site audit with parallel subagents:**\n\n![SEO Audit Demo](screenshots/seo-audit-demo.gif)',
    },
    'commands': {
        "description": '| Command | Description |\n|---------|-------------|\n| `/seo audit <url>` | Full website audit with parallel subagent delegation |\n| `/seo page <url>` | Deep single-page analysis |\n| `/seo sitemap <url',
        "guidance": '| Command | Description |\n|---------|-------------|\n| `/seo audit <url>` | Full website audit with parallel subagent delegation |\n| `/seo page <url>` | Deep single-page analysis |\n| `/seo sitemap <url>` | Analyze existing XML sitemap |\n| `/seo sitemap generate` | Generate new sitemap with industry templates |\n| `/seo schema <url>` | Detect, validate, and generate Schema.org markup |\n| `/seo images <url>` | Image optimization analysis |\n| `/seo technical <url>` | Technical SEO audit (9 categories) |\n| `/seo content <url>` | E-E-A-T and content quality analysis |\n| `/seo geo <url>` | AI Overviews / Generative Engine Optimization |\n| `/seo plan <type>` | Strategic SEO planning (saas, local, ecommerce, publisher, agency) |\n| `/seo programmatic <url>` | Programmatic SEO analysis and planning |\n| `/seo competitor-pages <url>` | Competitor comparison page generation |\n| `/seo local <url>` | Local SEO analysis (GBP, citations, reviews, map pack) |\n| `/seo maps [command]` | Maps intelligence (geo-grid, GBP audit, reviews, competitors) |\n| `/seo hreflang <url>` | Hreflang/i18n SEO audit and generation |\n| `/seo google [command] [url]` | Google SEO APIs (GSC, PageSpeed, CrUX, Indexing, GA4) |\n| `/seo google report [type]` | Generate PDF/HTML report with charts (cwv-audit, gsc-performance, full) |\n| `/seo backlinks <url>` | Backlink profile analysis (free: Moz, Bing, Common Crawl) |\n| `/seo cluster <seed-keyword>` | SERP-based semantic clustering and content architecture |\n| `/seo sxo <url>` | Search Experience Optimization: page-type, user stories, personas |\n| `/seo drift baseline <url>` | Capture SEO baseline for change monitoring |\n| `/seo drift compare <url>` | Compare current state to stored baseline |\n| `/seo drift history <url>` | Show drift history over time |\n| `/seo ecommerce <url>` | E-commerce SEO: product schema, marketplace intelligence |\n| `/seo firecrawl [command] <url>` | Full-site crawling and site mapping (extension) |\n| `/seo dataforseo [command]` | Live SEO data via DataForSEO (extension) |\n| `/seo image-gen [use-case] <desc>` | AI image generation for SEO assets (extension) |\n\n### `/seo programmatic [url|plan]`\n**Programmatic SEO Analysis & Planning**\n\nBuild SEO pages at scale from data sources with quality safeguards.\n\n**Capabilities:**\n- Analyze existing programmatic pages for thin content and cannibalization\n- Plan URL patterns and template structures for data-driven pages\n- Internal linking automation between generated pages\n- Canonical strategy and index bloat prevention\n- Quality gates: WARNING at 100+ pages, HARD STOP at 500+ without audit\n\n### `/seo competitor-pages [url|generate]`\n**Competitor Comparison Page Generator**\n\nCreate high-converting "X vs Y" and "alternatives to X" pages.\n\n**Capabilities:**\n- Structured comparison tables with feature matrices\n- Product schema markup with AggregateRating\n- Conversion-optimized layouts with CTA placement\n- Keyword targeting for comparison intent queries\n- Fairness guidelines for accurate competitor representation\n\n### `/seo hreflang [url]`\n**Hreflang / i18n SEO Audit & Generation**\n\nValidate and generate hreflang tags for multi-language sites.\n\n**Capabilities:**\n- Generate hreflang tags (HTML, HTTP headers, or XML sitemap)\n- Validate self-referencing tags, return tags, x-default\n- Detect common mistakes (missing returns, invalid codes, HTTP/HTTPS mismatch)\n- Cross-domain hreflang support\n- Language/region code validation (ISO 639-1 + ISO 3166-1)',
    },
    'features': {
        "description": '### Core Web Vitals (Current Metrics)\n- **LCP** (Largest Contentful Paint): Target < 2.',
        "guidance": "### Core Web Vitals (Current Metrics)\n- **LCP** (Largest Contentful Paint): Target < 2.5s\n- **INP** (Interaction to Next Paint): Target < 200ms\n- **CLS** (Cumulative Layout Shift): Target < 0.1\n\n> Note: INP replaced FID on March 12, 2024. FID was fully removed from all Chrome tools on September 9, 2024.\n\n### E-E-A-T Analysis\nUpdated to September 2025 Quality Rater Guidelines:\n- **Experience**: First-hand knowledge signals\n- **Expertise**: Author credentials and depth\n- **Authoritativeness**: Industry recognition\n- **Trustworthiness**: Contact info, security, transparency\n\n### Schema Markup\n- Detection: JSON-LD (preferred), Microdata, RDFa\n- Validation against Google's supported types\n- Generation with templates\n- Deprecation awareness:\n  - HowTo: Deprecated (Sept 2023)\n  - FAQ: Restricted to gov/health sites (Aug 2023)\n  - SpecialAnnouncement: Deprecated (July 2025)\n\n### AI Search Optimization (GEO)\nNew for 2026 - optimize for:\n- Google AI Overviews\n- ChatGPT web search\n- Perplexity\n- Other AI-powered search\n\n### Google SEO APIs (New in v1.7.0)\nDirect integration with Google's SEO data:\n- **PageSpeed Insights + CrUX**: Lab and field Core Web Vitals data\n- **Search Console**: Top queries, URL inspection, sitemap status\n- **Indexing API**: Notify Google of new/updated/removed URLs\n- **GA4**: Organic traffic, top landing pages, device/country breakdown\n- **PDF Reports**: Enterprise A4 reports with charts via WeasyPrint + matplotlib\n\n4-tier credential system — get value at every level:\n| Tier | Auth | APIs |\n|------|------|------|\n| 0 | API key | PSI, CrUX, CrUX History |\n| 1 | + OAuth/SA | + GSC, URL Inspection, Indexing |\n| 2 | + GA4 config | + GA4 organic traffic |\n| 3 | + Ads token | + Keyword Planner |\n\n### Local SEO & Maps Intelligence (New in v1.6.0)\n- Google Business Profile optimization\n- NAP consistency auditing\n- Citation and review analysis\n- Geo-grid rank tracking and competitor radius mapping\n\n### Quality Gates\n- Warning at 30+ location pages\n- Hard stop at 50+ location pages\n- Thin content detection per page type\n- Doorway page prevention",
    },
    'architecture': {
        "description": '```\n~/.',
        "guidance": '```\n~/.claude/skills/seo/         # Main orchestrator skill\n~/.claude/skills/seo-*/       # Sub-skills (21 + 3 extensions)\n~/.claude/agents/seo-*.md     # Subagents (15 + 2 extensions)\n```\n\n### Video & Live Schema (New)\nAdditional schema types for video content, live streaming, and key moments:\n- VideoObject: Video page markup with thumbnails, duration, upload date\n- BroadcastEvent: LIVE badge support for live streaming content\n- Clip: Key moments / chapters within videos\n- SeekToAction: Enable seek functionality in video rich results\n- SoftwareSourceCode: Open source and code repository pages\n\nSee `schema/templates.json` for ready-to-use JSON-LD snippets.\n\n### Recently Added\n- Programmatic SEO skill (`/seo programmatic`)\n- Competitor comparison pages skill (`/seo competitor-pages`)\n- Multi-language hreflang validation (`/seo hreflang`)\n- Video & Live schema types (VideoObject, BroadcastEvent, Clip, SeekToAction)\n- Google SEO quick-reference guide',
    },
    'requirements': {
        "description": '- Python 3.',
        "guidance": '- Python 3.10+\n- Claude Code CLI\n- Optional: Playwright for screenshots\n- Optional: Google API credentials for enriched data (see `/seo google setup`)',
    },
    'uninstall': {
        "description": '```bash\ngit clone --depth 1 https://github.',
        "guidance": '```bash\ngit clone --depth 1 https://github.com/AgriciDaniel/claude-seo.git\nbash claude-seo/uninstall.sh\n```\n\n<details>\n<summary>One-liner (curl)</summary>\n\n```bash\ncurl -fsSL https://raw.githubusercontent.com/AgriciDaniel/claude-seo/main/uninstall.sh | bash\n```\n\n</details>\n\n### MCP Integrations\n\nIntegrates with MCP servers for live SEO data, including official servers from **Ahrefs** (`@ahrefs/mcp`) and **Semrush**, plus community servers for Google Search Console, PageSpeed Insights, and DataForSEO. See [MCP Integration Guide](docs/MCP-INTEGRATION.md) for setup.',
    },
    'extensions': {
        "description": 'Optional add-ons that integrate external data sources via MCP servers.',
        "guidance": 'Optional add-ons that integrate external data sources via MCP servers.\n\n### DataForSEO\n\nLive SERP data, keyword research, backlinks, on-page analysis, content analysis, business listings, AI visibility checking, and LLM mention tracking. 22 commands across 9 API modules.\n\n```bash\n# Install (requires DataForSEO account)\n./extensions/dataforseo/install.sh\n```\n\n```bash\n# Example commands\n/seo dataforseo serp best coffee shops\n/seo dataforseo keywords seo tools\n/seo dataforseo backlinks example.com\n/seo dataforseo ai-mentions your brand\n/seo dataforseo ai-scrape your brand name\n```\n\nSee [DataForSEO Extension](extensions/dataforseo/README.md) for full documentation.\n\n### Banana (AI Image Generation)\n\nGenerate SEO images (OG previews, blog heroes, product photos, infographics) using the\n[Claude Banana](https://github.com/AgriciDaniel/banana-claude) Creative Director pipeline.\n\n```bash\n# Install extension\n./extensions/banana/install.sh\n```\n\n```bash\n# Example commands\n/seo image-gen og "Professional SaaS dashboard"\n/seo image-gen hero "AI-powered content creation"\n/seo image-gen batch "Product photography" 3\n```\n\nSee [Banana Extension](extensions/banana/README.md) for full documentation.\nAlready using standalone Claude Banana? The extension reuses your existing nanobanana-mcp setup.\n\n### Firecrawl (Site Crawling)\n\nFull-site crawling and URL discovery using the [Firecrawl](https://www.firecrawl.dev/) MCP server.\n\n```bash\n# Install extension\n./extensions/firecrawl/install.sh\n```\n\n```bash\n# Example commands\n/seo firecrawl crawl https://example.com\n/seo firecrawl map https://example.com\n```\n\nSee [Firecrawl Extension](extensions/firecrawl/README.md) for full documentation.',
    },
    'showcase': {
        "description": 'Community projects built on top of Claude SEO:\n\n<table>\n<tr>\n<td width="40%">\n  <a href="https://github.',
        "guidance": 'Community projects built on top of Claude SEO:\n\n<table>\n<tr>\n<td width="40%">\n  <a href="https://github.com/avalonreset/claude-seo-dungeon">\n    <img src="https://raw.githubusercontent.com/avalonreset/claude-seo-dungeon/main/screenshots/battle-scene.webp" alt="Claude SEO Dungeon - turn-based SEO battle scene with Guild Ledger">\n  </a>\n</td>\n<td width="60%">\n\n**[Claude SEO Dungeon](https://github.com/avalonreset/claude-seo-dungeon)** -- a 16-bit gamified dungeon crawler that turns SEO audits into boss battles. Built on Claude SEO v1.9.0 with Phaser 3, every detected issue becomes a demon and every fix becomes a real commit to your codebase. The Guild Ledger streams Claude\'s tool calls in real time as you fight.\n\nBuilt by [@avalonreset](https://github.com/avalonreset) -- live at [seodungeon.com](https://seodungeon.com).\n\n</td>\n</tr>\n</table>\n\nWant your project featured here? [Open an issue](https://github.com/AgriciDaniel/claude-seo/issues/new) with a link.',
    },
    'ecosystem': {
        "description": 'Claude SEO is part of a family of Claude Code skills that work together:\n\n| Skill | What it does | How it connects |\n|-------|-------------|-----------------|\n| [Claude SEO](https://github.',
        "guidance": 'Claude SEO is part of a family of Claude Code skills that work together:\n\n| Skill | What it does | How it connects |\n|-------|-------------|-----------------|\n| [Claude SEO](https://github.com/AgriciDaniel/claude-seo) | SEO analysis, audits, schema, GEO | Core -- analyzes sites, generates action plans |\n| [Claude Blog](https://github.com/AgriciDaniel/claude-blog) | Blog writing, optimization, scoring | Companion -- write content optimized by SEO findings |\n| [Claude Banana](https://github.com/AgriciDaniel/banana-claude) | AI image generation via Gemini | Shared -- generates images for SEO assets and blog posts |\n| [Codex SEO](https://github.com/AgriciDaniel/codex-seo) | Codex-first SEO skill suite | Port -- same SEO system adapted for Codex skills, TOML agents, plugins, and deterministic runners |\n| [AI Marketing Claude](https://github.com/zubair-trabzada/ai-marketing-claude) | Copywriting, emails, social, ads, funnels, CRO | Community -- post-audit marketing action from SEO findings |\n| [FLOW](https://github.com/AgriciDaniel/flow) | Evidence-led SEO framework (41 AI prompts, CC BY 4.0) | Knowledge base — powers `seo-flow` prompts |\n\n**Workflow example:**\n1. `/seo audit https://example.com` -- identify content gaps and technical issues\n2. `/seo backlinks https://example.com` -- analyze link profile and competitor gaps\n3. `/blog write "target keyword"` -- create SEO-optimized blog posts\n4. `/seo image-gen hero "blog topic"` -- generate hero images (banana extension)\n5. `/seo geo https://example.com/blog/post` -- optimize for AI citations',
    },
    'documentation': {
        "description": '- [Installation Guide](docs/INSTALLATION.',
        "guidance": '- [Installation Guide](docs/INSTALLATION.md)\n- [Commands Reference](docs/COMMANDS.md)\n- [Architecture](docs/ARCHITECTURE.md)\n- [MCP Integration](docs/MCP-INTEGRATION.md)\n- [Troubleshooting](docs/TROUBLESHOOTING.md)',
    },
    'community-contributors': {
        "description": 'v1.',
        "guidance": 'v1.9.0 includes contributions from the [AI Marketing Hub](https://www.skool.com/ai-marketing-hub) Pro Hub Challenge:\n\n| Contributor | Contribution |\n|------------|-------------|\n| **Lutfiya Miller** (Winner) | Semantic Cluster Engine → `seo-cluster` |\n| **Florian Schmitz** | SXO Skill → `seo-sxo` |\n| **Dan Colta** | SEO Drift Monitor → `seo-drift` |\n| **Chris Muller** | Multi-lingual SEO → `seo-hreflang` enhancements |\n| **Matej Marjanovic** | E-commerce + DataForSEO Cost Config → `seo-ecommerce` + cost guardrails |\n\nSee [CONTRIBUTORS.md](CONTRIBUTORS.md) for full details and original repo links.',
    },
    'license': {
        "description": 'MIT License - see [LICENSE](LICENSE) for details.',
        "guidance": 'MIT License - see [LICENSE](LICENSE) for details.',
    },
    'contributing': {
        "description": 'Contributions welcome! Please read [CONTRIBUTING.',
        "guidance": 'Contributions welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting PRs.\n\n---\n\nBuilt for Claude Code by [@AgriciDaniel](https://github.com/AgriciDaniel)\n\n---',
    },
    'publishing-pipeline': {
        "description": 'For a full GUI-based publishing workflow from SEO research to published content, see [Rankenstein](https://rankenstein.',
        "guidance": 'For a full GUI-based publishing workflow from SEO research to published content, see [Rankenstein](https://rankenstein.pro) - the AI content engine built on the same SEO principles.\n\n---',
    },
    'author': {
        "description": 'Built by [Agrici Daniel](https://agricidaniel.',
        "guidance": 'Built by [Agrici Daniel](https://agricidaniel.com/about) - AI Workflow Architect.\n\n- [Blog](https://agricidaniel.com/blog) - Deep dives on AI marketing automation\n- [AI Marketing Hub](https://www.skool.com/ai-marketing-hub) - Free community, 2,800+ members\n- [YouTube](https://www.youtube.com/@AgriciDaniel) - Tutorials and demos\n- [All open-source tools](https://github.com/AgriciDaniel)',
    },
}


@mcp.tool()
def list_claude_seo_skills() -> dict:
    """List all available claude_seo skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_claude_seo_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific claude_seo skill."""
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
    hint = get_presentation_hint('claude_seo', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@claude_seo",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'claude_seo',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
