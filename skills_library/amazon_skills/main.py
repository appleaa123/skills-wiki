"""Amazon Skills — keyword research, listing optimisation, FBA calculator, PPC, and more.

Source: https://github.com/nexscope-ai/Amazon-Skills (MIT)
Supports 12 Amazon marketplaces. No API key required.
"""

from fastmcp import FastMCP

from core.skill_config import get_presentation_hint

mcp = FastMCP("amazon-skills")

_SKILL_NAME = "amazon_skills"

_SKILLS: dict[str, dict] = {
    "amazon-keyword-research": {
        "status": "production",
        "description": "Long-tail keyword mining from Amazon autocomplete across 12 marketplaces.",
        "guidance": """# Amazon Keyword Research

## Process (No API Key Required)
1. **Autocomplete harvesting** — query Amazon search for seed keyword + alphabet expansion
   (e.g. "yoga mat a", "yoga mat b", ... "yoga mat z", plus "best yoga mat", "yoga mat for...")
2. **Competitor ASIN extraction** — pull keywords from top 3-5 ASIN titles, bullets, and descriptions
3. **Intent classification** — label each keyword: purchase-ready / research / brand search
4. **Competition scoring** — estimate via number of results, sponsored product density, and top-3 BSR
5. **Seasonal check** — Google Trends 12-month pattern for demand seasonality

## Output Structure
- Long-tail keywords grouped by intent (commercial / informational / niche)
- Competition metrics table: sponsored density, estimated seller count, price range
- Seasonal trend summary
- Opportunity score (1-10) for top 10 keywords

## Marketplaces Supported
US (amazon.com), UK (.co.uk), DE (.de), FR (.fr), IT (.it), ES (.es),
JP (.co.jp), CA (.ca), AU (.com.au), IN (.in), MX (.com.mx), BR (.com.br)

## Tips
- Start with 3-5 seed keywords from your product category
- Focus on 3-5 word phrases (long-tail) for lower competition
- Prioritise purchase-intent keywords for main listings
""",
    },
    "amazon-listing-optimization": {
        "status": "production",
        "description": "Audit existing listings and create keyword-optimised copy across 12 marketplaces.",
        "guidance": """# Amazon Listing Optimization

## Two Modes

### Mode A — Create (New Listing)
Input: seed keywords OR competitor ASINs OR both
Output: ready-to-paste listing copy for Amazon Seller Central

### Mode B — Audit + Optimise (Existing Listing)
Input: existing title, bullets, description + target keywords
Output: gap analysis + rewritten components

## Listing Components & Rules

| Component | Character Limit | Rules |
|-----------|----------------|-------|
| Title | 200 chars | Primary keyword first; brand; key attributes (size, color, count); NO ALL CAPS; no promotional claims |
| Bullet 1 | 500 chars | Lead benefit; primary keyword natural placement |
| Bullet 2-5 | 500 chars each | Secondary features + benefits; include supporting keywords |
| Description | 2000 chars | Story-style; expand on benefits; include remaining keywords |
| Backend Search Terms | 250 bytes | No repeats from title/bullets; alternate spellings; synonyms |

## Keyword Tier Priority
- **Tier 1** (title): highest-volume, most purchase-intent keywords
- **Tier 2** (bullets): secondary keywords that support Tier 1 themes
- **Tier 3** (description + backend): informational, alternate spellings, long-tail

## 8-Dimension Audit Score
Title / Bullets / Description / Images / A+ Content / Pricing / Reviews / SEO Coverage
Score each 1-10; prioritise fixing anything below 6.

## Marketplace Language
Output language automatically matches target marketplace:
DE → German, JP → Japanese, FR → French, ES → Spanish, etc.
""",
    },
    "amazon-ppc-campaign": {
        "status": "production",
        "description": "Build and optimise Amazon PPC campaigns with ACoS targeting.",
        "guidance": """# Amazon PPC Campaign Management

## Campaign Structure (Recommended)
```
Campaign 1: Auto (Discovery)
  Ad Group: All Products
  → Harvests converting search terms for manual campaigns

Campaign 2: Manual Exact (Scale Winners)
  Ad Group per keyword cluster
  → Exact match on proven keywords; tight bid control

Campaign 3: Manual Broad/Phrase (Expansion)
  Ad Group: Research
  → Finds new variations; feed winners to Exact campaign
```

## ACoS Targets by Goal
| Goal | Target ACoS |
|------|------------|
| Launch (rank building) | 50-80% (invest in rank) |
| Breakeven | Product margin % |
| Profitable | 15-25% (category dependent) |

## Bid Optimisation Rules
- Increase bids 20-30% for keywords with ACoS < target and < 20 clicks
- Decrease bids 20% for keywords with ACoS > 2× target
- Pause keywords with >40 clicks and 0 conversions
- Harvest converting search terms weekly from Auto → exact match

## Negative Keywords
Add negatives to prevent wasted spend:
- Irrelevant categories
- Competitor brand names (unless intentional)
- Terms with 0% conversion rate after 30+ clicks

## Key Metrics
- **ACoS** = Ad Spend / Ad Revenue (lower = more efficient)
- **TACoS** = Ad Spend / Total Revenue (measures ad dependency)
- **ROAS** = Ad Revenue / Ad Spend (higher = better)
""",
    },
    "amazon-sales-estimator": {
        "status": "production",
        "description": "Estimate monthly sales from BSR or ASIN for any Amazon category.",
        "guidance": """# Amazon Sales Estimator (BSR Method)

## How BSR → Sales Estimation Works
Amazon's Best Seller Rank (BSR) is updated hourly and reflects relative sales velocity.
No official sales data is public, so estimation uses category-specific BSR curves.

## BSR to Monthly Sales — Approximate Ranges

### Books
| BSR | Est. Monthly Sales |
|-----|-------------------|
| 1-100 | 3,000-50,000+ |
| 100-1,000 | 500-3,000 |
| 1,000-10,000 | 50-500 |
| 10,000-100,000 | 5-50 |

### Home & Kitchen / Sports & Outdoors
| BSR | Est. Monthly Sales |
|-----|-------------------|
| 1-500 | 2,000-20,000 |
| 500-5,000 | 200-2,000 |
| 5,000-50,000 | 20-200 |
| 50,000-500,000 | 2-20 |

### Electronics
| BSR | Est. Monthly Sales |
|-----|-------------------|
| 1-100 | 5,000-100,000 |
| 100-1,000 | 500-5,000 |
| 1,000-10,000 | 50-500 |

## Caveats
- BSR fluctuates hourly; spot checks can be misleading — track 7-day average
- Sub-category BSR ≠ main category BSR
- Seasonal products will have higher BSR in off-season despite strong annual sales
- Combine with review velocity (new reviews/month) to cross-validate estimates
""",
    },
    "amazon-fba-calculator": {
        "status": "production",
        "description": "Complete FBA fee breakdown and profit analysis with 2024 rates.",
        "guidance": "Use the calculate_fba_fees() tool for real calculations. See tool description for inputs.",
    },
    "tariff-calculator-amazon": {
        "status": "production",
        "description": "Import duties and landed cost calculation for Amazon FBA importing.",
        "guidance": """# Amazon Tariff & Landed Cost Calculator

## Landed Cost Formula
Landed Cost = Product Cost + Freight + Import Duty + Customs Fees + FBA Prep + FBA Fees

## US Import Duty — Common Categories
| Product Category | HTS Chapter | Typical Duty Rate |
|-----------------|-------------|------------------|
| Clothing/Apparel | 61-62 | 12-28% |
| Electronics | 84-85 | 0-5% |
| Toys & Games | 95 | 0% |
| Furniture | 94 | 0-5% |
| Kitchenware | 73 | 3.7% |
| Sporting Goods | 95 | 4% |

**Note**: Section 301 tariffs may add 7.5-25% for goods of Chinese origin.
Always verify current HTS code + duty rate at hts.usitc.gov

## Freight Cost Benchmarks (2024, China → US)
| Method | Timeline | Cost per CBM |
|--------|----------|-------------|
| Sea LCL | 30-45 days | $80-120 |
| Sea FCL (20ft) | 30-45 days | $1,500-3,000 |
| Air Express | 5-10 days | $5-10/kg |

## Customs Fees (US)
- ISF Filing: ~$35
- Customs Bond: ~$50 (single entry) or $500/yr (continuous)
- Customs Exam: $200-500 if selected

## Profitability Rule of Thumb
Target landed cost ≤ 25-30% of selling price to allow for FBA fees, PPC, and margin.
""",
    },
}

