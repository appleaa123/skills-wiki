"""Skill: wonda."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("wonda")


_SKILLS: dict[str, dict] = {
    'install': {
        "description": '![npm](https://img.',
        "guidance": '![npm](https://img.shields.io/badge/npm-CB3837?style=flat-square&logo=npm&logoColor=white)\n\n```bash\nnpm i -g @degausai/wonda\n```\n\n![Homebrew](https://img.shields.io/badge/Homebrew-FBB040?style=flat-square&logo=homebrew&logoColor=black)\n\n```bash\nbrew tap degausai/tap && brew install wonda\n```',
    },
    'get-started': {
        "description": '```bash\nwonda auth login          # Authenticate (opens browser)\nwonda skill install -o.',
        "guidance": '```bash\nwonda auth login          # Authenticate (opens browser)\nwonda skill install -o .  # Install skill file for your AI assistant\n```\n\nThen ask your agent: *"Use wonda to generate a product video of this image."*',
    },
    'agent-plugin': {
        "description": 'Wonda ships as a native plugin for AI coding agents.',
        "guidance": 'Wonda ships as a native plugin for AI coding agents. Install it once and your agent learns every command, model, and workflow automatically.\n\n| Agent | Install |\n|---|---|\n| Any agent | `npx skills add degausai/wonda` |\n| Claude Code | `/plugin marketplace add degausai/wonda` then `/plugin install wonda@degausai` |\n| Gemini CLI | `gemini extensions install https://github.com/degausai/wonda` |\n| Project-local | `wonda skill install -o .` |',
    },
    'made-with-wonda': {
        "description": '<p align="center">\n<img src="assets/example-1.',
        "guidance": '<p align="center">\n<img src="assets/example-1.webp" alt="Product content" width="140" />&nbsp;&nbsp;\n<img src="assets/example-3.webp" alt="AI-generated content" width="140" />&nbsp;&nbsp;\n<img src="assets/example-5.webp" alt="Ad creative" width="140" />&nbsp;&nbsp;\n<img src="assets/example-4.webp" alt="Product ad" width="140" />\n</p>\n\n<p align="center"><em>Product videos, UGC-style content, ad creatives — generated, edited, and published from the terminal.</em></p>',
    },
    'pricing': {
        "description": 'An account is required.',
        "guidance": 'An account is required. Sign up at [wonda.sh](https://wonda.sh).\n\nGenerations cost credits. Top up anytime:\n\n```bash\nwonda topup    # Add credits\nwonda balance  # Check remaining credits\n```\n\nUse `wonda pricing estimate` to check costs before generating.',
    },
    'commands': {
        "description": '### Generation\n\n| Command | Description |\n|---|---|\n| `generate image` | Generate an image from a text prompt |\n| `generate video` | Generate a video from a text prompt or reference image |\n| `generat',
        "guidance": "### Generation\n\n| Command | Description |\n|---|---|\n| `generate image` | Generate an image from a text prompt |\n| `generate video` | Generate a video from a text prompt or reference image |\n| `generate text` | Generate text content |\n| `generate music` | Generate a music track from a text prompt |\n| `audio speech` | Text-to-speech |\n| `audio transcribe` | Speech-to-text |\n| `audio dialogue` | Multi-speaker dialogue generation |\n\n### Editing\n\nTikTok/Reels-style video editing operations — designed for short-form social content.\n\n| Operation | What it does |\n|---|---|\n| `animatedCaptions` | Auto-transcribe and burn animated word-by-word captions |\n| `textOverlay` | Add styled text with custom fonts, positions, and sizing |\n| `editAudio` | Mix background music with video audio (volume control) |\n| `merge` | Stitch multiple clips into one video |\n| `overlay` | Picture-in-picture — layer one video over another |\n| `splitScreen` | Side-by-side or top-bottom split of two videos |\n| `trim` | Cut to a specific time range |\n| `speed` | Speed up or slow down |\n| `splitScenes` | Auto-detect and split scenes (or omit a scene) |\n| `extractAudio` | Pull the audio track from a video |\n| `extractFrame` | Extract a single frame at a specific timestamp |\n| `reverseVideo` | Play backwards |\n| `skipSilence` | Remove silent gaps |\n| `motionDesign` | Motion design and animation |\n| `enhanceAudio` | Enhance audio quality |\n| `voiceExtractor` | Isolate vocals from audio |\n| `audioTrim` | Trim audio files |\n| `imageToVideo` | Convert images to video |\n| `imageCrop` | Crop to a target aspect ratio |\n| `birefnet-bg-removal` | Remove image background |\n| `bria-video-background-removal` | Remove video background |\n| `topaz-video-upscale` | Upscale video resolution (1-4x) |\n| `sync-lipsync-v2-pro` | Sync lip movements to audio |\n\n### Analysis\n\n| Command | Description |\n|---|---|\n| `analyze video` | Extract composite frame grid + audio transcript for video understanding |\n\n### Publishing\n\n| Command | Description |\n|---|---|\n| `publish instagram` | Publish a single post |\n| `publish tiktok` | Publish a single post |\n| `publish instagram-carousel` | Publish a carousel (2-10 images) |\n| `publish tiktok-carousel` | Publish a photo carousel (2-35 images) |\n| `publish history` | View publish history |\n\n### LinkedIn\n\nSupports search, profiles, companies, messaging, and engagement.\n\n| Command | Description |\n|---|---|\n| `linkedin auth set` | Store LinkedIn session credentials (see `wonda linkedin auth --help`) |\n| `linkedin auth check` | Verify stored session validity |\n| `linkedin me` | Your LinkedIn identity |\n| `linkedin search` | Search people, companies, or all (`--type PEOPLE\\|COMPANIES\\|ALL`) |\n| `linkedin profile` | View a profile by vanity name or URL (includes follower count) |\n| `linkedin posts` | Recent posts with engagement stats (`--comments` to include top comments) |\n| `linkedin comments` | Get comments on a specific post |\n| `linkedin company` | View a company page |\n| `linkedin conversations` | List message threads |\n| `linkedin messages` | Read messages in a thread |\n| `linkedin notifications` | Recent notifications |\n| `linkedin connections` | Your connections |\n| `linkedin like` | Like a post |\n| `linkedin unlike` | Remove a like |\n| `linkedin send-message` | Send a message in a conversation |\n| `linkedin post` | Create a LinkedIn post (`--visibility ANYONE\\|CONNECTIONS_ONLY`) |\n| `linkedin delete-post` | Delete a post |\n\n### X/Twitter\n\nSupports search, timelines, tweets, and social graph.\n\n| Command | Description |\n|---|---|\n| `x auth set` | Store X session credentials (see `wonda x auth --help`) |\n| `x auth check` | Verify stored session validity |\n| `x search` | Search tweets |\n| `x user` | User profile |\n| `x user-tweets` | User's recent tweets |\n| `x read` | Read a single tweet |\n| `x replies` | Replies to a tweet |\n| `x thread` | Full thread (author's self-replies) |\n| `x home` | Home timeline (`--following` for Following tab) |\n| `x bookmarks` | Your bookmarks |\n| `x likes` | Your liked tweets |\n| `x following` | Who a user follows |\n| `x followers` | A user's followers |\n| `x lists` | User's lists (`--member-of` for memberships) |\n| `x list-timeline` | Tweets from a list |\n| `x news` | Trending topics (`--tab trending\\|for_you\\|news\\|sports\\|entertainment`) |\n| `x tweet` | Post a tweet |\n| `x reply` | Reply to a tweet |\n| `x like` | Like a tweet |\n| `x unlike` | Unlike a tweet |\n| `x retweet` | Retweet |\n| `x unretweet` | Unretweet |\n| `x follow` | Follow a user |\n| `x unfollow` | Unfollow a user |\n\n### Reddit\n\n| Command | Description |\n|---|---|\n| `reddit submit` | Submit a self or link post to a subreddit |\n| `reddit comment` | Reply to a post or comment |\n| `reddit vote` | Upvote or downvote |\n| `reddit subscribe` | Subscribe to a subreddit |\n| `reddit save` | Save a post |\n| `reddit delete` | Delete your post |\n| `reddit chat inbox` | List DM conversations |\n| `reddit chat messages` | Fetch messages from a conversation |\n| `reddit chat send` | Send a DM |\n| `reddit chat accept-all` | Accept pending chat requests |\n\n### Marketing & Analytics\n\n| Command | Description |\n|---|---|\n| `scrape social` | Scrape Instagram/TikTok/Reddit profiles (posts, engagement, bio) |\n| `scrape ads` | Search the Meta Ads Library for competitor ads |\n| `analytics instagram\\|tiktok` | Performance metrics for connected accounts |\n| `brand` | View brand identity, products, website data |\n\n### Media & Workflows\n\n| Command | Description |\n|---|---|\n| `media upload\\|download\\|list` | Media library management |\n| `blueprint list\\|create\\|run` | Blueprint workflow management |\n| `skill list\\|get\\|install` | AI agent skill files and content guides |\n| `models list\\|info` | Available models and their parameters |\n| `pricing list\\|estimate` | Pricing info and cost estimates |",
    },
    'examples': {
        "description": '### Generate an image\n\n```bash\nwonda generate image \\\n  --model nano-banana-2 \\\n  --prompt "Product photo of headphones on marble" \\\n  --wait -o photo.',
        "guidance": '### Generate an image\n\n```bash\nwonda generate image \\\n  --model nano-banana-2 \\\n  --prompt "Product photo of headphones on marble" \\\n  --wait -o photo.png\n```\n\n### Generate a video from a reference image\n\n```bash\nMEDIA=$(wonda media upload ./product.jpg --quiet)\nwonda generate video --model sora2 \\\n  --prompt "Slow orbit, dramatic lighting" \\\n  --attach "$MEDIA" --duration 8 --wait -o video.mp4\n```\n\n### Add animated captions (TikTok-style)\n\n```bash\nwonda edit video --operation animatedCaptions --media "$VID_MEDIA" \\\n  --params \'{"fontFamily":"TikTok Sans","position":"bottom-center","highlightColor":"#FFD700"}\' \\\n  --wait -o captioned.mp4\n```\n\n### Full pipeline: generate → music → captions → publish\n\n```bash\n# Generate a product video\nVID=$(wonda generate video --model sora2 --prompt "Ocean waves" --wait --quiet)\nVID_MEDIA=$(wonda jobs get inference "$VID" --jq \'.outputs[0].media.mediaId\')\n\n# Add background music\nMUSIC=$(wonda generate music --model suno-music --prompt "lo-fi ambient" --wait --quiet)\nMUSIC_MEDIA=$(wonda jobs get inference "$MUSIC" --jq \'.outputs[0].media.mediaId\')\nMIXED=$(wonda edit video --operation editAudio --media "$VID_MEDIA" --audio-media "$MUSIC_MEDIA" \\\n  --params \'{"videoVolume":80,"audioVolume":30}\' --wait --quiet)\nMIXED_MEDIA=$(wonda jobs get editor "$MIXED" --jq \'.outputs[0].mediaId\')\n\n# Burn in animated captions\nFINAL=$(wonda edit video --operation animatedCaptions --media "$MIXED_MEDIA" \\\n  --params \'{"fontFamily":"Montserrat","position":"bottom-center"}\' --wait --quiet)\nFINAL_MEDIA=$(wonda jobs get editor "$FINAL" --jq \'.outputs[0].mediaId\')\n\n# Publish\nwonda publish tiktok --media "$FINAL_MEDIA" --account tiktok_acct_123 \\\n  --caption "Summer vibes" --privacy-level PUBLIC_TO_EVERYONE\n```\n\n### Publish to Instagram\n\n```bash\nwonda publish instagram \\\n  --media med_abc123 \\\n  --account ig_acct_456 \\\n  --caption "New drop. Link in bio."\n```',
    },
    'output-formats': {
        "description": 'All commands output JSON to stdout.',
        "guidance": 'All commands output JSON to stdout. Errors go to stderr.\n\n```bash\n# Default — formatted JSON\nwonda generate image --model nano-banana-2 --prompt "A cat"\n\n# Quiet — just the ID, useful for shell variables\nJOB=$(wonda generate image --model nano-banana-2 --prompt "A cat" --quiet)\n\n# Field selection\nwonda jobs get inference "$JOB" --fields status,outputs\n\n# Built-in jq (no external dependency)\nwonda generate image --model nano-banana-2 --prompt "A cat" --wait \\\n  --jq \'.outputs[0].media.url\'\n```\n\nWhen stdout is piped, JSON mode is enabled automatically.',
    },
    'ai-agent-integration': {
        "description": 'Just point your agent at `wonda` — it reads `--help`, finds the built-in skill file, and figures out model selection, prompt strategies, and content workflows on its own.',
        "guidance": 'Just point your agent at `wonda` — it reads `--help`, finds the built-in skill file, and figures out model selection, prompt strategies, and content workflows on its own.\n\n```bash\nwonda skill install              # Sync skill file to ~/.wonda/skill/\nwonda skill install --all -o .   # Install main + all content skills locally\nwonda skill list                 # Browse available content skills\nwonda skill get product-b-roll   # Fetch a specific content guide\n```\n\nThe skill file auto-syncs in the background. No configuration needed — your agent discovers it automatically.',
    },
    'platforms': {
        "description": 'macOS · Linux · Windows — x64 + ARM64.',
        "guidance": 'macOS · Linux · Windows — x64 + ARM64',
    },
    'license': {
        "description": 'Proprietary — see [wonda.',
        "guidance": 'Proprietary — see [wonda.sh](https://wonda.sh) for terms.',
    },
}


@mcp.tool()
def list_wonda_skills() -> dict:
    """List all available wonda skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_wonda_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific wonda skill."""
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
    hint = get_presentation_hint('wonda', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@wonda",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'wonda',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
