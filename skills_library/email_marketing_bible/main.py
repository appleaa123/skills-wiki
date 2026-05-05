"""Skill: email_marketing_bible."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("email-marketing-bible")


_SKILLS: dict[str, dict] = {
    'why-this-exists': {
        "description": 'Most email marketing advice is surface-level.',
        "guidance": 'Most email marketing advice is surface-level. "Personalise your subject lines." "Segment your list." "A/B test everything." You\'ve heard it. It doesn\'t help when you\'re staring at a 2% open rate wondering what\'s actually broken.\n\nThis skill gives Claude the same knowledge that comes from running an email platform serving 28,000 customers: the patterns that repeat across industries, the mistakes that destroy campaigns, and the specific strategies that consistently generate outsized returns.\n\nEvery claim is backed by data. Every recommendation has been tested by practitioners. No theory. No filler. Specific things you can implement this week.',
    },
    'install': {
        "description": '```bash\ngit clone https://github.',
        "guidance": "```bash\ngit clone https://github.com/CosmoBlk/email-marketing-bible.git ~/.claude/skills/email-marketing-bible\n```\n\nThat's it. One command. Claude now has access to the full knowledge base.",
    },
    'what-the-skill-does': {
        "description": 'Once installed, Claude can:\n\n| Task | What it does |\n|------|-------------|\n| **Audit your setup** | Review your current email marketing stack (flows, segments, deliverability, compliance) and tell yo',
        "guidance": 'Once installed, Claude can:\n\n| Task | What it does |\n|------|-------------|\n| **Audit your setup** | Review your current email marketing stack (flows, segments, deliverability, compliance) and tell you exactly what\'s missing |\n| **Draft email copy** | Write emails using proven frameworks (PAS, AIDA, Before-After-Bridge) with subject lines, preview text, body copy, and CTAs |\n| **Build automation flows** | Design welcome series, abandoned cart, post-purchase, win-back, sunset, and nurture sequences with timing and triggers |\n| **Pull industry benchmarks** | Get open rates, click rates, conversion rates, and revenue-per-email for your specific vertical |\n| **Fix deliverability** | Diagnose inbox placement issues with a 10-step framework covering authentication, reputation, content, and infrastructure |\n| **Compare platforms** | Get honest platform comparisons based on your list size, budget, and use case, not affiliate commissions |\n| **Review compliance** | Check your setup against GDPR, CAN-SPAM, CASL, CCPA, and the Australian Spam Act |\n| **Write cold email** | Build cold outreach sequences with proper infrastructure separation, warming, and personalisation |\n| **Design emails** | Reference 57 curated best-in-class email designs with specific design patterns, typography, colour, visual hierarchy, and "steal this" notes |',
    },
    'how-to-use-it-with-claude': {
        "description": 'Install the skill, then talk to Claude like you would an email marketing consultant.',
        "guidance": 'Install the skill, then talk to Claude like you would an email marketing consultant. Here are some examples:\n\n**Review your current email marketing:**\n```\n"Review my current email setup. I\'m running Klaviyo for a DTC skincare brand,\ndoing about $2M/year. I have a welcome series, abandoned cart, and one weekly\nnewsletter. What am I missing?"\n```\n\n**Fix a specific problem:**\n```\n"My emails are landing in Gmail promotions tab and my open rates dropped from\n22% to 14% over the last 3 months. What\'s going on and how do I fix it?"\n```\n\n**Build flows from scratch:**\n```\n"Build me a complete post-purchase email sequence for my Shopify store. I sell\npremium coffee. Average order is $45, repeat purchase cycle is 30-45 days."\n```\n\n**Get industry-specific advice:**\n```\n"I\'m launching a B2B SaaS product. What does my email marketing stack need\nto look like from day one? Give me the flows, segments, and metrics I should\nbe tracking."\n```\n\n**Draft copy:**\n```\n"Write a win-back email sequence for subscribers who haven\'t opened in 90 days.\nMy brand voice is casual and direct. We sell fitness equipment."\n```\n\nClaude will pull from 68,000 words of research, benchmarks, frameworks, and real case studies to give you specific, actionable advice, not generic platitudes.',
    },
    'what-s-inside-the-knowledge-base': {
        "description": '### 17 chapters\n\n| # | Chapter | What you get |\n|---|---------|-------------|\n| 1 | The Fundamentals | Why email wins, the marketing stack, key metrics, common mistakes |\n| 2 | Building Your List | Or',
        "guidance": '### 17 chapters\n\n| # | Chapter | What you get |\n|---|---------|-------------|\n| 1 | The Fundamentals | Why email wins, the marketing stack, key metrics, common mistakes |\n| 2 | Building Your List | Organic growth, popups, double vs single opt-in, spam traps, validation |\n| 3 | Segmentation & Personalisation | RFM scoring, engagement tiers, zero-party data, waterfall segmentation |\n| 4 | The Emails That Make Money | Welcome series, abandoned cart, post-purchase, win-back, with timing and benchmarks |\n| 5 | Copywriting That Converts | Subject lines, preview text, body copy, CTAs, frameworks (PAS, AIDA, BAB) |\n| 6 | Design & Technical | Mobile-first, dark mode, accessibility, email client compatibility |\n| 7 | Deliverability | SPF, DKIM, DMARC, BIMI, sender reputation, IP warming, spam filters |\n| 8 | Testing & Optimisation | A/B testing, statistical significance, send time optimisation |\n| 9 | Analytics & Measurement | KPIs by campaign type, attribution, subscriber LTV, incrementality |\n| 10 | Compliance & Privacy | GDPR, CAN-SPAM, CASL, CCPA, Australian Spam Act, one-click unsubscribe |\n| 11 | Industry Playbooks | Segment-specific tactics for 19 verticals (see below) |\n| 12 | Choosing Your Platform | Honest comparison of Klaviyo, Mailchimp, Kit, beehiiv, Sendlane, and more |\n| 13 | Cold Email & B2B Outbound | Infrastructure, tools, writing, personalisation, follow-up sequences |\n| 14 | AI & the Future of Email | Where AI helps, where it doesn\'t, practical integration, MCP |\n| 15 | Company Case Studies | How Casper, Morning Brew, Duolingo, Spotify, and 6 others use email |\n| 16 | Expert Directory | 44 practitioners referenced throughout, who to follow and why |\n| 17 | Best Email Designs 2026 | 57 curated designs with design best practices, visual hierarchy, brand voice, and "steal this" notes |\n\n### 19 industry playbooks\n\nEvery vertical gets its own playbook with specific tactics, benchmarks, and automation flows:\n\n`Ecommerce DTC` · `SaaS B2B` · `SaaS B2C` · `Newsletter & Creator` · `Agency` · `Nonprofit` · `Healthcare` · `Financial Services` · `Real Estate` · `Travel & Hospitality` · `Education` · `Professional Services` · `Retail` · `Events` · `B2B Manufacturing` · `Restaurant & Food` · `Fitness` · `Media & Publishing` · `Marketplace & Platform`\n\n### 44 expert contributors\n\nInsights from practitioners including Chad S. White (Zeta Global), Joanna Wiebe (Copyhackers), Chase Dimond (Structured Agency), Nathan Barry (Kit), Ann Handley (MarketingProfs), Troy Ericson (EmailDeliverability.com), Tyler Denk (beehiiv), Ben Settle (Email Players), and 36 others. Full directory in Chapter 16.',
    },
    'read-the-full-guide': {
        "description": 'The complete 68,000-word Email Marketing Bible is available at **[emailmarketingskill.',
        "guidance": 'The complete 68,000-word Email Marketing Bible is available at **[emailmarketingskill.com](https://emailmarketingskill.com)**, searchable, browsable, with all 17 chapters and 4 appendices.',
    },
    'research': {
        "description": '908 sources across industry reports (Litmus, Klaviyo, Campaign Monitor, HubSpot, Salesforce), practitioner blogs, academic research, platform documentation, and community discussions from Reddit, Shop',
        "guidance": '908 sources across industry reports (Litmus, Klaviyo, Campaign Monitor, HubSpot, Salesforce), practitioner blogs, academic research, platform documentation, and community discussions from Reddit, Shopify forums, and X.\n\nThe research crawler is open source at [github.com/CosmoBlk/emb-research](https://github.com/CosmoBlk/emb-research).',
    },
    'contributing': {
        "description": "Found an error? Have better data? Know a tactic that's missing? PRs and issues welcome.",
        "guidance": "Found an error? Have better data? Know a tactic that's missing? PRs and issues welcome. This is an open-source knowledge base, and the more practitioners contribute, the better it gets for everyone.",
    },
    'license': {
        "description": 'MIT.',
        "guidance": 'MIT. Use it however you want.\n\n---\n\n*Built by [George Hartley](https://x.com/GTHartley). Follow for updates.*',
    },
}


@mcp.tool()
def list_email_marketing_bible_skills() -> dict:
    """List all available email_marketing_bible skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_email_marketing_bible_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific email_marketing_bible skill."""
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
    hint = get_presentation_hint('email_marketing_bible', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@email_marketing_bible",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'email_marketing_bible',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
