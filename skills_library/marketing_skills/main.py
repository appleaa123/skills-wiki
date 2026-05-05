"""Marketing Skills — 44+ conversion, content, SEO, and growth skills.

Source: https://github.com/coreyhaines31/marketingskills (MIT)
"""

from fastmcp import FastMCP

from core.skill_config import get_presentation_hint

mcp = FastMCP("marketing-skills")
_SKILL_NAME = "marketing_skills"

_SKILLS: dict[str, dict] = {
    "product-marketing-context": {
        "category": "foundation",
        "description": "Foundation skill all others depend on — defines product, audience, and positioning.",
        "guidance": """# Product Marketing Context

This skill must be completed before using any other marketing skill.
It defines the shared context (product, ICP, positioning) that all other skills reference.

## Required Context to Capture

### Product
- What does the product do in one sentence?
- What is the primary outcome for the user?
- What is the pricing model and entry point?

### Ideal Customer Profile (ICP)
- Job title / role
- Company size and industry
- Primary pain being solved
- Where they discover solutions (channels)
- What they've tried before

### Positioning
- Category: what market does this compete in?
- Differentiation: what do you do better / differently than alternatives?
- Proof points: 2-3 specific, verifiable claims (numbers, case studies, awards)

### Voice & Tone
- 3 adjectives that describe the brand voice
- 3 adjectives that describe what the brand is NOT
- Approved / avoided terminology

## Output
A one-page context doc used to brief all other marketing skills.
""",
    },
    "copywriting": {
        "category": "content",
        "description": "Write persuasive website copy for homepages, landing pages, and pricing pages.",
        "guidance": """# Copywriting Skill

## Applies To
Homepages, landing pages, pricing pages, product pages. Not email or popups (separate skills).

## Before Writing — Gather Context
- Page purpose and primary desired action (CTA)
- Target audience and their primary pain point
- Product differentiation and proof points (specifics, not generalities)
- Traffic source: paid, organic, referral (affects assumed awareness level)

## Non-Negotiable Principles
- **Clarity over cleverness** — if the message requires decoding, rewrite it.
- **Benefits over features** — lead with outcomes, explain mechanics second.
- **Specificity wins** — "Cut reporting from 4 hours to 15 minutes" beats "Save time."
- **Customer language** — use the words prospects use to describe their pain, not internal jargon.
- **One idea per section** — don't bury the lead with multiple competing messages.

## Structure (Standard Landing Page)
1. **Hero**: Primary headline (biggest benefit or boldest claim) + sub-headline + CTA
2. **Problem**: Agitate the pain; make the prospect feel understood
3. **Solution**: Introduce the product as the answer
4. **Features → Benefits**: 3-5 key capabilities, each followed by the customer outcome
5. **Social Proof**: Testimonials, logos, case studies, numbers
6. **FAQ**: Pre-empt the top 3-5 objections
7. **CTA**: Restate the offer and primary CTA

## Writing Style
- Short sentences. Active voice. No jargon.
- Remove qualifiers: "very", "really", "quite", "somewhat"
- No exclamation points (they signal desperation)
- Fabricated stats/testimonials are never acceptable — legal liability + trust erosion

## Deliverables
- Full page copy by section
- 2-3 headline alternatives with rationale
- Meta title + meta description
""",
    },
    "cold-email": {
        "category": "content",
        "description": "Write cold outreach emails with high reply rates using proven frameworks.",
        "guidance": """# Cold Email Skill

## Framework: PPPP
- **Problem**: Open with their pain (not your product)
- **Promise**: One-sentence value proposition
- **Proof**: Specific, verifiable evidence
- **Proposal**: Clear, low-friction CTA

## Rules
- Subject line: 2-5 words, curiosity-driven, no spam triggers
- Body: 3-5 sentences max for first email
- One CTA per email (not "or" options)
- Personalisation: at minimum, their name + company + one relevant detail

## Subject Line Templates
- "Quick question about [their challenge]"
- "[Mutual connection] suggested I reach out"
- "[Specific observation about their work]"

## Sequence Structure (5-touch)
1. Initial pitch (value-first)
2. Follow-up: add one new proof point
3. Follow-up: soften ask ("just 10 minutes?")
4. Breakup email ("should I close your file?")
5. Re-engage 30 days later with new angle

## What to Avoid
- "I hope this email finds you well" (delete)
- Long paragraphs about your company's history
- Multiple links or attachments in first email
""",
    },
    "email-sequence": {
        "category": "content",
        "description": "Design multi-email nurture and onboarding sequences.",
        "guidance": """# Email Sequence Design

## Sequence Types
- **Welcome / Onboarding**: 5-7 emails over 14 days for new signups
- **Nurture**: 4-6 emails over 30 days for leads not yet ready to buy
- **Re-engagement**: 3-email sequence for dormant subscribers
- **Post-purchase**: 3-5 emails to reduce churn and drive expansion

## Email Anatomy
| Element | Best Practice |
|---------|--------------|
| Subject | 40 chars max, preview text complements it |
| Preview text | Extends subject, don't repeat it |
| Opening | Acknowledge where they are in the journey |
| Body | One main idea per email |
| CTA | One button, action-oriented label |

## Onboarding Sequence Example
1. Day 0: Welcome + first win (get them to the 'aha' moment)
2. Day 2: Feature highlight #1 (most popular feature)
3. Day 4: Social proof (case study from similar customer)
4. Day 7: Feature highlight #2 + tips
5. Day 10: Overcome common objection
6. Day 14: Upgrade / conversion CTA
""",
    },
    "page-cro": {
        "category": "conversion",
        "description": "Audit and optimise landing pages for conversion rate improvement.",
        "guidance": """# Page CRO Audit

## Conversion Hierarchy
Fix in this order: clarity → relevance → value → friction → trust

## Clarity Checks
- Can a stranger understand what the page offers in 5 seconds?
- Is the primary CTA above the fold?
- Are there competing CTAs confusing visitors?

## Relevance Checks
- Does the headline match the ad / email that sent traffic here?
- Is the content appropriate for the visitor's awareness stage?

## Value Checks
- Is the value proposition specific and differentiated?
- Are benefits stated before features?
- Is there enough social proof (testimonials, logos, numbers)?

## Friction Checks
- Is the form asking for more than necessary?
- How many clicks to complete the primary action?
- Is there friction on mobile (tap targets, load time)?

## Trust Checks
- Are there trust signals near the CTA (security badges, guarantees)?
- Are testimonials attributed to real people with photos?

## Testing Priorities
| Test | Expected Lift |
|------|--------------|
| Headline rewrite | 10-30% |
| CTA button copy | 5-15% |
| Form field reduction | 10-40% |
| Social proof addition | 5-20% |
| Page speed improvement | 5-20% |
""",
    },
    "seo-audit": {
        "category": "seo",
        "description": "Full SEO audit covering technical, on-page, and content factors.",
        "guidance": """# Marketing SEO Audit

## Phase 1: Technical Foundation
- Crawlability: robots.txt, sitemap, no crawl blocks on key pages
- Indexability: canonical tags, no noindex on key pages
- Performance: Core Web Vitals (LCP <2.5s, CLS <0.1, INP <200ms)
- Mobile: responsive design, no content clipped on mobile

## Phase 2: On-Page
- Title tags: unique, keyword-first, 50-60 chars
- Meta descriptions: unique, include CTA, 150-160 chars
- H1: one per page, contains primary keyword
- Content depth: matches or exceeds top competitors for target keywords

## Phase 3: Content Strategy
- Keyword coverage: are all key topics in your ICP's search journey covered?
- Topical authority: do you have cluster content supporting pillar pages?
- Content freshness: pages older than 2 years audited for update need

## Output: Priority Fix List
| Issue | Affected Pages | Impact | Effort | Fix |
""",
    },
    "paid-ads": {
        "category": "paid",
        "description": "Strategy and copy for paid advertising campaigns (Google, Meta, LinkedIn).",
        "guidance": """# Paid Ads Strategy & Copy

## Campaign Structure
- **Google Search**: intent-based; match types, negative keywords, quality score
- **Meta**: audience-based; cold→warm→hot funnel, lookalikes, retargeting
- **LinkedIn**: professional targeting; job title + company size + seniority

## Ad Copy Framework (AIDA)
- **Attention**: hook in first line / headline
- **Interest**: key benefit or proof point
- **Desire**: create urgency or FOMO
- **Action**: specific CTA with low commitment language

## Google Ad Structure
- 3 headlines (max 30 chars each): Keyword | Benefit | CTA
- 2 descriptions (max 90 chars each): expand on benefit + social proof
- Extensions: sitelinks, callouts, structured snippets, location

## Meta Ad Copy
- Hook (first line, no truncation): Bold statement or question
- Body: Pain → Solution → Proof
- CTA button: matches offer (Learn More / Shop Now / Sign Up)

## Testing Framework
Test one variable at a time: hook, audience, offer, format.
Run for minimum 1,000 impressions or 7 days before judging.
""",
    },
    "analytics-tracking": {
        "category": "measurement",
        "description": "Set up conversion tracking and attribution for marketing campaigns.",
        "guidance": """# Analytics & Conversion Tracking Setup

## Essential Events to Track
| Event | Tool | Priority |
|-------|------|----------|
| Page view | GA4 | Must have |
| Signup / registration | GA4 + CRM | Must have |
| Purchase / upgrade | GA4 + payment tool | Must have |
| Demo request / form submit | GA4 | Must have |
| Email open / click | Email platform | Nice to have |
| Trial activation | Product analytics | Must have |

## Attribution Models
- **Last-click**: simple, over-credits bottom-funnel channels
- **First-click**: credits discovery channels (good for brand)
- **Data-driven**: GA4 default; requires sufficient conversion volume
- **Linear**: distributes credit across all touchpoints

## UTM Tagging Convention
`utm_source=google&utm_medium=cpc&utm_campaign=brand-search&utm_content=ad-variant-a`

All paid links must have UTMs. Set a team standard and enforce it.

## Reporting Cadence
- Daily: paid spend and conversion pacing
- Weekly: channel performance vs. targets
- Monthly: full funnel + attribution analysis
""",
    },
    "pricing-strategy": {
        "category": "strategy",
        "description": "Design pricing tiers, anchor points, and value-metric alignment.",
        "guidance": """# Pricing Strategy Framework

## Value Metric Selection
The unit your pricing scales with should correlate directly to customer value:
- Seats (collaboration tools)
- Usage / API calls (infrastructure)
- Revenue % (payment tools)
- Features (project management)
- Contacts (email marketing)

## Tier Architecture
| Tier | Target | Purpose |
|------|--------|---------|
| Free / Freemium | Trial users | Acquisition, viral loop |
| Starter | SMBs | Revenue floor, low touch |
| Pro | Growing teams | Primary revenue driver |
| Enterprise | Large orgs | High ACV, custom contracts |

## Pricing Psychology
- **Anchoring**: show highest tier first (makes middle seem reasonable)
- **Decoy pricing**: add a third option that makes your preferred option look better
- **Charm pricing**: $99 vs $100 (left-digit effect)
- **Annual discount**: 15-20% off to improve retention and cash flow

## Common Mistakes
- Pricing on cost rather than value
- Too many tiers (3 is usually optimal)
- No clear upgrade trigger between tiers
- Annual-only pricing without a monthly entry point
""",
    },
    "launch-strategy": {
        "category": "strategy",
        "description": "Plan and execute a product or feature launch across channels.",
        "guidance": """# Product Launch Strategy

## Launch Tiers
- **Tier 1 (Major)**: New product / major feature — full campaign
- **Tier 2 (Notable)**: Significant improvement — blog + email + social
- **Tier 3 (Minor)**: Bug fix / small feature — changelog + in-app notification

## Tier 1 Launch Checklist

### Pre-Launch (4 weeks out)
- [ ] Messaging doc: positioning, key benefits, proof points
- [ ] Landing page live with waitlist / early access CTA
- [ ] Email sequence written (announcement + follow-ups)
- [ ] PR outreach to relevant journalists/bloggers
- [ ] Influencer / partner coordination

### Launch Week
- [ ] Email announcement to full list
- [ ] Product Hunt / Hacker News post (if applicable)
- [ ] Social media content calendar live
- [ ] Paid media campaigns activated
- [ ] Customer success briefed on new feature

### Post-Launch (2 weeks)
- [ ] Collect user feedback + testimonials
- [ ] Update docs and help content
- [ ] Analyse adoption metrics vs. launch goals
- [ ] Retrospective and iterate
""",
    },
    "churn-prevention": {
        "category": "retention",
        "description": "Identify at-risk customers and intervene before they cancel.",
        "guidance": """# Churn Prevention Playbook

## Leading Indicators of Churn
- Login frequency drops below baseline
- Feature adoption declining (using fewer features)
- Support tickets increasing
- NPS score drops
- Billing failures / downgrades

## Intervention Playbook

### Low engagement (4+ days no login)
- In-app notification: "Here's what you missed"
- Trigger email: use case tip or success story

### Feature non-adoption (never used key feature)
- In-app tooltip or empty state prompt
- Email: "[Feature] could save you X hours/week"

### High-risk (NPS detractor / multiple support tickets)
- CSM personal outreach within 24 hours
- Executive sponsor check-in for enterprise accounts

## Cancellation Flow
- Show value summary (what they've accomplished)
- Offer pause instead of cancel (for seasonal users)
- Offer downgrade instead of cancel
- Exit survey: capture reason (use to fix product)

## Measurement
- Track churn rate by cohort, plan tier, and acquisition channel
- Set monthly churn targets by segment
""",
    },
}


