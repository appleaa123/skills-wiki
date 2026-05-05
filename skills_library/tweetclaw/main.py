"""Skill: tweetclaw."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("tweetclaw")


_SKILLS: dict[str, dict] = {
    'pricing': {
        "description": "TweetClaw uses Xquik's credit-based pricing.",
        "guidance": "TweetClaw uses Xquik's credit-based pricing. 1 credit = $0.00015.\n\n### vs Official X API\n\n| | Xquik (via TweetClaw) | X API Basic | X API Pro |\n|---|---|---|---|\n| **Monthly cost** | **$20** | $100 | $5,000 |\n| **Cost per tweet read** | **$0.00015** | ~$0.01 | ~$0.005 |\n| **Cost per user lookup** | **$0.00015** | ~$0.01 | ~$0.005 |\n| **Write actions** | **$0.0015** | Limited | Limited |\n| **Bulk extraction** | **$0.00015/result** | Not available | Not available |\n| **Monitoring + webhooks** | **Free** | Not available | Not available |\n| **Giveaway draws** | **$0.00015/entry** | Not available | Not available |\n\n### Per-Operation Costs\n\n| Operation | Credits | Cost |\n|-----------|---------|------|\n| Read (tweet, search, timeline, bookmarks, etc.) | 1 | $0.00015 |\n| Read (user profile, verified followers, followers you know) | 1 | $0.00015 |\n| Read (favoriters) | 1 | $0.00015 |\n| Read (trends) | 3 | $0.00045 |\n| Follow check, article | 7 | $0.00105 |\n| Write (tweet, like, retweet, follow, DM, etc.) | 10 | $0.0015 |\n| Extraction (tweets, replies, quotes, mentions, posts, likes, media, search, favoriters, retweeters, community members, people search, list members, list followers) | 1/result | $0.00015/result |\n| Extraction (followers, following, verified followers) | 1/result | $0.00015/result |\n| Extraction (articles) | 5/result | $0.00075/result |\n| Draw | 1/entry | $0.00015/entry |\n| Monitors, webhooks, radar, compose, drafts | 0 | **Free** |\n\n### Pay-Per-Use (No Subscription)\n\nTwo options:\n\n- **Credits**: Top up credits via the API. 1 credit = $0.00015. Works with all 111 endpoints.\n- **MPP**: 32 read-only X-API endpoints accept anonymous on-chain payments via Machine Payments Protocol. No account needed. SDK: `npm i mppx viem`.\n\n### Free Operations\n\nTweet composition, style analysis, drafts, curated radar (7 sources), account management, support tickets - all free, no credits consumed.",
    },
    'install': {
        "description": '```bash\nopenclaw plugins install @xquik/tweetclaw\n```\n\n> **Note:** `@xquik/tweetclaw` is the only official npm package.',
        "guidance": '```bash\nopenclaw plugins install @xquik/tweetclaw\n```\n\n> **Note:** `@xquik/tweetclaw` is the only official npm package. Any other scope (for example `@intentsolutionsio/tweetclaw`) is an unofficial redistribution and may ship stale metadata or outdated endpoint counts.',
    },
    'configure': {
        "description": '### Option A: API key (full access, 111 endpoints)\n\nGet an API key at [dashboard.',
        "guidance": '### Option A: API key (full access, 111 endpoints)\n\nGet an API key at [dashboard.xquik.com](https://dashboard.xquik.com/). Store it in an environment variable and configure TweetClaw to use it:\n\n```bash\nopenclaw config set plugins.entries.tweetclaw.config.apiKey "$XQUIK_API_KEY"\n```\n\n**Security**: Always reference your key via an environment variable - never paste raw keys into shell commands or config files.\n\n### Option B: Credits (pay-per-use, no subscription)\n\nTop up credits from the Xquik dashboard or via `POST /credits/topup`. All 111 endpoints available. 1 credit = $0.00015.\n\n### Option C: MPP pay-per-use (no account needed, 32 read-only endpoints)\n\nMPP (Machine Payments Protocol) lets agents pay per API call without an account, API key, or subscription. 32 read-only endpoints. Create an MPP account with `mppx account create`. The signing key stays local and is only used to sign payment proofs.\n\n```bash\nnpm i mppx viem\nopenclaw config set plugins.entries.tweetclaw.config.tempoSigningKey "$MPP_SIGNING_KEY"\n```\n\n**Security**: Always store your signing key in an environment variable - never paste raw keys into shell commands or config files.\n\nMPP-eligible endpoints: tweet lookup ($0.00015), tweet search ($0.00015/tweet), user lookup ($0.00015), user tweets ($0.00015/tweet), follower check ($0.00105), article lookup ($0.00105), media download ($0.00015/media), trends ($0.00045), X trends ($0.00045), quotes ($0.00015/tweet), replies ($0.00015/tweet), retweeters ($0.00015/user), favoriters ($0.00015/user), thread ($0.00015/tweet), user likes ($0.00015/tweet), user media ($0.00015/tweet), community info ($0.00015), community members ($0.00015/user), community moderators ($0.00015/user), community tweets ($0.00015/tweet), community search ($0.00015/community), communities tweets ($0.00015/tweet), list followers ($0.00015/user), list members ($0.00015/user), list tweets ($0.00015/tweet), users batch ($0.00015/user), users search ($0.00015/user), user followers ($0.00015/user), followers you know ($0.00015/user), user following ($0.00015/user), user mentions ($0.00015/tweet), verified followers ($0.00015/user).\n\n### Optional settings\n\n```bash\nopenclaw config set plugins.entries.tweetclaw.config.pollingEnabled true\nopenclaw config set plugins.entries.tweetclaw.config.pollingInterval 60\n```',
    },
    'tools': {
        "description": "TweetClaw uses Xquik's 2-tool approach to cover the entire API:\n\n### `explore` (free, no network)\n\nSearch the API spec to find endpoints.",
        "guidance": 'TweetClaw uses Xquik\'s 2-tool approach to cover the entire API:\n\n### `explore` (free, no network)\n\nSearch the API spec to find endpoints. No API calls are made.\n\n```\nYou: "What endpoints are available for tweet composition?"\n\nAI uses explore → filters spec by category "composition"\n→ Returns matching endpoints with parameters and response shapes\n```\n\n### `tweetclaw` (execute API calls)\n\nExecute authenticated API calls. Auth is injected automatically - the LLM never sees your API key.\n\n```\nYou: "Post a tweet saying \'Hello from TweetClaw!\'"\n\nAI uses tweetclaw → finds connected account, posts tweet\n→ Returns { tweetId, success: true }\n```\n\n```\nYou: "Search tweets about AI agents"\n\nAI uses explore → finds /api/v1/x/tweets/search\nAI uses tweetclaw → calls the endpoint with auth\n→ Returns tweet results\n```',
    },
    'commands': {
        "description": 'Instant responses, no LLM needed:\n\n| Command | Description |\n|---------|-------------|\n| `/xstatus` | Account info, subscription status, usage, credit balance |\n| `/xtrends` | Trending topics from cur',
        "guidance": 'Instant responses, no LLM needed:\n\n| Command | Description |\n|---------|-------------|\n| `/xstatus` | Account info, subscription status, usage, credit balance |\n| `/xtrends` | Trending topics from curated sources |\n| `/xtrends tech` | Trending topics filtered by category |',
    },
    'event-notifications': {
        "description": 'When polling is enabled (default), TweetClaw checks for new events every 60 seconds and delivers them to your chat:\n\n- **Monitor alerts**: New tweets, replies, quotes, retweets from monitored accounts',
        "guidance": 'When polling is enabled (default), TweetClaw checks for new events every 60 seconds and delivers them to your chat:\n\n- **Monitor alerts**: New tweets, replies, quotes, retweets from monitored accounts\n\nSet up a monitor first:\n\n```\nYou: "Monitor @elonmusk for new tweets, replies, and retweets"\n```',
    },
    'api-coverage': {
        "description": '111 endpoints across 11 categories:\n\n| Category | Examples | Cost |\n|----------|---------|------|\n| **Write Actions** | Post tweets, reply, like, retweet, follow, unfollow, DM, update profile, avatar,',
        "guidance": '111 endpoints across 11 categories:\n\n| Category | Examples | Cost |\n|----------|---------|------|\n| **Write Actions** | Post tweets, reply, like, retweet, follow, unfollow, DM, update profile, avatar, banner | 10 credits |\n| **Media** | Upload media via URL, download tweet media, get gallery links | 1-2 credits |\n| **Twitter** | Search tweets, look up users, user tweets/likes/media, favoriters, mutual followers, check follows, articles, bookmarks, notifications, timeline, DM history | 1-5 credits |\n| **Composition** | Compose, refine, score tweets; manage drafts; analyze writing styles | Free |\n| **Extraction** | Run extraction jobs (23 tool types: replies, followers, communities, favoriters, user_likes, user_media, etc.) | 1-5 credits/result |\n| **Draws** | Run giveaway draws on tweets, export results | 1 credit/entry |\n| **Monitoring** | Create monitors, view events, manage webhooks | Free |\n| **Account** | Manage API keys, subscription, connected X accounts | Free |\n| **Credits** | Check balance, top up credits | Free |\n| **Trends** | X trending topics, curated radar from 7 sources | 3 credits / Free |\n| **Support** | Create tickets, reply, track status | Free |',
    },
    'links': {
        "description": '- [Xquik Platform](https://xquik.',
        "guidance": '- [Xquik Platform](https://xquik.com)\n- [API Documentation](https://docs.xquik.com)\n- [Billing & Pricing](https://docs.xquik.com/guides/billing)\n- Framework guides: [Mastra](https://docs.xquik.com/guides/mastra), [CrewAI](https://docs.xquik.com/guides/crewai), [LangChain](https://docs.xquik.com/guides/langchain), [Pydantic AI](https://docs.xquik.com/guides/pydantic-ai), [Google ADK](https://docs.xquik.com/guides/google-adk), [Microsoft Agent Framework](https://docs.xquik.com/guides/microsoft-agent-framework), [n8n](https://docs.xquik.com/guides/n8n), [Zapier](https://docs.xquik.com/guides/zapier), [Composio migration](https://docs.xquik.com/guides/composio-migration)\n- [npm Package](https://www.npmjs.com/package/@xquik/tweetclaw)\n- [OpenClaw](https://github.com/openclaw/openclaw)',
    },
    'license': {
        "description": 'MIT.',
        "guidance": 'MIT',
    },
}


@mcp.tool()
def list_tweetclaw_skills() -> dict:
    """List all available tweetclaw skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_tweetclaw_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific tweetclaw skill."""
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
    hint = get_presentation_hint('tweetclaw', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@tweetclaw",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'tweetclaw',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
