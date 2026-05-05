"""SEO & GEO Skills — 20 skills across 4 execution phases for search optimization.

Source: https://github.com/aaron-he-zhu/seo-geo-claude-skills (MIT)
"""

from fastmcp import FastMCP

from core.skill_config import get_presentation_hint

mcp = FastMCP("seo-geo")
_SKILL_NAME = "seo_geo"

_SKILLS: dict[str, dict] = {
    "keyword-research": {
        "phase": "research",
        "description": "Identify high-value keywords using seed terms, competitor analysis, and search intent classification.",
        "guidance": """# Keyword Research

## Objective
Find keywords with strong commercial intent, manageable competition, and clear user need.

## Process
1. **Seed expansion** — Start with 3-5 seed terms, expand via autocomplete, related searches, and 'People Also Ask'.
2. **Intent classification** — Label each keyword: Informational / Commercial / Transactional / Navigational.
3. **Competition assessment** — Check top-10 SERP DR, content depth, and freshness.
4. **Volume signals** — Use Google Trends, autocomplete frequency, and SERP ad presence as proxies.
5. **Long-tail mining** — Extract 3-5 word phrases; lower competition, higher conversion.

## Output Format
| Keyword | Intent | Est. Volume | Competition | Priority |
|---------|--------|------------|-------------|----------|

## Prioritization
- High: Transactional + low DR competitors + trend upward
- Medium: Commercial + medium competition + stable trend
- Low: Informational + high competition (build for topical authority)
""",
    },
    "competitor-analysis": {
        "phase": "research",
        "description": "Map competitor content gaps, backlink profiles, and ranking patterns.",
        "guidance": """# Competitor SEO Analysis

## Steps
1. Identify top 3-5 organic competitors (not paid) for your target keywords.
2. Audit their top pages: URL structure, title patterns, content depth.
3. Run content gap analysis: keywords they rank for that you don't.
4. Assess backlink profile: DR, referring domains, anchor text distribution.
5. Note SERP feature wins: featured snippets, People Also Ask, image packs.

## Output
- Competitor keyword gap list
- Content opportunity matrix (topic × competitor coverage)
- Backlink acquisition targets
""",
    },
    "serp-analysis": {
        "phase": "research",
        "description": "Analyse SERP composition to understand what Google rewards for a query.",
        "guidance": """# SERP Analysis

## What to Examine
- **Top-10 content types**: blog posts, product pages, videos, tools, listicles
- **Content length**: average word count of ranking pages
- **Freshness signals**: publication / update dates in snippets
- **SERP features**: featured snippet format, PAA questions, local pack, image results
- **Brand dominance**: % of results from authoritative brands

## Implications
- Match the dominant content type — if top results are listicles, publish a listicle.
- Match depth — thin content won't outrank comprehensive guides.
- Target featured snippet format (paragraph, list, or table).
""",
    },
    "content-gap-analysis": {
        "phase": "research",
        "description": "Find topics competitors cover that your site doesn't — ranked by opportunity.",
        "guidance": """# Content Gap Analysis

## Process
1. Export your ranking keywords and competitors' ranking keywords.
2. Find set difference: competitor keywords − your keywords.
3. Filter by intent and volume signals.
4. Group by topic cluster.
5. Prioritize by: business relevance × search demand × content creation cost.

## Output: Opportunity Matrix
| Topic Cluster | Gap Keywords | Priority | Recommended Content Type |
""",
    },
    "seo-content-writer": {
        "phase": "build",
        "description": "Write SEO-optimised content that serves both search engines and readers.",
        "guidance": """# SEO Content Writing

## Pre-Writing Checklist
- [ ] Primary keyword confirmed
- [ ] Secondary/LSI keywords identified
- [ ] Target content type and format chosen (based on SERP analysis)
- [ ] Competitor content reviewed for depth benchmark

## Writing Rules
- **Title**: Primary keyword near start, under 60 chars, compelling hook.
- **H1**: Matches or closely mirrors title.
- **Introduction**: Answer the query in the first 100 words (featured snippet bait).
- **H2/H3 structure**: Use secondary keywords naturally in subheadings.
- **Keyword density**: 1-2% primary keyword; no stuffing.
- **Internal links**: 3-5 relevant internal links with descriptive anchor text.
- **External links**: 2-3 authoritative sources to support claims.
- **Conclusion**: Summarise, include a CTA, and optionally re-answer the query.

## GEO Optimisation (Generative Engine Optimisation)
For AI search (Perplexity, ChatGPT, Gemini) visibility:
- Use clear, factual statements that can be cited.
- Include statistics with source citations.
- Structure content with defined entities (who, what, when, where).
- Write in third-person declarative style for key facts.
""",
    },
    "geo-content-optimizer": {
        "phase": "build",
        "description": "Optimise existing content for visibility in AI-generated answers (GEO).",
        "guidance": """# GEO Content Optimisation

## GEO vs SEO
- SEO = ranking in blue-link results
- GEO = being cited or summarised in AI-generated answers (Perplexity, ChatGPT, Google AI Overview)

## Optimisation Tactics
1. **Entity clarity**: Name your product, company, people, and places explicitly. Avoid vague pronouns.
2. **Fact density**: Include specific numbers, dates, and verifiable claims with citations.
3. **Quote-ready sentences**: Write 1-2 sentence summaries of key points that AI can lift verbatim.
4. **Structured data**: Add FAQ, HowTo, or Article schema to help AI parse your content.
5. **Authority signals**: Link to and be linked from authoritative sources in your topic area.
6. **Freshness**: Update statistics and dates — AI prefers recent, accurate information.
""",
    },
    "meta-tags-optimizer": {
        "phase": "build",
        "description": "Write compelling title tags and meta descriptions that maximise CTR.",
        "guidance": """# Meta Tags Optimisation

## Title Tag Rules
- Length: 50-60 characters (Google truncates at ~600px / ~60 chars)
- Include primary keyword near the start
- Add a differentiator: year, number, power word
- Format: [Primary Keyword] — [Benefit/Hook] | [Brand]

## Meta Description Rules
- Length: 150-160 characters
- Include primary keyword (Google bolds it in SERPs)
- One clear CTA: Learn, Discover, Get, Compare
- Reflect the page content exactly (avoid bait-and-switch)

## Examples
**Good title**: "Amazon Keyword Research: 7 Free Methods (2024) | ToolName"
**Good meta**: "Find high-converting Amazon keywords without paid tools. Step-by-step guide covering autocomplete, competitor ASINs, and long-tail mining."
""",
    },
    "schema-markup-generator": {
        "phase": "build",
        "description": "Generate JSON-LD schema markup for rich SERP features.",
        "guidance": """# Schema Markup Generation

## Common Schema Types
| Page Type | Schema | Rich Feature |
|-----------|--------|-------------|
| Blog post | Article | Byline, date |
| FAQ page | FAQPage | Expandable Q&A in SERP |
| How-to guide | HowTo | Step cards |
| Product page | Product | Stars, price, availability |
| Local business | LocalBusiness | Map pack |
| Recipe | Recipe | Cook time, calories |

## Implementation
Add JSON-LD in <script type="application/ld+json"> block in <head>.
Validate at: https://search.google.com/test/rich-results

## FAQ Schema Example
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "What is keyword research?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Keyword research is the process of finding search terms..."
    }
  }]
}
```
""",
    },
    "on-page-seo-auditor": {
        "phase": "optimize",
        "description": "Audit a page against 30+ on-page SEO factors and produce a prioritised fix list.",
        "guidance": """# On-Page SEO Audit

## Audit Checklist

### Technical On-Page
- [ ] Title tag: length, keyword placement, uniqueness
- [ ] Meta description: length, keyword, CTA
- [ ] H1: one per page, contains primary keyword
- [ ] URL: short, keyword-rich, hyphens not underscores
- [ ] Canonical tag: present and correct
- [ ] Image alt text: descriptive, keyword where natural

### Content Quality
- [ ] Matches search intent (informational / commercial / transactional)
- [ ] Comprehensive coverage vs. top-ranking competitors
- [ ] Reading level appropriate for audience
- [ ] No thin content (<300 words for informational pages)
- [ ] Internal links: 3-5 with descriptive anchors
- [ ] External links: 2-3 authoritative sources

### Core Web Vitals
- [ ] LCP < 2.5s
- [ ] CLS < 0.1
- [ ] INP < 200ms

## Output: Priority Fix List
| Issue | Impact | Effort | Fix |
""",
    },
    "technical-seo-checker": {
        "phase": "optimize",
        "description": "Identify crawlability, indexability, and site structure issues.",
        "guidance": """# Technical SEO Checklist

## Crawl & Index
- [ ] robots.txt not blocking key pages
- [ ] Sitemap submitted to Google Search Console
- [ ] No orphan pages (all pages reachable via internal links)
- [ ] Crawl budget not wasted on paginated / filtered URLs

## Site Structure
- [ ] URL depth ≤ 3 clicks from homepage for key pages
- [ ] Breadcrumb navigation present
- [ ] No redirect chains (A→B→C; use A→C directly)
- [ ] 404 errors resolved or redirected

## Mobile & Performance
- [ ] Mobile-responsive
- [ ] Core Web Vitals passing (LCP, CLS, INP)
- [ ] HTTPS across all pages

## Structured Data
- [ ] No schema validation errors
- [ ] Rich results eligible pages implemented
""",
    },
    "internal-linking-optimizer": {
        "phase": "optimize",
        "description": "Build a strategic internal linking structure to distribute PageRank and improve crawlability.",
        "guidance": """# Internal Linking Strategy

## Principles
- Link from high-authority pages to pages you want to rank.
- Use descriptive, keyword-rich anchor text (not 'click here').
- Aim for 3-5 internal links per page.
- Prioritise links from pages closest to the homepage (lower click depth).

## Pillar-Cluster Model
1. Create a **pillar page** covering a broad topic comprehensively.
2. Create **cluster pages** covering subtopics in depth.
3. Link cluster pages to the pillar and vice versa.
4. Cross-link related cluster pages.

## Audit Steps
1. Map all pages and their current internal link counts.
2. Identify orphan pages (0 internal links pointing to them).
3. Identify high-value pages with few inbound internal links.
4. Add contextual links from relevant existing content.
""",
    },
    "content-refresher": {
        "phase": "optimize",
        "description": "Update existing content to recapture lost rankings and improve freshness signals.",
        "guidance": """# Content Refresh Process

## When to Refresh
- Rankings dropped in past 3-6 months
- Content references outdated stats/dates
- Competitors have published more comprehensive pieces
- Core Web Vitals failing

## Refresh Checklist
1. Update all statistics with current data + source links.
2. Add new sections covering gaps vs. current top competitors.
3. Remove outdated sections or tools.
4. Update publish date to today (only if substantial changes made).
5. Add new internal links to recently published related content.
6. Re-optimise title and meta for current SERP format.
7. Add or update schema markup.

## What NOT to Do
- Don't change the URL (301 redirect if essential).
- Don't remove content that still drives traffic.
- Don't change the primary keyword without a redirect strategy.
""",
    },
    "rank-tracker": {
        "phase": "monitor",
        "description": "Set up systematic rank tracking and interpret position changes.",
        "guidance": """# Rank Tracking Setup

## What to Track
- Primary target keywords (1 per page)
- Secondary/supporting keywords (2-4 per page)
- Brand keywords
- Competitor comparison keywords

## Tracking Cadence
- Weekly for high-priority keywords
- Monthly for long-tail / informational keywords

## Interpreting Changes
| Signal | Possible Cause |
|--------|---------------|
| Sudden drop 10+ positions | Algorithm update, manual action, technical issue |
| Gradual decline over weeks | Competitor gaining authority, content freshness loss |
| Fluctuation ±3 positions | Normal SERP volatility |
| Sudden jump | New backlink, content refresh indexed |

## Tools (No API Key Required)
- Google Search Console (free, 16 months data)
- Google Trends (volume signals)
- Manual SERP check in incognito mode
""",
    },
    "backlink-analyzer": {
        "phase": "monitor",
        "description": "Audit backlink profile quality and identify toxic or lost links.",
        "guidance": """# Backlink Analysis

## Metrics to Review
- **Total referring domains** (unique domains, not total links)
- **Domain Rating / Authority** distribution
- **Anchor text distribution**: branded vs. keyword vs. generic
- **Link velocity**: rate of new links over time
- **Lost links**: previously acquired links now returning 404 or removed

## Red Flags
- High % of exact-match keyword anchors (over-optimisation)
- Links from unrelated / low-quality domains
- Sudden spike in links (potential negative SEO or link scheme)

## Action Items
1. Disavow toxic links via Google Search Console disavow tool.
2. Reclaim lost links by contacting webmasters or fixing broken pages.
3. Identify link patterns from competitors to find similar acquisition opportunities.
""",
    },
    "performance-reporter": {
        "phase": "monitor",
        "description": "Generate a structured SEO performance report from available data.",
        "guidance": """# SEO Performance Report Template

## Executive Summary
- Overall organic traffic trend (MoM, YoY)
- Top 3 wins this period
- Top 3 concerns or opportunities

## Traffic Metrics
| Metric | This Period | Last Period | Change |
|--------|------------|------------|--------|
| Organic sessions | | | |
| Organic conversions | | | |
| Top landing pages | | | |

## Rankings
- Keywords improved: list top movers
- Keywords declined: list top fallers
- New keywords entering top 10

## Technical Health
- Crawl errors resolved / new errors
- Core Web Vitals status
- Index coverage changes

## Next Steps
1. [Priority action]
2. [Priority action]
3. [Priority action]
""",
    },
    "alert-manager": {
        "phase": "monitor",
        "description": "Define alert thresholds for SEO anomalies and create monitoring workflows.",
        "guidance": """# SEO Alert Thresholds

## Recommended Alerts

| Metric | Alert Threshold | Check Frequency |
|--------|----------------|-----------------|
| Organic traffic | Drop >20% WoW | Weekly |
| Core Web Vitals | Any metric fails | Daily |
| Crawl errors | >50 new 404s | Daily |
| Index coverage | Drop >5% | Weekly |
| Top keyword ranking | Drop >5 positions | Weekly |
| Backlinks | Sudden +100 or -50 | Weekly |

## Alert Channels
- Google Search Console email alerts (built-in)
- Google Analytics anomaly detection
- Manual weekly dashboard review

## Triage Process
1. Confirm the anomaly is real (not a tracking issue).
2. Check if it correlates with a known event (deploy, algorithm update).
3. Identify affected pages.
4. Implement fix within 48 hours for critical drops.
""",
    },
}


