"""Skill: swift_patterns."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("swift-patterns")


_SKILLS: dict[str, dict] = {
    'what-this-skill-provides': {
        "description": 'Comprehensive SwiftUI expertise across:\n\n### Core Topics\n- **State Management** – Property wrapper selection (`@State`, `@Binding`, `@Observable`), ownership rules, data flow patterns\n- **Modern APIs*',
        "guidance": "Comprehensive SwiftUI expertise across:\n\n### Core Topics\n- **State Management** – Property wrapper selection (`@State`, `@Binding`, `@Observable`), ownership rules, data flow patterns\n- **Modern APIs** – iOS 17/18/26 replacements for deprecated APIs, complete migration guides\n- **View Composition** – Extraction patterns, parent/child data flow, view identity and performance\n- **Navigation** – `NavigationStack`, sheets, deep linking, type-safe routing patterns\n\n### Advanced Areas\n- **Lists & Collections** – Stable identity with `ForEach`, pagination, lazy containers\n- **Performance Optimization** – View optimization strategies, avoiding recomputation, memory management\n- **Testing & Dependency Injection** – Protocol-based patterns, test doubles, testable architecture\n- **Code Quality** – Refactoring playbooks, code smell detection, anti-pattern identification\n\nAll guidance is based on Apple's official documentation and focuses on **facts over opinions** – no architectural mandates.",
    },
    'quick-start': {
        "description": 'Install with a single command:\n\n```bash\nnpx skills add https://github.',
        "guidance": 'Install with a single command:\n\n```bash\nnpx skills add https://github.com/efremidze/swift-patterns-skill --skill swift-patterns\n```\n\nThen use it in your AI assistant:\n> Review my SwiftUI view for state management issues\n\n[View on skills.sh →](https://skills.sh/efremidze/swift-patterns-skill/swift-patterns)',
    },
    'installation': {
        "description": '### Recommended: Using skills.',
        "guidance": '### Recommended: Using skills.sh CLI\n\nThe easiest way to install:\n\n```bash\nnpx skills add https://github.com/efremidze/swift-patterns-skill --skill swift-patterns\n```\n\nThis installs the skill and makes it available to your AI assistant.\n\n### Alternative: Claude Code Plugin\n\nFor Claude Code users, add via the marketplace:\n\n1. Add the marketplace:\n   ```bash\n   /plugin marketplace add efremidze/swift-patterns-skill\n   ```\n\n2. Install the skill:\n   ```bash\n   /plugin install swift-patterns@swift-patterns-skill\n   ```\n\nOr configure for your team in `.claude/settings.json`:\n\n```json\n{\n  "enabledPlugins": {\n    "swift-patterns@swift-patterns-skill": true\n  },\n  "extraKnownMarketplaces": {\n    "swift-patterns-skill": {\n      "source": {\n        "source": "github",\n        "repo": "efremidze/swift-patterns-skill"\n      }\n    }\n  }\n}\n```\n\n### Manual Installation\n\nIf you prefer manual setup:\n\n1. Clone this repository\n2. Install or symlink `swift-patterns/` to your tool\'s skills directory\n3. Configure your AI tool to use `swift-patterns`',
    },
    'skill-structure': {
        "description": 'The skill follows a progressive disclosure model—core workflows in `SKILL.',
        "guidance": 'The skill follows a progressive disclosure model—core workflows in `SKILL.md`, detailed guidance in `references/`:\n\n```\nswift-patterns/\n  SKILL.md                          # Entry point: workflow routing, quick refs, review checklist\n  references/\n    state.md                        # Property wrappers, ownership, @Observable patterns\n    navigation.md                   # NavigationStack, sheets, deep linking\n    view-composition.md             # View extraction, data flow patterns\n    lists-collections.md            # ForEach identity, List vs LazyVStack\n    scrolling.md                    # Pagination, scroll position management\n    concurrency.md                  # .task modifier, async lifecycle\n    performance.md                  # View optimization, lazy loading strategies\n    testing-di.md                   # Dependency injection, test doubles\n    patterns.md                     # Container views, ViewModifiers, PreferenceKeys\n    modern-swiftui-apis.md          # iOS 17/18/26 API replacements and migration\n    refactor-playbooks.md           # Step-by-step refactoring guides\n    workflows-review.md             # Review methodology and standards\n    workflows-refactor.md           # Refactoring methodology, invariants\n    code-review-refactoring.md      # Code smells, anti-patterns, quality checks\n```',
    },
    'related-projects': {
        "description": '### Other Skills\n- **[swift-architecture-skill](https://github.',
        "guidance": "### Other Skills\n- **[swift-architecture-skill](https://github.com/efremidze/swift-architecture-skill)** – Architectural patterns and project structure guidance (complements this skill's focus on SwiftUI patterns)\n\n### Dynamic Runtime Tools\n- **[swift-patterns-mcp](https://github.com/efremidze/swift-patterns-mcp)** – MCP server with intelligent search, retrieval, and persistent memory\n\n**Key difference:**\n- **swift-patterns-skill** (this repo) = Static guidance, portable, no runtime dependencies\n- **swift-patterns-mcp** = Dynamic tooling with search, retrieval, and premium integrations",
    },
    'contributing': {
        "description": 'Contributions are welcome! This repository follows the [Agent Skills open format](https://agentskills.',
        "guidance": 'Contributions are welcome! This repository follows the [Agent Skills open format](https://agentskills.io/home).\n\nSee [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on improving the skill content and reference files.',
    },
    'license': {
        "description": 'MIT License.',
        "guidance": 'MIT License. See [LICENSE](LICENSE) for details.',
    },
}


@mcp.tool()
def list_swift_patterns_skills() -> dict:
    """List all available swift_patterns skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_swift_patterns_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific swift_patterns skill."""
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
    hint = get_presentation_hint('swift_patterns', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@swift_patterns",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'swift_patterns',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
