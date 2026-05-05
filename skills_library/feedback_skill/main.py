"""Feedback skill — submit qualitative feedback on any skill response.

Allows clients to rate and comment on skill output quality directly from
Claude.ai, ChatGPT, or the Gemini extension. Low-rated feedback is consumed
by supervisor.py to improve skill tone, accuracy, and formatting.
"""

import logging
import os

from fastmcp import FastMCP

logger = logging.getLogger(__name__)

mcp = FastMCP("feedback-skill")


@mcp.tool()
def submit_feedback(
    skill: str,
    rating: int,
    tool: str = "",
    comment: str = "",
) -> dict:
    """Submit feedback on a skill's response quality.

    Call this after any skill gives a response you want to improve. Low ratings
    (1-2) automatically trigger a skill improvement review.

    Args:
        skill: The skill that produced the response (e.g. 'amazon_skills').
        rating: Quality rating from 1 (very poor) to 5 (excellent).
        tool: Optional — specific tool within the skill (e.g. 'calculate_fba_fees').
        comment: Optional — what was wrong or how to improve (tone, accuracy, format, etc.).
    """
    if not 1 <= rating <= 5:
        return {"error": "Rating must be between 1 and 5."}

    client_id = os.getenv("CLIENT_ID", "unknown")

    try:
        from core.db import log_feedback
        log_feedback(
            client_id=client_id,
            skill=skill,
            tool=tool or None,
            rating=rating,
            comment=comment or None,
        )
    except Exception as exc:
        logger.warning("feedback_logs insert failed: %s", exc)

    if rating <= 2:
        return {
            "status": "ok",
            "message": f"Feedback recorded (rating {rating}/5). This will be reviewed to improve the skill.",
        }
    return {
        "status": "ok",
        "message": f"Feedback recorded (rating {rating}/5). Thank you!",
    }
