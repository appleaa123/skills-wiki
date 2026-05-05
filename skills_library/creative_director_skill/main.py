"""Skill: creative_director_skill."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("creative-director-skill")


_SKILLS: dict[str, dict] = {
    'what-it-does': {
        "description": 'Feed it a brief in any format — text, voice transcript, PDF, raw notes — and it runs a full creative cycle:\n\n1.',
        "guidance": "Feed it a brief in any format — text, voice transcript, PDF, raw notes — and it runs a full creative cycle:\n\n1. **INTAKE** — extracts the brief's DNA: product, audience, objectives, constraints\n2. **INSIGHT** — mines consumer insights using 7 proven techniques (Mark Pollard, JTBD, Tension Spotting, HMW, Abstraction Laddering)\n3. **IDEATION** — generates 8-12 ideas using 3 methods from different categories (structural × associative × disruptive), rotating between 20+ methodologies\n4. **EVALUATE + REFINE** — scores against 6 weighted criteria + HumanKind + Grey Scale, then recursively improves until 9+ or convergence\n5. **ARTICULATE** — outputs in a presentation-ready format (one-pager, top-3, campaign platform, or quick response)\n\nYou can also enter at any phase: jump to insight mining, evaluate an existing idea, or generate concepts from a known insight.",
    },
    'why-this-exists': {
        "description": 'Most AI "creative" tools generate ideas by free association — producing volume without structure.',
        "guidance": 'Most AI "creative" tools generate ideas by free association — producing volume without structure. The result: hundreds of mediocre concepts that nobody can evaluate.\n\nThis skill enforces the discipline that separates award-winning work from filler:\n\n- **Insight-first** — no ideation without a validated consumer tension\n- **Structural methods** — SIT, TRIZ, SCAMPER, Bisociation, Synectics, not "give me 10 ideas"\n- **Honest scoring** — calibrated against real Cannes winners, with anti-inflation rules that prevent the model from rating everything 8+\n- **Recursive refinement** — weak criteria get targeted improvement using different methods each pass\n- **Kill Your Darlings** — the skill argues against its own favorite ideas to test their strength',
    },
    'what-s-inside': {
        "description": '```\ncreative-director/\n├── SKILL.',
        "guidance": '```\ncreative-director/\n├── SKILL.md                              # Core skill — phase router + instructions\n├── assets/\n│   └── output-templates.md               # 4 presentation formats\n└── references/\n    ├── methods-catalog.md                # 20 creative methodologies as executable cards\n    ├── method-selection-matrix.md        # Task → method routing + rotation rules\n    ├── insight-mining.md                 # 7 insight discovery techniques\n    ├── scoring-calibration.md            # Detailed rubrics + calibration anchors\n    ├── creative-constitution.md          # 3-layer evaluation system + feedback rules\n    └── storytelling-frameworks.md        # 6 narrative frameworks for advertising\n```\n\n### Methodologies (20+)\n\n| Category | Methods |\n|----------|---------|\n| **Structural** | SIT/Goldenberg Templates, SCAMPER, TRIZ (10 principles), Morphological Analysis |\n| **Association** | Bisociation, Random Entry, Forced Connections, Synectics |\n| **Inversion** | Reverse Brainstorming, Worst Possible Idea, Provocation PO |\n| **Perturbation** | Oblique Strategies, Six Thinking Hats, Disney Creative Strategy |\n| **Volume** | Crazy 8s, Brainwriting 6-3-5, Starbursting |\n| **Bonus** | First Principles Thinking, Lateral Thinking Toolkit, Design Sprint Sketch |\n\n### Evaluation System\n\nThree parallel scoring systems calibrated against real campaigns:\n\n- **6 Weighted Criteria** — Originality (0.25), Strategic Fit (0.20), Emotional Response (0.20), Feasibility (0.15), Scalability (0.10), Simplicity (0.10)\n- **HumanKind Scale** (Leo Burnett) — 1-10, from "Destructive" to "Changes the World"\n- **Grey Scale** (Grey Group) — 1-10, from "Toxic" to "Best in the World"\n\nAnti-inflation rules: batch control, normal distribution enforcement, real analogues test, specificity test, time test.\n\n### Storytelling Frameworks\n\nStory Spine (Pixar) · Sparkline (Nancy Duarte) · Freytag\'s Pyramid · Monroe\'s Motivated Sequence · Pixar Rules · Hero\'s Journey (StoryBrand)',
    },
    'installation': {
        "description": "### Claude Projects\n\nAdd the files to your Claude Project's knowledge base.",
        "guidance": "### Claude Projects\n\nAdd the files to your Claude Project's knowledge base. Upload all files from `creative-director/` — `SKILL.md` is the entry point, it references other files via `[[wikilinks]]`.\n\n### Claude Code / Cursor / Windsurf / Any AI Agent\n\nCopy the `creative-director/` folder to your project or skills directory:\n\n```bash\ngit clone https://github.com/smixs/creative-director-skill.git\n```\n\nThe skill works with any AI agent that supports structured instructions — Claude, GPT, Gemini, or local models. The core logic is in markdown files, no platform lock-in.",
    },
    'usage-examples': {
        "description": '**Full creative cycle:**\n> "Come up with a campaign for [brand].',
        "guidance": '**Full creative cycle:**\n> "Come up with a campaign for [brand]. Target audience: [who]. Budget: [range]. Channels: [where]."\n\n**Insight mining:**\n> "Find a consumer insight for [category]. The brief says [context]."\n\n**Evaluate an existing idea:**\n> "Evaluate this concept: [description]. The brief objective was [goal]."\n\n**Quick ideation:**\n> "Need 5 concepts for [brand] social media posts about [topic]."',
    },
    'idea-levels': {
        "description": 'The skill distinguishes between three levels and matches output to the brief:\n\n| Level | Scope | Example |\n|-------|-------|---------|\n| **Big Idea** | Brand platform for years | Nike "Just Do It", Do',
        "guidance": 'The skill distinguishes between three levels and matches output to the brief:\n\n| Level | Scope | Example |\n|-------|-------|---------|\n| **Big Idea** | Brand platform for years | Nike "Just Do It", Dove "Real Beauty" |\n| **Campaign Idea** | Time-limited, multi-channel | "Share a Coke", Spotify Wrapped |\n| **Execution Idea** | Single channel/format | A specific social post, banner, activation |\n\nA Big Idea for shelf talkers = waste. An Execution Idea for a rebrand = falling short.',
    },
    'how-recursion-works': {
        "description": '```\nGenerate ideas (3 methods, 8-12 ideas)\n        ↓\nScore top 3 (6 criteria + HumanKind + Grey)\n        ↓\n    Score ≥ 9? ──→ YES → Output final deliverable\n        ↓ NO\nIdentify weak criteria → Apply',
        "guidance": '```\nGenerate ideas (3 methods, 8-12 ideas)\n        ↓\nScore top 3 (6 criteria + HumanKind + Grey)\n        ↓\n    Score ≥ 9? ──→ YES → Output final deliverable\n        ↓ NO\nIdentify weak criteria → Apply different method → Rescore\n        ↓\n    5 passes or plateau? ──→ YES → Output best + honest assessment\n        ↓ NO\n    Continue refinement\n```',
    },
    'what-it-s-not-for': {
        "description": '- Media planning or budget allocation\n- Production management\n- Brand identity / logo design\n- Final copywriting (it generates concepts, not polished copy)\n- Market research data collection.',
        "guidance": '- Media planning or budget allocation\n- Production management\n- Brand identity / logo design\n- Final copywriting (it generates concepts, not polished copy)\n- Market research data collection',
    },
    'credits': {
        "description": 'Built on methodologies from: Jacob Goldenberg (SIT), Genrich Altshuller (TRIZ), Edward de Bono (Lateral Thinking, Six Hats, PO), Arthur Koestler (Bisociation), William Gordon (Synectics), Brian Eno (O',
        "guidance": "Built on methodologies from: Jacob Goldenberg (SIT), Genrich Altshuller (TRIZ), Edward de Bono (Lateral Thinking, Six Hats, PO), Arthur Koestler (Bisociation), William Gordon (Synectics), Brian Eno (Oblique Strategies), Nancy Duarte (Sparkline), Joseph Campbell / Donald Miller (Hero's Journey / StoryBrand), Leo Burnett (HumanKind), Mark Pollard (Strategy), Clayton Christensen (JTBD).\n\nCreative Constitution based on the Voskresensky/IKRA approach.",
    },
    'license': {
        "description": 'MIT — use it, fork it, make better ads.',
        "guidance": 'MIT — use it, fork it, make better ads.',
    },
}


@mcp.tool()
def list_creative_director_skill_skills() -> dict:
    """List all available creative_director_skill skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_creative_director_skill_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific creative_director_skill skill."""
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
    hint = get_presentation_hint('creative_director_skill', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@creative_director_skill",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'creative_director_skill',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
