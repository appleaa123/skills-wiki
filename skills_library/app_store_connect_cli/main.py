"""Skill: app_store_connect_cli."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("app-store-connect-cli")


_SKILLS: dict[str, dict] = {
    'installation': {
        "description": 'Install this skill pack:\n\n```bash\nnpx skills add rorkai/app-store-connect-cli-skills\n```.',
        "guidance": 'Install this skill pack:\n\n```bash\nnpx skills add rorkai/app-store-connect-cli-skills\n```',
    },
    'available-skills': {
        "description": '### asc-cli-usage\n\nGuidance for running `asc` commands (canonical verbs, flags, pagination, output, auth).',
        "guidance": '### asc-cli-usage\n\nGuidance for running `asc` commands (canonical verbs, flags, pagination, output, auth).\n\n**Use when:**\n- You need the correct `asc` command or flag combination\n- You want JSON-first output and pagination tips for automation\n\n**Example:**\n\n```bash\nFind the right asc command to list all builds for app 123456789 as JSON and paginate through everything.\n```\n\n### asc-workflow\n\nDefine and run repo-local automation graphs using `asc workflow` and `.asc/workflow.json`.\n\n**Use when:**\n- You are migrating from lane-based automation to repo-local workflows\n- You need multi-step orchestration with machine-parseable JSON output for CI/agents\n- You need hooks (`before_all`, `after_all`, `error`), conditionals (`if`), and private helper sub-workflows\n- You want validation (`asc workflow validate`) with cycle/reference checks before execution\n\n**Example:**\n\n```bash\nCreate an asc workflow that stages a release, validates it, and only submits when CONFIRM_RELEASE=true.\n```\n\n### asc-app-create-ui\n\nCreate a new App Store Connect app via browser automation when no API exists.\n\n**Use when:**\n- You need to create an app record (name, bundle ID, SKU, primary language)\n- You are comfortable logging in to App Store Connect in a real browser\n\n**Example:**\n\n```bash\nCreate a new App Store Connect app for com.example.myapp with SKU MYAPP123 and primary language English (U.S.).\n```\n\n### asc-xcode-build\n\nBuild, archive, export, and manage Xcode version/build numbers before uploading.\n\n**Use when:**\n- You need to create an IPA or PKG for upload\n- You\'re setting up CI/CD build pipelines\n- You need to configure ExportOptions.plist\n- You\'re troubleshooting encryption compliance issues\n\n**Example:**\n\n```bash\nArchive and export my macOS app as a PKG I can upload to App Store Connect.\n```\n\n### asc-shots-pipeline\n\nAgent-first screenshot pipeline using xcodebuild/simctl, AXe, JSON plans, `asc screenshots frame` (experimental), and `asc screenshots upload`.\n\n**Use when:**\n- You need a repeatable simulator screenshot automation flow\n- You want AXe-based UI driving before capture\n- You need a staged pipeline (capture -> frame -> upload)\n- You need to discover supported frame devices (`asc screenshots list-frame-devices`)\n- You want pinned Koubou guidance for deterministic framing (`koubou==0.18.1`)\n\n**Example:**\n\n```bash\nBuild my iOS app, capture the home and settings screens in the simulator, frame them, and prepare them for upload.\n```\n\n### asc-release-flow\n\nReadiness-first App Store submission guidance, including `asc release stage`, `asc submit preflight`, and first-time release blockers.\n\n**Use when:**\n- You want the quickest answer to "can I submit this app now?"\n- You need to separate API-fixable, web-session-fixable, and manual blockers\n- You\'re handling first-time submission issues around availability, IAPs, subscriptions, Game Center, or App Privacy\n\n**Example:**\n\n```bash\nCheck whether version 2.4.0 of my iOS app is ready for App Store submission, show the blockers, and tell me the next `asc` command to run.\n```\n\n### asc-signing-setup\n\nBundle IDs, capabilities, certificates, provisioning profiles, and encrypted signing sync.\n\n**Use when:**\n- You are onboarding a new app or bundle ID\n- You need to create or rotate signing assets\n\n**Example:**\n\n```bash\nSet up signing for com.example.app with iCloud enabled, a distribution certificate, and an App Store profile.\n```\n\n### asc-id-resolver\n\nResolve IDs for apps, builds, versions, groups, and testers.\n\n**Use when:**\n- A command requires IDs and you only have names\n- You want deterministic outputs for automation\n\n**Example:**\n\n```bash\nResolve the App Store Connect app ID, latest build ID, and TestFlight group IDs for MyApp.\n```\n\n### asc-metadata-sync\n\nMetadata and localization sync (including legacy metadata format migration).\n\n**Use when:**\n- You are updating App Store metadata or localizations\n- You need to validate character limits before upload\n- You need to update privacy policy URL or app-level metadata\n\n**Example:**\n\n```bash\nPull my App Store metadata into ./metadata, update the privacy policy URL, and push the changes back safely.\n```\n\n### asc-localize-metadata\n\nTranslate App Store metadata (description, keywords, what\'s new, subtitle) to multiple locales using LLM translation prompts and push via `asc`.\n\n**Use when:**\n- You want to localize an app\'s App Store listing from a source locale (usually en-US)\n- You need locale-aware keywords (not literal translations) and strict character limit enforcement\n- You want a review-before-upload workflow for translations\n\n**Example:**\n\n```bash\nTranslate my en-US App Store metadata into German, French, and Japanese, then show me the changes before upload.\n```\n\n### asc-aso-audit\n\nRun an offline ASO audit on canonical App Store metadata under `./metadata` and surface keyword gaps using Astro MCP.\n\n**Use when:**\n- You want to audit subtitle, keywords, description, and what\'s new fields for waste and formatting issues\n- You want keyword-gap analysis against Astro-tracked rankings and competitor terms\n- You want follow-up actions that map cleanly to `asc metadata keywords ...`\n\n**Example:**\n\n```bash\nAudit ./metadata for ASO problems, then show the highest-value keyword gaps from Astro for my latest version.\n```\n\n### asc-whats-new-writer\n\nGenerate engaging, localized App Store release notes from git log, bullet points, or free text using canonical metadata under `./metadata`.\n\n**Use when:**\n- You want polished What\'s New copy from rough release inputs\n- You want localized release notes across existing locales\n- You want a review-before-upload workflow using `asc metadata push` or direct metadata edits\n\n**Example:**\n\n```bash\nTurn these release bullet points into polished What\'s New notes for en-US and localize them across my existing metadata locales.\n```\n\n### asc-submission-health\n\nPreflight checks, digital-goods readiness validation, submission, and review monitoring.\n\n**Use when:**\n- You want to reduce submission failures\n- You need to track review status and re-submit safely\n- You\'re troubleshooting "version not in valid state" errors\n\n**Example:**\n\n```bash\nPreflight my iOS submission, check encryption/content-rights issues, and tell me what will block review.\n```\n\n### asc-testflight-orchestration\n\nBeta groups, testers, build distribution, and What to Test notes.\n\n**Use when:**\n- You manage multiple TestFlight groups and testers\n- You need consistent beta rollout steps\n\n**Example:**\n\n```bash\nExport my current TestFlight config, create a new external group, add testers, and attach the latest build.\n```\n\n### asc-build-lifecycle\n\nBuild processing, latest build resolution, and cleanup.\n\n**Use when:**\n- You are waiting on build processing\n- You want automated cleanup and retention policies\n\n**Example:**\n\n```bash\nFind the latest processed build for app 123456789 and preview expiring all TestFlight builds older than 90 days.\n```\n\n### asc-ppp-pricing\n\nTerritory-specific pricing using purchasing power parity (PPP).\n\n**Use when:**\n- You want different prices for different countries\n- You are implementing localized pricing strategies\n- You need to adjust prices based on regional purchasing power\n\n**Example:**\n\n```bash\nUpdate my subscription pricing for India, Brazil, and Mexico using a PPP-style rollout and verify the result.\n```\n\n### asc-subscription-localization\n\nBulk-localize subscription and IAP display names across all App Store locales.\n\n**Use when:**\n- You want to set the same subscription display name in every language at once\n- You need to fill in missing subscription/group/IAP localizations\n- You\'re tired of clicking through each locale in App Store Connect manually\n\n**Example:**\n\n```bash\nSet the display name Monthly Pro across all missing locales for this subscription and verify which locales were created.\n```\n\n### asc-revenuecat-catalog-sync\n\nReconcile App Store Connect subscriptions/IAP with RevenueCat products, entitlements, offerings, and packages.\n\n**Use when:**\n- You want to sync ASC product catalogs to RevenueCat\n- You need to create missing ASC subscriptions/IAPs before mapping them\n- You want an audit-first workflow with explicit apply confirmation\n\n**Example:**\n\n```bash\nAudit my App Store Connect subscriptions and IAPs against RevenueCat, then create any missing mappings after I approve the plan.\n```\n\n### asc-notarization\n\nArchive, export, and notarize macOS apps with Developer ID signing.\n\n**Use when:**\n- You need to notarize a macOS app for distribution outside the App Store\n- You want the full flow: archive → Developer ID export → zip → notarize → staple\n- You\'re troubleshooting Developer ID signing or trust chain issues\n\n**Example:**\n\n```bash\nArchive my macOS app, export it for Developer ID, notarize the ZIP, and staple the result.\n```\n\n### asc-crash-triage\n\nTriage TestFlight crashes, beta feedback, and performance diagnostics.\n\n**Use when:**\n- You want to review recent TestFlight crash reports\n- You need a crash summary grouped by signature, device, and build\n- You want to check beta tester feedback and screenshots\n- You need performance diagnostics (hangs, disk writes, launches) for a build\n\n**Example:**\n\n```bash\nShow me the latest TestFlight crashes and feedback for MyApp, grouped by signature and affected build.\n```\n\n### asc-wall-submit\n\nSubmit or update an app entry in the App-Store-Connect-CLI Wall of Apps using `asc apps wall submit`.\n\n**Use when:**\n- You want to add your app to the Wall of Apps\n- You want to update an existing Wall entry\n- You want the built-in CLI Wall submission flow\n\n**Example:**\n\n```bash\nSubmit app 1234567890 to the Wall of Apps using the built-in asc apps wall submit flow.\n```',
    },
    'usage': {
        "description": 'Skills are automatically available once installed.',
        "guidance": 'Skills are automatically available once installed. The agent will use them when relevant tasks are detected.',
    },
    'skill-structure': {
        "description": 'Each skill contains:\n- `SKILL.',
        "guidance": 'Each skill contains:\n- `SKILL.md` - Instructions for the agent\n- `scripts/` - Helper scripts for automation (optional)\n- `references/` - Supporting documentation (optional)',
    },
    'license': {
        "description": 'MIT.',
        "guidance": 'MIT',
    },
}


@mcp.tool()
def list_app_store_connect_cli_skills() -> dict:
    """List all available app_store_connect_cli skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_app_store_connect_cli_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific app_store_connect_cli skill."""
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
    hint = get_presentation_hint('app_store_connect_cli', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@app_store_connect_cli",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'app_store_connect_cli',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
