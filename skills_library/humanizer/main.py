"""Skill: humanizer."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("humanizer")


_SKILLS: dict[str, dict] = {
    'installation': {
        "description": "### Claude Code\n\nClone directly into Claude Code's skills directory:\n\n```bash\nmkdir -p ~/.",
        "guidance": "### Claude Code\n\nClone directly into Claude Code's skills directory:\n\n```bash\nmkdir -p ~/.claude/skills\ngit clone https://github.com/blader/humanizer.git ~/.claude/skills/humanizer\n```\n\nOr copy the skill file manually if you already have this repo cloned:\n\n```bash\nmkdir -p ~/.claude/skills/humanizer\ncp SKILL.md ~/.claude/skills/humanizer/\n```\n\n### OpenCode\n\nClone directly into OpenCode's skills directory:\n\n```bash\nmkdir -p ~/.config/opencode/skills\ngit clone https://github.com/blader/humanizer.git ~/.config/opencode/skills/humanizer\n```\n\nOr copy the skill file manually if you already have this repo cloned:\n\n```bash\nmkdir -p ~/.config/opencode/skills/humanizer\ncp SKILL.md ~/.config/opencode/skills/humanizer/\n```\n\n> **Note:** OpenCode also scans `~/.claude/skills/` for compatibility, so a single clone into `~/.claude/skills/humanizer/` works for both tools.",
    },
    'usage': {
        "description": '### Claude Code\n\n```\n/humanizer\n\n[paste your text here]\n```\n\n### OpenCode\n\n```\n/humanizer\n\n[paste your text here]\n```\n\nOr ask the model to humanize text directly in either tool:\n\n```\nPlease humanize t',
        "guidance": '### Claude Code\n\n```\n/humanizer\n\n[paste your text here]\n```\n\n### OpenCode\n\n```\n/humanizer\n\n[paste your text here]\n```\n\nOr ask the model to humanize text directly in either tool:\n\n```\nPlease humanize this text: [your text]\n```\n\n### Voice Calibration\n\nTo match your personal writing style, provide a sample of your own writing:\n\n```\n/humanizer\n\nHere\'s a sample of my writing for voice matching:\n[paste 2-3 paragraphs of your own writing]\n\nNow humanize this text:\n[paste AI text to humanize]\n```\n\nThe skill will analyze your sentence rhythm, word choices, and quirks, then apply them to the rewrite instead of producing generic "clean" output.',
    },
    'overview': {
        "description": 'Based on [Wikipedia\'s "Signs of AI writing"](https://en.',
        "guidance": 'Based on [Wikipedia\'s "Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) guide, maintained by WikiProject AI Cleanup. This comprehensive guide comes from observations of thousands of instances of AI-generated text.\n\nThe skill also includes a final "obviously AI generated" audit pass and a second rewrite, to catch lingering AI-isms in the first draft.\n\n### Key Insight from Wikipedia\n\n> "LLMs use statistical algorithms to guess what should come next. The result tends toward the most statistically likely result that applies to the widest variety of cases."',
    },
    '29-patterns-detected-with-before-after-examples': {
        "description": '### Content Patterns\n\n| # | Pattern | Before | After |\n|---|---------|--------|-------|\n| 1 | **Significance inflation** | "marking a pivotal moment in the evolution of.',
        "guidance": '### Content Patterns\n\n| # | Pattern | Before | After |\n|---|---------|--------|-------|\n| 1 | **Significance inflation** | "marking a pivotal moment in the evolution of..." | "was established in 1989 to collect regional statistics" |\n| 2 | **Notability name-dropping** | "cited in NYT, BBC, FT, and The Hindu" | "In a 2024 NYT interview, she argued..." |\n| 3 | **Superficial -ing analyses** | "symbolizing... reflecting... showcasing..." | Remove or expand with actual sources |\n| 4 | **Promotional language** | "nestled within the breathtaking region" | "is a town in the Gonder region" |\n| 5 | **Vague attributions** | "Experts believe it plays a crucial role" | "according to a 2019 survey by..." |\n| 6 | **Formulaic challenges** | "Despite challenges... continues to thrive" | Specific facts about actual challenges |\n\n### Language Patterns\n\n| # | Pattern | Before | After |\n|---|---------|--------|-------|\n| 7 | **AI vocabulary** | "Actually... additionally... testament... landscape... showcasing" | "also... remain common" |\n| 8 | **Copula avoidance** | "serves as... features... boasts" | "is... has" |\n| 9 | **Negative parallelisms / tailing negations** | "It\'s not just X, it\'s Y", "..., no guessing" | State the point directly |\n| 10 | **Rule of three** | "innovation, inspiration, and insights" | Use natural number of items |\n| 11 | **Synonym cycling** | "protagonist... main character... central figure... hero" | "protagonist" (repeat when clearest) |\n| 12 | **False ranges** | "from the Big Bang to dark matter" | List topics directly |\n| 13 | **Passive voice / subjectless fragments** | "No configuration file needed" | Name the actor when it helps clarity |\n\n### Style Patterns\n\n| # | Pattern | Before | After |\n|---|---------|--------|-------|\n| 14 | **Em dash overuse** | "institutions—not the people—yet this continues—" | Prefer commas or periods |\n| 15 | **Boldface overuse** | "**OKRs**, **KPIs**, **BMC**" | "OKRs, KPIs, BMC" |\n| 16 | **Inline-header lists** | "**Performance:** Performance improved" | Convert to prose |\n| 17 | **Title Case Headings** | "Strategic Negotiations And Partnerships" | "Strategic negotiations and partnerships" |\n| 18 | **Emojis** | "🚀 Launch Phase: 💡 Key Insight:" | Remove emojis |\n| 19 | **Curly quotes** | `said “the project”` | `said “the project”` |\n| 26 | **Hyphenated word pairs** | “cross-functional, data-driven, client-facing” | Drop hyphens on common word pairs |\n| 27 | **Persuasive authority tropes** | "At its core, what matters is..." | State the point directly |\n| 28 | **Signposting announcements** | "Let\'s dive in", "Here\'s what you need to know" | Start with the content |\n| 29 | **Fragmented headers** | "## Performance" + "Speed matters." | Let the heading do the work |\n\n### Communication Patterns\n\n| # | Pattern | Before | After |\n|---|---------|--------|-------|\n| 20 | **Chatbot artifacts** | "I hope this helps! Let me know if..." | Remove entirely |\n| 21 | **Cutoff disclaimers** | "While details are limited in available sources..." | Find sources or remove |\n| 22 | **Sycophantic tone** | "Great question! You\'re absolutely right!" | Respond directly |\n\n### Filler and Hedging\n\n| # | Pattern | Before | After |\n|---|---------|--------|-------|\n| 23 | **Filler phrases** | "In order to", "Due to the fact that" | "To", "Because" |\n| 24 | **Excessive hedging** | "could potentially possibly" | "may" |\n| 25 | **Generic conclusions** | "The future looks bright" | Specific plans or facts |',
    },
    'full-example': {
        "description": '**Before (AI-sounding):**\n> Great question! Here is an essay on this topic.',
        "guidance": "**Before (AI-sounding):**\n> Great question! Here is an essay on this topic. I hope this helps!\n>\n> AI-assisted coding serves as an enduring testament to the transformative potential of large language models, marking a pivotal moment in the evolution of software development. In today's rapidly evolving technological landscape, these groundbreaking tools—nestled at the intersection of research and practice—are reshaping how engineers ideate, iterate, and deliver, underscoring their vital role in modern workflows.\n>\n> At its core, the value proposition is clear: streamlining processes, enhancing collaboration, and fostering alignment. It's not just about autocomplete; it's about unlocking creativity at scale, ensuring that organizations can remain agile while delivering seamless, intuitive, and powerful experiences to users. The tool serves as a catalyst. The assistant functions as a partner. The system stands as a foundation for innovation.\n>\n> Industry observers have noted that adoption has accelerated from hobbyist experiments to enterprise-wide rollouts, from solo developers to cross-functional teams. The technology has been featured in The New York Times, Wired, and The Verge. Additionally, the ability to generate documentation, tests, and refactors showcases how AI can contribute to better outcomes, highlighting the intricate interplay between automation and human judgment.\n>\n> - 💡 **Speed:** Code generation is significantly faster, reducing friction and empowering developers.\n> - 🚀 **Quality:** Output quality has been enhanced through improved training, contributing to higher standards.\n> - ✅ **Adoption:** Usage continues to grow, reflecting broader industry trends.\n>\n> While specific details are limited based on available information, it could potentially be argued that these tools might have some positive effect. Despite challenges typical of emerging technologies—including hallucinations, bias, and accountability—the ecosystem continues to thrive. In order to fully realize this potential, teams must align with best practices.\n>\n> In conclusion, the future looks bright. Exciting times lie ahead as we continue this journey toward excellence. Let me know if you’d like me to expand on any section!\n\n**After (Humanized):**\n> AI coding assistants can speed up the boring parts of the job. They're great at boilerplate: config files and the little glue code you don't want to write. They can also help you sketch a test, but you still have to read it.\n>\n> The dangerous part is how confident the suggestions look. I've accepted code that compiled and passed lint, then discovered later it missed the point because I stopped paying attention.\n>\n> If you treat it like autocomplete and review every line, it's useful. If you use it to avoid thinking, it will help you ship bugs faster.\n>\n> The only real backstop is tests. Without them, you're mostly judging vibes.",
    },
    'references': {
        "description": '- [Wikipedia: Signs of AI writing](https://en.',
        "guidance": '- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) - Primary source\n- [WikiProject AI Cleanup](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup) - Maintaining organization',
    },
    'version-history': {
        "description": '- **2.',
        "guidance": '- **2.5.1** - Added a passive-voice / subjectless-fragment rule, raising the total to 29 patterns\n- **2.5.0** - Added patterns for persuasive framing, signposting, and fragmented headers; expanded negative parallelisms to cover tailing negations; tightened wording around em dash overuse; fixed frontmatter wording to use "filler phrases"\n- **2.4.0** - Added voice calibration: match the user\'s personal writing style from samples\n- **2.3.0** - Added pattern #25: hyphenated word pair overuse\n- **2.2.0** - Added a final "obviously AI generated" audit + second-pass rewrite prompts\n- **2.1.1** - Fixed pattern #18 example (curly quotes vs straight quotes)\n- **2.1.0** - Added before/after examples for all 24 patterns\n- **2.0.0** - Complete rewrite based on raw Wikipedia article content\n- **1.0.0** - Initial release',
    },
    'license': {
        "description": 'MIT.',
        "guidance": 'MIT',
    },
}


@mcp.tool()
def list_humanizer_skills() -> dict:
    """List all available humanizer skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_humanizer_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific humanizer skill."""
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
    hint = get_presentation_hint('humanizer', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@humanizer",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'humanizer',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
