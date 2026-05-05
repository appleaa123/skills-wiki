"""Skill: platform_design_skills."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("platform-design-skills")


_SKILLS: dict[str, dict] = {
    'available-skills': {
        "description": '### ios\n\nApple Human Interface Guidelines for iPhone.',
        "guidance": '### ios\n\nApple Human Interface Guidelines for iPhone. 67+ rules covering navigation, layout, accessibility, gestures, and iOS-specific components like tab bars, sheets, and Dynamic Island.\n\n**Use when:**\n- Building SwiftUI or UIKit interfaces for iPhone\n- Reviewing iOS app code for HIG compliance\n- Choosing between iOS navigation patterns\n- Implementing accessibility, Dark Mode, Dynamic Type\n\n### ipados\n\nApple HIG for iPad, covering multitasking, pointer support, sidebar navigation, keyboard shortcuts, and Stage Manager. Extends the iOS skill with iPad-specific patterns.\n\n**Use when:**\n- Building iPad-optimized interfaces\n- Implementing Split View, Slide Over, Stage Manager support\n- Adding pointer/trackpad and keyboard shortcut support\n- Designing responsive layouts for iPad screen sizes\n\n### macos\n\nApple HIG for Mac apps. Covers menu bars, window management, toolbars, keyboard-driven interaction, and the expectations of desktop power users.\n\n**Use when:**\n- Building macOS apps with SwiftUI or AppKit\n- Implementing menu bars, toolbars, and sidebars\n- Adding keyboard shortcuts and window management\n- Designing for Catalyst or native macOS\n\n### watchos\n\nApple HIG for Apple Watch. Covers glanceable interfaces, Digital Crown, complications, Always On display, and wrist-optimized interactions.\n\n**Use when:**\n- Building watchOS apps or complications\n- Designing for small screens and short interactions\n- Implementing health/fitness features on Watch\n\n### visionos\n\nApple HIG for Apple Vision Pro. Covers spatial UI, eye and hand input, windows, volumes, immersive spaces, and ornaments.\n\n**Use when:**\n- Building visionOS apps with RealityKit or SwiftUI\n- Designing for spatial computing and indirect gestures\n- Implementing immersive experiences\n\n### tvos\n\nApple HIG for Apple TV. Covers focus-based navigation, Siri Remote, Top Shelf, and living room viewing distances.\n\n**Use when:**\n- Building tvOS apps\n- Implementing focus-based navigation with Siri Remote\n- Designing for 10-foot viewing experiences\n\n### android\n\nGoogle Material Design 3 guidelines for Android. Covers Material You, dynamic color, navigation patterns, components, and Android-specific patterns.\n\n**Use when:**\n- Building Android apps with Jetpack Compose or XML layouts\n- Reviewing Android code for Material Design compliance\n- Implementing Material You and dynamic color\n- Choosing between Android navigation patterns\n\n### web\n\nWeb platform best practices covering responsive design, accessibility (WCAG), performance, progressive enhancement, and modern CSS/HTML patterns.\n\n**Use when:**\n- Building web interfaces with any framework\n- Auditing sites for accessibility compliance\n- Implementing responsive, performant web layouts\n- Reviewing web UI code for best practices',
    },
    'installation': {
        "description": '```bash\nnpx skills add ehmo/platform-design-skills\n```.',
        "guidance": '```bash\nnpx skills add ehmo/platform-design-skills\n```',
    },
    'contributing-pull-requests': {
        "description": '- Fork the repository and create a feature branch from the default branch.',
        "guidance": '- Fork the repository and create a feature branch from the default branch.\n- Keep PRs focused to one theme (one platform, one major design area, or one format rule set).\n- Update affected skill docs in `skills/<platform>/SKILL.md` and keep `metadata.json` entries aligned when behavior changes.\n- If adding or changing rule coverage, ensure:\n  - platform skill descriptions remain accurate,\n  - source signals in the skill files are still correct,\n  - and examples still reflect current platform behavior.\n- In the PR description include:\n  - what changed,\n  - why this matters for AI output quality,\n  - and a short before/after usage sample.\n- Suggested PR title format: `feat: ...`, `fix: ...`, `docs: ...`.\n\nExample PR checklist:\n\n- [ ] Scope matches the PR title\n- [ ] One platform or one rule family per PR\n- [ ] No broken relative links in touched files\n- [ ] AGENTS/skill assumptions still stated clearly\n- [ ] README and skill metadata remain consistent',
    },
    'usage': {
        "description": 'Skills activate automatically when agents detect platform-relevant tasks.',
        "guidance": 'Skills activate automatically when agents detect platform-relevant tasks.\n\n```\nReview this SwiftUI view for iOS HIG compliance\n```\n```\nCheck this Android Compose screen against Material Design\n```\n```\nAudit this web page for accessibility\n```',
    },
    'skill-structure': {
        "description": 'Each skill contains:\n- `SKILL.',
        "guidance": 'Each skill contains:\n- `SKILL.md` — Agent instructions with frontmatter metadata\n- `metadata.json` — Version, references, and abstract\n- `rules/` — Individual rule files with examples\n- `AGENTS.md` — Quick context for agent consumption',
    },
    'sources': {
        "description": '### Platform-normative sources\n\n- Apple Human Interface Guidelines (2025) — developer.',
        "guidance": '### Platform-normative sources\n\n- Apple Human Interface Guidelines (2025) — developer.apple.com/design/human-interface-guidelines\n- Material Design 3 — m3.material.io\n- Web Content Accessibility Guidelines (WCAG) 2.2 — w3.org/WAI/WCAG22/quickref\n- MDN Web Docs — developer.mozilla.org\n\n### Supporting HCI references\n\nThese are secondary references used to sharpen guidance around recognition over recall, visible waiting states, and input effort. They do not override Apple HIG, Material, or WCAG.\n\n- Stuart K. Card, Thomas P. Moran, and Allen Newell, *The Psychology of Human-Computer Interaction* (1983) — https://archive.org/details/psychologyofhuma0000card\n- Allen Newell and Stuart K. Card, *Prospects for Psychological Science in Human-Computer Interaction* (includes Model Human Processor summary and operating principles) — https://iiif.library.cmu.edu/file/Newell_box00042_fld03533_doc0001/Newell_box00042_fld03533_doc0001.pdf\n- Tiffany Jastrzembski and Neil Charness, *The Model Human Processor and the Older Adult: Parameter Estimation and Validation Within a Mobile Phone Task* (2007 / PMC) — https://pmc.ncbi.nlm.nih.gov/articles/PMC4591021/\n- Human Processor Model overview (discovery/reference pointer) — https://en.wikipedia.org/wiki/Human_processor_model',
    },
    'license': {
        "description": 'MIT.',
        "guidance": 'MIT',
    },
}


@mcp.tool()
def list_platform_design_skills_skills() -> dict:
    """List all available platform_design_skills skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_platform_design_skills_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific platform_design_skills skill."""
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
    hint = get_presentation_hint('platform_design_skills', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@platform_design_skills",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'platform_design_skills',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
