"""Skill: youtube_clipper."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("youtube-clipper")


_SKILLS: dict[str, dict] = {
    'features': {
        "description": '- **AI Semantic Analysis** - Generate fine-grained chapters (2-5 minutes each) by understanding video content, not just mechanical time splitting\n- **Precise Clipping** - Use FFmpeg to extract video s',
        "guidance": '- **AI Semantic Analysis** - Generate fine-grained chapters (2-5 minutes each) by understanding video content, not just mechanical time splitting\n- **Precise Clipping** - Use FFmpeg to extract video segments with frame-accurate timing\n- **Bilingual Subtitles** - Batch translate subtitles to Chinese/English with 95% API call reduction\n- **Subtitle Burning** - Hardcode bilingual subtitles into videos with customizable styling\n- **Content Summarization** - Auto-generate social media content (Xiaohongshu, Douyin, WeChat)\n\n---',
    },
    'installation': {
        "description": '### Option 1: npx skills (Recommended)\n\n```bash\nnpx skills add https://github.',
        "guidance": '### Option 1: npx skills (Recommended)\n\n```bash\nnpx skills add https://github.com/op7418/Youtube-clipper-skill\n```\n\nThis command will automatically install the skill to `~/.claude/skills/youtube-clipper/`.\n\n### Option 2: Manual Installation\n\n```bash\ngit clone https://github.com/op7418/Youtube-clipper-skill.git\ncd Youtube-clipper-skill\nbash install_as_skill.sh\n```\n\nThe install script will:\n- Copy files to `~/.claude/skills/youtube-clipper/`\n- Install Python dependencies (yt-dlp, pysrt, python-dotenv)\n- Check system dependencies (Python, yt-dlp, FFmpeg)\n- Create `.env` configuration file\n\n---',
    },
    'requirements': {
        "description": '### System Dependencies\n\n| Dependency | Version | Purpose | Installation |\n|------------|---------|---------|--------------|\n| **Python** | 3.',
        "guidance": '### System Dependencies\n\n| Dependency | Version | Purpose | Installation |\n|------------|---------|---------|--------------|\n| **Python** | 3.8+ | Script execution | [python.org](https://www.python.org/downloads/) |\n| **yt-dlp** | Latest | YouTube download | `brew install yt-dlp` (macOS)<br>`sudo apt install yt-dlp` (Ubuntu)<br>`pip install yt-dlp` (pip) |\n| **FFmpeg with libass** | Latest | Video processing & subtitle burning | `brew install ffmpeg-full` (macOS)<br>`sudo apt install ffmpeg libass-dev` (Ubuntu) |\n\n### Python Packages\n\nThese are automatically installed by the install script:\n- `yt-dlp` - YouTube downloader\n- `pysrt` - SRT subtitle parser\n- `python-dotenv` - Environment variable management\n\n### Important: FFmpeg libass Support\n\n**macOS users**: The standard `ffmpeg` package from Homebrew does NOT include libass support (required for subtitle burning). You must install `ffmpeg-full`:\n\n```bash\n# Remove standard ffmpeg (if installed)\nbrew uninstall ffmpeg\n\n# Install ffmpeg-full (includes libass)\nbrew install ffmpeg-full\n```\n\n**Verify libass support**:\n```bash\nffmpeg -filters 2>&1 | grep subtitles\n# Should output: subtitles    V->V  (...)\n```\n\n---',
    },
    'usage': {
        "description": '### In Claude Code\n\nSimply tell Claude to clip a YouTube video:\n\n```\nClip this YouTube video: https://youtube.',
        "guidance": '### In Claude Code\n\nSimply tell Claude to clip a YouTube video:\n\n```\nClip this YouTube video: https://youtube.com/watch?v=VIDEO_ID\n```\n\nor\n\n```\n剪辑这个 YouTube 视频：https://youtube.com/watch?v=VIDEO_ID\n```\n\n### Workflow\n\n1. **Environment Check** - Verifies yt-dlp, FFmpeg, and Python dependencies\n2. **Video Download** - Downloads video (up to 1080p) and English subtitles\n3. **AI Chapter Analysis** - Claude analyzes subtitles to generate semantic chapters (2-5 min each)\n4. **User Selection** - Choose which chapters to clip and processing options\n5. **Processing** - Clips video, translates subtitles, burns subtitles (if requested)\n6. **Output** - Organized files in `./youtube-clips/<timestamp>/`\n\n### Output Files\n\nFor each clipped chapter:\n\n```\n./youtube-clips/20260122_143022/\n└── Chapter_Title/\n    ├── Chapter_Title_clip.mp4              # Original clip (no subtitles)\n    ├── Chapter_Title_with_subtitles.mp4    # With burned subtitles\n    ├── Chapter_Title_bilingual.srt         # Bilingual subtitle file\n    └── Chapter_Title_summary.md            # Social media content\n```\n\n---',
    },
    'configuration': {
        "description": 'The skill uses environment variables for customization.',
        "guidance": 'The skill uses environment variables for customization. Edit `~/.claude/skills/youtube-clipper/.env`:\n\n### Key Settings\n\n```bash\n# FFmpeg path (auto-detected if empty)\nFFMPEG_PATH=\n\n# Output directory (default: current working directory)\nOUTPUT_DIR=./youtube-clips\n\n# Video quality limit (720, 1080, 1440, 2160)\nMAX_VIDEO_HEIGHT=1080\n\n# Translation batch size (20-25 recommended)\nTRANSLATION_BATCH_SIZE=20\n\n# Target language for translation\nTARGET_LANGUAGE=中文\n\n# Target chapter duration in seconds (180-300 recommended)\nTARGET_CHAPTER_DURATION=180\n```\n\nFor full configuration options, see [.env.example](.env.example).\n\n---',
    },
    'examples': {
        "description": '### Example 1: Extract highlights from a tech interview\n\n**Input**:\n```\nClip this video: https://youtube.',
        "guidance": "### Example 1: Extract highlights from a tech interview\n\n**Input**:\n```\nClip this video: https://youtube.com/watch?v=Ckt1cj0xjRM\n```\n\n**Output** (AI-generated chapters):\n```\n1. [00:00 - 03:15] AGI as an exponential curve, not a point in time\n2. [03:15 - 06:30] China's gap in AI development\n3. [06:30 - 09:45] The impact of chip bans\n...\n```\n\n**Result**: Select chapters → Get clipped videos with bilingual subtitles + social media content\n\n### Example 2: Create short clips from a course\n\n**Input**:\n```\nClip this lecture video and create bilingual subtitles: https://youtube.com/watch?v=LECTURE_ID\n```\n\n**Options**:\n- Generate bilingual subtitles: Yes\n- Burn subtitles into video: Yes\n- Generate summary: Yes\n\n**Result**: High-quality clips ready for sharing on social media platforms\n\n---",
    },
    'key-differentiators': {
        "description": "### AI Semantic Chapter Analysis\n\nUnlike mechanical time-based splitting, this skill uses Claude's AI to:\n- Understand content semantics\n- Identify natural topic transitions\n- Generate meaningful chap",
        "guidance": "### AI Semantic Chapter Analysis\n\nUnlike mechanical time-based splitting, this skill uses Claude's AI to:\n- Understand content semantics\n- Identify natural topic transitions\n- Generate meaningful chapter titles and summaries\n- Ensure complete coverage with no gaps\n\n**Example**:\n```\n❌ Mechanical splitting: [0:00-30:00], [30:00-60:00]\n✅ AI semantic analysis:\n   - [00:00-03:15] AGI definition\n   - [03:15-07:30] China's AI landscape\n   - [07:30-12:00] Chip ban impacts\n```\n\n### Batch Translation Optimization\n\nTranslates 20 subtitles at once instead of one-by-one:\n- 95% reduction in API calls\n- 10x faster translation\n- Better translation consistency\n\n### Bilingual Subtitle Format\n\nGenerated subtitle files contain both English and Chinese:\n\n```srt\n1\n00:00:00,000 --> 00:00:03,500\nThis is the English subtitle\n这是中文字幕\n\n2\n00:00:03,500 --> 00:00:07,000\nAnother English line\n另一行中文\n```\n\n---",
    },
    'troubleshooting': {
        "description": '### FFmpeg subtitle burning fails\n\n**Error**: `Option not found: subtitles` or `filter not found`\n\n**Solution**: Install `ffmpeg-full` (macOS) or ensure `libass-dev` is installed (Ubuntu):\n```bash\n# m',
        "guidance": '### FFmpeg subtitle burning fails\n\n**Error**: `Option not found: subtitles` or `filter not found`\n\n**Solution**: Install `ffmpeg-full` (macOS) or ensure `libass-dev` is installed (Ubuntu):\n```bash\n# macOS\nbrew uninstall ffmpeg\nbrew install ffmpeg-full\n\n# Ubuntu\nsudo apt install ffmpeg libass-dev\n```\n\n### Video download is slow\n\n**Solution**: Set a proxy in `.env`:\n```bash\nYT_DLP_PROXY=http://proxy-server:port\n# or\nYT_DLP_PROXY=socks5://proxy-server:port\n```\n\n### Subtitle translation fails\n\n**Cause**: API rate limiting or network issues\n\n**Solution**: The skill automatically retries up to 3 times. If persistent, check:\n- Network connectivity\n- Claude API status\n- Reduce `TRANSLATION_BATCH_SIZE` in `.env`\n\n### Special characters in filenames\n\n**Issue**: Filenames with `:`, `/`, `?`, etc. may cause errors\n\n**Solution**: The skill automatically sanitizes filenames by:\n- Removing special characters: `/ \\ : * ? " < > |`\n- Replacing spaces with underscores\n- Limiting length to 100 characters\n\n---',
    },
    'documentation': {
        "description": '- **[SKILL.',
        "guidance": '- **[SKILL.md](SKILL.md)** - Complete workflow and technical details\n- **[TECHNICAL_NOTES.md](TECHNICAL_NOTES.md)** - Implementation notes and design decisions\n- **[FIXES_AND_IMPROVEMENTS.md](FIXES_AND_IMPROVEMENTS.md)** - Changelog and bug fixes\n- **[references/](references/)** - FFmpeg, yt-dlp, and subtitle formatting guides\n\n---',
    },
    'contributing': {
        "description": 'Contributions are welcome! Please:\n- Report bugs via [GitHub Issues](https://github.',
        "guidance": 'Contributions are welcome! Please:\n- Report bugs via [GitHub Issues](https://github.com/op7418/Youtube-clipper-skill/issues)\n- Submit feature requests\n- Open pull requests for improvements\n\n---',
    },
    'license': {
        "description": 'This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.',
        "guidance": 'This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.\n\n---',
    },
    'acknowledgements': {
        "description": '- **[Claude Code](https://claude.',
        "guidance": '- **[Claude Code](https://claude.ai/claude-code)** - The AI-powered CLI tool\n- **[yt-dlp](https://github.com/yt-dlp/yt-dlp)** - YouTube download engine\n- **[FFmpeg](https://ffmpeg.org/)** - Video processing powerhouse\n\n---\n\n<div align="center">\n\n**Made with ❤️ by [op7418](https://github.com/op7418)**\n\nIf this skill helps you, please give it a ⭐️\n\n</div>',
    },
}


@mcp.tool()
def list_youtube_clipper_skills() -> dict:
    """List all available youtube_clipper skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_youtube_clipper_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific youtube_clipper skill."""
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
    hint = get_presentation_hint('youtube_clipper', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@youtube_clipper",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'youtube_clipper',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
