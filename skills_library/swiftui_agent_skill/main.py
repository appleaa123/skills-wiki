"""Skill: swiftui_agent_skill."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("swiftui-agent-skill")


_SKILLS: dict[str, dict] = {
    'who-this-is-for': {
        "description": '- Teams adopting modern SwiftUI APIs who want quick, correct defaults\n- Developers reviewing or refactoring SwiftUI views and data flow\n- Anyone shipping performant lists, scrolling, sheets, and navig',
        "guidance": '- Teams adopting modern SwiftUI APIs who want quick, correct defaults\n- Developers reviewing or refactoring SwiftUI views and data flow\n- Anyone shipping performant lists, scrolling, sheets, and navigation in SwiftUI',
    },
    'see-also-my-other-skills': {
        "description": '- [Swift Concurrency Expert](https://github.',
        "guidance": '- [Swift Concurrency Expert](https://github.com/AvdLee/Swift-Concurrency-Agent-Skill)\n- [Core Data Expert](https://github.com/AvdLee/Core-Data-Agent-Skill)\n- [Swift Testing Expert](https://github.com/AvdLee/Swift-Testing-Agent-Skill)',
    },
    'how-to-use-this-skill': {
        "description": '### Option A: Using skills.',
        "guidance": '### Option A: Using skills.sh\nInstall this skill with a single command:\n\n```bash\nnpx skills add https://github.com/avdlee/swiftui-agent-skill --skill swiftui-expert-skill\n```\n\nFor more information, [visit the skills.sh platform page](https://skills.sh/avdlee/swiftui-agent-skill/swiftui-expert-skill).\n\nThen use the skill in your AI agent, for example:\n> Use the swiftui expert skill and review the current SwiftUI code for state-management and performance improvements\n\n### Option B: Claude Code Plugin\n\n#### Personal Usage\nTo install this Skill for your personal use in Claude Code:\n\n1. Add the marketplace:\n\n```bash\n/plugin marketplace add AvdLee/SwiftUI-Agent-Skill\n```\n\n2. Install the Skill:\n\n```bash\n/plugin install swiftui-expert@swiftui-expert-skill\n```\n\n### Option C: Cursor plugin (coming soon)\nThis repository is now packaged for Cursor plugin submission, but the marketplace listing is not live yet.\n\nOnce approved, you\'ll be able to install it from the Cursor Marketplace.\n\n#### Project Configuration\nTo automatically provide this Skill to everyone working in a repository, configure the repository\'s `.claude/settings.json`:\n\n```json\n{\n  "enabledPlugins": {\n    "swiftui-expert@swiftui-expert-skill": true\n  },\n  "extraKnownMarketplaces": {\n    "swiftui-expert-skill": {\n      "source": {\n        "source": "github",\n        "repo": "AvdLee/SwiftUI-Agent-Skill"\n      }\n    }\n  }\n}\n```\n\nWhen team members open the project, Claude Code will prompt them to install the Skill.\n\n### Option D: Codex / OpenAI-compatible tools\nThis repository includes an `agents/openai.yaml` manifest. Copy or symlink the `swiftui-expert-skill/` folder into your Codex skills directory:\n\n```bash\ncp -R swiftui-expert-skill/ "$CODEX_HOME/skills/swiftui-expert-skill"\n```\n\nSee [Codex skills documentation](https://developers.openai.com/codex/skills/) for details on where to save skills.\n\n### Option E: Using pi package manager\n\nInstall via [pi](https://github.com/badlogic/pi-mono):\n```bash\npi install https://github.com/AvdLee/SwiftUI-Agent-Skill\n```\n\nThe skill will be available automatically in pi sessions.\n\n### Option F: Manual install\n1) **Clone** this repository.\n2) **Install or symlink** the `swiftui-expert-skill/` folder following your tool’s official skills installation docs (see links below).\n3) **Use your AI tool** as usual and ask it to use the “swiftui-expert” skill for SwiftUI tasks.\n\n#### Where to Save Skills\nFollow your tool’s official documentation, here are a few popular ones:\n- **Codex:** [Where to save skills](https://developers.openai.com/codex/skills/#where-to-save-skills)\n- **Claude:** [Using Skills](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)\n- **Cursor:** [Plugins documentation](https://cursor.com/docs/plugins) or [Enabling Skills](https://cursor.com/docs/context/skills#enabling-skills)\n\n**How to verify**:\n\nYour agent should reference the workflow/checklists in `swiftui-expert-skill/SKILL.md` and jump into the relevant reference file for your task.',
    },
    'what-s-inside': {
        "description": 'This skill covers the full surface of SwiftUI development -- from state management and view composition to Swift Charts, macOS multi-window scenes, animations, and iOS 26+ Liquid Glass -- without bloa',
        "guidance": "This skill covers the full surface of SwiftUI development -- from state management and view composition to Swift Charts, macOS multi-window scenes, animations, and iOS 26+ Liquid Glass -- without bloating your agent's task context. Reference files load on demand, so your agent gets deep guidance only for the topic at hand.\n\n- **State management** -- property wrapper selection, `@Observable`, data flow patterns\n- **View composition** -- extraction patterns, container views, identity stability\n- **Performance** -- hot-path optimization, lazy loading, `@Observable` granularity\n- **Lists & ForEach** -- stable identity, Table, inline filtering pitfalls\n- **Navigation & sheets** -- NavigationStack, NavigationSplitView, Inspector, enum-based sheets\n- **Swift Charts** -- marks, axes, selection, styling, accessibility, Chart3D\n- **Animations** -- implicit/explicit, transitions, phase/keyframe, `@Animatable` macro\n- **macOS** -- scenes, window styling, Table, HSplitView, AppKit interop\n- **Liquid Glass** -- iOS 26+ glass effects, containers, fallback patterns\n- **Accessibility** -- VoiceOver, Dynamic Type, grouping, traits\n- **Image optimization** -- AsyncImage, downsampling, caching\n- **Latest APIs** -- deprecated-to-modern migration guide (iOS 15+ through iOS 26+)\n- **Instruments trace recording & analysis** -- bundled `xctrace` toolchain for diagnosing hangs, hitches, and expensive SwiftUI view updates (see below)\n\nNon-opinionated: focuses on correctness and performance, not architecture or code style.",
    },
    'recording-analysing-instruments-traces': {
        "description": 'Unlike the other reference files — which are text guidance — this part of the skill ships an executable Python toolchain that wraps `xctrace`.',
        "guidance": "Unlike the other reference files — which are text guidance — this part of the skill ships an executable Python toolchain that wraps `xctrace`. It lets the agent **record** a new `.trace` and **analyse** an existing one end-to-end: the parser reads the Time Profiler, Hangs, Animation Hitches, SwiftUI updates, and SwiftUI cause-graph lanes, correlates hangs/hitches with main-thread samples, and emits JSON + markdown so the agent can reason over structured data instead of the raw `xctrace export` firehose.\n\n**When it triggers:**\n\n- A `.trace` path appears in the prompt (analysis).\n- The user asks to record, profile, or capture a session (recording).\n\n**What the agent can then ask:**\n\n```text\nAnalyse ~/Desktop/MyApp.trace and tell me what's wrong.\n\nFocus analysis on what happens right after the 'feed loaded' log.\n\nWhich of my SwiftUI views is responsible for the hang around 6s?\n\nRecord a new trace: attach to MyApp on my iPhone — I'll tell you when I'm done.\n```\n\n**Under the hood:**\n\n- `scripts/record_trace.py` — wraps `xctrace record`. Supports attach / launch / all-processes, stop-file for agent-driven sessions, time-limits, JSON device & template discovery.\n- `scripts/analyze_trace.py` — runs the five-lane analysis. Discovery modes `--list-logs`, `--list-signposts`, `--fanin-for` let the agent scope to a time window or trace a specific view back to its invalidation sources. `--window START_MS:END_MS` restricts every lane to a slice.\n- `scripts/instruments_parser/` — one module per lane (`time_profiler`, `hangs`, `hitches`, `swiftui`, `causes`), plus cross-lane `correlate` and a markdown `summary` renderer. Pure stdlib Python 3; only external dep is `xctrace` (ships with Xcode).\n\n**Key diagnostic:** `main_running_coverage_pct` on each hang/hitch correlation. < 25 % → main thread was blocked (I/O, lock, sync await); ≥ 75 % → CPU-bound. This single metric separates two radically different fix paths.\n\nFull guidance: [`swiftui-expert-skill/references/trace-analysis.md`](swiftui-expert-skill/references/trace-analysis.md) and [`swiftui-expert-skill/references/trace-recording.md`](swiftui-expert-skill/references/trace-recording.md).",
    },
    'skill-structure': {
        "description": '<!-- BEGIN REFERENCE STRUCTURE -->\n```text\nswiftui-expert-skill/\n  SKILL.',
        "guidance": '<!-- BEGIN REFERENCE STRUCTURE -->\n```text\nswiftui-expert-skill/\n  SKILL.md\n  references/\n    accessibility-patterns.md - Accessibility traits, grouping, Dynamic Type, and VoiceOver\n    animation-advanced.md - Performance, interpolation, and complex animation chains\n    animation-basics.md - Core animation concepts, implicit/explicit animations, timing\n    animation-transitions.md - View transitions, matchedGeometryEffect, and state changes\n    charts-accessibility.md - Charts accessibility, fallback strategies, and WWDC sessions\n    charts.md - Swift Charts marks, axes, selection, styling, composition, and Chart3D\n    focus-patterns.md\n    image-optimization.md - AsyncImage usage, downsampling, caching\n    latest-apis.md\n    layout-best-practices.md - Layout patterns and GeometryReader alternatives\n    liquid-glass.md - iOS 26+ glass effects and fallback patterns\n    list-patterns.md - ForEach identity and list performance\n    macos-scenes.md - Scene lifecycle, multi-window setups, and menu bar scenes on macOS\n    macos-views.md - macOS-specific SwiftUI views and platform differences from iOS\n    macos-window-styling.md - Window chrome, toolbar, and title bar styling in SwiftUI\n    performance-patterns.md - Hot-path optimizations and update control\n    scroll-patterns.md - ScrollViewReader and programmatic scrolling\n    sheet-navigation-patterns.md - Sheets and type-safe navigation\n    state-management.md - Property wrapper selection and data flow\n    view-structure.md - View extraction and composition patterns\n```\n<!-- END REFERENCE STRUCTURE -->',
    },
    'maintenance': {
        "description": 'The repository includes a maintenance skill for keeping API guidance current:\n\n```text.',
        "guidance": 'The repository includes a maintenance skill for keeping API guidance current:\n\n```text\n.agents/skills/update-swiftui-apis/\n  SKILL.md               - Workflow for scanning Apple docs and updating latest-apis.md\n  references/\n    scan-manifest.md     - Categorized API areas, doc paths, and search queries to scan\n```\n\nUse this skill after new iOS or Xcode releases to refresh the deprecated API reference. It requires the [Sosumi MCP](https://github.com/NSHipster/sosumi.ai) to be available. See `AGENTS.md` or `CONTRIBUTING.md` for details.\n\nNote: only `swiftui-expert-skill` is intended to be published in the Cursor plugin. The maintenance skill remains a repository workflow utility.',
    },
    'contributing': {
        "description": 'Contributions are welcome! This repository follows the [Agent Skills open format](https://agentskills.',
        "guidance": 'Contributions are welcome! This repository follows the [Agent Skills open format](https://agentskills.io/home), which has specific structural requirements.\n\nPlease read [CONTRIBUTING.md](CONTRIBUTING.md) for:\n- How to contribute improvements to `SKILL.md` and the reference files\n- Format requirements and quality standards\n- Pull request process',
    },
    'acknowledgments': {
        "description": 'Several SwiftUI guidelines in this skill were inspired by or derived from the following works:\n\n- [Skills](https://github.',
        "guidance": 'Several SwiftUI guidelines in this skill were inspired by or derived from the following works:\n\n- [Skills](https://github.com/Dimillian/Skills) by [Thomas Ricouard](https://github.com/Dimillian) — a collection of SwiftUI-focused Codex skills covering UI patterns, performance auditing, and Liquid Glass.\n- [SwiftLee SwiftUI articles](https://www.avanderlee.com/category/swiftui/) and [Swift articles](https://www.avanderlee.com/category/swift/) by [Antoine van der Lee](https://www.avanderlee.com) — practical SwiftUI best practices covering state management, accessibility, view composition, performance debugging, image optimization, and more.\n- [Swift Charts Examples](https://github.com/jordibruin/Swift-Charts-Examples) by [Jordi Bruin](https://x.com/jordibruin) — a comprehensive collection of Swift Charts examples covering line, bar, area, range, heat map, and point charts with accessibility and customization patterns. Used with permission.',
    },
    'about-the-authors': {
        "description": 'Created by [Antoine van der Lee](https://www.',
        "guidance": 'Created by [Antoine van der Lee](https://www.avanderlee.com) and [Omar Elsayed](https://www.swiftdifferently.com). With years of experience in Swift & SwiftUI, this skill distills practical knowledge into actionable guidance for AI assistants. Antoine [published tens of articles on SwiftUI](https://www.avanderlee.com/category/swiftui/) on his blog called SwiftLee.',
    },
    'resources': {
        "description": '- [Story behind this skill](https://www.',
        "guidance": '- [Story behind this skill](https://www.swiftdifferently.com/blog/swiftui/How%20I%20stopped-resisting-ai-and-atarted-teaching-it)',
    },
    'license': {
        "description": 'This skill is open-source and available under the MIT License.',
        "guidance": 'This skill is open-source and available under the MIT License. See [LICENSE](LICENSE) for details.',
    },
}


@mcp.tool()
def list_swiftui_agent_skill_skills() -> dict:
    """List all available swiftui_agent_skill skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_swiftui_agent_skill_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific swiftui_agent_skill skill."""
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
    hint = get_presentation_hint('swiftui_agent_skill', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@swiftui_agent_skill",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'swiftui_agent_skill',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