@mcp.tool()
def list_marketing_skills(category: str = "") -> dict:
    """List available marketing skills, optionally filtered by category.

    Args:
        category: One of 'foundation', 'content', 'conversion', 'seo', 'paid',
                  'measurement', 'strategy', 'retention'. Leave empty for all.
    """
    categories = {"foundation", "content", "conversion", "seo", "paid", "measurement", "strategy", "retention"}

    if category:
        category = category.lower().strip()
        if category not in categories:
            return {"error": f"Unknown category '{category}'", "available_categories": sorted(categories)}
        filtered = {name: s["description"] for name, s in _SKILLS.items() if s["category"] == category}
        return {category: filtered}

    grouped: dict[str, dict] = {}
    for name, skill in _SKILLS.items():
        c = skill["category"]
        grouped.setdefault(c, {})[name] = skill["description"]
    return grouped


@mcp.tool()
def get_marketing_skill(skill_name: str = None) -> dict:
    """Get the full guidance for a specific marketing skill.

    Args:
        skill_name: Skill slug (e.g. 'copywriting', 'page-cro', 'cold-email').
    """
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
    hint = get_presentation_hint('marketing_skills', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@marketing_skills",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'marketing_skills',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }

@mcp.tool()
def get_marketing_workflow(objective: str) -> dict:
    """Get a recommended skill sequence for a marketing objective.

    Args:
        objective: What you're trying to accomplish (e.g. 'launch a new product',
                   'reduce churn', 'increase landing page conversions', 'run paid ads').
    """
    obj = objective.lower()

    if any(w in obj for w in ["launch", "release", "announce"]):
        sequence = ["product-marketing-context", "copywriting", "email-sequence", "paid-ads", "launch-strategy"]
        rationale = "Launch: set context → write copy → email → ads → execute launch plan."
    elif any(w in obj for w in ["churn", "retention", "cancel", "renew"]):
        sequence = ["product-marketing-context", "churn-prevention", "email-sequence"]
        rationale = "Retention: understand context, then deploy churn playbook backed by email sequences."
    elif any(w in obj for w in ["conversion", "landing page", "cro", "convert"]):
        sequence = ["product-marketing-context", "page-cro", "copywriting"]
        rationale = "CRO: audit the page for friction, then rewrite copy based on findings."
    elif any(w in obj for w in ["email", "outreach", "cold"]):
        sequence = ["product-marketing-context", "cold-email", "email-sequence"]
        rationale = "Email: ICP context first, then build cold outreach and nurture sequence."
    elif any(w in obj for w in ["seo", "search", "organic", "content"]):
        sequence = ["product-marketing-context", "seo-audit", "copywriting"]
        rationale = "SEO: audit current state, then produce optimised content with product context."
    elif any(w in obj for w in ["paid", "ads", "ppc", "advertising"]):
        sequence = ["product-marketing-context", "paid-ads", "analytics-tracking"]
        rationale = "Paid: set context, write ads, ensure tracking is in place before spend."
    else:
        sequence = ["product-marketing-context", "copywriting", "analytics-tracking", "launch-strategy"]
        rationale = "General marketing: foundation → messaging → measurement → launch."

    return {
        "objective": objective,
        "recommended_sequence": sequence,
        "rationale": rationale,
        "note": "Always start with product-marketing-context before any other skill.",
        "tip": "Call get_marketing_skill() with each skill name to get the full guidance.",
    }
