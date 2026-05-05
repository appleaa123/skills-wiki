"""eCommerce Skills — 86+ skills across Amazon, Shopify, Etsy, TikTok Shop, eBay, Walmart.

Source: https://github.com/nexscope-ai/eCommerce-Skills (MIT)
29 production-ready skills, 57 in beta.
"""

from fastmcp import FastMCP

from core.skill_config import get_presentation_hint

mcp = FastMCP("ecommerce-skills")
_SKILL_NAME = "ecommerce_skills"

_SKILLS: dict[str, dict] = {
    # Product Research
    "ecommerce-keyword-research": {
        "category": "product-research",
        "platforms": ["amazon", "shopify", "etsy", "google-shopping", "tiktok-shop", "walmart"],
        "status": "production",
        "description": "Cross-platform keyword research identifying high-converting search terms.",
        "guidance": """# eCommerce Keyword Research (Cross-Platform)

## Platform Differences

| Platform | Algorithm Focus | Keyword Priority |
|----------|----------------|-----------------|
| Amazon | Purchase intent + conversion rate | Exact match in title + bullets |
| Shopify/Site | Google SEO + user intent | Long-tail informational + commercial |
| Etsy | Niche + handmade language | Descriptive, style-based phrases |
| TikTok Shop | Trending + hashtag hybrid | Short, viral-friendly terms |
| Walmart | Amazon-like but less competition | Similar to Amazon approach |

## Research Process
1. **Gather context**: product type, target buyer, primary platform
2. **Seed keyword expansion**: platform autocomplete + related searches
3. **Intent mapping**: purchase-ready / research / discovery
4. **Competition check**: top results count, ad density, listing quality
5. **Seasonality**: Google Trends 12-month + platform-specific trends
6. **Long-tail mining**: 3-5 word phrases with commercial intent

## Output
- Platform-specific keyword list with intent labels
- Competition assessment per keyword
- Priority ranking (HIGH/MEDIUM/LOW)
- Seasonal opportunity flags
""",
    },
    "product-opportunity-finder": {
        "category": "product-research",
        "platforms": ["amazon", "etsy", "shopify"],
        "status": "production",
        "description": "Identify underserved niches and white-space product opportunities.",
        "guidance": """# Product Opportunity Finder

## Opportunity Signals
1. **Demand without supply**: Many searches, few good listings
2. **High BSR with low reviews**: Selling well despite poor social proof
3. **Rising trend**: Google Trends up >20% YoY; new hashtag gaining traction
4. **Price clustering gap**: Products at $10-15 and $40-50, but nothing at $20-30
5. **Weak review quality**: Competitors have 3.5★ or lower — you can do better

## Evaluation Framework (Score each 1-5)

| Criterion | Weight | Notes |
|-----------|--------|-------|
| Search demand | 30% | Volume signals on target platform |
| Competition level | 25% | Fewer, weaker competitors = better |
| Margin potential | 25% | Selling price vs. landed cost |
| Differentiation path | 20% | Can you make it meaningfully better? |

## Minimum Thresholds (Amazon)
- BSR in target category: <50,000
- Review count of #1 seller: <500 (easier to compete)
- Target selling price: $20-$80 (FBA economics work best)
- Estimated monthly sales: >200 units

## Red Flags
- Dominated by one large brand (>40% of page 1)
- Patent-protected designs
- Seasonal only (< 3 months demand per year)
- Regulated/restricted category
""",
    },
    "competitor-price-analysis": {
        "category": "competitor-analysis",
        "platforms": ["amazon", "shopify", "etsy", "ebay", "walmart"],
        "status": "production",
        "description": "Map competitor pricing, promotions, and positioning across platforms.",
        "guidance": """# Competitor Price Analysis

## Data Points to Collect
For each top competitor:
- Current price (regular + sale)
- Price history (has it changed in past 90 days?)
- Bundle / variation pricing
- Shipping cost (if applicable)
- Promotional cadence (how often do they run sales?)

## Pricing Strategy Signals

| Observation | Implication |
|-------------|-------------|
| All competitors within 10% of each other | Price-competitive market; compete on value/brand |
| Wide price range ($15-$80 for same product) | Price = quality signal; premium positioning viable |
| Frequent sales/coupons | Race to bottom; consider value-add instead |
| Few competitors with high prices | Opportunity to undercut profitably |

## Output: Competitive Price Map
| Competitor | Price | BSR/Reviews | Strengths | Weaknesses |
|------------|-------|------------|-----------|------------|

## Recommended Positioning
- **Penetration**: Price 10-15% below market average to gain initial reviews
- **Parity**: Price at market average once you have 50+ reviews
- **Premium**: Price 20-30% above average only with clear differentiator
""",
    },
    "listing-title-optimizer": {
        "category": "listing-optimization",
        "platforms": ["amazon", "etsy", "walmart", "ebay"],
        "status": "production",
        "description": "Write keyword-optimised, conversion-focused product titles per platform.",
        "guidance": """# Product Title Optimisation

## Title Formulas by Platform

### Amazon
`[Brand] [Primary Keyword] [Key Attribute 1] [Key Attribute 2] [Pack Size/Variant] - [Benefit]`
- Max 200 chars; Amazon displays ~80 on mobile
- Primary keyword as close to start as possible
- Avoid: ALL CAPS, promotional claims, subjective claims ("best")

### Etsy
`[Descriptor] [Primary Keyword] - [Style/Material] [Use Case] [Gift Occasion]`
- Max 140 chars
- Lead with what it IS, not your brand
- Include gift occasions (e.g. "Birthday Gift for Mom")

### Walmart
Similar to Amazon; Brand name usually comes first per Walmart policy.

### eBay
`[Brand] [Model/SKU] [Primary Keyword] [Key Specs] [Condition]`
- Max 80 chars; include model number for electronics
- Include condition (New, Used, Refurbished) if relevant

## Universal Rules
- No keyword stuffing — titles must read naturally
- Include size, color, quantity if variations exist
- Test alternative titles on poor-performing listings (A/B if platform supports)
""",
    },
    "shopify-seo": {
        "category": "listing-optimization",
        "platforms": ["shopify"],
        "status": "production",
        "description": "Optimise Shopify store and product pages for Google organic search.",
        "guidance": """# Shopify SEO Optimisation

## Store-Level SEO
- **Homepage title**: Brand | Category | Primary keyword
- **Navigation**: keyword-rich category names (not "Collection 1")
- **URL structure**: /collections/[category] → /products/[descriptive-slug]
- **Site speed**: Compress images, limit apps, use a fast theme

## Product Page SEO
- **Title tag**: Primary keyword first | Brand (50-60 chars)
- **Meta description**: Benefit + keyword + CTA (150-160 chars)
- **H1**: Match product title exactly
- **Product description**: 200+ words; natural keyword integration; benefits-first
- **Image alt text**: Descriptive + keyword where natural (not keyword stuffing)

## Collection Page SEO
- Add 150-300 word collection description at top
- Use keyword-rich H1 for the collection name
- Internal links from blog posts to collection pages

## Technical Checklist
- [ ] Submit sitemap to Google Search Console
- [ ] Fix broken links (404 pages)
- [ ] Enable canonical tags (Shopify does this by default)
- [ ] Add structured data (Product schema) — use a schema app
- [ ] Check mobile speed score in PageSpeed Insights
""",
    },
    "etsy-seo": {
        "category": "listing-optimization",
        "platforms": ["etsy"],
        "status": "production",
        "description": "Optimise Etsy listings for Etsy search and Google Shopping.",
        "guidance": """# Etsy SEO Optimisation

## Etsy Search Algorithm Factors
1. **Relevancy**: How well your title + tags match the search query
2. **Recency**: New listings get a temporary boost
3. **Conversion rate**: Higher CVR = better ranking over time
4. **Customer & Market Experience (CME)**: Reviews, shipping speed, shop policies

## Title Optimisation
- Use all 140 characters
- Front-load the most important keywords
- Include occasion keywords: "Birthday Gift", "Wedding", "Christmas"
- Separate concepts with commas, hyphens, or spaces (not pipes)

## Tag Strategy (13 tags × 20 chars each)
- Use all 13 tags — leaving any blank is wasted opportunity
- Match tags to phrases customers actually search
- Include: materials, style, occasion, recipient, size, color, technique
- Don't repeat exact title phrases — use variations and synonyms

## Description (for Google Shopping)
- First 160 chars appear in Google Shopping snippets
- Include primary keyword in first sentence
- Describe materials, dimensions, and use cases specifically

## Etsy-Specific Tips
- Refresh listings every 90 days (small boost from recency)
- Run Etsy Ads at $1-3/day to collect click data; pause low-performers
- Free shipping on orders $35+ often improves Etsy search ranking
""",
    },
    "amazon-fba-profit-calculator": {
        "category": "pricing-profitability",
        "platforms": ["amazon"],
        "status": "production",
        "description": "Platform-specific FBA profit analysis (use amazon_skills/calculate_fba_fees for full computation).",
        "guidance": "For full FBA fee calculation, use the amazon_skills skill which has an integrated calculate_fba_fees() tool with 2024 rates.",
    },
    "shopify-profit-calculator": {
        "category": "pricing-profitability",
        "platforms": ["shopify"],
        "status": "production",
        "description": "Shopify profit calculation accounting for Shopify fees, payment processing, and shipping.",
        "guidance": """# Shopify Profit Calculator

## Fee Structure

| Plan | Monthly Fee | Transaction Fee | CC Processing |
|------|------------|----------------|--------------|
| Basic | $39 | 2% (without Shopify Payments) | 2.9% + 30¢ |
| Shopify | $105 | 1% | 2.6% + 30¢ |
| Advanced | $399 | 0.5% | 2.4% + 30¢ |

Note: Transaction fee waived when using Shopify Payments.

## Profit Formula
Net Profit = Revenue − COGS − Shopify Fee (monthly ÷ units) − Payment Processing − Shipping − Returns − Ad Spend

## Example
- Selling price: $45
- COGS: $12
- Shopify plan share: $1.05 (105 orders/month on Shopify plan)
- Payment processing: $1.47 (2.6% + 30¢)
- Shipping: $5.50
- **Gross Profit: $25.98 (57.7% margin)**

## Rules of Thumb
- Target 40-60% gross margin before ad spend
- Ad spend typically 15-25% of revenue for DTC brands
- Net profit target: 10-20% for healthy eCommerce business
""",
    },
    "google-shopping-ads": {
        "category": "advertising",
        "platforms": ["shopify", "woocommerce"],
        "status": "production",
        "description": "Set up and optimise Google Shopping campaigns for eCommerce stores.",
        "guidance": """# Google Shopping Campaigns

## Campaign Structure
```
Performance Max (primary) — let Google optimise across surfaces
  + Asset Group per product category
  + High-quality product images, titles, descriptions in feed

Standard Shopping (control) — manual bidding, more granular control
  + Campaign per product category or margin tier
  + Ad Group per product type
```

## Product Feed Optimisation (Critical)
The feed is your "ad" — Google uses it to match your products to searches.
- **Title**: Primary keyword + key attributes (color, size, material)
- **Description**: 500-5000 chars; benefit-focused; includes keywords naturally
- **Category**: Use Google's taxonomy (not your own categories)
- **Images**: White background preferred for standard, lifestyle for PMax
- **Price**: Must match landing page price exactly
- **GTIN/MPN**: Add for all products — improves eligibility for Shopping results

## Bidding Strategy
- Launch with Target ROAS (2-4× depending on margins)
- New campaigns: Start with Maximize Clicks to gather data (2-4 weeks)
- Optimise with Target ROAS once 30+ conversions/month accumulated

## Key Metrics
- **ROAS**: Target 3-5× for 30-40% margin products
- **CTR**: 0.5-2% is typical for Shopping; below 0.3% = feed quality issue
- **Impression Share**: Target >60% for core products
""",
    },
    "email-marketing-ecommerce": {
        "category": "ecommerce-marketing",
        "platforms": ["shopify", "woocommerce", "amazon"],
        "status": "production",
        "description": "eCommerce email flows: welcome, abandoned cart, post-purchase, win-back.",
        "guidance": """# eCommerce Email Marketing Flows

## Essential Automated Flows

### 1. Welcome Series (3 emails)
- Email 1 (immediate): Welcome + brand story + bestseller highlight
- Email 2 (day 3): Social proof (reviews, UGC) + 10% first order discount
- Email 3 (day 7): Product education or use-case guide

### 2. Abandoned Cart (3 emails)
- Email 1 (1 hour): "You left something behind" — show cart contents
- Email 2 (24 hours): Address objections (returns policy, reviews)
- Email 3 (72 hours): Urgency or small incentive (5-10% off)
Average recovery rate: 5-10% of abandoned carts

### 3. Post-Purchase (3 emails)
- Email 1 (immediate): Order confirmation + shipping timeline
- Email 2 (day 3 after delivery): How to get the best results from your purchase
- Email 3 (day 14): Review request + next purchase recommendation

### 4. Win-Back (3 emails)
- Email 1 (90 days inactive): "We miss you" — best-of content
- Email 2 (105 days): Strong offer (15-20% off)
- Email 3 (120 days): "Last chance" before unsubscribe

## Key Metrics
| Flow | Benchmark Open Rate | Benchmark CVR |
|------|--------------------|-----------|
| Welcome | 50-60% | 3-5% |
| Abandoned Cart | 40-50% | 5-10% |
| Post-Purchase | 60-70% | 2-5% |
| Win-Back | 25-35% | 1-3% |
""",
    },
    "conversion-rate-optimization": {
        "category": "operations-analytics",
        "platforms": ["shopify", "woocommerce"],
        "status": "production",
        "description": "Systematic CRO for eCommerce: product page, cart, and checkout optimisation.",
        "guidance": """# eCommerce CRO Playbook

## Conversion Funnel Benchmarks
| Step | Benchmark CVR | If Below |
|------|--------------|----------|
| Product page → Add to Cart | 3-5% | Fix images, description, price |
| Add to Cart → Checkout | 40-60% | Reduce friction, add trust signals |
| Checkout → Purchase | 60-80% | Simplify form, add payment options |
| Overall store CVR | 1.5-3.5% | Focus on highest drop-off step |

## Product Page Optimisation
- Hero image: product on white + lifestyle image (first 2 slots)
- Price: show savings vs. MSRP or single-unit vs. bundle
- Reviews: show star rating + count near the title
- Description: bullets first (benefits), then full description below fold
- Urgency: real stock scarcity ("Only 8 left") — never fake
- Social proof: UGC photos, review snippets, media logos

## Checkout Optimisation
- Guest checkout option (required)
- Show trust badges near payment (SSL, secure checkout, return policy)
- Progress indicator for multi-step checkouts
- Autofill-friendly form fields
- Offer multiple payment methods (card, PayPal, Apple/Google Pay, BNPL)

## A/B Testing Priority
1. Product images (highest impact, easiest to test)
2. Price / bundle presentation
3. CTA button copy and colour
4. Review placement and format
5. Shipping threshold messaging
""",
    },
    "inventory-management": {
        "category": "supply-chain",
        "platforms": ["amazon", "shopify", "walmart"],
        "status": "production",
        "description": "Inventory planning, reorder point calculation, and stockout prevention.",
        "guidance": """# Inventory Management

## Key Formulas

### Reorder Point
Reorder Point = (Average Daily Sales × Lead Time in Days) + Safety Stock

### Safety Stock
Safety Stock = Z-score × √Lead Time × Standard Deviation of Daily Sales
- Z = 1.65 for 95% service level
- Z = 2.05 for 98% service level

### Economic Order Quantity (EOQ)
EOQ = √(2 × Annual Demand × Order Cost / Holding Cost per Unit per Year)

## Example
- Daily sales: 20 units
- Lead time: 30 days
- Safety stock: 150 units (5-day buffer)
- Reorder point: 20 × 30 + 150 = **750 units**

## Amazon FBA-Specific
- FBA IPI score: keep above 450 to avoid storage limits
- Avoid long-term storage fees: audit every 6 months for slow-movers
- Inbound shipment lead time: add 7-14 days to manufacturer lead time for processing
- Peak season (Q4): order 3-4 months in advance; FBA storage restrictions apply

## Stockout Prevention
- Set reorder alerts in inventory management system
- For fast-movers: maintain 60-90 days of inventory
- For slow-movers: 30-45 days; use FBM as backup for stockouts
""",
    },
}


