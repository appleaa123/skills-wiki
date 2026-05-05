"""Skill: tutor_skill."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("tutor-skill")


_SKILLS: dict[str, dict] = {
    'how-it-works': {
        "description": '```\n  Documents / Code                    Obsidian                    Quiz Session\n ┌──────────────────┐           ┌──────────────────┐          ┌──────────────────┐\n │  PDF, MD, HTML,  │  /tutor   │ ',
        "guidance": '```\n  Documents / Code                    Obsidian                    Quiz Session\n ┌──────────────────┐           ┌──────────────────┐          ┌──────────────────┐\n │  PDF, MD, HTML,  │  /tutor   │   StudyVault/    │  /tutor  │  4 questions per  │\n │  EPUB, source    │──setup──▶ │   structured     │────────▶ │  round, graded,   │\n │  code projects   │           │   interlinked    │          │  concept tracking  │\n └──────────────────┘           │   notes + MOC    │          └────────┬─────────┘\n                                └──────────────────┘                   │\n                                         ▲                             │\n                                         └─────── progress updates ────┘\n```',
    },
    'skills-overview': {
        "description": '| Skill | Command | Purpose | Input | Output |\n|-------|---------|---------|-------|--------|\n| **tutor-setup** | `/tutor-setup` | Generate a StudyVault | Documents or source code | Obsidian vault wit',
        "guidance": '| Skill | Command | Purpose | Input | Output |\n|-------|---------|---------|-------|--------|\n| **tutor-setup** | `/tutor-setup` | Generate a StudyVault | Documents or source code | Obsidian vault with notes, dashboards, practice questions |\n| **tutor** | `/tutor` | Interactive quiz tutor | An existing StudyVault | Quiz sessions with concept-level progress tracking |',
    },
    'quick-start': {
        "description": '### One-line install (recommended)\n\n```bash\nnpx skills add RoundTable02/tutor-skills\n```\n\n> Requires [npx skills](https://github.',
        "guidance": '### One-line install (recommended)\n\n```bash\nnpx skills add RoundTable02/tutor-skills\n```\n\n> Requires [npx skills](https://github.com/vercel-labs/skills) — works with Claude Code, Cursor, Windsurf, and more.\n\n### Manual install\n\n```bash\ngit clone https://github.com/RoundTable02/tutor-skills.git\ncd tutor-skills\n./install.sh\n```\n\n### Step 1: Generate a StudyVault\n\n```bash\ncd ~/study-materials/          # or any source code project\nclaude\n> /tutor-setup\n```\n\n### Step 2: Start Quizzing\n\n```bash\nclaude\n> /tutor\n```\n\n---',
    },
    'tutor-setup': {
        "description": 'Transforms knowledge sources into a structured Obsidian StudyVault.',
        "guidance": 'Transforms knowledge sources into a structured Obsidian StudyVault. Mode is auto-detected:\n\n| Marker Found | Mode |\n|---|---|\n| `package.json`, `pom.xml`, `build.gradle`, `Cargo.toml`, `go.mod`, etc. | Codebase Mode |\n| No project markers | Document Mode |\n\n### Document Mode\n\nTurns PDFs, text files, web pages, and other sources into comprehensive study notes.\n\n- Auto-scans working directory for source files (PDF, TXT, MD, HTML, EPUB)\n- Extracts and analyzes content with verified source mapping\n- Generates concept notes with comparison tables, ASCII diagrams, and exam patterns\n- Creates practice questions with hidden answers (active recall via fold callouts)\n- Builds a dashboard with Map of Content (MOC), Quick Reference, and Exam Traps\n- Full interlinking with `[[wiki-links]]` across all notes\n\n**Phases**\n\n| Phase | Name | Description |\n|-------|------|-------------|\n| D1 | Source Discovery | Scan, extract, and verify source content mapping |\n| D2 | Content Analysis | Build topic hierarchy and dependency map |\n| D3 | Tag Standard | Define English kebab-case tag registry |\n| D4 | Vault Structure | Create numbered folders per topic |\n| D5 | Dashboard | MOC, Quick Reference, Exam Traps |\n| D6 | Concept Notes | Structured notes with tables, diagrams, callouts |\n| D7 | Practice Questions | Active recall with fold callouts (8+ per topic) |\n| D8 | Interlinking | Cross-reference all notes with wiki-links |\n| D9 | Self-Review | Verify against quality checklist |\n\n**Generated structure**\n\n```\nStudyVault/\n  00-Dashboard/          # MOC + Quick Reference + Exam Traps\n  01-<Topic1>/           # Concept notes + practice questions\n  02-<Topic2>/\n  ...\n```\n\n### Codebase Mode\n\nGenerates a new-developer onboarding vault from a source code project.\n\n- Auto-detects tech stack, architecture patterns, and module boundaries\n- Traces request flows and data flows end-to-end\n- Creates per-module notes with key files, public interfaces, and dependency maps\n- Generates onboarding exercises (code reading, configuration, debugging, extension)\n- Builds a dashboard with architecture overview, module map, API surface, and getting started guide\n\n**Phases**\n\n| Phase | Name | Description |\n|-------|------|-------------|\n| C1 | Project Exploration | Scan files, detect tech stack, map layout |\n| C2 | Architecture Analysis | Identify patterns, trace flows, map modules |\n| C3 | Tag Standard | Define `#arch-*`, `#module-*`, `#pattern-*` registry |\n| C4 | Vault Structure | Create dashboard + per-module folders |\n| C5 | Dashboard | MOC with module map, API surface, getting started |\n| C6 | Module Notes | Purpose, key files, interface, flow, dependencies |\n| C7 | Exercises | Code reading, config, debugging, extension tasks |\n| C8 | Interlinking | Cross-link all modules and exercises |\n| C9 | Self-Review | Verify against quality checklist |\n\n**Generated structure**\n\n```\nStudyVault/\n  00-Dashboard/          # MOC + Quick Reference + Getting Started\n  01-Architecture/       # System overview, request flow, data flow\n  02-<Module1>/          # Per-module notes\n  03-<Module2>/\n  ...\n  NN-DevOps/             # Build, deploy, CI/CD\n  NN+1-Exercises/        # Onboarding exercises\n```\n\n---',
    },
    'tutor': {
        "description": "Interactive quiz tutor that tracks what you know and don't know at the **concept level**.",
        "guidance": "Interactive quiz tutor that tracks what you know and don't know at the **concept level**. Works with any StudyVault generated by `tutor-setup`.\n\n### Session Types\n\n| Type | When Available | Focus |\n|------|----------------|-------|\n| Diagnostic | Unmeasured areas (⬜) exist | Broad assessment of new areas |\n| Drill weak areas | Weak areas (🟥/🟨) exist | Targeted practice on struggles |\n| Choose a section | Always | Study any area on demand |\n| Hard-mode review | All areas 🟩/🟦 | Challenge mastered material |\n\n### Quiz Flow\n\n1. Detects your StudyVault and reads the learning dashboard\n2. Presents session options based on your current proficiency\n3. Delivers 4 questions per round (4 options each, zero hints)\n4. Grades answers and explains mistakes\n5. Updates concept files and dashboard automatically\n\n### Progress Tracking\n\nProficiency is tracked per area with emoji badges:\n\n| Badge | Level | Rate |\n|-------|-------|------|\n| 🟥 | Weak | 0–39% |\n| 🟨 | Fair | 40–69% |\n| 🟩 | Good | 70–89% |\n| 🟦 | Mastered | 90–100% |\n| ⬜ | Unmeasured | No data |\n\nConcept-level tracking stores attempts, correct count, last tested date, and error notes for wrong answers — so drill sessions rephrase missed concepts in new contexts.\n\n---",
    },
    'the-learning-cycle': {
        "description": '```\n           ┌────────────────────────────┐\n           │   /tutor-setup             │\n           │   Generate StudyVault      │\n           └──────────┬─────────────────┘\n                      │\n    ',
        "guidance": '```\n           ┌────────────────────────────┐\n           │   /tutor-setup             │\n           │   Generate StudyVault      │\n           └──────────┬─────────────────┘\n                      │\n                      ▼\n           ┌────────────────────────────┐\n           │   Read & review notes      │\n           │   in Obsidian              │\n           └──────────┬─────────────────┘\n                      │\n                      ▼\n           ┌────────────────────────────┐\n           │   /tutor                   │\n           │   Take diagnostic quiz     │◀──────────┐\n           └──────────┬─────────────────┘           │\n                      │                              │\n                      ▼                              │\n           ┌────────────────────────────┐           │\n           │   Review weak areas        │           │\n           │   in Obsidian              │           │\n           └──────────┬─────────────────┘           │\n                      │                              │\n                      ▼                              │\n           ┌────────────────────────────┐           │\n           │   /tutor                   │           │\n           │   Drill weak concepts      │───────────┘\n           └────────────────────────────┘\n```',
    },
    'requirements': {
        "description": '- [Claude Code CLI](https://docs.',
        "guidance": '- [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code) installed and configured\n- [Obsidian](https://obsidian.md/) (recommended) to open and navigate the generated vault',
    },
    'repository-structure': {
        "description": '```\ntutor-skill/\n├── skills/\n│   ├── tutor-setup/              # Vault generation skill\n│   │   ├── SKILL.',
        "guidance": '```\ntutor-skill/\n├── skills/\n│   ├── tutor-setup/              # Vault generation skill\n│   │   ├── SKILL.md\n│   │   └── references/\n│   │       ├── templates.md\n│   │       ├── codebase-workflow.md\n│   │       ├── quality-checklist.md\n│   │       └── codebase-templates.md\n│   └── tutor/                    # Interactive quiz skill\n│       ├── SKILL.md\n│       └── references/\n│           └── quiz-rules.md\n├── examples/\n├── install.sh\n├── uninstall.sh\n├── README.md\n└── LICENSE\n```',
    },
    'uninstall': {
        "description": '```bash.',
        "guidance": '```bash\n./uninstall.sh\n```\n\nOr manually:\n\n```bash\nrm -rf ~/.claude/skills/tutor-setup\nrm -rf ~/.claude/skills/tutor\n```',
    },
    'license': {
        "description": '[MIT](LICENSE).',
        "guidance": '[MIT](LICENSE)',
    },
}


@mcp.tool()
def list_tutor_skill_skills() -> dict:
    """List all available tutor_skill skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_tutor_skill_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific tutor_skill skill."""
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
    hint = get_presentation_hint('tutor_skill', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@tutor_skill",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'tutor_skill',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
