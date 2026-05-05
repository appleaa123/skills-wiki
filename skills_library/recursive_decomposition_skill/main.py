"""Skill: recursive_decomposition_skill."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("recursive-decomposition-skill")


_SKILLS: dict[str, dict] = {
    'the-problem': {
        "description": "When analyzing large codebases, processing many documents, or aggregating information across dozens of files, Claude's context window becomes a bottleneck.",
        "guidance": 'When analyzing large codebases, processing many documents, or aggregating information across dozens of files, Claude\'s context window becomes a bottleneck. As context grows, **"context rot"** degrades performance:\n\n- Missed details in long documents\n- Decreased accuracy on information retrieval\n- Hallucinated connections between distant content\n- Degraded reasoning over large evidence sets',
    },
    'the-solution': {
        "description": "This skill implements **Recursive Language Model (RLM)** strategies from [Zhang, Kraska, and Khattab's 2025 research](https://arxiv.",
        "guidance": "This skill implements **Recursive Language Model (RLM)** strategies from [Zhang, Kraska, and Khattab's 2025 research](https://arxiv.org/abs/2512.24601), enabling Claude Code to handle inputs **up to 2 orders of magnitude beyond normal context limits**.\n\nInstead of cramming everything into context, Claude learns to:\n\n1. **Filter** — Narrow search space before deep analysis\n2. **Chunk** — Partition inputs strategically\n3. **Recurse** — Spawn sub-agents for independent segments\n4. **Verify** — Re-check answers on smaller, focused windows\n5. **Synthesize** — Aggregate results programmatically\n\n---",
    },
    'what-it-does': {
        "description": '| Task Type | Without Skill | With Skill |\n|-----------|---------------|------------|\n| Analyze 100+ files | Context overflow / degraded results | Systematic coverage via decomposition |\n| Multi-docum',
        "guidance": '| Task Type | Without Skill | With Skill |\n|-----------|---------------|------------|\n| Analyze 100+ files | Context overflow / degraded results | Systematic coverage via decomposition |\n| Multi-document QA | Missed information | Comprehensive extraction |\n| Codebase-wide search | Manual iteration | Parallel sub-agent analysis |\n| Information aggregation | Incomplete synthesis | Map-reduce pattern |\n\n### Real Test Results\n\nWe tested on the [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook) (196 files, 356MB):\n\n```\nTask: "Find all Anthropic API calling patterns across the codebase"\n\nResults:\n├── Files scanned: 142\n├── Files with API calls: 18\n├── Patterns identified: 8 distinct patterns\n├── Anti-patterns detected: 4\n└── Output: Comprehensive report with file:line references\n```\n\n---',
    },
    'installation': {
        "description": '### Via Claude Code Marketplace\n\n```bash\n# Add the marketplace\nclaude plugin marketplace add massimodeluisa/recursive-decomposition-skill\n\n# Install the plugin\nclaude plugin install recursive-decompos',
        "guidance": "### Via Claude Code Marketplace\n\n```bash\n# Add the marketplace\nclaude plugin marketplace add massimodeluisa/recursive-decomposition-skill\n\n# Install the plugin\nclaude plugin install recursive-decomposition@recursive-decomposition\n```\n\n### From Local Clone\n\n```bash\n# Clone the repository\ngit clone https://github.com/massimodeluisa/recursive-decomposition-skill.git ~/recursive-decomposition-skill\n\n# Add as local marketplace\nclaude plugin marketplace add ~/recursive-decomposition-skill\n\n# Install the plugin\nclaude plugin install recursive-decomposition\n```\n\n### Manual Installation (Skills Directory)\n\n```bash\n# Copy skill directly to Claude's skills directory\ncp -r plugins/recursive-decomposition/skills/recursive-decomposition ~/.claude/skills/\n```\n\nAfter installation, **restart Claude Code** for the skill to take effect.\n\n### Updating\n\n```bash\n# Update marketplace index\nclaude plugin marketplace update\n\n# Update the plugin\nclaude plugin update recursive-decomposition@recursive-decomposition\n```\n\n---",
    },
    'usage': {
        "description": 'The skill activates automatically when you describe tasks involving:\n\n- Large-scale file analysis (`"analyze all files in.',
        "guidance": 'The skill activates automatically when you describe tasks involving:\n\n- Large-scale file analysis (`"analyze all files in..."`)\n- Multi-document processing (`"aggregate information from..."`)\n- Codebase-wide searches (`"find all occurrences across..."`)\n- Long-context reasoning (`"summarize these 50 documents..."`)\n\n### Example Prompts\n\n```\n"Analyze error handling patterns across this entire codebase"\n\n"Find all TODO comments in the project and categorize by priority"\n\n"What API endpoints are defined across all route files?"\n\n"Summarize the key decisions from all meeting notes in /docs"\n\n"Find security vulnerabilities across all Python files"\n```\n\n### Trigger Phrases\n\nThe skill recognizes these patterns:\n- `"analyze all files"`\n- `"process this large document"`\n- `"aggregate information from"`\n- `"search across the codebase"`\n- Tasks involving 10+ files or 50k+ tokens\n\n---',
    },
    'when-to-use': {
        "description": 'The skill is designed for **complex, long-context tasks**.',
        "guidance": 'The skill is designed for **complex, long-context tasks**. Use it when:\n\n- Analyzing 10+ files simultaneously\n- Processing documents exceeding 50k tokens\n- Performing codebase-wide pattern analysis\n- Extracting information from multiple scattered sources\n- Multi-hop reasoning requiring evidence synthesis\n\n**When NOT to use:**\n\n- Single file edits → Direct processing is faster\n- Specific function lookup → Use Grep directly\n- Tasks < 30k tokens → Overhead not worth it\n- Time-critical operations → Latency matters more than completeness\n\n---',
    },
    'how-it-works': {
        "description": '### Decomposition Strategies\n\n#### 1.',
        "guidance": '### Decomposition Strategies\n\n#### 1. Filter Before Deep Analysis\n```\n1000 files → Glob filter → 100 files\n100 files  → Grep filter → 20 files\n20 files   → Deep analysis\n```\n**Result:** 50x reduction before expensive processing\n\n#### 2. Strategic Chunking\n- **Uniform:** Split by line count or natural boundaries\n- **Semantic:** Partition by logical units (functions, classes)\n- **Keyword-based:** Group by shared characteristics\n\n#### 3. Parallel Sub-Agents\n```\nMain Agent\n├── Sub-Agent 1 (Batch A) ─┐\n├── Sub-Agent 2 (Batch B) ─┼── Parallel\n├── Sub-Agent 3 (Batch C) ─┘\n└── Synthesize results\n```\n\n#### 4. Verification Pass\nRe-check synthesized answers against focused evidence to catch context rot errors.\n\n---',
    },
    'benchmarks': {
        "description": 'From the [RLM paper](https://arxiv.',
        "guidance": 'From the [RLM paper](https://arxiv.org/abs/2512.24601):\n\n| Task | Direct Model | With RLM | Improvement |\n|------|--------------|----------|-------------|\n| Multi-hop QA (6-11M tokens) | 70% | 91% | **+21%** |\n| Linear aggregation | Baseline | +28-33% | **Significant** |\n| Quadratic reasoning | <0.1% | 58% | **Massive** |\n| Context scaling | 2^14 tokens | 2^18 tokens | **16x** |\n\n**Cost:** RLM approaches are ~3x cheaper than summarization baselines while achieving superior quality.\n\n---',
    },
    'repository-structure': {
        "description": '```\nrecursive-decomposition-skill/\n├──.',
        "guidance": '```\nrecursive-decomposition-skill/\n├── .claude-plugin/\n│   └── marketplace.json          # Marketplace manifest\n├── plugins/\n│   └── recursive-decomposition/\n│       ├── .claude-plugin/\n│       │   └── plugin.json       # Plugin manifest\n│       ├── README.md             # Plugin documentation\n│       └── skills/\n│           └── recursive-decomposition/\n│               ├── SKILL.md      # Core skill instructions\n│               └── references/\n│                   ├── rlm-strategies.md\n│                   ├── cost-analysis.md\n│                   ├── codebase-analysis.md\n│                   └── document-aggregation.md\n├── assets/\n│   └── logo.png                  # Project logo\n├── AGENTS.md                     # Agent-facing docs\n├── CONTRIBUTING.md               # Contribution guidelines\n├── LICENSE\n└── README.md\n```\n\n---',
    },
    'skill-contents': {
        "description": '| File | Purpose |\n|------|---------|\n| [`SKILL.',
        "guidance": '| File | Purpose |\n|------|---------|\n| [`SKILL.md`](plugins/recursive-decomposition/skills/recursive-decomposition/SKILL.md) | Core decomposition strategies and patterns |\n| [`references/rlm-strategies.md`](plugins/recursive-decomposition/skills/recursive-decomposition/references/rlm-strategies.md) | Detailed techniques from the RLM paper |\n| [`references/cost-analysis.md`](plugins/recursive-decomposition/skills/recursive-decomposition/references/cost-analysis.md) | When to use recursive vs. direct approaches |\n| [`references/codebase-analysis.md`](plugins/recursive-decomposition/skills/recursive-decomposition/references/codebase-analysis.md) | Full walkthrough: multi-file error handling analysis |\n| [`references/document-aggregation.md`](plugins/recursive-decomposition/skills/recursive-decomposition/references/document-aggregation.md) | Full walkthrough: multi-document feature extraction |\n\n---',
    },
    'acknowledgments': {
        "description": 'This skill is based on the **Recursive Language Models** research paper.',
        "guidance": 'This skill is based on the **Recursive Language Models** research paper. Huge thanks to the authors for their groundbreaking work:\n\n<table>\n  <tr>\n    <td align="center">\n      <a href="https://x.com/a1zhang">\n        <b>Alex L. Zhang</b>\n      </a>\n      <br>\n      <a href="https://x.com/a1zhang">@a1zhang</a>\n      <br>\n      <sub>MIT CSAIL</sub>\n    </td>\n    <td align="center">\n      <a href="https://x.com/tim_kraska">\n        <b>Tim Kraska</b>\n      </a>\n      <br>\n      <a href="https://x.com/tim_kraska">@tim_kraska</a>\n      <br>\n      <sub>MIT Professor</sub>\n    </td>\n    <td align="center">\n      <a href="https://x.com/lateinteraction">\n        <b>Omar Khattab</b>\n      </a>\n      <br>\n      <a href="https://x.com/lateinteraction">@lateinteraction</a>\n      <br>\n      <sub>MIT CSAIL, Creator of DSPy</sub>\n    </td>\n  </tr>\n</table>\n\n### Paper\n\n> **Recursive Language Models**\n>\n> *Alex L. Zhang, Tim Kraska, Omar Khattab*\n>\n> arXiv:2512.24601 • December 2025\n>\n> We propose Recursive Language Models (RLMs), an inference technique enabling LLMs to handle prompts up to two orders of magnitude beyond model context windows through programmatic decomposition and recursive self-invocation over prompt segments.\n\n<p>\n  <a href="https://arxiv.org/abs/2512.24601"><img src="https://img.shields.io/badge/arXiv-2512.24601-b31b1b?style=for-the-badge" alt="arXiv Paper"></a>\n  <a href="https://arxiv.org/pdf/2512.24601"><img src="https://img.shields.io/badge/PDF-Download-blue?style=for-the-badge" alt="PDF Download"></a>\n</p>\n\n---',
    },
    'references': {
        "description": '- [Agent Skills Specification](https://agentskills.',
        "guidance": '- [Agent Skills Specification](https://agentskills.io/specification)\n- [Claude Code Documentation](https://docs.anthropic.com/claude-code)\n\n---',
    },
    'contributing': {
        "description": 'Contributions welcome! Please see [CONTRIBUTING.',
        "guidance": 'Contributions welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.\n\n---',
    },
    'author': {
        "description": '<p>\n  <a href="https://x.',
        "guidance": '<p>\n  <a href="https://x.com/massimodeluisa">\n    <img src="https://img.shields.io/badge/X-@massimodeluisa-000000?style=flat-square&logo=x" alt="X (Twitter)">\n  </a>\n  <a href="https://github.com/massimodeluisa">\n    <img src="https://img.shields.io/badge/GitHub-massimodeluisa-181717?style=flat-square&logo=github" alt="GitHub">\n  </a>\n</p>\n\n**Massimo De Luisa** — [@massimodeluisa](https://x.com/massimodeluisa)\n\n---',
    },
    'license': {
        "description": 'MIT License — see [LICENSE](LICENSE) for details.',
        "guidance": 'MIT License — see [LICENSE](LICENSE) for details.\n\n---',
    },
}


@mcp.tool()
def list_recursive_decomposition_skill_skills() -> dict:
    """List all available recursive_decomposition_skill skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_recursive_decomposition_skill_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific recursive_decomposition_skill skill."""
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
    hint = get_presentation_hint('recursive_decomposition_skill', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@recursive_decomposition_skill",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'recursive_decomposition_skill',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
