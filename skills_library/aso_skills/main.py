"""Skill: aso_skills."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("aso-skills")


_SKILLS: dict[str, dict] = {
    'why-this-exists': {
        "description": 'Most ASO knowledge lives in blog posts, courses, and expensive consultants.',
        "guidance": 'Most ASO knowledge lives in blog posts, courses, and expensive consultants. We packaged it into skills that any AI agent can use — so you get expert-level ASO guidance directly in your IDE.\n\nEach skill contains battle-tested frameworks, scoring rubrics, and output templates. The agent reads the skill, pulls real data from the App Store (via Appeeky), and gives you actionable recommendations — not generic advice.',
    },
    'quick-start': {
        "description": '**Cursor** — Settings (Cmd+Shift+J) → Rules → Add Rule → Remote Rule (Github) → paste `https://github.',
        "guidance": '**Cursor** — Settings (Cmd+Shift+J) → Rules → Add Rule → Remote Rule (Github) → paste `https://github.com/eronred/aso-skills`\n\n**Claude Code** — `npx skills add eronred/aso-skills`\n\n**Manual** — `git clone https://github.com/eronred/aso-skills.git && cp -r aso-skills/skills/* .cursor/skills/`\n\nThen ask your agent:\n\n```\n"Run an ASO audit for my app (id: 1617391485)"\n"Find the best keywords for a meditation app"\n"Optimize my App Store title and subtitle"\n"How many downloads do I need to reach top 10 in Health & Fitness?"\n"What apps are rising in the charts right now?"\n"Give me a market briefing for the Games category"\n"How are my downloads and revenue trending this month?"\n"Help me plan a Christmas In-App Event"\n"What seasonal keywords should I add in December?"\n"Optimize my Google Play listing"\n"My app rating dropped — how do I recover it?"\n"Set up a weekly competitor monitoring routine for apps X, Y, Z"\n"Help me pitch TechCrunch for my app launch"\n"Build an Apple Search Ads campaign structure for my fitness app"\n"My app has a crash affecting 2% of sessions — help me triage it"\n```\n\nOr invoke directly: `/aso-audit`, `/keyword-research`, `/metadata-optimization`, `/market-movers`, `/market-pulse`, `/asc-metrics`, `/in-app-events`, `/seasonal-aso`, `/android-aso`, `/apple-search-ads`, `/competitor-tracking`',
    },
    'skills': {
        "description": '### ASO Core\n\n| Skill | What it does |\n|-------|-------------|\n| [`aso-audit`](skills/aso-audit) | Scores your listing across 10 factors (0-100), flags problems, gives a prioritized fix list |\n| [`key',
        "guidance": "### ASO Core\n\n| Skill | What it does |\n|-------|-------------|\n| [`aso-audit`](skills/aso-audit) | Scores your listing across 10 factors (0-100), flags problems, gives a prioritized fix list |\n| [`keyword-research`](skills/keyword-research) | Finds keywords by volume × difficulty × relevance, groups them into primary/secondary/long-tail |\n| [`metadata-optimization`](skills/metadata-optimization) | Writes title, subtitle, keyword field, description — with 3 variants and character counts |\n| [`competitor-analysis`](skills/competitor-analysis) | Keyword gaps, creative teardown, positioning map, and specific opportunities to exploit |\n| [`seasonal-aso`](skills/seasonal-aso) | Seasonal keyword calendar, metadata swap strategy, timing checklist, and trending-moment tactics |\n| [`android-aso`](skills/android-aso) | Google Play-specific ASO — indexed description strategy, short description, Play Experiments, rating recovery |\n\n### Creative & International\n\n| Skill | What it does |\n|-------|-------------|\n| [`screenshot-optimization`](skills/screenshot-optimization) | 10-slot screenshot strategy with design briefs, text overlay copy, and competitor audit |\n| [`app-icon-optimization`](skills/app-icon-optimization) | Icon design principles, A/B testing via PPO/Play Experiments, category differentiation, and icon briefs |\n| [`review-management`](skills/review-management) | Sentiment analysis, response templates (HEAR framework), rating improvement tactics |\n| [`localization`](skills/localization) | Market prioritization matrix, per-country keyword research, cultural adaptation checklist |\n\n### Growth\n\n| Skill | What it does |\n|-------|-------------|\n| [`app-launch`](skills/app-launch) | 8-week launch timeline with daily checklists, channel strategy, and press outreach templates |\n| [`ua-campaign`](skills/ua-campaign) | Apple Search Ads, Meta, Google UAC — campaign structure, bidding, creative specs, budget allocation |\n| [`apple-search-ads`](skills/apple-search-ads) | Deep-dive ASA — campaign structure, match types, CPP routing, bid strategy, weekly optimization checklist |\n| [`app-store-featured`](skills/app-store-featured) | Featuring readiness score, Apple tech checklist, pitch template, In-App Events calendar |\n| [`in-app-events`](skills/in-app-events) | Plan and write App Store In-App Events — copy, image brief, keyword strategy, submission timeline |\n| [`app-clips`](skills/app-clips) | App Clip use cases, card design, URL scheme setup, SKOverlay handoff, and measurement |\n| [`press-and-pr`](skills/press-and-pr) | Media targeting tiers, pitch templates, press kit checklist, embargo strategy, Product Hunt launch |\n\n### Revenue & Retention\n\n| Skill | What it does |\n|-------|-------------|\n| [`monetization-strategy`](skills/monetization-strategy) | Pricing tiers, paywall timing/design, trial optimization, category benchmarks |\n| [`subscription-lifecycle`](skills/subscription-lifecycle) | Trial nurture sequences, voluntary/involuntary churn reduction, dunning, and win-back campaigns |\n| [`retention-optimization`](skills/retention-optimization) | Activation → habit → engagement framework, push notification sequences, churn prevention |\n| [`onboarding-optimization`](skills/onboarding-optimization) | First-run flow audit, activation event definition, permission prompt timing, sign-up friction reduction |\n| [`rating-prompt-strategy`](skills/rating-prompt-strategy) | SKStoreReviewRequest / Play In-App Review timing, pre-prompt survey, version-gating, and rating recovery |\n\n### Analytics & Testing\n\n| Skill | What it does |\n|-------|-------------|\n| [`app-analytics`](skills/app-analytics) | Event tracking plan, dashboard setup, KPI framework with category benchmarks |\n| [`ab-test-store-listing`](skills/ab-test-store-listing) | Hypothesis → variant design → sample size → interpretation for App Store A/B tests |\n| [`asc-metrics`](skills/asc-metrics) | Analyze your exact App Store Connect data (downloads, revenue, subscriptions, countries) via Appeeky Connect |\n| [`crash-analytics`](skills/crash-analytics) | Crashlytics setup, crash triage framework (P0–P3), symbolication, phased release strategy, rating recovery |\n\n### Market Intelligence\n\n| Skill | What it does |\n|-------|-------------|\n| [`market-movers`](skills/market-movers) | Identifies top chart gainers/losers, new entries, and dropped apps — explains what's driving changes |\n| [`market-pulse`](skills/market-pulse) | Full market briefing: chart movements + trending keywords + featured apps + new launches in one view |\n| [`competitor-tracking`](skills/competitor-tracking) | Weekly competitor surveillance — metadata changes, keyword shifts, rating trends, chart movement deltas |\n\n### Foundation\n\n| Skill | What it does |\n|-------|-------------|\n| [`app-marketing-context`](skills/app-marketing-context) | Creates a context doc (app, audience, competitors, goals) that all other skills reference |",
    },
    'how-it-works': {
        "description": '```\nYou: "Run an ASO audit for Headspace"\n\nAgent:\n  1.',
        "guidance": '```\nYou: "Run an ASO audit for Headspace"\n\nAgent:\n  1. Reads aso-audit/SKILL.md (framework, scoring rubric, output template)\n  2. Calls Appeeky API → fetches metadata, keywords, ratings, competitors\n  3. Scores each factor (title: 8/10, subtitle: 6/10, keywords: 4/10...)\n  4. Returns: ASO Score Card + Quick Wins + High-Impact Changes + Strategic Recs\n```\n\nSkills reference each other — `aso-audit` might suggest running `keyword-research` for deeper analysis, which then feeds into `metadata-optimization` for implementation.',
    },
    'installation': {
        "description": '### Cursor\n\n| Method | Command |\n|--------|---------|\n| GitHub Import | Settings → Rules → Add Rule → Remote Rule → `https://github.',
        "guidance": '### Cursor\n\n| Method | Command |\n|--------|---------|\n| GitHub Import | Settings → Rules → Add Rule → Remote Rule → `https://github.com/eronred/aso-skills` |\n| Project-level | `cp -r aso-skills/skills/* .cursor/skills/` |\n| Global | `cp -r aso-skills/skills/* ~/.cursor/skills/` |\n\n### Claude Code\n\n| Method | Command |\n|--------|---------|\n| CLI | `npx skills add eronred/aso-skills` |\n| Specific skills | `npx skills add eronred/aso-skills --skill aso-audit keyword-research` |\n| Manual | `cp -r aso-skills/skills/* .claude/skills/` |\n\n### Any Agent\n\n```bash\ngit submodule add https://github.com/eronred/aso-skills.git .agents/aso-skills\n```\n\nWorks with any tool that supports the [Agent Skills](https://agentskills.io) standard (`.agents/skills/`, `.cursor/skills/`, `.claude/skills/`, `.codex/skills/`).',
    },
    'appeeky-integration': {
        "description": 'Skills work standalone with general ASO knowledge.',
        "guidance": 'Skills work standalone with general ASO knowledge. Connect [Appeeky](https://docs.appeeky.com/mcp) for real-time App Store data:\n\n```json\n{\n  "mcpServers": {\n    "appeeky": {\n      "url": "https://mcp.appeeky.com/mcp",\n      "headers": { "Authorization": "Bearer apk_your_key_here" }\n    }\n  }\n}\n```\n\nWith Appeeky connected, skills can pull live keyword rankings, competitor metadata, download estimates, trending keywords, and featured apps.\n\n### Appeeky Connect — First-Party ASC Data\n\nThe `asc-metrics` skill uses **Appeeky Connect**, a new integration that syncs your exact App Store Connect data (downloads, revenue, subscriptions, trials, IAP, and country breakdowns) into Appeeky nightly.\n\nConnect once at [appeeky.com → Settings → Integrations](https://appeeky.com) and then ask:\n\n```\n"How are my downloads trending this month?"\n"What are my top 5 markets by revenue?"\n"Compare this month\'s subscriptions to last month"\n```\n\nRequires Indie plan( coffee price: $8/month) or higher. See [tools/integrations/appeeky-connect.md](tools/integrations/appeeky-connect.md) for the full API reference.\n\nSee [tools/REGISTRY.md](tools/REGISTRY.md) for the full capability matrix.',
    },
    'contributing': {
        "description": 'PRs welcome — fix an inaccuracy, improve a framework, or add a new skill.',
        "guidance": 'PRs welcome — fix an inaccuracy, improve a framework, or add a new skill. See [CONTRIBUTING.md](CONTRIBUTING.md).',
    },
    'license': {
        "description": 'MIT.',
        "guidance": 'MIT',
    },
}


@mcp.tool()
def list_aso_skills_skills() -> dict:
    """List all available aso_skills skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_aso_skills_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific aso_skills skill."""
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
    hint = get_presentation_hint('aso_skills', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@aso_skills",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'aso_skills',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
