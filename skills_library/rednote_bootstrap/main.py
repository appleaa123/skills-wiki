"""Skill: rednote_bootstrap."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("rednote-bootstrap")


_SKILLS: dict[str, dict] = {
    'core-philosophy': {
        "description": '### "Research Once, Reuse Forever"\n\nContent platform rules and best practices change constantly.',
        "guidance": '### "Research Once, Reuse Forever"\n\nContent platform rules and best practices change constantly. The traditional approach — manually searching, reading posts, compiling notes — is time-consuming, quickly outdated, and not reusable. rednote-bootstrap automates and systematizes this entire process:\n\n1. **Search-First**: Instead of relying on pre-trained knowledge, it fetches first-hand information directly from XiaoHongShu\'s live content\n2. **Adaptive Depth**: Rather than mechanically reading a fixed number of posts, it dynamically decides when to stop based on information saturation\n3. **Knowledge Distillation**: Fragments of knowledge scattered across multiple posts are cross-validated and distilled into structured, actionable guides\n4. **Registry & Reuse**: All generated knowledge is registered as sub-Skills; subsequent queries hit the registry first — if matched, reuse immediately\n5. **Incremental Updates**: If a new question partially matches an existing Skill, only the gap is researched and merged incrementally\n\nThis makes it a "learning operations assistant" — the more you use it, the more it knows, and the faster it responds.\n\n### Why Not Just Ask an LLM?\n\nXiaoHongShu operations knowledge has three characteristics that make pure LLM answers unreliable:\n\n- **Highly time-sensitive**: Platform rules update frequently (e.g., mandatory AI content labeling introduced in 2026) — training data may be outdated\n- **Practitioner-driven**: Many critical details live in creators\' hands-on experience, not in official documentation\n- **Embedded in images**: The core content of XiaoHongShu posts is often inside images (not plain text in the DOM), requiring visual understanding to extract\n\nrednote-bootstrap uses browser automation + visual understanding to read real, up-to-date creator experiences directly from the platform, ensuring both accuracy and timeliness.\n\n---',
    },
    'architecture': {
        "description": '```\nrednote-bootstrap/\n├── SKILL.',
        "guidance": '```\nrednote-bootstrap/\n├── SKILL.md                          # Entry point: routing logic + workflow definition\n├── registry.json                     # Sub-Skill registry (auto-maintained)\n├── LICENSE                           # Apache 2.0\n├── xhs-auth-state.json               # XiaoHongShu auth state persistence (auto-generated)\n├── reference/\n│   ├── platforms.md                  # Platform adapter config (DOM structure, interaction patterns)\n│   ├── search-first-skill.md         # Core research engine (5-phase workflow)\n│   └── agent-browser/                # Browser automation capability (dependency)\n├── templates/\n│   └── sub-skill-template.md         # Sub-Skill generation template\n└── generated-skills/                 # Generated sub-Skills (knowledge base, continuously growing)\n    ├── xiaohongshu-publishing-guide/\n    │   └── SKILL.md\n    ├── xiaohongshu-daily-account-nurturing/\n    │   └── SKILL.md\n    └── .../\n```\n\nThe system consists of three layers:\n\n| Layer | Component | Responsibility |\n|-------|-----------|----------------|\n| **Routing** | `SKILL.md` + `registry.json` | Understand user intent, match existing sub-Skills or trigger new research |\n| **Research Engine** | `search-first-skill.md` | 5-phase automated research (analyze → collect → evaluate → distill → register) |\n| **Knowledge Base** | `generated-skills/` | Ever-growing collection of sub-Skills, each an independent executable operations guide |\n\n---',
    },
    'how-it-works': {
        "description": "### Five-Phase Research Engine\n\nWhen a user asks a question that doesn't match any existing sub-Skill, the research engine kicks in:\n\n```\nPhase 1                Phase 2                Phase 3\nTopic An",
        "guidance": '### Five-Phase Research Engine\n\nWhen a user asks a question that doesn\'t match any existing sub-Skill, the research engine kicks in:\n\n```\nPhase 1                Phase 2                Phase 3\nTopic Analysis         Content Collection     Adaptive Depth Control\n───────────────        ───────────────        ───────────────\nDecompose into   ──→   Multi-round       ──→   Information saturation\n3~5 sub-dimensions     search                  assessment\nGenerate search        Open & read each        Dimension coverage check\nterm strategies        post one by one         Contradiction detection\n(direct/long-tail/     Screenshot + OCR        Dynamically decide\n reverse)              extraction              to continue or stop\n        │                                            │\n        │         Phase 5              Phase 4       │\n        │         Registration         Knowledge     │\n        │                              Distillation  │\n        │         ───────────────      ───────────────\n        └────────  Update registry ←── Deduplicate + cross-validate\n                   Route future          Resolve conflicts\n                   queries here          Annotate timeliness\n                                        Generate sub-Skill\n```\n\n### Adaptive Depth Control\n\nThis is the core innovation of the research engine. Instead of collecting a fixed number of posts, it uses four metrics to dynamically assess "is this enough?":\n\n| Metric | Meaning | Stop Threshold |\n|--------|---------|----------------|\n| Information Novelty Rate | New unique insights this round / Total insights extracted | < 20% → saturated |\n| Dimension Coverage | Dimensions with substantial content / Total dimensions | > 80% → sufficient |\n| Contradiction Detection | Do different posts present conflicting viewpoints? | Conflicts found → keep researching |\n| Authority | Does the collection include official accounts or verified creators? | Lacking → need more sources |\n\nSafety boundaries are also enforced: max 5 search rounds, max 30 posts, max 15 minutes per research session.\n\n### Sub-Skill Routing\n\nWhen a user asks a question again, the registry is checked first:\n\n```\nUser Question\n  │\n  ├─ Exact topic match ──→ Load and execute sub-Skill directly\n  │\n  ├─ Keywords overlap > 70% ──→ Load sub-Skill, check if incremental update needed\n  │\n  └─ No match ──→ Launch five-phase research engine, generate new sub-Skill\n```\n\nIncremental update strategy for existing sub-Skills:\n\n- Request falls within existing coverage → execute directly, no re-research\n- New sub-dimensions identified → research only the gap, merge incrementally\n- Sub-Skill older than 30 days → prompt user whether to refresh (platform rules may have changed)\n\n---',
    },
    'capabilities': {
        "description": '### Supported Operations Scenarios\n\nThrough the research engine, rednote-bootstrap can generate sub-Skills for any operations topic on demand.',
        "guidance": '### Supported Operations Scenarios\n\nThrough the research engine, rednote-bootstrap can generate sub-Skills for any operations topic on demand. Here are examples already generated:\n\n**📝 Post Publishing Workflow** — A complete 7-step guide from account setup to publishing, covering Creator Center entry tips, cover design, title formulas, hashtag strategies, and the latest 2026 rules including mandatory AI content labeling, CES scoring weights, traffic diversion red lines, and tiered penalty standards. Includes a golden posting time table for every niche and a checklist of 20 behaviors that trigger traffic throttling.\n\n**🌱 Daily Account Nurturing** — Pentagon weight system breakdown, 7-day new account nurturing plan (pure browsing → trial posting → stable operations), daily interaction behavior guidelines, 8 account-damaging taboos, and dormant account revival workflow.\n\n**📋 More Topics (On Demand)** — Prohibited word detection, niche competitor analysis, viral title writing, comment section engagement tactics, data analysis methodology... just ask, and it will research.\n\n### Technical Capabilities\n\n- **Browser Automation**: Controls Chrome via agent-browser with login state management, search, pagination, and screenshots\n- **Visual Understanding**: Extracts text and structure from image-heavy posts through screenshots + multimodal comprehension\n- **Platform Adaptation**: Built-in XiaoHongShu DOM structure mapping (search box, result list, post detail, image pagination) — works out of the box\n- **Session Persistence**: Saves authentication state after first QR code login, automatically reuses it — no repeated logins\n\n---',
    },
    'quick-start': {
        "description": '### Prerequisites\n\n- [QoderWork](https://qoder.',
        "guidance": "### Prerequisites\n\n- [QoderWork](https://qoder.com) desktop app\n- [agent-browser](https://github.com/anthropics/agent-browser): `npm i -g agent-browser && agent-browser install`\n- Chrome / Chromium browser\n\n### Installation\n\nClone this repository into QoderWork's Skills directory:\n\n```bash\ngit clone https://github.com/anthropics/rednote-bootstrap.git \\\n  ~/.qoderwork/skills/rednote-bootstrap\n```\n\nOr install the `.skill` file directly within QoderWork.\n\n### Usage\n\nSimply ask questions in QoderWork — the Skill loads automatically:\n\n```\nYou: What's the XiaoHongShu posting workflow?\nYou: How do I nurture a new account?\nYou: What are the prohibited words on XiaoHongShu?\nYou: How to write viral titles?\n```\n\nFirst use requires scanning a QR code with the XiaoHongShu app or WeChat (one-time only — auth state is saved automatically).\n\n---",
    },
    'sub-skill-structure': {
        "description": 'Every auto-generated sub-Skill follows a unified template, ensuring reliability and traceability:\n\n```markdown\n---\nname: {skill_id}\ndescription: {description}\ntopic: {topic}\ncreatedAt: {creation_date}',
        "guidance": 'Every auto-generated sub-Skill follows a unified template, ensuring reliability and traceability:\n\n```markdown\n---\nname: {skill_id}\ndescription: {description}\ntopic: {topic}\ncreatedAt: {creation_date}\nresearchDepth: {depth} (analyzed N posts)\n---\n\n# {Topic}\n\n> Auto-generated by content-researcher on YYYY-MM-DD\n> Sources: N posts from XiaoHongShu, cross-validated\n> Confidence: High / Medium / Low\n> Last updated: YYYY-MM-DD',
    },
    'knowledge-gaps-honestly-flags-what-the-research-couldn-t-cover': {
        "description": '```\n\nKey design decisions:\n\n- **Confidence annotation**: Insights mentioned by 3+ posts are marked "high confidence"; single-source insights marked "low"\n- **Conflict resolution**: Contradictory viewp',
        "guidance": '```\n\nKey design decisions:\n\n- **Confidence annotation**: Insights mentioned by 3+ posts are marked "high confidence"; single-source insights marked "low"\n- **Conflict resolution**: Contradictory viewpoints are presented side by side, never forcibly resolved\n- **Timeliness annotation**: Notes which platform rule version the info is based on, warns about potential expiry\n- **Knowledge gaps**: Honestly acknowledges what the research didn\'t cover, rather than fabricating answers\n\n---',
    },
    'distillation-rules': {
        "description": 'The distillation process from raw posts to sub-Skills follows five rules:\n\n1.',
        "guidance": 'The distillation process from raw posts to sub-Skills follows five rules:\n\n1. **Deduplication**: Merge repeated insights across different posts\n2. **Cross-Validation**: Multi-source confirmed insights get high-confidence labels\n3. **Conflict Resolution**: Contradictory viewpoints presented in parallel, no forced arbitration\n4. **Timeliness Annotation**: Flag information shelf-life, warn about potential expiry\n5. **Actionability**: Transform vague advice into concrete, step-by-step operations\n\nThis ensures the output is not "information dumping" but verified, directly executable knowledge.\n\n---',
    },
    'design-decisions': {
        "description": '**Why use a browser instead of an API?** XiaoHongShu has no public content search API and enforces strict anti-crawling measures.',
        "guidance": '**Why use a browser instead of an API?** XiaoHongShu has no public content search API and enforces strict anti-crawling measures. Real browser automation via agent-browser, browsing as a normal user, is the most stable and reliable approach.\n\n**Why take screenshots instead of reading DOM text?** Because the core content of XiaoHongShu posts is heavily embedded in images, not as plain text in the DOM. Screenshots + visual understanding (OCR / multimodal models) are required to extract complete information.\n\n**Why generate Skills instead of answering directly?** Generating reusable sub-Skills has three advantages: (1) zero-latency response for similar future questions; (2) knowledge can be incrementally updated instead of starting over; (3) users can review, edit, and share structured knowledge.\n\n**Why adaptive depth instead of fixed counts?** Different topics have vastly different information densities — a prohibited word list may need 15 posts to cover comprehensively, while a specific workflow may only need 3. Adaptive depth avoids both "under-researching" and "over-collecting."\n\n---',
    },
    'platform-adaptation': {
        "description": 'Currently provides primary support for XiaoHongShu (REDnote).',
        "guidance": 'Currently provides primary support for XiaoHongShu (REDnote). `reference/platforms.md` defines the complete platform adapter configuration:\n\n- DOM selectors and interaction patterns for the search flow\n- Parsing rules for search result lists\n- Content extraction patterns for post detail pages\n- Image post pagination mechanism\n- Content quality signals (like thresholds, comment counts, recency, verification badges)\n\nThe architecture is designed to be extensible — new content platforms can be supported by adding new platform configurations.\n\n---',
    },
    'contributing': {
        "description": 'Contributions are welcome:\n\n- **New platform adapters**: Write `platforms.',
        "guidance": 'Contributions are welcome:\n\n- **New platform adapters**: Write `platforms.md` adapter configs for other content platforms\n- **Template improvements**: Improve the knowledge distillation template structure\n- **Engine enhancements**: Optimize the saturation assessment model, search term generation strategies\n- **Sub-Skill sharing**: Share your high-quality generated sub-Skills with the community\n\n---',
    },
    'license': {
        "description": '[Apache License 2.',
        "guidance": '[Apache License 2.0](./LICENSE)',
    },
}


@mcp.tool()
def list_rednote_bootstrap_skills() -> dict:
    """List all available rednote_bootstrap skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_rednote_bootstrap_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific rednote_bootstrap skill."""
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
    hint = get_presentation_hint('rednote_bootstrap', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@rednote_bootstrap",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'rednote_bootstrap',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
