"""Skill: claude_ecom."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("claude-ecom")


_SKILLS: dict[str, dict] = {
    'who-this-is-for': {
        "description": '- Data Analysts / Marketers who write monthly business reviews from scratch every time\n- D2C brand owners, retail managers, or ecommerce managers without an analyst on staff\n- Anyone who knows revenue',
        "guidance": "- Data Analysts / Marketers who write monthly business reviews from scratch every time\n- D2C brand owners, retail managers, or ecommerce managers without an analyst on staff\n- Anyone who knows revenue dropped but can't explain why",
    },
    'quick-start': {
        "description": '```bash\n# Install\ncurl -fsSL https://raw.',
        "guidance": '```bash\n# Install\ncurl -fsSL https://raw.githubusercontent.com/takechanman1228/claude-ecom/v0.1.3/install.sh | bash\n\n# Drop your orders CSV, Start Claude Code, and run:\n/ecom review\n```\n\nRequires: Claude Code CLI, Python 3.10+, and git\n\n### Alternative: Install as a Claude Code plugin\n\n```\n/plugin marketplace add takechanman1228/claude-ecom\n/plugin install claude-ecom@claude-ecom\n/reload-plugins\n```\n\nRestart Claude Code. The Python backend installs automatically on session start.\nThe command becomes `/claude-ecom:ecom review` when installed as a plugin.',
    },
    'what-you-get': {
        "description": 'A single `REVIEW.',
        "guidance": 'A single `REVIEW.md` that reads like a consultant wrote it:\n\n\n```\n# Business Review\n> Revenue reached $9.37M for the year, essentially flat YoY (-1.7%), despite strong\n> short-term momentum — the last 90 days surged 84% and November posted +28.5%,\n> both driven by Q4 seasonal demand rather than structural growth. The flat annual...\n```\n\n```\n           30d Pulse       90d Momentum     365d Structure\nRevenue    $1.47M (+ 28%)  $3.73M (+ 84%)   $9.37M (= -2%)\nOrders     3,499 (+ 26%)   8,814 (+ 60%)    24,812 (- 11%)\nAOV        $419 (+ 2%)     $424 (+ 15%)     $378 (+ 10%)\nCustomers  1,676 (+ 11%)   2,918 (+ 51%)    4,296 (= flat)\n...\n```\n```\nRevenue $9.37M (YoY: -1.7%)\n├── 🔴 New Customer Revenue $1.45M (15.5%)\n│   ├── New Customers: 1,559 (-57.8%)\n│   └── New Customer AOV: $305\n└── 🟢 Existing Customer Revenue $7.92M (84.5%)\n    ├── Returning Customers: 2,737 (+345%)\n    ├── Returning AOV: $395\n    └── Repeat Purchase Rate: 75.4%\n```\nExecutive summary → Multi-horizon dashboard → KPI trees with 🔴/🟢 signals → Findings with "what / why / what to do" → Prioritized action plan with deadlines, success metrics, and guardrails.\n[See a full example output →](examples/online-retail-ii/REVIEW.md)',
    },
    'commands': {
        "description": '| Command | Description |\n|---------|-------------|\n| `/ecom review` | Full business review — auto-selects 30d / 90d / 365d |\n| `/ecom review 30d` / `90d` / `365d` | Focus on a specific period |\n| `/e',
        "guidance": "| Command | Description |\n|---------|-------------|\n| `/ecom review` | Full business review — auto-selects 30d / 90d / 365d |\n| `/ecom review 30d` / `90d` / `365d` | Focus on a specific period |\n| `/ecom review How's retention?` | Ask a question instead of a full report |",
    },
    'input': {
        "description": 'Any e-commerce/retail orders CSV works.',
        "guidance": "Any e-commerce/retail orders CSV works. \n\nRequired columns: order ID, order date, customer ID or email, revenue (after discounts, before tax/shipping).\nOptional (enables deeper analysis): quantity, SKU or product name, discount amount. In many cases, column names don't need to match exactly.",
    },
    'how-it-works': {
        "description": '```\nOrders CSV → Python engine → review.',
        "guidance": '```\nOrders CSV → Python engine → review.json → Claude → REVIEW.md\n```\n\nPython computes every KPI and runs health checks. Claude reads the structured output and writes the business narrative. Numbers are precise because Python owns them. Interpretation is sharp because Claude owns that.',
    },
    'example': {
        "description": 'Tested on [Online Retail II](https://archive.',
        "guidance": 'Tested on [Online Retail II](https://archive.ics.uci.edu/dataset/502/online+retail+ii) (UCI, CC BY 4.0) — a real UK retailer with ~1M transactions over 2 years.\n\n[See the full report →](examples/online-retail-ii/REVIEW.md) | [Try it yourself →](examples/online-retail-ii/)',
    },
    'roadmap': {
        "description": '- [ ] Shopify API integration (skip CSV export)\n- [ ] Weekly digest mode\n- [ ] Multi-store comparison.',
        "guidance": '- [ ] Shopify API integration (skip CSV export)\n- [ ] Weekly digest mode\n- [ ] Multi-store comparison',
    },
    'acknowledgements': {
        "description": 'Inspired by [claude-ads](https://github.',
        "guidance": 'Inspired by [claude-ads](https://github.com/AgriciDaniel/claude-ads) by [@AgriciDaniel](https://github.com/AgriciDaniel).',
    },
    'license': {
        "description": 'MIT.',
        "guidance": 'MIT',
    },
}


@mcp.tool()
def list_claude_ecom_skills() -> dict:
    """List all available claude_ecom skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_claude_ecom_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific claude_ecom skill."""
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
    hint = get_presentation_hint('claude_ecom', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@claude_ecom",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'claude_ecom',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
