"""Skill: Architecture."""

from fastmcp import FastMCP

mcp = FastMCP("architecture")


_GUIDANCE = {'display_name': 'Architecture', 'description': '```\nrednote-bootstrap/\n├── SKILL.', 'guidance': '```\nrednote-bootstrap/\n├── SKILL.md                          # Entry point: routing logic + workflow definition\n├── registry.json                     # Sub-Skill registry (auto-maintained)\n├── LICENSE                           # Apache 2.0\n├── xhs-auth-state.json               # XiaoHongShu auth state persistence (auto-generated)\n├── reference/\n│   ├── platforms.md                  # Platform adapter config (DOM structure, interaction patterns)\n│   ├── search-first-skill.md         # Core research engine (5-phase workflow)\n│   └── agent-browser/                # Browser automation capability (dependency)\n├── templates/\n│   └── sub-skill-template.md         # Sub-Skill generation template\n└── generated-skills/                 # Generated sub-Skills (knowledge base, continuously growing)\n    ├── xiaohongshu-publishing-guide/\n    │   └── SKILL.md\n    ├── xiaohongshu-daily-account-nurturing/\n    │   └── SKILL.md\n    └── .../\n```\n\nThe system consists of three layers:\n\n| Layer | Component | Responsibility |\n|-------|-----------|----------------|\n| **Routing** | `SKILL.md` + `registry.json` | Understand user intent, match existing sub-Skills or trigger new research |\n| **Research Engine** | `search-first-skill.md` | 5-phase automated research (analyze → collect → evaluate → distill → register) |\n| **Knowledge Base** | `generated-skills/` | Ever-growing collection of sub-Skills, each an independent executable operations guide |\n\n---'}


@mcp.tool()
def get_guidance() -> dict:
    """Get the full guidance for this skill."""
    return _GUIDANCE