# FBA fee tables (2024 rates)
_FBA_SIZE_TIERS = [
    {"name": "Small Standard", "max_weight_lb": 1.0, "max_l": 15, "max_w": 12, "max_h": 0.75, "fee": 3.06},
    {"name": "Large Standard", "max_weight_lb": 20.0, "max_l": 18, "max_w": 14, "max_h": 8, "fee_base": 3.68, "fee_per_lb": 0.08, "base_weight_lb": 1.0},
    {"name": "Small Oversize", "max_weight_lb": 70.0, "max_l": 60, "max_w": 30, "max_h": None, "fee_base": 9.61, "fee_per_lb": 0.38, "base_weight_lb": 2.0},
    {"name": "Medium Oversize", "max_weight_lb": 150.0, "fee_base": 19.05, "fee_per_lb": 0.38, "base_weight_lb": 2.0},
    {"name": "Large Oversize", "max_weight_lb": 150.0, "fee_base": 89.98, "fee_per_lb": 0.83, "base_weight_lb": 90.0},
    {"name": "Special Oversize", "max_weight_lb": float("inf"), "fee_base": 158.49, "fee_per_lb": 0.83, "base_weight_lb": 90.0},
]

_REFERRAL_RATES: dict[str, float] = {
    "apparel": 0.17,
    "automotive": 0.12,
    "baby": 0.08,
    "beauty": 0.08,
    "books": 0.15,
    "camera": 0.08,
    "electronics": 0.08,
    "furniture": 0.15,
    "grocery": 0.08,
    "health": 0.08,
    "home": 0.15,
    "jewelry": 0.20,
    "kitchen": 0.15,
    "music": 0.15,
    "office": 0.15,
    "pet": 0.15,
    "shoes": 0.15,
    "software": 0.15,
    "sports": 0.15,
    "tools": 0.15,
    "toys": 0.15,
    "video_games": 0.15,
    "watches": 0.16,
}

