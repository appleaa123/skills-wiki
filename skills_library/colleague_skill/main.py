"""Colleague Skill — distill a person into an AI-powered skill persona.

Source: https://github.com/titanwings/colleague-skill (MIT)

Wraps the core colleague skill creation workflow: gather work + personality
data and generate a structured SKILL.md that an LLM can embody.
"""

from fastmcp import FastMCP

from core.skill_config import get_presentation_hint

mcp = FastMCP("colleague-skill")
_SKILL_NAME = "colleague_skill"

_WORK_TEMPLATE = """---
name: {name}
type: colleague
company: {company}
role: {role}
version: 1.0.0
---

# {name} — Work Profile

## Identity
{identity}

## Technical Standards
{technical_standards}

## Workflow Patterns
{workflow_patterns}

## Communication Style (Work)
{work_communication}

## Key Deliverables
{deliverables}
"""

_PERSONA_TEMPLATE = """# {name} — Personality Profile

## Core Traits
{core_traits}

## Decision-Making Style
{decision_style}

## Communication Preferences
{communication_preferences}

## Known Triggers & Patterns
{triggers}

## Relationship Dynamics
{relationship_dynamics}
"""

_SKILL_TEMPLATE = """---
name: {name}
type: colleague
company: {company}
role: {role}
version: 1.0.0
---

# {name}

You are {name}, {identity}.

## How You Work
{technical_standards}

{workflow_patterns}

## How You Communicate
{work_communication}

{communication_preferences}

## Your Personality
{core_traits}

## How You Make Decisions
{decision_style}
"""


@mcp.tool()
def build_colleague_skill(
    name: str,
    company: str,
    role: str,
    mbti: str = "",
    technical_standards: str = "",
    workflow_patterns: str = "",
    work_communication: str = "",
    deliverables: str = "",
    core_traits: str = "",
    decision_style: str = "",
    communication_preferences: str = "",
    triggers: str = "",
    relationship_dynamics: str = "",
) -> dict:
    """Generate a complete colleague skill profile (SKILL.md content) from provided data.

    Transforms information about a real person into a structured AI persona that
    can be embodied by an LLM to simulate that colleague's thinking and style.

    Args:
        name: Full name of the colleague.
        company: Company or team they work at.
        role: Job title / role (e.g. 'Senior Backend Engineer').
        mbti: Optional MBTI type (e.g. 'INTJ').
        technical_standards: Their coding/technical standards and preferences.
        workflow_patterns: How they approach tasks, review PRs, run meetings, etc.
        work_communication: How they communicate in work contexts (Slack style, doc style).
        deliverables: What they typically produce (code, docs, designs, etc.).
        core_traits: Core personality traits (3-5 bullet points).
        decision_style: How they make decisions — fast/slow, data-driven/intuitive, etc.
        communication_preferences: Personal communication style outside pure work context.
        triggers: Things that energize or frustrate them.
        relationship_dynamics: How they build trust, handle conflict, collaborate.
    """
    identity_parts = [f"{role} at {company}"]
    if mbti:
        identity_parts.append(f"MBTI: {mbti}")
    identity = ", ".join(identity_parts)

    skill_md = _SKILL_TEMPLATE.format(
        name=name,
        company=company,
        role=role,
        identity=identity,
        technical_standards=technical_standards or "(not provided)",
        workflow_patterns=workflow_patterns or "(not provided)",
        work_communication=work_communication or "(not provided)",
        communication_preferences=communication_preferences or "(not provided)",
        core_traits=core_traits or "(not provided)",
        decision_style=decision_style or "(not provided)",
    )

    work_md = _WORK_TEMPLATE.format(
        name=name,
        company=company,
        role=role,
        identity=identity,
        technical_standards=technical_standards or "(not provided)",
        workflow_patterns=workflow_patterns or "(not provided)",
        work_communication=work_communication or "(not provided)",
        deliverables=deliverables or "(not provided)",
    )

    persona_md = _PERSONA_TEMPLATE.format(
        name=name,
        core_traits=core_traits or "(not provided)",
        decision_style=decision_style or "(not provided)",
        communication_preferences=communication_preferences or "(not provided)",
        triggers=triggers or "(not provided)",
        relationship_dynamics=relationship_dynamics or "(not provided)",
    )

    result = {
        "skill_md": skill_md,
        "work_md": work_md,
        "persona_md": persona_md,
        "meta": {
            "name": name,
            "company": company,
            "role": role,
            "mbti": mbti,
            "version": "1.0.0",
        },
        "usage": f"Paste SKILL.md content into your agent system prompt to embody {name}.",
        "source": "https://github.com/titanwings/colleague-skill",
    }
    hint = get_presentation_hint(_SKILL_NAME)
    if hint:
        result["_presentation_hint"] = hint
    return result


@mcp.tool()
def get_colleague_intake_questions(skill_family: str = "colleague") -> dict:
    """Return the intake questions to gather information for building a colleague skill.

    Args:
        skill_family: One of 'colleague', 'relationship', or 'celebrity'.
    """
    questions = {
        "colleague": {
            "description": "Captures work capability and communication style of a professional colleague.",
            "work_questions": [
                "What is their role and primary responsibilities?",
                "What technical standards or coding practices do they follow?",
                "How do they structure their work day / manage tasks?",
                "How do they communicate in Slack / email / docs?",
                "What are their typical deliverables (code, docs, designs)?",
                "What tools/stack do they prefer?",
            ],
            "persona_questions": [
                "What are 3-5 core personality traits?",
                "How do they make decisions — fast/slow, data vs gut?",
                "What energizes them? What frustrates them?",
                "How do they handle conflict or pushback?",
                "How do they build trust with teammates?",
                "What is their MBTI type (if known)?",
            ],
        },
        "relationship": {
            "description": "Captures emotional patterns and conflict dynamics of a personal relationship.",
            "questions": [
                "How do they express affection or care?",
                "What are their emotional triggers?",
                "How do they handle conflict — fight, flight, or freeze?",
                "What do they need to feel safe in a relationship?",
                "What are their core values in relationships?",
            ],
        },
        "celebrity": {
            "description": "Captures the mental models of a public figure from their public work.",
            "dimensions": [
                "Works: books, films, companies, inventions",
                "Interviews: recurring themes and stated beliefs",
                "Decisions: key choices and reasoning",
                "Expression: communication style and vocabulary",
                "Evaluation: how they judge quality or success",
                "Timeline: evolution of their thinking over time",
            ],
        },
    }

    if skill_family not in questions:
        return {"error": f"Unknown skill family '{skill_family}'", "available": list(questions.keys())}

    return questions[skill_family]
