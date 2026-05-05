"""Skill: claude_memory_kit."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("claude-memory-kit")


_SKILLS: dict[str, dict] = {
    'the-problem': {
        "description": 'Every time you open Claude, it forgets everything.',
        "guidance": "Every time you open Claude, it forgets everything. Yesterday you locked the brand voice. Today you have to explain it again. Last week it helped you find the right campaign angle — this week you can't remember exactly how.\n\nThe first 10 minutes of every session go to re-explaining what Claude **already knew**.\n\n**Memory Kit fixes this. Free. Runs on top of your Claude Pro or Max subscription.**",
    },
    'quick-start': {
        "description": '```bash\ngit clone https://github.',
        "guidance": "```bash\ngit clone https://github.com/awrshift/claude-memory-kit.git my-projects\ncd my-projects\nclaude\n```\n\nThat's it. Claude sets itself up and asks a couple of questions (your name, what you're working on).\n\n> [!TIP]\n> Say `/tour` after install — Claude walks you through the system using your own files.\n\n---",
    },
    'before-after': {
        "description": '![](.',
        "guidance": '![](.github/assets/01-before-after.png)\n\n| | Without Memory Kit | With Memory Kit |\n|---|---|---|\n| **New session** | "What were we working on?" | Knows the project, recent decisions, current tasks |\n| **After 10 sessions** | Nothing accumulates | Searchable base of decisions, tones, patterns |\n| **Multiple clients** | Chaos | Each client has its own folder, everything in place |\n| **Context compaction** | Silently loses data | Hook blocks compaction until state is saved |\n| **Tomorrow morning** | "Remind me what we did?" | Already knows — auto-loaded on session start |\n\n---',
    },
    'your-day': {
        "description": '![](.',
        "guidance": '![](.github/assets/02-daily-workflow.png)\n\nThree steps. That\'s the entire workflow:\n\n### 1. Open a session\nClaude auto-loads context — project state, recent decisions, knowledge base. You do nothing.\n\n### 2. Work as usual\nTalk to Claude. Write copy. Do research. Lock the tone. Safety hooks run silently — they save progress every ~50 messages and before context compacts.\n\n### 3. Close the day\nWhen you\'re done — say `/close-day`. Claude **doesn\'t just** dump logs. It **audits** what happened today, compares it against accumulated memory, and proposes: "noticed you rejected em-dashes in three short copies this week — make it a tone-of-voice rule?". You say "yes". It writes.\n\n**Tomorrow you continue exactly where you left off.**\n\n---',
    },
    'memory-layers': {
        "description": '![](.',
        "guidance": '![](.github/assets/03-memory-layers.png)\n\nThree places memory lives. Agent writes all of them. Each layer answers a different question:\n\n| Layer | Answers | Written by |\n|---|---|---|\n| `daily/YYYY-MM-DD.md` | "what happened today" | Agent (via `/close-day`) |\n| `.claude/memory/MEMORY.md` | "what patterns repeat" | Agent — while you talk |\n| `knowledge/concepts/*.md` | "facts and rationale by topic" | Agent — after your "yes" on `/close-day` |\n| `.claude/rules/*.md` | "what must always / never happen" | Agent — after 6+ months of stable pattern |\n\n---',
    },
    'promotion-pipeline': {
        "description": '![](.',
        "guidance": '![](.github/assets/04-promotion-pipeline.png)\n\nA pattern\'s journey from observation to law. Agent-driven at every step. User says "yes" — agent writes the patch.\n\n- **Week 1:** Baseline patterns captured in `MEMORY.md`. Agent starts referencing.\n- **Week 2–4:** Repeated patterns surface as `/close-day` audit candidates. Wiki articles begin.\n- **Month 2+:** Stable patterns crystallise into `.claude/rules/`. Full knowledge base with search.\n\n---',
    },
    'multiple-clients': {
        "description": '![](.',
        "guidance": '![](.github/assets/05-multi-project.png)\n\nEach client = their own folder. Shared layers (rules, memory, wiki) load for every project. Per-project materials load when you name the project.\n\nSay "we\'re working on Nestlé" — Claude unloads other clients and loads that scope only.\n\n---',
    },
    'hooks-and-operators': {
        "description": '![](.',
        "guidance": '![](.github/assets/06-hooks-and-operators.png)\n\nFive hooks run silently — they survive your context across compaction and crashes. Five slash operators give you direct control.\n\nEverything in plain text files. No databases. No external services. `git checkout` restores anything.\n\n---',
    },
    'faq': {
        "description": "<details>\n<summary><b>I'm not a programmer.",
        "guidance": '<details>\n<summary><b>I\'m not a programmer. Will this work?</b></summary>\n\nYes. You talk to Claude in plain language. "Read the client brief and propose three newsletter topics" — works. Install is one command.\n\n</details>\n\n<details>\n<summary><b>How much does it cost?</b></summary>\n\nThe kit itself is free, open source. You need a Claude Pro or Max subscription (which you probably already have). No additional cost.\n\n</details>\n\n<details>\n<summary><b>Is my data private?</b></summary>\n\nYes. Everything is stored on your computer in plain text files. Nothing leaves.\n\n</details>\n\n<details>\n<summary><b>Can I use it with an in-progress project?</b></summary>\n\nYes. On install, tell Claude you already have a project — it analyses it and integrates.\n\n</details>\n\n<details>\n<summary><b>What if I forget to run /close-day?</b></summary>\n\nNothing breaks. Safety hooks save progress automatically. `/close-day` is the cherry on top — a deliberate end-of-day audit. Not critical.\n\n</details>\n\n<details>\n<summary><b>What if I accidentally break a memory file?</b></summary>\n\nEverything is in git. `git checkout .claude/memory/` reverts in a second. The kit\'s principle is "user only talks, Claude writes" — you shouldn\'t be editing these files manually anyway.\n\n</details>\n\n<details>\n<summary><b>What if I\'m migrating from v3?</b></summary>\n\nDon\'t try to upgrade an old project in place. Clone v4 into a new folder and tell Claude: "I have an old v3 project, help me migrate". It walks you through.\n\n</details>\n\n---',
    },
    'what-s-inside': {
        "description": '```\nREADME.',
        "guidance": "```\nREADME.md               ← You are here\nLICENSE                 ← MIT\nCLAUDE.md               ← Agent's brain — who it is, how it works\nSKILL.md                ← Metadata for skill aggregators\nprojects/               ← Real client / product folders (tasks + materials)\nexperiments/            ← Sandbox for hypotheses + prototypes (date-named)\ndaily/                  ← Daily logs (private by default, gitignored)\nknowledge/              ← Knowledge base (grows over time)\ncontext/                ← Session-to-session handoff\n.claude/                ← Kit core: memory, hooks, skills, rules\n.kit/                   ← Documentation about the kit ITSELF (version\n                          history, architecture, contributor guide).\n                          Safe to delete after onboarding — it's about\n                          the kit, not your project.\n```\n\n**`projects/` vs `experiments/`** — `projects/<name>/` for real client work (polished, indefinite lifetime, patterns promote to rules); `experiments/<name>-YYYYMMDD/` for hypotheses and prototypes (rough OK, days-to-weeks lifetime, distill into projects/concepts on close, then delete). Full spec: [`experiments/README.md`](experiments/README.md).\n\n**Full architecture:** [.kit/ARCHITECTURE.md](.kit/ARCHITECTURE.md)\n**Version history:** [.kit/CHANGELOG.md](.kit/CHANGELOG.md)\n**Contributing:** [.kit/CONTRIBUTING.md](.kit/CONTRIBUTING.md)\n\n---",
    },
    'origin': {
        "description": 'Ideas from [Andrej Karpathy](https://karpathy.',
        "guidance": 'Ideas from [Andrej Karpathy](https://karpathy.ai/) and [Cole Medin](https://github.com/coleam00). Rebuilt around Anthropic-native Claude Code primitives.\n\n700+ real sessions across 7+ projects. This is what survived all the iterations.',
    },
    'help': {
        "description": 'Issues and PRs welcome.',
        "guidance": 'Issues and PRs welcome. See [.kit/CONTRIBUTING.md](.kit/CONTRIBUTING.md).',
    },
    'license': {
        "description": 'MIT — see [LICENSE](LICENSE).',
        "guidance": 'MIT — see [LICENSE](LICENSE).',
    },
}


@mcp.tool()
def list_claude_memory_kit_skills() -> dict:
    """List all available claude_memory_kit skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_claude_memory_kit_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific claude_memory_kit skill."""
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
    hint = get_presentation_hint('claude_memory_kit', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@claude_memory_kit",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'claude_memory_kit',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
