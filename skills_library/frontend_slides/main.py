"""Skill: frontend_slides."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("frontend-slides")


_SKILLS: dict[str, dict] = {
    'what-this-does': {
        "description": '**Frontend Slides** helps non-designers create beautiful web presentations without knowing CSS or JavaScript.',
        "guidance": '**Frontend Slides** helps non-designers create beautiful web presentations without knowing CSS or JavaScript. It uses a "show, don\'t tell" approach: instead of asking you to describe your aesthetic preferences in words, it generates visual previews and lets you pick what you like.\n\nHere is a deck about the skill, made through the skill:\n\nhttps://github.com/user-attachments/assets/ef57333e-f879-432a-afb9-180388982478\n\n### Key Features\n\n- **Zero Dependencies** — Single HTML files with inline CSS/JS. No npm, no build tools, no frameworks.\n- **Visual Style Discovery** — Can\'t articulate design preferences? No problem. Pick from generated visual previews.\n- **PPT Conversion** — Convert existing PowerPoint files to web, preserving all images and content.\n- **Anti-AI-Slop** — Curated distinctive styles that avoid generic AI aesthetics (bye-bye, purple gradients on white).\n- **Production Quality** — Accessible, responsive, well-commented code you can customize.',
    },
    'installation': {
        "description": '### Via Plugin Marketplace (Recommended)\n\nInstall directly from Claude Code in two commands:\n\n```bash\n/plugin marketplace add zarazhangrui/frontend-slides\n/plugin install frontend-slides@frontend-slid',
        "guidance": '### Via Plugin Marketplace (Recommended)\n\nInstall directly from Claude Code in two commands:\n\n```bash\n/plugin marketplace add zarazhangrui/frontend-slides\n/plugin install frontend-slides@frontend-slides\n```\n\nThen use it by typing `/frontend-slides` in Claude Code.\n\n### Manual Installation\n\nCopy the skill files to your Claude Code skills directory:\n\n```bash\n# Create the skill directory\nmkdir -p ~/.claude/skills/frontend-slides/scripts\n\n# Copy all files (or clone this repo directly)\ncp SKILL.md STYLE_PRESETS.md viewport-base.css html-template.md animation-patterns.md ~/.claude/skills/frontend-slides/\ncp scripts/extract-pptx.py ~/.claude/skills/frontend-slides/scripts/\n```\n\nOr clone directly:\n\n```bash\ngit clone https://github.com/zarazhangrui/frontend-slides.git ~/.claude/skills/frontend-slides\n```\n\nThen use it by typing `/frontend-slides` in Claude Code.',
    },
    'usage': {
        "description": '### Create a New Presentation\n\n```\n/frontend-slides\n\n> "I want to create a pitch deck for my AI startup"\n```\n\nThe skill will:\n\n1.',
        "guidance": '### Create a New Presentation\n\n```\n/frontend-slides\n\n> "I want to create a pitch deck for my AI startup"\n```\n\nThe skill will:\n\n1. Ask about your content (slides, messages, images)\n2. Ask about the feeling you want (impressed? excited? calm?)\n3. Generate 3 visual style previews for you to compare\n4. Create the full presentation in your chosen style\n5. Open it in your browser\n\n### Convert a PowerPoint\n\n```\n/frontend-slides\n\n> "Convert my presentation.pptx to a web slideshow"\n```\n\nThe skill will:\n\n1. Extract all text, images, and notes from your PPT\n2. Show you the extracted content for confirmation\n3. Let you pick a visual style\n4. Generate an HTML presentation with all your original assets',
    },
    'included-styles': {
        "description": '### Dark Themes\n\n- **Bold Signal** — Confident, high-impact, vibrant card on dark\n- **Electric Studio** — Clean, professional, split-panel\n- **Creative Voltage** — Energetic, retro-modern, electric bl',
        "guidance": '### Dark Themes\n\n- **Bold Signal** — Confident, high-impact, vibrant card on dark\n- **Electric Studio** — Clean, professional, split-panel\n- **Creative Voltage** — Energetic, retro-modern, electric blue + neon\n- **Dark Botanical** — Elegant, sophisticated, warm accents\n\n### Light Themes\n\n- **Notebook Tabs** — Editorial, organized, paper with colorful tabs\n- **Pastel Geometry** — Friendly, approachable, vertical pills\n- **Split Pastel** — Playful, modern, two-color vertical split\n- **Vintage Editorial** — Witty, personality-driven, geometric shapes\n\n### Specialty\n\n- **Neon Cyber** — Futuristic, particle backgrounds, neon glow\n- **Terminal Green** — Developer-focused, hacker aesthetic\n- **Swiss Modern** — Minimal, Bauhaus-inspired, geometric\n- **Paper & Ink** — Literary, drop caps, pull quotes',
    },
    'architecture': {
        "description": 'This skill uses **progressive disclosure** — the main `SKILL.',
        "guidance": 'This skill uses **progressive disclosure** — the main `SKILL.md` is a concise map (~180 lines), with supporting files loaded on-demand only when needed:\n\n| File                      | Purpose                        | Loaded When               |\n| ------------------------- | ------------------------------ | ------------------------- |\n| `SKILL.md`                | Core workflow and rules        | Always (skill invocation) |\n| `STYLE_PRESETS.md`        | 12 curated visual presets      | Phase 2 (style selection) |\n| `viewport-base.css`       | Mandatory responsive CSS       | Phase 3 (generation)      |\n| `html-template.md`        | HTML structure and JS features | Phase 3 (generation)      |\n| `animation-patterns.md`   | CSS/JS animation reference     | Phase 3 (generation)      |\n| `scripts/extract-pptx.py` | PPT content extraction         | Phase 4 (conversion)      |\n| `scripts/deploy.sh`       | Deploy to Vercel               | Phase 6 (sharing)         |\n| `scripts/export-pdf.sh`   | Export slides to PDF           | Phase 6 (sharing)         |\n\nThis design follows [OpenAI\'s harness engineering](https://openai.com/index/harness-engineering/) principle: "give the agent a map, not a 1,000-page instruction manual."',
    },
    'philosophy': {
        "description": 'This skill was born from the belief that:\n\n1.',
        "guidance": "This skill was born from the belief that:\n\n1. **You don't need to be a designer to make beautiful things.** You just need to react to what you see.\n\n2. **Dependencies are debt.** A single HTML file will work in 10 years. A React project from 2019? Good luck.\n\n3. **Generic is forgettable.** Every presentation should feel custom-crafted, not template-generated.\n\n4. **Comments are kindness.** Code should explain itself to future-you (or anyone else who opens it).",
    },
    'sharing-your-presentations': {
        "description": 'After creating a presentation, the skill offers two ways to share it:\n\n### Deploy to a Live URL\n\nOne command deploys your slides to a permanent, shareable URL that works on any device — phones, tablet',
        "guidance": "After creating a presentation, the skill offers two ways to share it:\n\n### Deploy to a Live URL\n\nOne command deploys your slides to a permanent, shareable URL that works on any device — phones, tablets, laptops:\n\n```bash\nbash scripts/deploy.sh ./my-deck/\n# or\nbash scripts/deploy.sh ./presentation.html\n```\n\nUses [Vercel](https://vercel.com) (free tier). The skill walks you through signup and login if it's your first time.\n\n### Export to PDF\n\nConvert your slides to a PDF for email, Slack, Notion, or printing:\n\n```bash\nbash scripts/export-pdf.sh ./my-deck/index.html\nbash scripts/export-pdf.sh ./presentation.html ./output.pdf\n```\n\nUses [Playwright](https://playwright.dev) to screenshot each slide at 1920×1080 and combine into a PDF. Installs automatically if needed. Animations are not preserved (it's a static snapshot).",
    },
    'requirements': {
        "description": '- [Claude Code](https://claude.',
        "guidance": '- [Claude Code](https://claude.ai/claude-code) CLI\n- For PPT conversion: Python with `python-pptx` library\n- For URL deployment: Node.js + Vercel account (free)\n- For PDF export: Node.js (Playwright installs automatically)',
    },
    'credits': {
        "description": 'Created by [@zarazhangrui](https://github.',
        "guidance": 'Created by [@zarazhangrui](https://github.com/zarazhangrui) with Claude Code.\n\nInspired by the "Vibe Coding" philosophy — building beautiful things without being a traditional software engineer.',
    },
    'license': {
        "description": 'MIT — Use it, modify it, share it.',
        "guidance": 'MIT — Use it, modify it, share it.',
    },
}


@mcp.tool()
def list_frontend_slides_skills() -> dict:
    """List all available frontend_slides skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_frontend_slides_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific frontend_slides skill."""
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
    hint = get_presentation_hint('frontend_slides', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@frontend_slides",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'frontend_slides',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
