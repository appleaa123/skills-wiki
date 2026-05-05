"""Skill: ai_marketing."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("ai-marketing")


_SKILLS: dict[str, dict] = {
    'what-are-agent-skills': {
        "description": 'Agent Skills are an [open standard](https://agentskills.',
        "guidance": 'Agent Skills are an [open standard](https://agentskills.ai) for packaging expertise as instructions that AI agents can follow.\n\n**Traditional content:** You read it → You apply it → You forget half of it.\n\n**Agent Skills:** Your agent reads it → Your agent applies it → Every time. Perfectly.\n\nThink of it like giving Claude Code a playbook written by an expert. Instead of prompting from scratch every time, the skill provides the framework, questions, and output format automatically.\n\n---',
    },
    'quick-install-claude-code': {
        "description": '```bash\n# Clone the repo\ngit clone https://github.',
        "guidance": "```bash\n# Clone the repo\ngit clone https://github.com/BrianRWagner/ai-marketing-claude-code-skills.git\n\n# Copy skills to Claude Code's skills folder\nmkdir -p ~/.claude/skills\ncp -r ai-marketing-claude-code-skills/* ~/.claude/skills/\n```\n\nThat's it. Claude Code will now automatically use these skills when you mention related topics.\n\n---",
    },
    'available-skills': {
        "description": '### Strategy & Positioning\n\n#### 🎯 Positioning Basics\nCore positioning framework for founders and marketers.',
        "guidance": '### Strategy & Positioning\n\n#### 🎯 Positioning Basics\nCore positioning framework for founders and marketers. Clarify who you\'re for, what you do, and why you\'re different.\n\n**Use when:** "Help me with positioning", "Who is this for?", "What makes us different?"\n\n→ [positioning-basics/SKILL.md](./positioning-basics/SKILL.md)\n\n---\n\n#### 🔍 AI Discoverability Audit\nAudit how a brand appears in AI-powered search and recommendation systems (ChatGPT, Perplexity, Claude, Gemini).\n\n**Use when:** "How do I show up in ChatGPT?", "AI search visibility", "AEO audit"\n\n→ [ai-discoverability-audit/SKILL.md](./ai-discoverability-audit/SKILL.md)\n\n---\n\n#### 📚 Marketing Principles\nApply timeless marketing and business principles from the masters (Drucker, Ogilvy, Godin, Buffett, Munger, Bezos, Jobs).\n\n**Use when:** "First principles thinking", "Should I do X?", "What would work here?", strategic decisions\n\n→ [marketing-principles/SKILL.md](./marketing-principles/SKILL.md)\n\n---\n\n### Content & Authority\n\n#### 💼 LinkedIn Authority Builder\nBuild a LinkedIn content system for thought leadership. Positioning, content pillars, formats, and posting rhythm.\n\n**Use when:** "LinkedIn strategy", "Build my presence", "Content system", "Thought leadership"\n\n→ [linkedin-authority-builder/SKILL.md](./linkedin-authority-builder/SKILL.md)\n\n---\n\n#### 💡 Content Idea Generator\nGenerate content ideas based on your positioning and ICP. Multiple frameworks for different content types.\n\n**Use when:** "What should I post?", "Content ideas", "Blog topics", "LinkedIn content"\n\n→ [content-idea-generator/SKILL.md](./content-idea-generator/SKILL.md)\n\n---\n\n#### 🎙️ Voice Extractor\nExtract and document someone\'s authentic writing voice from samples. Create voice guides for AI training or ghostwriting.\n\n**Use when:** "Capture my voice", "Voice guide", "Write like me", "Train AI on my style"\n\n→ [voice-extractor/SKILL.md](./voice-extractor/SKILL.md) | [$9 premium version on Claw Mart →](https://www.shopclawmart.com/listings/voice-extractor-f1578cb8)\n\n---\n\n#### 🧹 De-AI-ify\nRemove AI-generated jargon and restore human voice to text. Built from analyzing 1,000+ AI vs human content pieces.\n\n**Use when:** "This sounds like AI", "Make it human", "Remove AI voice", "De-robotify this"\n\n→ [de-ai-ify/SKILL.md](./de-ai-ify/SKILL.md)\n\n---\n\n#### 📱 Social Card Generator\nGenerate platform-specific social post variants (Twitter, LinkedIn, Reddit) from one source input. No API dependency.\n\n**Use when:** "Turn this into social posts", "Repurpose for Twitter/LinkedIn", "Create social variants"\n\n→ [social-card-gen/SKILL.md](./social-card-gen/SKILL.md)\n\n---\n\n### Research & Intelligence\n\n#### 🔬 Last 30 Days Research\nResearch any topic across Reddit, X, and web from the last 30 days. Current trends, real community sentiment, and actionable insights in 7 minutes vs 2 hours manual research.\n\n**Use when:** "What are people saying about X?", "Current trends in Y", "Market research", "Community sentiment"\n\n→ [last30days/SKILL.md](./last30days/SKILL.md)\n\n---\n\n#### 🔎 Reddit Insights\nSearch and analyze Reddit content using semantic AI search. Find user pain points, discover niche markets, validate business ideas with real user feedback.\n\n**Use when:** "Search Reddit for...", "What does Reddit think about?", "Find pain points", "Validate this idea"\n\n→ [reddit-insights/SKILL.md](./reddit-insights/SKILL.md)\n\n---\n\n#### 🎬 YouTube Summarizer\nFetch YouTube video transcripts, generate structured summaries with key insights and metadata. Supports full transcript delivery.\n\n**Use when:** "Summarize this YouTube video", "Get transcript from...", "Key takeaways from this video"\n\n→ [youtube-summarizer/SKILL.md](./youtube-summarizer/SKILL.md)\n\n---\n\n#### 🔗 LinkedIn Profile Optimizer\nAudit and rewrite your LinkedIn profile to attract the right people. Scores each section, rewrites headline and about copy, and includes an AI visibility checklist for ChatGPT/Perplexity/Claude search.\n\n**Use when:** "Optimize my LinkedIn", "Rewrite my about section", "LinkedIn profile help", "AI search visibility"\n\n→ [linkedin-profile-optimizer/SKILL.md](./linkedin-profile-optimizer/SKILL.md)\n\n---\n\n### Conversion & Sales\n\n#### 📄 Homepage Audit\nQuick conversion audit for any homepage or landing page. Get actionable feedback in minutes.\n\n**Use when:** "Review my homepage", "Why isn\'t my page converting?", "Audit my landing page"\n\n→ [homepage-audit/SKILL.md](./homepage-audit/SKILL.md)\n\n---\n\n#### 📧 Cold Outreach Sequence\nBuild personalized cold outreach sequences for LinkedIn and email. Research, connection requests, follow-ups, and conversion.\n\n**Use when:** "Cold outreach", "LinkedIn messages", "Prospecting sequence", "Sales emails"\n\n→ [cold-outreach-sequence/SKILL.md](./cold-outreach-sequence/SKILL.md)\n\n---\n\n#### 📊 Case Study Builder\nTurn client wins into formatted case studies for proposals, social proof, and sales conversations.\n\n**Use when:** "Write a case study", "Document results", "Client success story", "Build social proof"\n\n→ [case-study-builder/SKILL.md](./case-study-builder/SKILL.md)\n\n---\n\n#### ⭐ Testimonial Collector\nSystematically gather and format client testimonials for social proof.\n\n**Use when:** "Get testimonials", "Social proof", "Client quotes", "Build credibility"\n\n→ [testimonial-collector/SKILL.md](./testimonial-collector/SKILL.md)\n\n---\n\n### Productivity & Operations\n\n#### 📅 Plan My Day\nGenerate an energy-optimized, time-blocked daily plan based on circadian rhythm research and GTD principles.\n\n**Use when:** "Plan my day", "Time block today", "What should I work on?", "Daily schedule"\n\n→ [plan-my-day/SKILL.md](./plan-my-day/SKILL.md)\n\n---\n\n#### 📧 Newsletter Creation & Curation\nIndustry-adaptive B2B newsletter creation with stage, role, and geography-aware workflows.\n\n**Use when:** "Create a newsletter", "Curate content for newsletter", "B2B newsletter", "Weekly digest"\n\n→ [newsletter-creation-curation/SKILL.md](./newsletter-creation-curation/SKILL.md)\n\n---\n\n#### 🚀 Go Mode\nDeep work execution mode. When you have a clear task and need to execute without distraction.\n\n**Use when:** "Go mode", "Execute this", "Let\'s build", "Ship it"\n\n→ [go-mode/SKILL.md](./go-mode/SKILL.md)\n\n---',
    },
    'installation': {
        "description": '### Quick Install (any platform)\n\n```bash\ngit clone https://github.',
        "guidance": "### Quick Install (any platform)\n\n```bash\ngit clone https://github.com/BrianRWagner/ai-marketing-claude-code-skills.git\ncd ai-marketing-claude-code-skills\nbash scripts/install.sh\n```\n\nAuto-detects Claude Code, OpenClaw, Cursor, and Windsurf. Walks you through the rest.\n\n**Flags:**\n```bash\nbash scripts/install.sh --all              # install to every detected platform\nbash scripts/install.sh --platform=cursor  # specific platform only\nbash scripts/install.sh --include-pro      # include pro/ skills (if purchased)\nbash scripts/install.sh --dry-run          # preview without writing files\n```\n\n### Platform Support\n\n| Platform | Install Location | File Used | Notes |\n|----------|-----------------|-----------|-------|\n| **Claude Code** | `~/.claude/skills/` | `SKILL.md` | Full detail, all phases |\n| **OpenClaw** | `~/.openclaw/skills/` | `SKILL-OC.md` ¹ | Token-efficient edition |\n| **Cursor** | `.cursor/rules/` (project) | `SKILL.md` → `.mdc` | Converted with rule frontmatter |\n| **Windsurf** | `.windsurf/rules/` (project) | `SKILL.md` → `.md` | Converted with rule frontmatter |\n| **Generic** | `./ai-marketing-skills/` | `SKILL.md` | Plain copy, any tool |\n\n> ¹ **Dual-file system:** Each skill ships two versions — `SKILL.md` (Claude Code, verbose, all phases) and `SKILL-OC.md` (OpenClaw, condensed, ~200 lines, token-efficient). The installer automatically routes the right file to the right platform. If `SKILL-OC.md` isn't present yet for a skill, it falls back to `SKILL.md`.\n\n### List Available Skills\n\n```bash\nbash scripts/list-skills.sh\n```\n\n### Convert to Platform Format\n\n```bash\nbash scripts/convert.sh --platform=cursor --output-dir=./.cursor/rules\nbash scripts/convert.sh --all   # convert for all platforms into ./converted/\n```\n\n---",
    },
    'compatibility': {
        "description": '| Platform | Status | Notes |\n|----------|--------|-------|\n| **Claude Code** | ✅ Native | Primary target |\n| **OpenClaw** | ✅ Compatible | Works as-is, [optimized version available](https://github.',
        "guidance": '| Platform | Status | Notes |\n|----------|--------|-------|\n| **Claude Code** | ✅ Native | Primary target |\n| **OpenClaw** | ✅ Compatible | Works as-is, [optimized version available](https://github.com/BrianRWagner/ai-marketing-openclaw-skills) |\n| **GitHub Copilot** | ✅ Compatible | Via .github/skills |\n| **Cursor** | ✅ Compatible | Via rules/context |\n| **ChatGPT** | ⚠️ Manual | Paste SKILL.md content |\n| **Claude.ai** | ⚠️ Manual | Paste SKILL.md content |\n\n---',
    },
    'premium-skills-gumroad': {
        "description": 'Full Claude Code editions with structured reasoning phases, self-critique loops, and output precision.',
        "guidance": 'Full Claude Code editions with structured reasoning phases, self-critique loops, and output precision.\n\n→ [Browse all on Gumroad](https://brianrwagner.gumroad.com)\n\n| Skill | Price | Link |\n|-------|-------|------|\n| AI Marketing Bundle (all 7) | $49 | [Buy →](https://brianrwagner.gumroad.com/l/brw-cc-marketing-bundle) |\n| AI Discoverability Audit v2 | $19 | [Buy →](https://brianrwagner.gumroad.com/l/ai-discoverability-audit) |\n| Founder Intelligence | $15 | [Buy →](https://brianrwagner.gumroad.com/l/brw-founder-intelligence) |\n| Competitor Intel Brief | $12 | [Buy →](https://brianrwagner.gumroad.com/l/brw-competitor-intel-brief) |\n| Morning Brief System | $14 | [Buy →](https://brianrwagner.gumroad.com/l/brw-morning-brief-system) |\n| Brand Voice Extractor | $9 | [Buy →](https://brianrwagner.gumroad.com/l/brand-voice-extractor) |\n| AI Employee Onboarding | $9 | [Buy →](https://brianrwagner.gumroad.com/l/brw-ai-employee-onboarding) |\n| Brand Positioning Audit | $9 | [Buy →](https://brianrwagner.gumroad.com/l/brw-brand-positioning-audit) |',
    },
    'about': {
        "description": 'Created by **Brian Wagner** — AI Marketing Architect\n\n15+ years building marketing systems for Fortune 500s and startups.',
        "guidance": 'Created by **Brian Wagner** — AI Marketing Architect\n\n15+ years building marketing systems for Fortune 500s and startups. Now packaging that expertise for the AI era.\n\n- 🌐 [brianrwagner.com](https://brianrwagner.com)\n- 🐦 [@BrianRWagner](https://twitter.com/BrianRWagner)\n- 💼 [LinkedIn](https://linkedin.com/in/brianrwagner)\n\n---',
    },
    'contributing': {
        "description": 'Found an issue? Have an improvement?\n\n1.',
        "guidance": "Found an issue? Have an improvement?\n\n1. Fork the repo\n2. Make your changes\n3. Submit a PR\n\nAll contributions welcome. Let's make these skills better together.\n\n---",
    },
    'license': {
        "description": 'MIT — Use freely.',
        "guidance": 'MIT — Use freely. Attribution appreciated.\n\n---\n\n*Marketing frameworks that Claude Code actually executes.* 🔱',
    },
}


@mcp.tool()
def list_ai_marketing_skills() -> dict:
    """List all available ai_marketing skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_ai_marketing_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific ai_marketing skill."""
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
    hint = get_presentation_hint('ai_marketing', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@ai_marketing",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'ai_marketing',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
