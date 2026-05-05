"""Skill: notebooklm_py."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("notebooklm-py")


_SKILLS: dict[str, dict] = {
    'what-you-can-build': {
        "description": '🤖 **AI Agent Tools** - Integrate NotebookLM into Claude Code, Codex, and other LLM agents.',
        "guidance": "🤖 **AI Agent Tools** - Integrate NotebookLM into Claude Code, Codex, and other LLM agents. Ships with a root [NotebookLM skill](SKILL.md) for GitHub and `npx skills add` discovery, local `notebooklm skill install` support for Claude Code and `.agents` skill directories, and repo-level Codex guidance in [`AGENTS.md`](AGENTS.md).\n\n📚 **Research Automation** - Bulk-import sources (URLs, PDFs, YouTube, Google Drive), run web/Drive research queries with auto-import, and extract insights programmatically. Build repeatable research pipelines.\n\n🎙️ **Content Generation** - Generate Audio Overviews (podcasts), videos, slide decks, quizzes, flashcards, infographics, data tables, mind maps, and study guides. Full control over formats, styles, and output.\n\n📥 **Downloads & Export** - Download all generated artifacts locally (MP3, MP4, PDF, PNG, CSV, JSON, Markdown). Export to Google Docs/Sheets. **Features the web UI doesn't offer**: batch downloads, quiz/flashcard export in multiple formats, mind map JSON extraction.",
    },
    'three-ways-to-use': {
        "description": '| Method | Best For |\n|--------|----------|\n| **Python API** | Application integration, async workflows, custom pipelines |\n| **CLI** | Shell scripts, quick tasks, CI/CD automation |\n| **Agent Integra',
        "guidance": '| Method | Best For |\n|--------|----------|\n| **Python API** | Application integration, async workflows, custom pipelines |\n| **CLI** | Shell scripts, quick tasks, CI/CD automation |\n| **Agent Integration** | Claude Code, Codex, LLM agents, natural language automation |',
    },
    'features': {
        "description": '### Complete NotebookLM Coverage\n\n| Category | Capabilities |\n|----------|--------------|\n| **Notebooks** | Create, list, rename, delete |\n| **Sources** | URLs, YouTube, files (PDF, text, Markdown, Wo',
        "guidance": "### Complete NotebookLM Coverage\n\n| Category | Capabilities |\n|----------|--------------|\n| **Notebooks** | Create, list, rename, delete |\n| **Sources** | URLs, YouTube, files (PDF, text, Markdown, Word, audio, video, images), Google Drive, pasted text; refresh, get guide/fulltext |\n| **Chat** | Questions, conversation history, custom personas |\n| **Research** | Web and Drive research agents (fast/deep modes) with auto-import |\n| **Sharing** | Public/private links, user permissions (viewer/editor), view level control |\n\n### Content Generation (All NotebookLM Studio Types)\n\n| Type | Options | Download Format |\n|------|---------|-----------------|\n| **Audio Overview** | 4 formats (deep-dive, brief, critique, debate), 3 lengths, 50+ languages | MP3/MP4 |\n| **Video Overview** | 3 formats (explainer, brief, cinematic), 9 visual styles, plus a dedicated `cinematic-video` CLI alias | MP4 |\n| **Slide Deck** | Detailed or presenter format, adjustable length; individual slide revision | PDF, PPTX |\n| **Infographic** | 3 orientations, 3 detail levels | PNG |\n| **Quiz** | Configurable quantity and difficulty | JSON, Markdown, HTML |\n| **Flashcards** | Configurable quantity and difficulty | JSON, Markdown, HTML |\n| **Report** | Briefing doc, study guide, blog post, or custom prompt | Markdown |\n| **Data Table** | Custom structure via natural language | CSV |\n| **Mind Map** | Interactive hierarchical visualization | JSON |\n\n### Beyond the Web UI\n\nThese features are available via API/CLI but not exposed in NotebookLM's web interface:\n\n- **Batch downloads** - Download all artifacts of a type at once\n- **Quiz/Flashcard export** - Get structured JSON, Markdown, or HTML (web UI only shows interactive view)\n- **Mind map data extraction** - Export hierarchical JSON for visualization tools\n- **Data table CSV export** - Download structured tables as spreadsheets\n- **Slide deck as PPTX** - Download editable PowerPoint files (web UI only offers PDF)\n- **Slide revision** - Modify individual slides with natural-language prompts\n- **Report template customization** - Append extra instructions to built-in format templates\n- **Save chat to notes** - Save Q&A answers or conversation history as notebook notes\n- **Source fulltext access** - Retrieve the indexed text content of any source\n- **Programmatic sharing** - Manage permissions without the UI",
    },
    'installation': {
        "description": '```bash\n# Basic installation\npip install notebooklm-py\n\n# With browser login support (required for first-time setup)\npip install "notebooklm-py[browser]"\nplaywright install chromium\n```\n\nIf `playwrigh',
        "guidance": '```bash\n# Basic installation\npip install notebooklm-py\n\n# With browser login support (required for first-time setup)\npip install "notebooklm-py[browser]"\nplaywright install chromium\n```\n\nIf `playwright install chromium` fails with `TypeError: onExit is not a function`, see the Linux workaround in [Troubleshooting](docs/troubleshooting.md#linux).\n\n### Development Installation\n\nFor contributors or testing unreleased features:\n\n```bash\npip install git+https://github.com/teng-lin/notebooklm-py@main\n```\n\n⚠️ The main branch may contain unstable changes. Use PyPI releases for production.',
    },
    'quick-start': {
        "description": '<p align="center">\n  <a href="https://asciinema.',
        "guidance": '<p align="center">\n  <a href="https://asciinema.org/a/767284" target="_blank"><img src="https://asciinema.org/a/767284.svg" width="600" /></a>\n  <br>\n  <em>16-minute session compressed to 30 seconds</em>\n</p>\n\n### CLI\n\n```bash\n# 1. Authenticate (opens browser)\nnotebooklm login\n# Or use Microsoft Edge (for orgs that require Edge for SSO)\n# notebooklm login --browser msedge\n\n# 2. Create a notebook and add sources\nnotebooklm create "My Research"\nnotebooklm use <notebook_id>\nnotebooklm source add "https://en.wikipedia.org/wiki/Artificial_intelligence"\nnotebooklm source add "./paper.pdf"\n\n# 3. Chat with your sources\nnotebooklm ask "What are the key themes?"\n\n# 4. Generate content\nnotebooklm generate audio "make it engaging" --wait\nnotebooklm generate video --style whiteboard --wait\nnotebooklm generate cinematic-video "documentary-style summary" --wait\nnotebooklm generate quiz --difficulty hard\nnotebooklm generate flashcards --quantity more\nnotebooklm generate slide-deck\nnotebooklm generate infographic --orientation portrait\nnotebooklm generate mind-map\nnotebooklm generate data-table "compare key concepts"\n\n# 5. Download artifacts\nnotebooklm download audio ./podcast.mp3\nnotebooklm download video ./overview.mp4\nnotebooklm download cinematic-video ./documentary.mp4\nnotebooklm download quiz --format markdown ./quiz.md\nnotebooklm download flashcards --format json ./cards.json\nnotebooklm download slide-deck ./slides.pdf\nnotebooklm download infographic ./infographic.png\nnotebooklm download mind-map ./mindmap.json\nnotebooklm download data-table ./data.csv\n```\n\nOther useful CLI commands:\n\n```bash\nnotebooklm auth check --test         # Diagnose auth/cookie issues\nnotebooklm agent show codex          # Print bundled Codex instructions\nnotebooklm agent show claude         # Print bundled Claude Code skill template\nnotebooklm language list             # List supported output languages\nnotebooklm metadata --json           # Export notebook metadata and sources\nnotebooklm share status              # Inspect sharing state\nnotebooklm source add-research "AI"  # Start web research and import sources\nnotebooklm skill status              # Check local agent skill installation\n```\n\n### Python API\n\n```python\nimport asyncio\nfrom notebooklm import NotebookLMClient\n\nasync def main():\n    async with await NotebookLMClient.from_storage() as client:\n        # Create notebook and add sources\n        nb = await client.notebooks.create("Research")\n        await client.sources.add_url(nb.id, "https://example.com", wait=True)\n\n        # Chat with your sources\n        result = await client.chat.ask(nb.id, "Summarize this")\n        print(result.answer)\n\n        # Generate content (podcast, video, quiz, etc.)\n        status = await client.artifacts.generate_audio(nb.id, instructions="make it fun")\n        await client.artifacts.wait_for_completion(nb.id, status.task_id)\n        await client.artifacts.download_audio(nb.id, "podcast.mp3")\n\n        # Generate quiz and download as JSON\n        status = await client.artifacts.generate_quiz(nb.id)\n        await client.artifacts.wait_for_completion(nb.id, status.task_id)\n        await client.artifacts.download_quiz(nb.id, "quiz.json", output_format="json")\n\n        # Generate mind map and export\n        result = await client.artifacts.generate_mind_map(nb.id)\n        await client.artifacts.download_mind_map(nb.id, "mindmap.json")\n\nasyncio.run(main())\n```\n\n### Agent Setup\n\n**Option 1 — CLI install**:\n\n```bash\nnotebooklm skill install\n```\n\nInstalls the skill into `~/.claude/skills/notebooklm` and `~/.agents/skills/notebooklm`.\n\n**Option 2 — `npx` install** (via the open skills ecosystem):\n\n```bash\nnpx skills add teng-lin/notebooklm-py\n```\n\nFetches the canonical [SKILL.md](SKILL.md) directly from GitHub.',
    },
    'documentation': {
        "description": '- **[CLI Reference](docs/cli-reference.',
        "guidance": '- **[CLI Reference](docs/cli-reference.md)** - Complete command documentation\n- **[Python API](docs/python-api.md)** - Full API reference\n- **[Configuration](docs/configuration.md)** - Storage and settings\n- **[Release Guide](docs/releasing.md)** - Release checklist and packaging verification\n- **[Troubleshooting](docs/troubleshooting.md)** - Common issues and solutions\n- **[API Stability](docs/stability.md)** - Versioning policy and stability guarantees\n\n### For Contributors\n\n- **[Development Guide](docs/development.md)** - Architecture, testing, and releasing\n- **[RPC Development](docs/rpc-development.md)** - Protocol capture and debugging\n- **[RPC Reference](docs/rpc-reference.md)** - Payload structures\n- **[Changelog](CHANGELOG.md)** - Version history and release notes\n- **[Security](SECURITY.md)** - Security policy and credential handling',
    },
    'platform-support': {
        "description": '| Platform | Status | Notes |\n|----------|--------|-------|\n| **macOS** | ✅ Tested | Primary development platform |\n| **Linux** | ✅ Tested | Fully supported |\n| **Windows** | ✅ Tested | Tested in CI |',
        "guidance": '| Platform | Status | Notes |\n|----------|--------|-------|\n| **macOS** | ✅ Tested | Primary development platform |\n| **Linux** | ✅ Tested | Fully supported |\n| **Windows** | ✅ Tested | Tested in CI |',
    },
    'star-history': {
        "description": '[![Star History Chart](https://api.',
        "guidance": '[![Star History Chart](https://api.star-history.com/image?repos=teng-lin/notebooklm-py&type=timeline&legend=top-left)](https://www.star-history.com/?repos=teng-lin%2Fnotebooklm-py&type=timeline&legend=top-left)',
    },
    'license': {
        "description": 'MIT License.',
        "guidance": 'MIT License. See [LICENSE](LICENSE) for details.',
    },
}


@mcp.tool()
def list_notebooklm_py_skills() -> dict:
    """List all available notebooklm_py skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_notebooklm_py_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific notebooklm_py skill."""
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
    hint = get_presentation_hint('notebooklm_py', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@notebooklm_py",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'notebooklm_py',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
