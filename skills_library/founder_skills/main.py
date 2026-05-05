"""Skill: founder_skills."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("founder-skills")


_SKILLS: dict[str, dict] = {
    'installation': {
        "description": '### Via Terminal (npx)\n\n```bash\nnpx skills add https://github.',
        "guidance": '### Via Terminal (npx)\n\n```bash\nnpx skills add https://github.com/ognjengt/founder-skills\n```\n\nInstall a specific skill:\n\n```bash\nnpx skills add https://github.com/ognjengt/founder-skills --skill prd-generator\n```\n\n### Manual Installation\n\nClone the repo and copy all skills to your project:\n\n```bash\ngit clone https://github.com/ognjengt/founder-skills\ncp -r founder-skills/skills/* .claude/skills/\n```\n\nOr copy a single skill:\n\n```bash\ncp -r founder-skills/skills/prd-generator .claude/skills/\n```\n\nTo install globally (available across all projects):\n\n```bash\ncp -r founder-skills/skills/* ~/.claude/skills/\n```',
    },
    'available-skills': {
        "description": '| Skill | Description |\n|-------|-------------|\n| `sop-creator` | Creates detailed Standard Operating Procedures for business processes |\n| `cro-optimization` | Analyzes landing pages against 13 CRO p',
        "guidance": '| Skill | Description |\n|-------|-------------|\n| `sop-creator` | Creates detailed Standard Operating Procedures for business processes |\n| `cro-optimization` | Analyzes landing pages against 13 CRO principles and provides detailed optimization recommendations with before/after examples |\n| `viral-hook-creator` | Creates viral hooks for content and marketing |\n| `lead-magnet-generator` | Creates viral lead magnet posts with CTAs that drive comments and DMs — produces quick and detailed formats for Twitter/X and LinkedIn |\n| `strategic-planning` | Analyzes your business to deliver 3 specific, high-impact next moves for growth (marketing/sales) — asks diagnostic questions when needed to uncover bottlenecks and opportunities |\n| `go-to-market-plan` | Delivers 3 best go-to-market strategies tailored to your product, stage, and market — asks diagnostic questions about product readiness, ICP, competitive positioning, and distribution channels |\n| `x-writer` | Creates 3 viral X (Twitter) posts in different proven formats with creator voice matching (Hormozi, Naval, Gazdecki, Dakota, Machina, Ognjen) — uses 51+ post templates and 8 format structures |\n| `linkedin-writer` | Creates 2 viral LinkedIn posts in different proven formats with voice matching — uses 8+ post templates and 7 format structures (Lessons Learned, Blueprint, Story, Strategy, Case Study, Hot Take, Quick Hack) |\n| `outreach-specialist` | Crafts high-converting outreach sequences (cold email, LinkedIn DM, X DM) using 8 proven templates with follow-up strategy, platform-specific rules, and personalized messaging that books calls |\n| `competitor-intel` | Analyzes competitors with verified metrics, leverage strategies, and predicted next moves |\n| `brand-copywriter` | Writes marketing copy using proven frameworks (AIDA, PAS, BAB, etc.) for ads, landing pages, emails, and more |\n| `pricing-strategist` | Builds comprehensive pricing strategies with tiered plans, price justifications, and revenue optimization through interactive Q&A |\n| `prd-generator` | Generates professional PRD documents optimized for AI coding tools — asks clarifying questions and outputs PDF to `./prd_outputs/` |\n| `product-hunt-launch-plan` | Creates comprehensive, personalized Product Hunt launch plans to rank #1 — includes hour-by-hour battle plan, templates, and 20+ alternative launch platforms |\n| `marketing-ideas` | Produces the 5 best marketing ideas for your business from a curated database of 160+ proven strategies — tailored to your industry, audience, and goals |',
    },
    'usage': {
        "description": 'After installation, use skills in Claude Code by typing:\n\n```\n/sop-creator create an employee onboarding process\n```\n\n```\n/linkedin-writer write a post about our new product launch\n```.',
        "guidance": 'After installation, use skills in Claude Code by typing:\n\n```\n/sop-creator create an employee onboarding process\n```\n\n```\n/linkedin-writer write a post about our new product launch\n```',
    },
    'customizing-for-your-business': {
        "description": 'After installation, create the `FOUNDER_CONTEXT.',
        "guidance": 'After installation, create the `FOUNDER_CONTEXT.md` in your project root, and copy the contents from this repository.\n\nThen replace the fields with your own custom values so that the skills are tailored to you:\n\n- Company name and industry\n- Target audience and value proposition\n- Brand voice and tone\n- Business goals\n- Products/services\n\nSkills automatically check for this file and use it to personalize outputs.\nEach project can have its own context file for different businesses or clients.',
    },
    'contributing': {
        "description": 'Want to add a new skill? See [CLAUDE.',
        "guidance": 'Want to add a new skill? See [CLAUDE.md](CLAUDE.md) for development guidelines.\n\n### Skill Structure\n\n```\nskills/\n└── your-skill/\n    ├── SKILL.md        # Main skill definition\n    └── references/     # Additional reference materials\n```',
    },
    'license': {
        "description": 'MIT.',
        "guidance": 'MIT',
    },
}


@mcp.tool()
def list_founder_skills_skills() -> dict:
    """List all available founder_skills skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_founder_skills_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific founder_skills skill."""
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
    hint = get_presentation_hint('founder_skills', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@founder_skills",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'founder_skills',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
