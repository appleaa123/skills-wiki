"""Skill: x_article_publisher_skill."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("x-article-publisher-skill")


_SKILLS: dict[str, dict] = {
    'the-problem': {
        "description": "If you're used to writing in Markdown, publishing to X Articles is a **painful process**:\n\n| Pain Point | Description |\n|------------|-------------|\n| **Format Loss** | Copy from Markdown editor → Pas",
        "guidance": "If you're used to writing in Markdown, publishing to X Articles is a **painful process**:\n\n| Pain Point | Description |\n|------------|-------------|\n| **Format Loss** | Copy from Markdown editor → Paste to X → All formatting gone |\n| **Manual Formatting** | Set each H2, bold, link manually — 15-20 min per article |\n| **Tedious Image Upload** | 5 clicks per image: Add media → Media → Add photo → Select → Wait |\n| **Position Errors** | Hard to remember where each image should go |\n\n### Time Comparison\n\n| Task | Manual | With This Skill |\n|------|--------|-----------------|\n| Format conversion | 15-20 min | 0 (automatic) |\n| Cover image | 1-2 min | 10 sec |\n| 5 content images | 5-10 min | 1 min |\n| **Total** | **20-30 min** | **2-3 min** |\n\n**10x efficiency improvement**\n\n---",
    },
    'the-solution': {
        "description": 'This skill automates the entire publishing workflow:\n\n```\nMarkdown File\n     ↓ Python parsing\nStructured Data (title, images with block_index, HTML)\n     ↓ Playwright MCP\nX Articles Editor (browser au',
        "guidance": 'This skill automates the entire publishing workflow:\n\n```\nMarkdown File\n     ↓ Python parsing\nStructured Data (title, images with block_index, HTML)\n     ↓ Playwright MCP\nX Articles Editor (browser automation)\n     ↓\nDraft Saved (never auto-publishes)\n```\n\n### Key Features\n\n- **Rich Text Paste**: Convert Markdown to HTML, paste via clipboard — all formatting preserved\n- **Block-Index Positioning** (v1.1): Precise image placement using element indices, not text matching\n- **Reverse Insertion**: Insert images from highest to lowest index to avoid position shifts\n- **Smart Wait Strategy**: Conditions return immediately when met, no wasted wait time\n- **Safe by Design**: Only saves as draft, never publishes automatically\n\n---',
    },
    'what-s-new-in-v1-1-0': {
        "description": '| Feature | Before | After |\n|---------|--------|-------|\n| Image positioning | Text matching (fragile) | Block index (precise) |\n| Insertion order | Sequential | Reverse (high→low) |\n| Wait behavior ',
        "guidance": '| Feature | Before | After |\n|---------|--------|-------|\n| Image positioning | Text matching (fragile) | Block index (precise) |\n| Insertion order | Sequential | Reverse (high→low) |\n| Wait behavior | Fixed delay | Immediate return on condition |\n\n### Why Block-Index?\n\nPreviously, images were positioned by matching surrounding text — this failed when:\n- Multiple paragraphs had similar content\n- Text was too short to be unique\n\nNow, each image has a `block_index` indicating exactly which block element it follows. This is deterministic and reliable.\n\n---',
    },
    'requirements': {
        "description": '| Requirement | Details |\n|-------------|---------|\n| Claude Code | [claude.',
        "guidance": '| Requirement | Details |\n|-------------|---------|\n| Claude Code | [claude.ai/code](https://claude.ai/code) |\n| Playwright MCP | Browser automation |\n| X Premium Plus | Required for Articles feature |\n| Python 3.9+ | With dependencies below |\n| OS | macOS or Windows |\n\n```bash\n# macOS\npip install Pillow pyobjc-framework-Cocoa\n\n# Windows\npip install Pillow pywin32 clip-util\n\n# For Mermaid diagrams (optional)\nnpm install -g @mermaid-js/mermaid-cli\n```\n\n---',
    },
    'installation': {
        "description": '### Method 1: Git Clone (Recommended)\n\n```bash\ngit clone https://github.',
        "guidance": '### Method 1: Git Clone (Recommended)\n\n```bash\ngit clone https://github.com/wshuyi/x-article-publisher-skill.git\ncp -r x-article-publisher-skill/skills/x-article-publisher ~/.claude/skills/\n```\n\n### Method 2: Plugin Marketplace\n\n```\n/plugin marketplace add wshuyi/x-article-publisher-skill\n/plugin install x-article-publisher@wshuyi/x-article-publisher-skill\n```\n\n---',
    },
    'usage': {
        "description": '### Natural Language\n\n```\nPublish /path/to/article.',
        "guidance": '### Natural Language\n\n```\nPublish /path/to/article.md to X\n```\n\n```\nHelp me post this article to X Articles: ~/Documents/my-post.md\n```\n\n### Skill Command\n\n```\n/x-article-publisher /path/to/article.md\n```\n\n---',
    },
    'workflow-steps': {
        "description": '```\n[1/7] Parse Markdown.',
        "guidance": '```\n[1/7] Parse Markdown...\n      → Extract title, cover image, content images with block_index\n      → Convert to HTML, count total blocks\n\n[2/7] Open X Articles editor...\n      → Navigate to x.com/compose/articles\n\n[3/7] Upload cover image...\n      → First image becomes cover\n\n[4/7] Fill title...\n      → H1 used as title (not included in body)\n\n[5/7] Paste article content...\n      → Rich text via clipboard\n      → All formatting preserved\n\n[6/7] Insert content images (reverse order)...\n      → Sort by block_index descending\n      → Click block element at index → Paste image\n      → Wait for upload (returns immediately when done)\n\n[7/7] Save draft...\n      → ✅ Review and publish manually\n```\n\n---',
    },
    'supported-markdown': {
        "description": '| Syntax | Result | Notes |\n|--------|--------|-------|\n| `# H1` | Article title | Extracted, not in body |\n| `## H2` | Section headers | Native support |\n| `**bold**` | **Bold text** | Native support',
        "guidance": '| Syntax | Result | Notes |\n|--------|--------|-------|\n| `# H1` | Article title | Extracted, not in body |\n| `## H2` | Section headers | Native support |\n| `**bold**` | **Bold text** | Native support |\n| `*italic*` | *Italic text* | Native support |\n| `[text](url)` | Hyperlinks | Native support |\n| `> quote` | Blockquotes | Native support |\n| `- item` | Unordered lists | Native support |\n| `1. item` | Ordered lists | Native support |\n| `![](img.jpg)` | Images | First = cover |\n| `---` | Dividers | Via Insert menu (v1.2) |\n| Tables | PNG images | Via table_to_image.py (v1.2) |\n| Mermaid | PNG images | Via mmdc CLI (v1.2) |\n\n---',
    },
    'example': {
        "description": '### Input: `article.',
        "guidance": '### Input: `article.md`\n\n```markdown\n# 5 AI Tools Worth Watching in 2024\n\n![cover](./images/cover.jpg)\n\nAI tools exploded in 2024. Here are 5 worth your attention.',
    },
    '1-claude-best-conversational-ai': {
        "description": '**Claude** by Anthropic excels at long-context understanding.',
        "guidance": "**Claude** by Anthropic excels at long-context understanding.\n\n> Claude's context window reaches 200K tokens.\n\n![claude-demo](./images/claude-demo.png)",
    },
    '2-midjourney-ai-art-leader': {
        "description": '[Midjourney](https://midjourney.',
        "guidance": '[Midjourney](https://midjourney.com) is the most popular AI art tool.\n\n![midjourney](./images/midjourney.jpg)\n```\n\n### Parsed Output (JSON)\n\n```json\n{\n  "title": "5 AI Tools Worth Watching in 2024",\n  "cover_image": "./images/cover.jpg",\n  "content_images": [\n    {"path": "./images/claude-demo.png", "block_index": 4},\n    {"path": "./images/midjourney.jpg", "block_index": 6}\n  ],\n  "total_blocks": 7\n}\n```\n\n### Insertion Order\n\nImages inserted in reverse: `block_index=6` first, then `block_index=4`.\n\n### Result\n\n- Cover: `cover.jpg` uploaded\n- Title: "5 AI Tools Worth Watching in 2024"\n- Content: Rich text with H2, bold, quotes, links\n- Images: Inserted at precise positions via block index\n- Status: **Draft saved** (ready for manual review)\n\n---',
    },
    'project-structure': {
        "description": '```\nx-article-publisher-skill/\n├──.',
        "guidance": '```\nx-article-publisher-skill/\n├── .claude-plugin/\n│   └── plugin.json              # Plugin config\n├── skills/\n│   └── x-article-publisher/\n│       ├── SKILL.md             # Skill instructions\n│       └── scripts/\n│           ├── parse_markdown.py    # Extracts block_index + dividers\n│           ├── copy_to_clipboard.py # Cross-platform clipboard\n│           └── table_to_image.py    # Markdown table → PNG (v1.2)\n├── docs/\n│   └── GUIDE.md                 # Detailed guide\n├── README.md                    # This file\n├── README_CN.md                 # Chinese version\n└── LICENSE\n```\n\n---',
    },
    'faq': {
        "description": '**Q: Why Premium Plus?**\nA: X Articles is exclusive to Premium Plus subscribers.',
        "guidance": '**Q: Why Premium Plus?**\nA: X Articles is exclusive to Premium Plus subscribers.\n\n**Q: Windows/Linux support?**\nA: Windows is now supported (v1.2). Linux support is still in progress — PRs welcome!\n\n**Q: Image upload failed?**\nA: Check: valid path, supported format (jpg/png/gif/webp), stable network.\n\n**Q: Can I publish to multiple accounts?**\nA: Not automatically. Switch accounts in browser manually before running.\n\n**Q: Why insert images in reverse order?**\nA: Each inserted image shifts subsequent block indices. Inserting from highest to lowest ensures earlier indices remain valid.\n\n**Q: What if text matching was used before?**\nA: v1.1 replaces text matching with `block_index`. The `after_text` field is kept for debugging but not used for positioning.\n\n**Q: Why does wait return immediately sometimes?**\nA: `browser_wait_for textGone="..."` returns as soon as the text disappears. The `time` parameter is just a maximum, not a fixed delay.\n\n---',
    },
    'documentation': {
        "description": '- [Detailed Usage Guide](docs/GUIDE.',
        "guidance": '- [Detailed Usage Guide](docs/GUIDE.md) — Complete documentation with examples\n\n---',
    },
    'changelog': {
        "description": '### v1.',
        "guidance": '### v1.2.0 (2025-01)\n- **Divider support**: Detect `---` in Markdown, insert via X Articles menu\n- **Table to image**: New `table_to_image.py` script converts Markdown tables to PNG\n- **Mermaid support**: Documentation for using `mmdc` to convert diagrams\n- **YAML frontmatter**: Automatically skip frontmatter in Markdown files\n- **Windows support**: Cross-platform clipboard operations (pywin32 + clip-util)\n\n### v1.1.0 (2025-12)\n- **Block-index positioning**: Replace text matching with precise element indices\n- **Reverse insertion order**: Prevent index shifts when inserting multiple images\n- **Optimized wait strategy**: Return immediately when upload completes\n- **H1 title handling**: H1 extracted as title, not included in body HTML\n\n### v1.0.0 (2025-12)\n- Initial release\n- Rich text paste via clipboard\n- Cover + content image support\n- Draft-only publishing\n\n---',
    },
    'license': {
        "description": 'MIT License - see [LICENSE](LICENSE).',
        "guidance": 'MIT License - see [LICENSE](LICENSE)',
    },
    'author': {
        "description": '[wshuyi](https://github.',
        "guidance": '[wshuyi](https://github.com/wshuyi)\n\n---',
    },
    'acknowledgments': {
        "description": 'v1.',
        "guidance": 'v1.2.0 features were inspired by and adapted from:\n\n- **[sugarforever/01coder-agent-skills](https://github.com/sugarforever/01coder-agent-skills)** — The `publish-x-article` skill contributed ideas for:\n  - Divider detection and menu-based insertion\n  - Table-to-image conversion script\n  - Mermaid diagram support documentation\n  - YAML frontmatter handling\n  - Windows clipboard implementation\n\nThank you to the community for building upon and improving this skill!\n\n---',
    },
    'contributing': {
        "description": '- **Issues**: Report bugs or request features\n- **PRs**: Welcome! Especially for Windows/Linux support.',
        "guidance": '- **Issues**: Report bugs or request features\n- **PRs**: Welcome! Especially for Windows/Linux support',
    },
}


@mcp.tool()
def list_x_article_publisher_skill_skills() -> dict:
    """List all available x_article_publisher_skill skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_x_article_publisher_skill_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific x_article_publisher_skill skill."""
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
    hint = get_presentation_hint('x_article_publisher_skill', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@x_article_publisher_skill",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'x_article_publisher_skill',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
