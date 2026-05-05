"""Skill: materials_simulation_skills."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("materials-simulation-skills")


_SKILLS: dict[str, dict] = {
    'table-of-contents': {
        "description": "- [The Problem](#the-problem)\n- [The Solution](#the-solution)\n- [What's Inside](#whats-inside)\n  - [Core Numerical Skills](#core-numerical-skills-skillscore-numerical)\n  - [Simulation Workflow Skills]",
        "guidance": "- [The Problem](#the-problem)\n- [The Solution](#the-solution)\n- [What's Inside](#whats-inside)\n  - [Core Numerical Skills](#core-numerical-skills-skillscore-numerical)\n  - [Simulation Workflow Skills](#simulation-workflow-skills-skillssimulation-workflow)\n  - [HPC Deployment Skills](#hpc-deployment-skills-skillshpc-deployment)\n  - [Ontology Skills](#ontology-skills-skillsontology)\n- [How Skills Work](#how-skills-work)\n- [Security](#security)\n- [Quick Start](#quick-start)\n- [Adding Skills to Your Agent](#adding-skills-to-your-agent)\n  - [Claude Code](#claude-code)\n  - [Gemini CLI](#gemini-cli)\n  - [OpenAI Codex](#openai-codex)\n  - [VS Code / GitHub Copilot](#vs-code--github-copilot)\n  - [Cursor](#cursor)\n  - [Other Agents](#other-agents)\n- [Repository Layout](#repository-layout)\n- [Contributing](#contributing)\n- [License](#license)\n- [Acknowledgements](#acknowledgements)\n\n---",
    },
    'the-problem': {
        "description": 'Simulation engineers repeat the same guidance to AI agents constantly: *"Check the CFL number before running," "Use Richardson extrapolation for grid convergence," "Exit code 2 means bad input.',
        "guidance": 'Simulation engineers repeat the same guidance to AI agents constantly: *"Check the CFL number before running," "Use Richardson extrapolation for grid convergence," "Exit code 2 means bad input."* General-purpose agents lack the domain knowledge to run reliable numerical simulations without heavy hand-holding.',
    },
    'the-solution': {
        "description": 'This project packages that domain knowledge into **skills** -- structured folders of instructions, scripts, and references that agents discover automatically and load on demand.',
        "guidance": "This project packages that domain knowledge into **skills** -- structured folders of instructions, scripts, and references that agents discover automatically and load on demand. Each skill teaches an agent a specific simulation competency, backed by validated Python scripts that produce reproducible results.\n\n```text\nYou: Check if dt=0.001 is stable for my advection problem with v=2.0 m/s and dx=0.01.\n\nAgent: I'll use the numerical-stability skill to check this.\n       [runs cfl_checker.py --dx 0.01 --dt 0.001 --velocity 2.0 --json]\n\n       CFL number = 0.2 (limit: 1.0) -- stable.\n       Recommended max dt = 0.005 with safety factor 1.0.\n```\n\nNo prompt engineering. No copy-pasting formulas. The agent finds the right skill, runs the script, and interprets the results.\n\n---",
    },
    'what-s-inside': {
        "description": '**17 skills** | **67 scripts** | **932 tests** | **78 eval cases** | **312 assertions** | Cross-platform CI on Python 3.',
        "guidance": '**17 skills** | **67 scripts** | **932 tests** | **78 eval cases** | **312 assertions** | Cross-platform CI on Python 3.10-3.12\n\n### Core Numerical Skills (`skills/core-numerical/`)\n\nFoundational numerical methods and analysis tools.\n\n| Skill | What it does |\n|-------|-------------|\n| `numerical-stability` | CFL/Fourier analysis, von Neumann stability, stiffness detection, matrix conditioning |\n| `time-stepping` | Time integrator selection, adaptive step-size control, output scheduling |\n| `mesh-generation` | Mesh quality metrics (aspect ratio, skewness, orthogonality), refinement guidance |\n| `convergence-study` | Grid/time convergence analysis, Richardson extrapolation, GCI calculation |\n| `numerical-integration` | Quadrature rule selection, error estimation, adaptive stepping |\n| `differentiation-schemes` | Finite difference stencil generation, truncation error analysis, scheme comparison |\n| `linear-solvers` | Iterative/direct solver selection, preconditioner advice, convergence diagnostics |\n| `nonlinear-solvers` | Newton/quasi-Newton/fixed-point selection, globalization strategies, convergence diagnostics |\n\n### Simulation Workflow Skills (`skills/simulation-workflow/`)\n\nEnd-to-end simulation management and automation.\n\n| Skill | What it does |\n|-------|-------------|\n| `simulation-validator` | Pre-flight checks, runtime log monitoring, post-flight validation |\n| `parameter-optimization` | DOE sampling (LHS, factorial), optimizer selection, sensitivity analysis |\n| `simulation-orchestrator` | Parameter sweeps, batch campaign management, result aggregation |\n| `post-processing` | Field extraction, time series analysis, derived quantity computation |\n| `performance-profiling` | Timing analysis, scaling studies, memory profiling, bottleneck detection |\n\n### HPC Deployment Skills (`skills/hpc-deployment/`)\n\nDeployment and job submission tooling for running simulations on HPC systems.\n\n| Skill | What it does |\n|-------|-------------|\n| `slurm-job-script-generator` | Generate `sbatch` scripts, sanity-check resource requests, and standardize `#SBATCH` directives |\n\n### Ontology Skills (`skills/ontology/`)\n\nMaterials science ontology understanding, mapping, and validation.\n\n| Skill | What it does |\n|-------|-------------|\n| `ontology-explorer` | Parse OWL/XML ontologies, browse class hierarchies, look up properties, search concepts (CMSO, ASMO, OCDO ecosystem) |\n| `ontology-mapper` | Map natural-language materials terms and crystal parameters to ontology classes and properties (CMSO, ASMO) |\n| `ontology-validator` | Validate annotations against ontology constraints, check completeness, verify relationship domain/range |\n\n---',
    },
    'how-skills-work': {
        "description": 'Skills follow the open [Agent Skills standard](https://agentskills.',
        "guidance": "Skills follow the open [Agent Skills standard](https://agentskills.io/specification). Each skill is a folder with three tiers of content, loaded progressively to keep context efficient:\n\n```\nskills/core-numerical/numerical-stability/\n    SKILL.md              # Instructions + YAML metadata (loaded when skill triggers)\n    scripts/              # Python CLI tools (executed for reproducible results)\n        cfl_checker.py\n        von_neumann_analyzer.py\n        matrix_condition.py\n        stiffness_detector.py\n    references/           # Deep domain knowledge (loaded only when needed)\n        stability_criteria.md\n        common_pitfalls.md\n        scheme_catalog.md\n    evals/                # Evaluation suite per agentskills.io spec\n        evals.json        # Test cases with prompts, assertions, expected outputs\n    CHANGELOG.md          # Version history\n```\n\n1. **Discovery** -- The agent sees each skill's name and description at startup (~100 tokens per skill)\n2. **Activation** -- When a task matches, the agent loads the full `SKILL.md` with decision guidance, workflows, and CLI examples\n3. **Execution** -- Scripts run as subprocesses with `--json` output for structured, parseable results\n\nAll scripts are standalone CLI tools with `--help`, a pure-function core for testing, and consistent error handling (exit code 2 for bad input, 1 for runtime errors).\n\n---",
    },
    'security': {
        "description": 'All skills are hardened against the [OWASP Top 10 for LLM Applications](https://owasp.',
        "guidance": 'All skills are hardened against the [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/), with 75 dedicated security tests. Key safeguards:\n\n- **No shell access by default** -- Skills use `allowed-tools: Read, Write, Grep, Glob` (no `Bash`), preventing the agent from executing arbitrary commands when processing untrusted data\n- **Input validation at every boundary** -- Numeric parameters are bounds-checked and validated as finite; string inputs (parameter names, field names, term names) are validated against regex allowlists\n- **Safe file loading** -- All JSON/CSV/NPY loaders enforce file size limits (100-500 MB) and structure validation (dict root required); `np.load()` uses `allow_pickle=False`\n- **No `eval()`/`exec()`** -- Region condition parsing uses strict regex matching, never dynamic code execution\n- **Prompt injection resistance** -- String values extracted from external files are truncated and stripped of control characters before surfacing to the agent; phase names from logs are sanitized\n- **Command construction safety** -- `shlex.quote()` escapes paths interpolated into shell commands; command templates are validated against a shell-operator denylist\n- **ReDoS prevention** -- User-supplied regex patterns are length-capped and checked for catastrophic backtracking constructs\n\nEach skill documents its specific safeguards in a **Security** section within its `SKILL.md`, with standardized subsections for Input Validation, File Access, Tool Restrictions, and Safety Measures.\n\n### Security Risk Tiers\n\nEvery skill is classified by its tool access surface:\n\n| Tier | Criteria | Skills |\n|------|----------|-------|\n| **HIGH** | Has `Bash` (can execute scripts) | 9 skills — numerical-stability, time-stepping, convergence-study, differentiation-schemes, nonlinear-solvers, ontology-explorer, ontology-validator, simulation-validator, slurm-job-script-generator |\n| **MEDIUM** | Has `Write` but no `Bash` | 7 skills — linear-solvers, mesh-generation, numerical-integration, parameter-optimization, performance-profiling, post-processing, simulation-orchestrator |\n| **LOW** | Read/Grep/Glob only | 1 skill — ontology-mapper |\n\n---',
    },
    'quality-evaluation': {
        "description": 'Every skill includes an evaluation suite (`evals/evals.',
        "guidance": 'Every skill includes an evaluation suite (`evals/evals.json`) following the [agentskills.io evaluation spec](https://agentskills.io/skill-creation/evaluating-skills). Each suite contains 4-5 test cases with realistic prompts, expected outputs, and verifiable assertions.\n\n**Current metrics:** 78 eval test cases | 312 assertions | All 17 skills evaluated\n\nThe CI pipeline validates:\n- SKILL.md frontmatter (name, description < 1024 chars, metadata block)\n- Eval suite completeness (every skill has evals.json with ≥ 3 test cases)\n- Security section presence (all skills must have `## Security`)\n- Changelog existence (all skills must have CHANGELOG.md)\n\n---',
    },
    'quick-start': {
        "description": '### Install\n\n```bash\ngit clone https://github.',
        "guidance": '### Install\n\n```bash\ngit clone https://github.com/heshamfs/materials-simulation-skills.git\ncd materials-simulation-skills\npip install -r requirements-dev.txt\n```\n\n### Run the test suite\n\n```bash\npython -m pytest tests/ -v --tb=short          # All 932 tests\npython -m pytest tests/unit -v --tb=short       # Unit tests only\npython -m pytest tests/integration -v           # Integration tests only\n```\n\n---',
    },
    'adding-skills-to-your-agent': {
        "description": 'These skills follow the open [Agent Skills standard](https://agentskills.',
        "guidance": "These skills follow the open [Agent Skills standard](https://agentskills.io) and work across 20+ AI coding tools. Choose your agent below.\n\n### Claude Code\n\nCopy individual skills (or the whole `skills/` tree) into your personal or project skills directory:\n\n```bash\n# Personal (available across all projects)\ncp -r skills/core-numerical/numerical-stability ~/.claude/skills/numerical-stability\n\n# Project-level (committed to version control)\ncp -r skills/core-numerical/numerical-stability .claude/skills/numerical-stability\n```\n\nOr clone the whole repo and point Claude Code at it with `--add-dir`:\n\n```bash\nclaude --add-dir /path/to/materials-simulation-skills/skills\n```\n\nVerify with: `What skills are available?` or type `/` to see skills in the autocomplete menu.\n\nSee the [Claude Code skills docs](https://code.claude.com/docs/en/skills) for more details.\n\n### Gemini CLI\n\nInstall directly from the repo, or copy skills into your Gemini skills directory:\n\n```bash\n# User-scoped (available across all workspaces)\ncp -r skills/core-numerical/numerical-stability ~/.gemini/skills/numerical-stability\n\n# Workspace-scoped (project-specific)\ncp -r skills/core-numerical/numerical-stability .gemini/skills/numerical-stability\n```\n\nVerify with: `gemini skills list`\n\nSee the [Gemini CLI skills docs](https://geminicli.com/docs/cli/skills/) for more details.\n\n### OpenAI Codex\n\nCopy skills into one of the Codex skills directories:\n\n```bash\n# User-scoped\ncp -r skills/core-numerical/numerical-stability ~/.agents/skills/numerical-stability\n\n# Repository-scoped\ncp -r skills/core-numerical/numerical-stability .agents/skills/numerical-stability\n```\n\nRestart Codex after adding skills. Use `/skills` or `$` to invoke skills by name.\n\nSee the [Codex skills docs](https://developers.openai.com/codex/skills) for more details.\n\n### VS Code / GitHub Copilot\n\nCopy skills into your workspace or personal skills directory:\n\n```bash\n# Workspace (committed to version control)\ncp -r skills/core-numerical/numerical-stability .github/skills/numerical-stability\n\n# Personal (across all workspaces)\ncp -r skills/core-numerical/numerical-stability ~/.copilot/skills/numerical-stability\n```\n\nType `/skills` in the chat input to see and invoke available skills.\n\nSee the [VS Code skills docs](https://code.visualstudio.com/docs/copilot/customization/agent-skills) for more details.\n\n### Cursor\n\nCopy skills into a `skills/` directory at your project root:\n\n```bash\ncp -r skills/core-numerical/numerical-stability skills/numerical-stability\n```\n\nCursor's MCP server auto-discovers skills from the `skills/` directory.\n\n### Other Agents\n\nAny agent that supports the [Agent Skills standard](https://agentskills.io) can use these skills. The general pattern:\n\n1. Copy the skill directory (containing `SKILL.md`, `scripts/`, `references/`) into your agent's skills folder\n2. The agent discovers the skill by its `name` and `description` in the YAML frontmatter\n3. Mention the skill by name or ask a task that matches its description\n\n```text\nUse numerical-stability to check a proposed dt for my phase-field run.\n```\n\nThe agent loads the skill's instructions, runs the appropriate scripts, and interprets the results.\n\n---",
    },
    'repository-layout': {
        "description": '```\nskills/\n    core-numerical/          # 8 skills: stability, solvers, meshing, convergence,.',
        "guidance": '```\nskills/\n    core-numerical/          # 8 skills: stability, solvers, meshing, convergence, ...\n    simulation-workflow/     # 5 skills: validation, optimization, orchestration, ...\n    hpc-deployment/          # 1 skill: SLURM job script generation\n    ontology/                # 3 skills: ontology exploration, mapping, validation\n    <each-skill>/\n        SKILL.md             # Instructions + YAML frontmatter (with metadata block)\n        scripts/             # Python CLI tools with --json output\n        references/          # Domain knowledge documents\n        evals/evals.json     # Evaluation suite (prompts, assertions)\n        CHANGELOG.md         # Version history\ntests/\n    unit/                    # Pure-function tests via load_module()\n    integration/             # Subprocess + JSON schema validation\n    fixtures/                # Sample data files for CI smoke tests\n.github/\n    workflows/ci.yml         # Cross-platform CI + quality validation\n    ISSUE_TEMPLATE/          # Bug reports, skill proposals\n    PULL_REQUEST_TEMPLATE.md # PR checklist\n```\n\n---',
    },
    'contributing': {
        "description": 'We welcome contributions of all kinds -- new skills, bug fixes, documentation, and tests.',
        "guidance": 'We welcome contributions of all kinds -- new skills, bug fixes, documentation, and tests. The project is designed to grow from 17 skills across 4 categories into a broader collection spanning materials physics, verification & validation, HPC deployment, and more.\n\nSee **[CONTRIBUTING.md](CONTRIBUTING.md)** for:\n- Step-by-step guide to creating a new skill\n- Script and test templates\n- Skill taxonomy and open categories for community contributions\n- PR guidelines and checklists\n\n---',
    },
    'license': {
        "description": '[Apache 2.',
        "guidance": '[Apache 2.0](LICENSE)',
    },
    'acknowledgements': {
        "description": '- [Agent Skills standard](https://agentskills.',
        "guidance": '- [Agent Skills standard](https://agentskills.io) -- Open specification for portable agent capabilities\n- [Anthropic](https://anthropic.com) -- Original developer of the Agent Skills format\n- [agentskills/agentskills](https://github.com/agentskills/agentskills) -- Reference implementation and validation library',
    },
}


@mcp.tool()
def list_materials_simulation_skills_skills() -> dict:
    """List all available materials_simulation_skills skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_materials_simulation_skills_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific materials_simulation_skills skill."""
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
    hint = get_presentation_hint('materials_simulation_skills', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@materials_simulation_skills",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'materials_simulation_skills',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
