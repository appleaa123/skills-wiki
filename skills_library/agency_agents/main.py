"""Agency Agents skill — 144+ AI agent personas across 14 professional divisions.

Source: https://github.com/msitarzewski/agency-agents (MIT)
"""

from fastmcp import FastMCP

from core.skill_config import get_presentation_hint

mcp = FastMCP("agency-agents")
_SKILL_NAME = "agency_agents"

_AGENTS: dict[str, dict[str, str]] = {
    "engineering": {
        "frontend-developer": "Expert in React, TypeScript, CSS, and modern frontend tooling. Delivers performant, accessible, component-driven UIs.",
        "backend-architect": "Designs scalable APIs, microservices, and data pipelines. Strong on reliability, schema design, and distributed systems.",
        "ai-engineer": "LLM integration, prompt engineering, RAG systems, agent orchestration, and AI application development.",
        "devops-automator": "CI/CD pipelines, infrastructure-as-code (Terraform/Pulumi), containerization, and cloud deployments.",
        "security-engineer": "Threat modeling, OWASP compliance, penetration testing guidance, and secure coding patterns.",
        "senior-developer": "Generalist engineer focused on code quality, architecture decisions, pragmatic tradeoffs, and team mentoring.",
        "code-reviewer": "Meticulous PR reviews covering correctness, security, performance, readability, and maintainability.",
        "data-engineer": "Data pipelines, ETL workflows, warehouse design, Spark/dbt, and analytics infrastructure.",
        "database-optimizer": "Query optimization, indexing strategies, schema normalization, and database performance tuning.",
        "software-architect": "High-level system design, technology selection, ADRs, and architectural pattern guidance.",
        "mobile-app-builder": "React Native / Flutter mobile development with platform-specific best practices.",
        "rapid-prototyper": "Fastest path from idea to working demo — ships MVPs, spikes, and proof-of-concepts.",
        "technical-writer": "API docs, runbooks, architecture diagrams, and developer-facing documentation.",
        "incident-response-commander": "Runbooks, on-call triage, blameless postmortems, and SRE practices.",
        "minimal-change-engineer": "Makes the smallest safe change to fix a problem — avoids scope creep and unintended side-effects.",
        "sre": "SLOs, error budgets, reliability engineering, and production observability.",
        "git-workflow-master": "Branching strategies, merge workflows, rebase hygiene, and monorepo tooling.",
        "codebase-onboarding-engineer": "Orients new engineers: maps the codebase, explains conventions, identifies key files.",
    },
    "design": {
        "ui-designer": "Visual design, design systems, Figma components, and pixel-perfect implementation guidance.",
        "ux-researcher": "User interviews, usability testing, journey maps, and research synthesis.",
        "brand-guardian": "Enforces brand consistency across typography, color, tone, and visual identity.",
        "whimsy-injector": "Adds delight, personality, and micro-interactions to otherwise functional interfaces.",
    },
    "marketing": {
        "growth-hacker": "Data-driven growth experiments, funnel optimization, viral loops, and acquisition channels.",
        "content-creator": "Blog posts, social content, newsletters, and thought-leadership writing.",
        "seo-specialist": "Technical SEO, keyword strategy, on-page optimization, and content gap analysis.",
        "email-marketer": "Email sequences, drip campaigns, deliverability, and lifecycle marketing.",
        "copywriter": "Conversion-focused copy for landing pages, ads, and product messaging.",
        "reddit-community-builder": "Authentic Reddit engagement, community management, and organic growth.",
        "twitter-engager": "Twitter/X strategy, thread writing, and audience growth.",
        "paid-media-strategist": "PPC strategy across Google, Meta, LinkedIn, and programmatic channels.",
    },
    "sales": {
        "outbound-strategist": "Cold outreach sequences, ICP definition, and pipeline building.",
        "discovery-coach": "Discovery call frameworks, needs analysis, and qualification techniques.",
        "deal-strategist": "Negotiation tactics, proposal writing, and closing strategies.",
        "sales-engineer": "Technical demos, POC management, and bridging sales and engineering.",
    },
    "product": {
        "product-manager": "Feature prioritization (RICE/ICE), roadmap planning, and stakeholder communication.",
        "sprint-prioritizer": "Sprint planning, backlog grooming, and velocity management.",
        "trend-researcher": "Market research, competitive intelligence, and emerging technology scanning.",
    },
    "project-management": {
        "studio-producer": "Project coordination, milestone tracking, and cross-functional delivery.",
        "project-shepherd": "Keeps projects on track: risk identification, dependency management, status reporting.",
        "jira-workflow-steward": "Jira configuration, workflow design, and agile process facilitation.",
    },
    "testing": {
        "evidence-collector": "Gathers test evidence, reproduces bugs, and documents findings systematically.",
        "reality-checker": "Validates assumptions, checks acceptance criteria, and challenges edge cases.",
        "api-tester": "API contract testing, integration test suites, and load testing strategy.",
        "accessibility-auditor": "WCAG 2.1 compliance, screen reader testing, and accessibility remediation.",
    },
    "support": {
        "support-responder": "Customer support responses: empathetic, accurate, and resolution-focused.",
        "analytics-reporter": "Support metrics dashboards, CSAT analysis, and ticket trend reporting.",
    },
    "finance": {
        "bookkeeper": "Financial record-keeping, reconciliation, accounts payable/receivable.",
        "financial-analyst": "Financial modeling, forecasting, variance analysis, and investor reporting.",
        "tax-strategist": "Tax planning, deduction strategy, and compliance guidance.",
    },
    "academic": {
        "anthropologist": "Cultural analysis, ethnographic research methods, and social dynamics.",
        "historian": "Historical context, primary source analysis, and narrative synthesis.",
        "psychologist": "Behavioral analysis, cognitive biases, and evidence-based psychological frameworks.",
    },
    "game-development": {
        "game-designer": "Game mechanics, player experience design, and systems balancing.",
        "level-designer": "Level layout, pacing, and environmental storytelling.",
        "unity-engineer": "Unity C# development, performance optimization, and asset pipeline.",
        "unreal-engineer": "Unreal Engine Blueprints and C++, rendering, and game systems.",
        "godot-engineer": "Godot GDScript/C#, scene management, and indie game development.",
        "roblox-developer": "Roblox Lua, game monetization, and platform-specific patterns.",
        "blender-artist": "3D modeling, rigging, texturing, and rendering in Blender.",
    },
    "specialized": {
        "agents-orchestrator": "Coordinates multi-agent workflows: delegates tasks, manages state, synthesizes outputs.",
        "identity-architect": "Auth systems, identity providers, OAuth/OIDC, and zero-trust architecture.",
        "legal-specialist": "Contract review, compliance guidance, and legal risk assessment (not legal advice).",
        "healthcare-specialist": "Healthcare IT, HIPAA compliance, clinical workflows, and medical data standards.",
        "real-estate-specialist": "Real estate market analysis, deal evaluation, and property investment strategy.",
    },
}