_STORAGE_RATES = {
    "standard_jan_sep": 0.87,   # per cubic foot per month
    "standard_oct_dec": 2.40,
    "oversize_jan_sep": 0.56,
    "oversize_oct_dec": 1.40,
}


def _classify_size_tier(length_in: float, width_in: float, height_in: float, weight_lb: float) -> dict:
    """Classify a product into an FBA size tier and return the tier info."""
    dims = sorted([length_in, width_in, height_in], reverse=True)
    longest, median, shortest = dims[0], dims[1], dims[2]

    # Small Standard
    if weight_lb <= 1.0 and longest <= 15 and median <= 12 and shortest <= 0.75:
        return {"tier": "Small Standard", "fee": 3.06, "oversize": False}

    # Large Standard (up to 20 lb, 18×14×8)
    if weight_lb <= 20.0 and longest <= 18 and median <= 14 and shortest <= 8:
        excess_lb = max(0, weight_lb - 1.0)
        fee = 3.68 + excess_lb * 0.08
        return {"tier": "Large Standard", "fee": round(fee, 2), "oversize": False}

    # Small Oversize (up to 70 lb, longest ≤ 60, median ≤ 30)
    if weight_lb <= 70.0 and longest <= 60 and median <= 30:
        excess_lb = max(0, weight_lb - 2.0)
        fee = 9.61 + excess_lb * 0.38
        return {"tier": "Small Oversize", "fee": round(fee, 2), "oversize": True}

    # Medium Oversize (up to 150 lb, girth ≤ 108)
    girth = longest + 2 * (median + shortest)
    if weight_lb <= 150.0 and girth <= 108:
        excess_lb = max(0, weight_lb - 2.0)
        fee = 19.05 + excess_lb * 0.38
        return {"tier": "Medium Oversize", "fee": round(fee, 2), "oversize": True}

    # Large Oversize (up to 150 lb, girth ≤ 165)
    if weight_lb <= 150.0 and girth <= 165:
        excess_lb = max(0, weight_lb - 90.0)
        fee = 89.98 + excess_lb * 0.83
        return {"tier": "Large Oversize", "fee": round(fee, 2), "oversize": True}

    # Special Oversize
    excess_lb = max(0, weight_lb - 90.0)
    fee = 158.49 + excess_lb * 0.83
    return {"tier": "Special Oversize", "fee": round(fee, 2), "oversize": True}


@mcp.tool()
def list_amazon_skills() -> dict:
    """List all available Amazon skills with their status and descriptions."""
    return {
        name: {"status": s["status"], "description": s["description"]}
        for name, s in _SKILLS.items()
    }


