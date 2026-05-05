"""Skill: video_db_skills."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("video-db-skills")


_SKILLS: dict[str, dict] = {
    'why-add-this-skill': {
        "description": 'This skill gives your agent one consistent interface to:\n\n- **See**: Realtime desktop screen, mic and system audio, RTSP streams, ingest files, URLs, YouTube.',
        "guidance": 'This skill gives your agent one consistent interface to:\n\n- **See**: Realtime desktop screen, mic and system audio, RTSP streams, ingest files, URLs, YouTube.\n\n- **Understand**: Visual understanding, transcribe, index and search moments with playble clips\n\n- **Act**: Stream results, trigger alerts on live feeds, edit timelines, generate subtitles and overlays, export clips.',
    },
    'what-it-does': {
        "description": 'VideoDB Skills lets your AI coding agent run end to end, server-side video workflows in real time and batch:\n\n- Capture desktop screen, mic, and system audio for real time processing.',
        "guidance": 'VideoDB Skills lets your AI coding agent run end to end, server-side video workflows in real time and batch:\n\n- Capture desktop screen, mic, and system audio for real time processing.\n- Upload and process RTSP streams, videos from YouTube, URLs, and local files.\n- Create realtime context of visual and spoken information. \n- Index and search spoken words and visual scenes anytime.\n- Generate transcripts, subtitles, and AI media.\n- Edit clips, overlays, and exports server side.\n\nReturn playable HLS links for anything you build.',
    },
    'get-started': {
        "description": 'Get started in two quick steps.',
        "guidance": 'Get started in two quick steps. Open your AI coding agent (Requires **Python 3.9+**) and follow along.\n\n\n### Step 1: Install the skill\n\n```bash\nnpx skills add video-db/skills\n```\n\nOr install with Claude Code plugin:\n\n```bash\n/plugin marketplace add video-db/skills\n/plugin install videodb@videodb-skills\n```\n\n### Step 2: Setup\n\n```\n/videodb setup\n```\n\nThe agent will guide setup for your [VideoDB API key](https://console.videodb.io) ($20 free credits, no credit card required), install the SDK, and verify the connection.\n\n\n> For Cursor, Copilot, and other agents, ask your agent to **"setup videodb"**\n\nSet your API key using either method:\n\n```bash\n# Recommended: Export in terminal\nexport VIDEO_DB_API_KEY=sk-xxx\n\n# Or add to your project\'s .env file\nVIDEO_DB_API_KEY=sk-xxx\n```\n\n---',
    },
    'give-your-agent-instructions': {
        "description": 'Ask your agent to run instructions like these.',
        "guidance": 'Ask your agent to run instructions like these. The skill loads automatically.\n\n- "Upload https://www.youtube.com/watch?v=MnrJzXM7a6o and give me a sharable stream link"\n- "Take clips from 10s-30s and 45s-60s and compile them"\n- "Generate a background music, and add to this Clip"\n- "Add subtitles to original video with white text on black background"\n- "Find every scene showing \'phone close-up\' or \'product on screen\'"\n- "Capture my screen for the next two minutes and write a report of what i\'m doing along with any insights or suggestions"*\n- "Here is the rtsp link for my IP Camera <rtsp url>, monitor and log the alert to text file along with timestamp whenever a person enters into the room"\n\n\n---',
    },
    'capability': {
        "description": 'VideoDB is the server side video stack for agents and apps.',
        "guidance": 'VideoDB is the server side video stack for agents and apps.\nRun reliable, scalable, cost efficient workflows across realtime streams and batch video, with built in AI understanding, without wiring up ffmpeg glue.\nKeep your client and agent stack light: send video in, get back structured context, searchable moments, and playable streams.\n\n### When to use VideoDB\n- Your app needs video workflows, but you do not want ffmpeg running everywhere\n- You want realtime perception from RTSP feeds or desktop capture\n- You need search by what was said or shown, then turn results into clips\n- You want server side editing, reframing, subtitles, dubbing, and streaming links\n\n| Capability              | What it unlocks                                                               |\n| ----------------------- | ----------------------------------------------------------------------------- |\n| **Capture**             | Capture desktop screen, mic, and system audio for realtime processing         |\n| **Upload**              | Ingest video from YouTube, URLs, or local files                               |\n| **Context**             | Generate realtime structured context for any RTSP feed or desktop stream      |\n| **Search**              | Find exact moments by speech, scenes, or metadata, return playable evidence   |\n| **Transcripts**         | Generate clean, timestamped transcripts from any video                        |\n| **Subtitles**           | Auto generate subtitles, then style and burn in or export                     |\n| **Edit**                | Trim, merge, clip, overlay text, images, audio, plus dubbing and translation  |\n| **AI Generate**         | Create images, video, music, sound effects, and voiceovers from text          |\n| **Transcode / Reframe** | Change resolution, quality, aspect ratio, and social crops, all on the server |\n| **Stream**              | Get instant playable HLS links (built in CDN) for anything you ingest or generate.             |\n\n\n### The idea in one line\nSee → Understand → Act, as an API, for video and audio.\n\n**Supported Platforms:** macOS, Linux, Windows (PowerShell)\n\n---',
    },
    'community-support': {
        "description": '- **Documentation:** [docs.',
        "guidance": '- **Documentation:** [docs.videodb.io](https://docs.videodb.io)\n- **Discord:** [Join our community](https://discord.com/invite/py9P639jGz)\n\n<div align="center">\n\nMade with ❤️ by the VideoDB team\n\n</div>',
    },
}


@mcp.tool()
def list_video_db_skills_skills() -> dict:
    """List all available video_db_skills skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_video_db_skills_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific video_db_skills skill."""
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
    hint = get_presentation_hint('video_db_skills', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@video_db_skills",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'video_db_skills',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