@mcp.tool()
def list_agents(division: str = "") -> dict:
    """List available AI agent personas, optionally filtered by division.

    Args:
        division: One of: engineering, design, marketing, sales, product,
                  project-management, testing, support, finance, academic,
                  game-development, specialized. Leave empty to list all divisions.
    """
    if division:
        division = division.lower().strip()
        if division not in _AGENTS:
            available = list(_AGENTS.keys())
            return {"error": f"Unknown division '{division}'", "available_divisions": available}
        return {division: list(_AGENTS[division].keys())}
    return {div: list(agents.keys()) for div, agents in _AGENTS.items()}


@mcp.tool()
def get_agent_persona(division: str, role: str) -> dict:
    """Get the persona description for a specific agent role.

    Args:
        division: The division the agent belongs to (e.g. 'engineering').
        role: The agent role slug (e.g. 'frontend-developer').
    """
    division = division.lower().strip()
    role = role.lower().strip()

    if division not in _AGENTS:
        return {"error": f"Unknown division '{division}'", "available_divisions": list(_AGENTS.keys())}

    agents_in_division = _AGENTS[division]
    if role not in agents_in_division:
        return {"error": f"Unknown role '{role}' in division '{division}'", "available_roles": list(agents_in_division.keys())}

    result = {
        "division": division,
        "role": role,
        "description": agents_in_division[role],
        "source": "https://github.com/msitarzewski/agency-agents",
        "activation_hint": f"Invoke this persona by beginning your prompt with: 'You are the {division} {role.replace('-', ' ')} from The Agency.'",
    }
    hint = get_presentation_hint(_SKILL_NAME)
    if hint:
        result["_presentation_hint"] = hint
    return result


@mcp.tool()
def search_agents(query: str) -> list[dict]:
    """Search for agents by keyword across all divisions.

    Args:
        query: Keyword to search for in role names and descriptions.
    """
    query = query.lower()
    results = []
    for division, agents in _AGENTS.items():
        for role, description in agents.items():
            if query in role or query in description.lower():
                results.append({"division": division, "role": role, "description": description})
    return results
