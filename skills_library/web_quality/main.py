"""Skill: web_quality."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("web-quality")


_SKILLS: dict[str, dict] = {
    'why-web-quality-skills': {
        "description": 'While interface guidelines tell you *what* to build, Web Quality Skills tell you *how* to build it performantly, accessibly, and optimally for search engines.',
        "guidance": 'While interface guidelines tell you *what* to build, Web Quality Skills tell you *how* to build it performantly, accessibly, and optimally for search engines. These skills encode the collective wisdom from:\n\n- **150+ Lighthouse audits** across Performance, Accessibility, SEO, and Best Practices\n- **Core Web Vitals** optimization patterns (LCP, INP, CLS)\n- **Real-world performance engineering** experience\n- **WCAG 2.2** accessibility standards\n- **Modern SEO** requirements',
    },
    'available-skills': {
        "description": '| Skill | Description | Use when |\n|-------|-------------|----------|\n| **[web-quality-audit](#web-quality-audit)** | Comprehensive quality review across all categories | "Audit my site", "Review this',
        "guidance": '| Skill | Description | Use when |\n|-------|-------------|----------|\n| **[web-quality-audit](#web-quality-audit)** | Comprehensive quality review across all categories | "Audit my site", "Review this for quality", "Check web quality" |\n| **[performance](#performance)** | Loading speed, runtime efficiency, resource optimization | "Optimize performance", "Speed up my site", "Fix slow loading" |\n| **[core-web-vitals](#core-web-vitals)** | LCP, INP, CLS specific optimizations | "Improve Core Web Vitals", "Fix LCP", "Reduce CLS" |\n| **[accessibility](#accessibility)** | WCAG compliance, screen reader support, keyboard navigation | "Improve accessibility", "WCAG audit", "a11y review" |\n| **[seo](#seo)** | Search engine optimization, crawlability, structured data | "Optimize for SEO", "Improve search ranking", "Fix meta tags" |\n| **[best-practices](#best-practices)** | Security, modern APIs, code quality patterns | "Apply best practices", "Security audit", "Code quality review" |',
    },
    'quick-start': {
        "description": '### Installation\n\nadd-skill is a powerful CLI tool that lets you install agent skills onto your coding agents from git repositories.',
        "guidance": "### Installation\n\nadd-skill is a powerful CLI tool that lets you install agent skills onto your coding agents from git repositories. Whether you're using OpenCode, Claude Code, Codex, or Cursor, the add-skill tool makes it simple to extend your agent's capabilities with specialized instruction sets. Use add-skill to automate release notes, create pull requests, integrate with external tools, and more. Simply run npx add-skill to get started.\n\n```bash\nnpx skills add addyosmani/web-quality-skills\n```\n\nor\n\n```\nnpx add-skill addyosmani/web-quality-skills\n```\n\nOr manually:\n\n```bash\ncp -r skills/* ~/.claude/skills/\n```\n\n#### claude.ai\n\nAdd skills to your project knowledge or paste the SKILL.md contents into your conversation.\n\n### Usage\n\nSkills activate automatically when your request matches their description. Examples:\n\n```\nAudit this page for web quality issues\n```\n\n```\nOptimize performance and fix Core Web Vitals\n```\n\n```\nReview accessibility and suggest improvements\n```\n\n```\nMake this SEO-ready\n```",
    },
    'skill-details': {
        "description": '### web-quality-audit\n\nThe comprehensive skill that orchestrates all other skills.',
        "guidance": '### web-quality-audit\n\nThe comprehensive skill that orchestrates all other skills. Use this for full-site audits or when you\'re unsure which specific area needs attention.\n\n**Trigger phrases:** "audit my site", "quality review", "lighthouse audit", "check web quality"\n\n**What it checks:**\n- All Core Web Vitals metrics\n- 50+ performance patterns\n- 40+ accessibility rules\n- 30+ SEO requirements\n- 20+ security/best practice patterns\n\n### performance\n\nDeep-dive into loading and runtime performance optimization.\n\n**Trigger phrases:** "speed up", "optimize performance", "reduce load time", "fix slow"\n\n**Key optimizations:**\n- Critical rendering path\n- JavaScript bundling and code splitting\n- Image optimization (formats, sizing, lazy loading)\n- Font loading strategies\n- Caching and preloading\n- Server response optimization\n\n### core-web-vitals\n\nSpecialized skill for the three Core Web Vitals that affect Google Search ranking.\n\n**Trigger phrases:** "Core Web Vitals", "LCP", "INP", "CLS", "page experience"\n\n**Metrics covered:**\n- **LCP** (Largest Contentful Paint) < 2.5s\n- **INP** (Interaction to Next Paint) < 200ms\n- **CLS** (Cumulative Layout Shift) < 0.1\n\n### accessibility\n\nComprehensive accessibility audit following WCAG 2.2 guidelines.\n\n**Trigger phrases:** "accessibility", "a11y", "WCAG", "screen reader", "keyboard navigation"\n\n**Categories:**\n- Perceivable (text alternatives, captions, contrast)\n- Operable (keyboard, timing, seizures, navigation)\n- Understandable (readable, predictable, input assistance)\n- Robust (compatible with assistive technologies)\n\n### seo\n\nSearch engine optimization for better visibility and ranking.\n\n**Trigger phrases:** "SEO", "search optimization", "meta tags", "structured data", "sitemap"\n\n**What it covers:**\n- Technical SEO (crawlability, indexability)\n- On-page SEO (meta tags, headings, content structure)\n- Structured data (JSON-LD, schema.org)\n- Mobile-friendliness\n- Performance signals\n\n### best-practices\n\nModern web development standards and security practices.\n\n**Trigger phrases:** "best practices", "security audit", "modern standards", "code quality"\n\n**Areas covered:**\n- HTTPS and security headers\n- Modern JavaScript APIs\n- Browser compatibility\n- Error handling\n- Console cleanliness',
    },
    'thresholds-reference': {
        "description": '### Core Web Vitals\n\n| Metric | Good | Needs improvement | Poor |\n|--------|------|-------------------|------|\n| LCP | ≤ 2.',
        "guidance": '### Core Web Vitals\n\n| Metric | Good | Needs improvement | Poor |\n|--------|------|-------------------|------|\n| LCP | ≤ 2.5s | 2.5s – 4.0s | > 4.0s |\n| INP | ≤ 200ms | 200ms – 500ms | > 500ms |\n| CLS | ≤ 0.1 | 0.1 – 0.25 | > 0.25 |\n\n### Performance budget recommendations\n\n| Resource type | Budget |\n|---------------|--------|\n| Total page weight | < 1.5 MB |\n| JavaScript | < 300 KB (compressed) |\n| CSS | < 100 KB (compressed) |\n| Images | < 500 KB total above-fold |\n| Fonts | < 100 KB |\n| Third-party | < 200 KB |\n\n### Lighthouse score targets\n\n| Category | Target score |\n|----------|--------------|\n| Performance | ≥ 90 |\n| Accessibility | 100 |\n| Best Practices | ≥ 95 |\n| SEO | ≥ 95 |',
    },
    'framework-specific-notes': {
        "description": 'These skills are framework-agnostic, but some common patterns:\n\n**React/Next.',
        "guidance": 'These skills are framework-agnostic, but some common patterns:\n\n**React/Next.js:** Use `next/image`, `React.lazy()`, `Suspense`, `useCallback`/`useMemo` for INP  \n**Vue/Nuxt:** Use `nuxt/image`, async components, `v-once`, computed properties  \n**Svelte/SvelteKit:** Use `{#await}`, `svelte:image`, reactive statements  \n**Astro:** Use `<Image>`, partial hydration, view transitions  \n**Static HTML:** Use native lazy loading, `<picture>`, preconnect hints',
    },
    'contributing': {
        "description": 'Contributions welcome! Please follow the [Agent Skills specification](https://agentskills.',
        "guidance": 'Contributions welcome! Please follow the [Agent Skills specification](https://agentskills.io/specification).\n\n1. Fork the repository\n2. Create your skill in `skills/{skill-name}/SKILL.md`\n3. Keep SKILL.md under 500 lines (use `references/` for details)\n4. Include practical examples and patterns\n5. Submit a pull request',
    },
    'resources': {
        "description": '- [Google Lighthouse Documentation](https://developer.',
        "guidance": '- [Google Lighthouse Documentation](https://developer.chrome.com/docs/lighthouse/)\n- [web.dev Learn Performance](https://web.dev/learn/performance/)\n- [Core Web Vitals](https://web.dev/articles/vitals)\n- [WCAG 2.2 Guidelines](https://www.w3.org/WAI/WCAG22/quickref/)\n- [Agent Skills Specification](https://agentskills.io/specification)',
    },
    'license': {
        "description": 'MIT License - see [LICENSE](LICENSE) for details.',
        "guidance": 'MIT License - see [LICENSE](LICENSE) for details.\n\n---\n\nBuilt with insights from the Chrome DevTools team, web performance experts, and accessibility advocates to help developers create high-quality web experiences.',
    },
}


@mcp.tool()
def list_web_quality_skills() -> dict:
    """List all available web_quality skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_web_quality_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific web_quality skill."""
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
    hint = get_presentation_hint('web_quality', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@web_quality",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'web_quality',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