@mcp.tool()
def list_seo_skills(phase: str = "") -> dict:
    """List available SEO/GEO skills, optionally filtered by phase.

    Args:
        phase: One of 'research', 'build', 'optimize', 'monitor'. Leave empty for all.
    """
    if phase:
        phase = phase.lower().strip()
        filtered = {name: {"phase": s["phase"], "description": s["description"]}
                    for name, s in _SKILLS.items() if s["phase"] == phase}
        if not filtered:
            return {"error": f"Unknown phase '{phase}'", "available_phases": ["research", "build", "optimize", "monitor"]}
        return {phase: filtered}

    grouped: dict[str, dict] = {}
    for name, skill in _SKILLS.items():
        p = skill["phase"]
        grouped.setdefault(p, {})[name] = skill["description"]
    return grouped


@mcp.tool()
def get_seo_skill(skill_name: str = None) -> dict:
    """Get the full guidance for a specific SEO/GEO skill.

    Args:
        skill_name: Skill slug (e.g. 'keyword-research', 'seo-content-writer').
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
    hint = get_presentation_hint('seo_geo', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@seo_geo",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'seo_geo',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }

@mcp.tool()
def get_seo_workflow(goal: str) -> dict:
    """Get a recommended skill sequence for a given SEO goal.

    Args:
        goal: What you're trying to accomplish (e.g. 'write a new article',
              'audit an existing page', 'track rankings', 'find keywords').
    """
    goal_lower = goal.lower()

    if any(w in goal_lower for w in ["new article", "write content", "create post", "new page"]):
        sequence = ["keyword-research", "serp-analysis", "seo-content-writer", "meta-tags-optimizer", "schema-markup-generator"]
        rationale = "New content: research first, then build with correct format and metadata."
    elif any(w in goal_lower for w in ["audit", "existing", "refresh", "update"]):
        sequence = ["on-page-seo-auditor", "competitor-analysis", "content-refresher", "internal-linking-optimizer"]
        rationale = "Content refresh: audit gaps, compare competitors, then update."
    elif any(w in goal_lower for w in ["keyword", "research", "find topic"]):
        sequence = ["keyword-research", "serp-analysis", "content-gap-analysis", "competitor-analysis"]
        rationale = "Keyword/topic research: full research phase before building anything."
    elif any(w in goal_lower for w in ["monitor", "track", "report", "rank"]):
        sequence = ["rank-tracker", "backlink-analyzer", "performance-reporter", "alert-manager"]
        rationale = "Monitoring setup: establish tracking before setting alerts."
    elif any(w in goal_lower for w in ["technical", "crawl", "index", "site"]):
        sequence = ["technical-seo-checker", "on-page-seo-auditor", "internal-linking-optimizer"]
        rationale = "Technical audit: start with crawl health, then on-page, then structure."
    else:
        sequence = ["keyword-research", "serp-analysis", "seo-content-writer", "on-page-seo-auditor", "rank-tracker"]
        rationale = "General SEO workflow: full cycle from research to monitoring."

    return {
        "goal": goal,
        "recommended_sequence": sequence,
        "rationale": rationale,
        "tip": "Call get_seo_skill() for each skill name to get the full guidance.",
    }