@mcp.tool()
def list_ecommerce_skills(
    category: str = "",
    platform: str = "",
    status: str = "",
) -> dict:
    """List available eCommerce skills with optional filters.

    Args:
        category: Filter by category (e.g. 'product-research', 'listing-optimization',
                  'pricing-profitability', 'advertising', 'ecommerce-marketing',
                  'operations-analytics', 'supply-chain', 'competitor-analysis').
        platform: Filter by platform (e.g. 'amazon', 'shopify', 'etsy', 'tiktok-shop',
                  'walmart', 'ebay').
        status: Filter by 'production' or 'beta'.
    """
    results = {}
    for name, skill in _SKILLS.items():
        if category and skill["category"] != category.lower().strip():
            continue
        if platform and platform.lower().strip() not in skill["platforms"]:
            continue
        if status and skill["status"] != status.lower().strip():
            continue
        results[name] = {
            "category": skill["category"],
            "platforms": skill["platforms"],
            "status": skill["status"],
            "description": skill["description"],
        }

    if not results:
        return {
            "message": "No skills matched filters",
            "available_categories": sorted({s["category"] for s in _SKILLS.values()}),
            "available_platforms": sorted({p for s in _SKILLS.values() for p in s["platforms"]}),
        }
    return results


@mcp.tool()
def get_ecommerce_skill(skill_name: str = None) -> dict:
    """Get the full guidance for a specific eCommerce skill.

    Args:
        skill_name: Skill slug (e.g. 'ecommerce-keyword-research', 'shopify-seo', 'etsy-seo').
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
    hint = get_presentation_hint('ecommerce_skills', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@ecommerce_skills",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'ecommerce_skills',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }

@mcp.tool()
def get_ecommerce_workflow(platform: str, goal: str) -> dict:
    """Get a recommended skill sequence for a specific platform and goal.

    Args:
        platform: Target platform (e.g. 'amazon', 'shopify', 'etsy', 'tiktok-shop').
        goal: What you're trying to accomplish (e.g. 'launch a product', 'increase conversions',
              'find a product to sell', 'reduce inventory risk').
    """
    platform_lower = platform.lower().strip()
    goal_lower = goal.lower()

    platform_sequences: dict[str, dict[str, list[str]]] = {
        "amazon": {
            "launch": ["ecommerce-keyword-research", "product-opportunity-finder", "listing-title-optimizer", "email-marketing-ecommerce"],
            "convert": ["listing-title-optimizer", "competitor-price-analysis", "conversion-rate-optimization"],
            "research": ["ecommerce-keyword-research", "product-opportunity-finder", "competitor-price-analysis"],
            "inventory": ["inventory-management", "amazon-fba-profit-calculator"],
        },
        "shopify": {
            "launch": ["ecommerce-keyword-research", "shopify-seo", "google-shopping-ads", "email-marketing-ecommerce"],
            "convert": ["conversion-rate-optimization", "shopify-profit-calculator"],
            "research": ["ecommerce-keyword-research", "competitor-price-analysis", "product-opportunity-finder"],
            "inventory": ["inventory-management", "shopify-profit-calculator"],
        },
        "etsy": {
            "launch": ["ecommerce-keyword-research", "listing-title-optimizer", "etsy-seo"],
            "convert": ["etsy-seo", "listing-title-optimizer", "competitor-price-analysis"],
            "research": ["ecommerce-keyword-research", "product-opportunity-finder"],
            "inventory": ["inventory-management"],
        },
    }

    if any(w in goal_lower for w in ["launch", "start", "new product", "list"]):
        goal_key = "launch"
    elif any(w in goal_lower for w in ["convert", "sales", "cro", "improve"]):
        goal_key = "convert"
    elif any(w in goal_lower for w in ["research", "find", "discover", "niche"]):
        goal_key = "research"
    elif any(w in goal_lower for w in ["inventory", "stock", "reorder", "supply"]):
        goal_key = "inventory"
    else:
        goal_key = "launch"

    sequences = platform_sequences.get(platform_lower, platform_sequences["shopify"])
    sequence = sequences.get(goal_key, sequences["launch"])

    return {
        "platform": platform,
        "goal": goal,
        "recommended_sequence": sequence,
        "tip": "Call get_ecommerce_skill() with each skill name for full guidance.",
        "source": "https://github.com/nexscope-ai/eCommerce-Skills",
    }
