"""Skill: app_store_preflight."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("app-store-preflight")


_SKILLS: dict[str, dict] = {
    'overview': {
        "description": 'Preflight helps developers catch potential App Store Review guideline violations **before** submitting their app.',
        "guidance": 'Preflight helps developers catch potential App Store Review guideline violations **before** submitting their app. It scans your Xcode project, source code, metadata, and configuration files to flag issues that commonly result in rejections from Apple.\n\nThis skill integrates with the [`asc` CLI](https://github.com/rudrankriyam/App-Store-Connect-CLI) (`brew install asc`) and the [ASC CLI Skills](https://github.com/rudrankriyam/app-store-connect-cli-skills) to pull and inspect App Store metadata.\n\nMost metadata examples assume the canonical JSON layout written by\n`asc metadata pull`. If you are starting from fastlane metadata, adapt the path\nexamples or pull the canonical `asc` layout first.',
    },
    'install': {
        "description": '```bash\nnpx skills add truongduy2611/app-store-preflight-skills\n```.',
        "guidance": '```bash\nnpx skills add truongduy2611/app-store-preflight-skills\n```',
    },
    'guideline-index-by-app-type': {
        "description": 'The `references/guidelines/` directory contains a **complete index of all 100+ Apple Review Guidelines** and **10 app-type specific checklists**:\n\n| Checklist | App Type |\n|-----------|----------|\n| [',
        "guidance": 'The `references/guidelines/` directory contains a **complete index of all 100+ Apple Review Guidelines** and **10 app-type specific checklists**:\n\n| Checklist | App Type |\n|-----------|----------|\n| [all_apps.md](./references/guidelines/by-app-type/all_apps.md) | Universal (every submission) |\n| [subscription_iap.md](./references/guidelines/by-app-type/subscription_iap.md) | Subscriptions / In-App Purchases |\n| [social_ugc.md](./references/guidelines/by-app-type/social_ugc.md) | Social / User-Generated Content |\n| [kids.md](./references/guidelines/by-app-type/kids.md) | Kids Category |\n| [health_fitness.md](./references/guidelines/by-app-type/health_fitness.md) | Health, Fitness & Medical |\n| [games.md](./references/guidelines/by-app-type/games.md) | Games |\n| [macos.md](./references/guidelines/by-app-type/macos.md) | macOS / Mac App Store |\n| [ai_apps.md](./references/guidelines/by-app-type/ai_apps.md) | AI / Generative AI |\n| [crypto_finance.md](./references/guidelines/by-app-type/crypto_finance.md) | Crypto, Finance & Trading |\n| [vpn.md](./references/guidelines/by-app-type/vpn.md) | VPN & Networking |\n\n📖 Full guideline reference: [references/guidelines/README.md](./references/guidelines/README.md)',
    },
    'how-it-works': {
        "description": '1.',
        "guidance": '1. **Identify app type** → load the matching checklist from `references/guidelines/by-app-type/`\n2. **Pull metadata** using `asc metadata pull --app "<APP_ID>" --version "<VERSION>" --dir ./metadata` (or the `asc-metadata-sync` skill)\n3. **Scan** against rejection rules in `references/rules/`\n4. **Report** findings with severity, affected files, and resolution steps\n5. **Autofix + Validate** — apply fixes, re-run affected checks\n\nSee [`SKILL.md`](./SKILL.md) for the full AI agent instructions.',
    },
    'rejection-rules': {
        "description": 'All rules live in `references/rules/`, organized by category:\n\n### Metadata (`references/rules/metadata/`)\n\n| Rule | Guideline | What It Catches |\n|------|-----------|----------------|\n| [competitor_t',
        "guidance": 'All rules live in `references/rules/`, organized by category:\n\n### Metadata (`references/rules/metadata/`)\n\n| Rule | Guideline | What It Catches |\n|------|-----------|----------------|\n| [competitor_terms](./references/rules/metadata/competitor_terms.md) | 2.3.1 | Android, Google Play, and other competitor brands |\n| [apple_trademark](./references/rules/metadata/apple_trademark.md) | 5.2.5 | Apple device images in icon, Apple trademark misuse |\n| [china_storefront](./references/rules/metadata/china_storefront.md) | 5 | OpenAI/ChatGPT/Gemini references (China) |\n| [accurate_metadata](./references/rules/metadata/accurate_metadata.md) | 2.3.4 | Device frames in app preview videos |\n| [subscription_metadata](./references/rules/metadata/subscription_metadata.md) | 3.1.2 | Missing ToS/EULA and Privacy Policy links |\n\n### Subscriptions (`references/rules/subscription/`)\n\n| Rule | Guideline | What It Catches |\n|------|-----------|----------------|\n| [missing_tos_pp](./references/rules/subscription/missing_tos_pp.md) | 3.1.2 | No Terms or Privacy Policy in app/metadata |\n| [misleading_pricing](./references/rules/subscription/misleading_pricing.md) | 3.1.2 | Monthly price more prominent than billed amount |\n\n### Privacy (`references/rules/privacy/`)\n\n| Rule | Guideline | What It Catches |\n|------|-----------|----------------|\n| [unnecessary_data](./references/rules/privacy/unnecessary_data.md) | 5.1.1 | Requiring irrelevant personal data |\n| [privacy_manifest](./references/rules/privacy/privacy_manifest.md) | 5.1.1 | Missing `PrivacyInfo.xcprivacy` |\n\n### Design (`references/rules/design/`)\n\n| Rule | Guideline | What It Catches |\n|------|-----------|----------------|\n| [sign_in_with_apple](./references/rules/design/sign_in_with_apple.md) | 4.0 | Asking name/email after SIWA |\n| [minimum_functionality](./references/rules/design/minimum_functionality.md) | 4.2 | WebView wrappers, apps with < 3 screens, no unique value |\n\n### Entitlements (`references/rules/entitlements/`)\n\n| Rule | Guideline | What It Catches |\n|------|-----------|----------------|\n| [unused_entitlements](./references/rules/entitlements/unused_entitlements.md) | 2.4.5(i) | Unused entitlements in Xcode project |',
    },
    'adding-new-rules': {
        "description": 'Create a `.',
        "guidance": 'Create a `.md` file in the appropriate `references/rules/` subdirectory:\n\n```markdown\n# Rule: [Short Title]\n- **Guideline**: [Apple Guideline Number]\n- **Severity**: REJECTION | WARNING\n- **Category**: metadata | subscription | privacy | design | entitlements',
    },
    'example-rejection': {
        "description": '```.',
        "guidance": '```',
    },
    'related-skills': {
        "description": '- [app-store-connect-cli-skills](https://github.',
        "guidance": '- [app-store-connect-cli-skills](https://github.com/rudrankriyam/app-store-connect-cli-skills) — ASC CLI skills for metadata sync, ASO audit, release flow',
    },
    'license': {
        "description": 'MIT.',
        "guidance": 'MIT',
    },
}


@mcp.tool()
def list_app_store_preflight_skills() -> dict:
    """List all available app_store_preflight skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_app_store_preflight_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific app_store_preflight skill."""
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
    hint = get_presentation_hint('app_store_preflight', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@app_store_preflight",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'app_store_preflight',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