@mcp.tool()
def get_amazon_skill(skill_name: str = None) -> dict:
    """Get the full guidance for a specific Amazon skill.

    Args:
        skill_name: Skill slug (e.g. 'amazon-keyword-research', 'amazon-ppc-campaign').
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
    hint = get_presentation_hint('amazon_skills', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@amazon_skills",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'amazon_skills',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }

@mcp.tool()
def calculate_fba_fees(
    length_in: float,
    width_in: float,
    height_in: float,
    weight_lb: float,
    selling_price: float,
    product_cost: float,
    category: str = "home",
    inbound_shipping_cost: float = 0.0,
    storage_months: float = 1.0,
    peak_season: bool = False,
) -> dict:
    """Calculate complete Amazon FBA fees and profit breakdown (2024 US rates).

    Args:
        length_in: Product length in inches.
        width_in: Product width in inches.
        height_in: Product height in inches.
        weight_lb: Product weight in pounds.
        selling_price: Listed selling price in USD.
        product_cost: Your cost to source the product in USD.
        category: Product category for referral fee (e.g. 'home', 'electronics', 'toys').
                  Run list_amazon_skills() for full category list.
        inbound_shipping_cost: Cost to ship one unit to FBA warehouse in USD.
        storage_months: How many months of average monthly storage to include.
        peak_season: True if storing Oct-Dec (peak storage rates apply).
    """
    # Size tier + fulfillment fee
    tier_info = _classify_size_tier(length_in, width_in, height_in, weight_lb)
    fulfillment_fee = tier_info["fee"]

    # Referral fee
    category_lower = category.lower().strip()
    referral_rate = _REFERRAL_RATES.get(category_lower, 0.15)
    referral_fee = round(selling_price * referral_rate, 2)
    min_referral = 0.30
    referral_fee = max(referral_fee, min_referral)

    # Storage fee
    cubic_feet = (length_in * width_in * height_in) / 1728
    if tier_info["oversize"]:
        storage_rate = _STORAGE_RATES["oversize_oct_dec"] if peak_season else _STORAGE_RATES["oversize_jan_sep"]
    else:
        storage_rate = _STORAGE_RATES["standard_oct_dec"] if peak_season else _STORAGE_RATES["standard_jan_sep"]
    monthly_storage_fee = round(cubic_feet * storage_rate, 2)
    total_storage_fee = round(monthly_storage_fee * storage_months, 2)

    # Totals
    total_fees = round(fulfillment_fee + referral_fee + total_storage_fee, 2)
    total_cost = round(product_cost + inbound_shipping_cost + total_fees, 2)
    gross_profit = round(selling_price - total_cost, 2)
    gross_margin_pct = round((gross_profit / selling_price) * 100, 1) if selling_price > 0 else 0
    roi_pct = round((gross_profit / (product_cost + inbound_shipping_cost)) * 100, 1) if (product_cost + inbound_shipping_cost) > 0 else 0

    # Optimisation tips
    tips = []
    if tier_info["tier"] == "Large Standard" and weight_lb > 15:
        tips.append("Weight is close to Small Oversize threshold. Reducing weight below 20 lb keeps you in standard tiers.")
    if gross_margin_pct < 20:
        tips.append(f"Margin ({gross_margin_pct}%) is below the 20% minimum recommended for FBA. Consider raising price or reducing COGS.")
    if roi_pct < 50:
        tips.append(f"ROI ({roi_pct}%) is below 50%. Aim for 50-100%+ for sustainable FBA business.")
    if cubic_feet > 2 and not tier_info["oversize"]:
        tips.append("Product volume is significant. Monitor storage fees during Q4 (peak season rates are 2.75× higher).")

    result = {
        "size_tier": tier_info["tier"],
        "fee_breakdown": {
            "fulfillment_fee": fulfillment_fee,
            "referral_fee": referral_fee,
            "referral_rate_pct": f"{int(referral_rate * 100)}%",
            "monthly_storage_fee": monthly_storage_fee,
            "total_storage_fee": total_storage_fee,
            "total_fba_fees": total_fees,
        },
        "cost_breakdown": {
            "product_cost": product_cost,
            "inbound_shipping": inbound_shipping_cost,
            "total_fba_fees": total_fees,
            "total_cost": total_cost,
        },
        "profit_analysis": {
            "selling_price": selling_price,
            "gross_profit": gross_profit,
            "gross_margin_pct": gross_margin_pct,
            "roi_pct": roi_pct,
        },
        "optimisation_tips": tips if tips else ["Fees and margins look healthy."],
        "source": "https://github.com/nexscope-ai/Amazon-Skills",
        "note": "2024 US FBA rates. Rates change annually — verify at sellercentral.amazon.com.",
    }
    hint = get_presentation_hint(_SKILL_NAME)
    if hint:
        result["_presentation_hint"] = hint
    return result
