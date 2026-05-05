"""Skill: Capabilities."""

from fastmcp import FastMCP

mcp = FastMCP("capabilities")


_GUIDANCE = {'display_name': 'Capabilities', 'description': '### Supported Operations Scenarios\n\nThrough the research engine, rednote-bootstrap can generate sub-Skills for any operations topic on demand.', 'guidance': '### Supported Operations Scenarios\n\nThrough the research engine, rednote-bootstrap can generate sub-Skills for any operations topic on demand. Here are examples already generated:\n\n**📝 Post Publishing Workflow** — A complete 7-step guide from account setup to publishing, covering Creator Center entry tips, cover design, title formulas, hashtag strategies, and the latest 2026 rules including mandatory AI content labeling, CES scoring weights, traffic diversion red lines, and tiered penalty standards. Includes a golden posting time table for every niche and a checklist of 20 behaviors that trigger traffic throttling.\n\n**🌱 Daily Account Nurturing** — Pentagon weight system breakdown, 7-day new account nurturing plan (pure browsing → trial posting → stable operations), daily interaction behavior guidelines, 8 account-damaging taboos, and dormant account revival workflow.\n\n**📋 More Topics (On Demand)** — Prohibited word detection, niche competitor analysis, viral title writing, comment section engagement tactics, data analysis methodology... just ask, and it will research.\n\n### Technical Capabilities\n\n- **Browser Automation**: Controls Chrome via agent-browser with login state management, search, pagination, and screenshots\n- **Visual Understanding**: Extracts text and structure from image-heavy posts through screenshots + multimodal comprehension\n- **Platform Adaptation**: Built-in XiaoHongShu DOM structure mapping (search box, result list, post detail, image pagination) — works out of the box\n- **Session Persistence**: Saves authentication state after first QR code login, automatically reuses it — no repeated logins\n\n---'}


@mcp.tool()
def get_guidance() -> dict:
    """Get the full guidance for this skill."""
    return _GUIDANCE
