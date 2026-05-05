"""Skill: taste_skill."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("taste-skill")


_SKILLS: dict[str, dict] = {
    'disclaimer': {
        "description": 'Taste Skill has no official token, coin, or crypto project.',
        "guidance": 'Taste Skill has no official token, coin, or crypto project. Any token using my name, image, or project is unaffiliated and not endorsed by me.\n\n<p align="center"><sub><a href="#disclaimer">Disclaimer</a> · <a href="#installing">Install</a> · <a href="#skills">Skills</a> · <a href="#settings-taste-skill-only">Settings</a> · <a href="#examples">Examples</a> · <a href="#support-the-project">Sponsor</a> · <a href="#research">Research</a> · <a href="#common-questions">FAQ</a> · <a href="#license">License</a></sub></p>',
    },
    'feedback-contributions': {
        "description": 'We would love your feedback.',
        "guidance": 'We would love your feedback. Suggestions and bug reports:\n\n- Open a Pull Request or Issue on GitHub  \n- DM [@lexnlin](https://x.com/lexnlin) or [@blueemi99](https://x.com/blueemi99)  \n- Email us at [hello@tasteskill.dev](mailto:hello@tasteskill.dev)',
    },
    'installing': {
        "description": 'The [`npx skills add`](https://github.',
        "guidance": 'The [`npx skills add`](https://github.com/vercel-labs/agent-skills) CLI scans the `skills/` folder in this repo, so **all skills below (code and image-generation) install the same way.**\n\n```bash\nnpx skills add https://github.com/Leonxlnx/taste-skill\n```\n\nInstall a single skill by name (example):\n\n```bash\nnpx skills add https://github.com/Leonxlnx/taste-skill --skill "imagegen-frontend-mobile"\n```\n\nYou can also copy any `SKILL.md` into your project or paste it into ChatGPT / Codex conversations.',
    },
    'skills': {
        "description": 'Each skill does one job; you do not need all of them at once.',
        "guidance": 'Each skill does one job; you do not need all of them at once. **Implementation skills** output code. **Image-generation skills** output reference images only.\n\n| Skill | Description |\n| --- | --- |\n| **taste-skill** | Default all-rounder for premium frontend output without locking one narrow visual style. |\n| **gpt-taste** | Stricter variant for GPT/Codex: higher layout variance, stronger GSAP direction, aggressive anti-slop. |\n| **image-to-code-skill** | Image-first pipeline: generate site references, analyze them, then implement the frontend to match. |\n| **redesign-skill** | Existing projects: audit the UI first, then fix layout, spacing, hierarchy, styling. |\n| **soft-skill** | Polished, calm, expensive UI with softer contrast, whitespace, premium fonts, spring motion. |\n| **output-skill** | When the model ships half-finished work: full output, no placeholder comments. |\n| **minimalist-skill** | Editorial product UI (Notion/Linear vibes), restrained palette, crisp structure. |\n| **brutalist-skill** | ⚠️ `BETA` Hard mechanical language: Swiss type, sharp contrast, experimental layout. |\n| **stitch-skill** | Google Stitch-compatible rules, including optional `DESIGN.md` export format. |\n\n### Image generation skills\n\nThese produce design images only (no code). Use with ChatGPT Images, Codex image mode, or any agent that generates images.\n\n| Skill | Description |\n| --- | --- |\n| **imagegen-frontend-web** | Website comps: hero, landing, multi-section with strong typography, spacing, anti-slop art direction. |\n| **imagegen-frontend-mobile** | Mobile screens and flows: iOS/Android/cross-platform, mockups, readable type, coherent sets. |\n| **brandkit** | Brand-kit boards: logo directions, palettes, type, identity applications across categories. |\n\n### Which one should I use?\n\n- Start with **taste-skill** for the safest general default.  \n- Use **gpt-taste** when you want the stricter GPT/Codex-oriented rules and motion/layout enforcement.  \n- Use **image-to-code-skill** for image → analyze → code website workflows.  \n- Use **redesign-skill** to improve an existing codebase instead of greenfield styling.  \n- Add **soft-skill**, **minimalist-skill**, or **brutalist-skill** when the visual direction is already chosen.  \n- Add **output-skill** if the agent keeps truncating output.  \n- Use **imagegen-frontend-web**, **imagegen-frontend-mobile**, or **brandkit** when the deliverable is **images** (comps, flows, identity boards), then pass results to your coding agent.\n\n### Image-first tip\n\nFor **image-to-code-skill**, state the pipeline in the prompt, e.g.: `follow the skill: generate images, then analyze, then code`.\n\n### ChatGPT Images and Codex\n\nAttach or paste **`imagegen-frontend-web`**, **`imagegen-frontend-mobile`**, or **`brandkit`** and ask for the frames you need, then feed the renders to Codex, Cursor, or Claude Code. Use **image-to-code-skill** when you want one workflow that both generates references and implements the site in code.',
    },
    'settings-taste-skill-only': {
        "description": 'Numbers at the top of the file are 1-10 dials:\n\n- **DESIGN_VARIANCE**: Layout experimentation (lower: centered/clean · higher: asymmetric/modern).',
        "guidance": 'Numbers at the top of the file are 1-10 dials:\n\n- **DESIGN_VARIANCE**: Layout experimentation (lower: centered/clean · higher: asymmetric/modern).\n- **MOTION_INTENSITY**: Animation depth (lower: hover · higher: scroll/magnetic).\n- **VISUAL_DENSITY**: Information per viewport (lower: spacious · higher: dense dashboards).',
    },
    'examples': {
        "description": 'Created with taste-skill:\n\n<p>\n  <img src="examples/floria-top.',
        "guidance": 'Created with taste-skill:\n\n<p>\n  <img src="examples/floria-top.webp" width="400" />\n  <img src="examples/floria-bottom.webp" width="400" />\n</p>',
    },
    'support-the-project': {
        "description": 'If Taste Skill helps you, consider sponsoring:\n\n[Sponsor on GitHub](https://github.',
        "guidance": 'If Taste Skill helps you, consider sponsoring:\n\n[Sponsor on GitHub](https://github.com/sponsors/Leonxlnx)\n\n### Current Sponsors\n\n<a href="https://github.com/robinebers"><img src="https://github.com/robinebers.png" width="40" height="40" style="border-radius:50%" alt="robinebers" title="robinebers" /></a>\n<a href="https://github.com/JKc66"><img src="https://github.com/JKc66.png" width="40" height="40" style="border-radius:50%" alt="JKc66" title="JKc66" /></a>\n<a href="https://github.com/u2393696078-rgb"><img src="https://github.com/u2393696078-rgb.png" width="40" height="40" style="border-radius:50%" alt="u2393696078-rgb" title="u2393696078-rgb" /></a>\n<a href="https://github.com/a-human-created-this"><img src="https://github.com/a-human-created-this.png" width="40" height="40" style="border-radius:50%" alt="a-human-created-this" title="a-human-created-this" /></a>\n<a href="https://github.com/AtharvaJaiswal005"><img src="https://github.com/AtharvaJaiswal005.png" width="40" height="40" style="border-radius:50%" alt="AtharvaJaiswal005" title="AtharvaJaiswal005" /></a>\n<a href="https://github.com/ghughes7"><img src="https://github.com/ghughes7.png" width="40" height="40" style="border-radius:50%" alt="ghughes7" title="ghughes7" /></a>\n<a href="https://github.com/mccun934"><img src="https://github.com/mccun934.png" width="40" height="40" style="border-radius:50%" alt="mccun934" title="mccun934" /></a>\n<a href="https://github.com/navanchauhan"><img src="https://github.com/navanchauhan.png" width="40" height="40" style="border-radius:50%" alt="navanchauhan" title="navanchauhan" /></a>\n\n<p align="center">\n <a href="https://www.star-history.com/leonxlnx/taste-skill">\n  <picture>\n   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/badge?repo=Leonxlnx/taste-skill&theme=dark" />\n   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/badge?repo=Leonxlnx/taste-skill" />\n   <img alt="Star History Rank" src="https://api.star-history.com/badge?repo=Leonxlnx/taste-skill" />\n  </picture>\n </a>\n</p>',
    },
    'research': {
        "description": 'Background writing that shaped these skills lives in [`research/`](research/).',
        "guidance": 'Background writing that shaped these skills lives in [`research/`](research/).',
    },
    'common-questions': {
        "description": '**How is this different from other AI design skills?**  \nMultiple specialized variants, adjustable dials in key skills, anti-repetition rules informed by dedicated research.',
        "guidance": '**How is this different from other AI design skills?**  \nMultiple specialized variants, adjustable dials in key skills, anti-repetition rules informed by dedicated research. All are framework agnostic across major coding agents.\n\n**Does it work with React, Vue, Svelte?**  \nYes. Rules target design intent, not a single framework API.\n\n**What is SKILL.md?**  \nA portable instruction file agents can load automatically; install via `npx skills add` or by copying into a repo or conversation.\n\n**Do image-generation skills install with `npx skills add`?**  \nYes. They live under `skills/` alongside the code skills so the same CLI discovers them.',
    },
    'license': {
        "description": '[MIT License](LICENSE) · Copyright (c) 2026 Leonxlnx.',
        "guidance": '[MIT License](LICENSE) · Copyright (c) 2026 Leonxlnx',
    },
}


@mcp.tool()
def list_taste_skill_skills() -> dict:
    """List all available taste_skill skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_taste_skill_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific taste_skill skill."""
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
    hint = get_presentation_hint('taste_skill', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@taste_skill",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'taste_skill',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
