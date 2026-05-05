"""Skill: skill_optimizer."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("skill-optimizer")


_SKILLS: dict[str, dict] = {
    'what-it-does': {
        "description": "**6 scored dimensions** (weighted into composite score):\n\n| Dimension | What's Measured |\n|-----------|----------------|\n| **Trigger Rate** | How often is the skill actually invoked vs.",
        "guidance": "**6 scored dimensions** (weighted into composite score):\n\n| Dimension | What's Measured |\n|-----------|----------------|\n| **Trigger Rate** | How often is the skill actually invoked vs. how often it should be? |\n| **User Reaction** | Does the user accept, correct, or reject the skill after invocation? |\n| **Workflow Completion** | How far through the skill's defined steps does execution get? |\n| **Static Quality** | 14 checks: YAML safety, CSO compliance, info position, word count, etc. |\n| **Undertrigger** | Missed opportunities — user needed the skill but it wasn't invoked |\n| **Token Economics** | Cost-effectiveness and progressive disclosure tier compliance |\n\n**3 qualitative dimensions** (reported but not scored):\n\n| Dimension | What's Measured |\n|-----------|----------------|\n| **Overtrigger** | False positives — skill fired but user didn't want it |\n| **Cross-Skill Conflicts** | Trigger keyword overlap and contradictory guidance between skills |\n| **Environment Consistency** | Broken file paths, missing CLI tools, non-existent directories |",
    },
    'installation': {
        "description": "Copy the command below and paste it directly into your agent's chat — it will install automatically:\n\n### Claude Code\n\n```\nInstall the skill-optimizer skill from https://github.",
        "guidance": "Copy the command below and paste it directly into your agent's chat — it will install automatically:\n\n### Claude Code\n\n```\nInstall the skill-optimizer skill from https://github.com/hqhq1025/skill-optimizer\n```\n\n### Codex\n\n```\nInstall the skill-optimizer skill from https://github.com/hqhq1025/skill-optimizer into ~/.codex/skills/\n```\n\n### Other Agents (Cursor, OpenCode, Gemini CLI, etc.)\n\n```\nInstall the skill-optimizer skill from https://github.com/hqhq1025/skill-optimizer into ~/.agents/skills/\n```\n\n<details>\n<summary>Manual install</summary>\n\n```bash\n# Claude Code\ngit clone https://github.com/hqhq1025/skill-optimizer.git /tmp/skill-optimizer\ncp -r /tmp/skill-optimizer/skills/skill-optimizer ~/.claude/skills/\nrm -rf /tmp/skill-optimizer\n\n# Codex\ngit clone https://github.com/hqhq1025/skill-optimizer.git /tmp/skill-optimizer\ncp -r /tmp/skill-optimizer/skills/skill-optimizer ~/.codex/skills/\nrm -rf /tmp/skill-optimizer\n\n# Shared (any agent)\ngit clone https://github.com/hqhq1025/skill-optimizer.git /tmp/skill-optimizer\ncp -r /tmp/skill-optimizer/skills/skill-optimizer ~/.agents/skills/\nrm -rf /tmp/skill-optimizer\n```\n\n</details>",
    },
    'usage': {
        "description": '```\n/optimize-skill              # Scan all skills\n/optimize-skill my-skill     # Single skill\n/optimize-skill skill-a skill-b  # Multiple skills\n```\n\nThe skill generates a diagnostic report with:\n- *',
        "guidance": '```\n/optimize-skill              # Scan all skills\n/optimize-skill my-skill     # Single skill\n/optimize-skill skill-a skill-b  # Multiple skills\n```\n\nThe skill generates a diagnostic report with:\n- **Overview table** — all skills at a glance with scores\n- **P0 Fixes** — blocking issues that must be resolved\n- **P1 Improvements** — experience improvements\n- **P2 Optimizations** — optional tweaks\n- **Per-skill diagnostics** — all 8 dimensions for each skill',
    },
    'multi-platform-session-analysis': {
        "description": 'The optimizer auto-detects available platforms and scans session data from all of them:\n\n| Platform | Skills Path | Session Data Path |\n|----------|------------|-------------------|\n| Claude Code | `~',
        "guidance": 'The optimizer auto-detects available platforms and scans session data from all of them:\n\n| Platform | Skills Path | Session Data Path |\n|----------|------------|-------------------|\n| Claude Code | `~/.claude/skills/` | `~/.claude/projects/**/*.jsonl` |\n| Codex | `~/.codex/skills/` | `~/.codex/sessions/**/*.jsonl` |\n| Shared | `~/.agents/skills/` | — |',
    },
    'research-background': {
        "description": 'The analysis dimensions are grounded in peer-reviewed research:\n\n| Research | Key Finding | Applied In |\n|----------|-------------|------------|\n| [Memento-Skills](https://arxiv.',
        "guidance": 'The analysis dimensions are grounded in peer-reviewed research:\n\n| Research | Key Finding | Applied In |\n|----------|-------------|------------|\n| [Memento-Skills](https://arxiv.org/abs/2603.18743) (2026) | Skills as structured files require accurate routing; unrouted skills cannot self-improve via the read-write learning loop | Undertrigger detection, compounding risk assessment |\n| [MCP Description Quality](https://arxiv.org/abs/2602.18914) (2026) | Well-written descriptions achieve 72% tool selection rate vs. 20% random baseline (3.6x improvement) | Description quality checks, evidence-based rewrite suggestions |\n| [Lost in the Middle](https://arxiv.org/abs/2307.03172) (Liu et al., TACL 2024) | LLM attention follows a U-shaped curve — middle content is ignored | Critical info position check |\n| [Prompt Format Impact](https://arxiv.org/abs/2411.10541) (He et al., 2024) | Format changes alone cause 9-40% performance variance | Static quality analysis |\n| [IFEval](https://arxiv.org/abs/2311.07911) (Zhou et al., 2023) | LLMs struggle with multi-constraint prompts | Trigger condition count check |\n| [Meincke et al.](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5357179) (2025) | Persuasion directives have inconsistent effects across models | MUST/NEVER density guidance |',
    },
    'how-it-works': {
        "description": '```\nIdentify target skills (scan ~/.',
        "guidance": '```\nIdentify target skills (scan ~/.claude/skills/, ~/.codex/skills/, ~/.agents/skills/)\n        ↓\nCollect session data (auto-detect platform, scan JSONL transcripts)\n        ↓\nRun 8 analysis dimensions (6 scored + 3 qualitative)\n        ↓\nCompute composite scores (weighted average of 6 scored dimensions)\n        ↓\nOutput report with P0/P1/P2 prioritized fixes\n```\n\n**Scored dimensions (weighted average):**\n- Trigger rate: 25%\n- User reaction: 20%\n- Workflow completion: 15%\n- Static quality: 15%\n- Undertrigger: 15%\n- Token economics: 10%\n\n**Qualitative dimensions** (overtrigger, cross-skill conflicts, environment consistency) are reported with examples but do not affect the numeric score.',
    },
    'compatibility': {
        "description": 'Works with any agent that supports the [Agent Skills](https://agentskills.',
        "guidance": 'Works with any agent that supports the [Agent Skills](https://agentskills.io) open standard:\n- Claude Code\n- Codex\n- Cursor\n- OpenCode\n- Gemini CLI',
    },
    'community': {
        "description": '- [LINUX DO](https://linux.',
        "guidance": '- [LINUX DO](https://linux.do) — Where we first shared this project',
    },
    'license': {
        "description": 'MIT.',
        "guidance": 'MIT',
    },
}


@mcp.tool()
def list_skill_optimizer_skills() -> dict:
    """List all available skill_optimizer skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_skill_optimizer_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific skill_optimizer skill."""
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
    hint = get_presentation_hint('skill_optimizer', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@skill_optimizer",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'skill_optimizer',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
