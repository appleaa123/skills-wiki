"""Per-client skill configuration helpers.

Fetches presentation preferences from client_skill_configs and converts them
into a natural-language hint that skills append to their output. The LLM
(Claude / ChatGPT / Gemini) reads the hint and formats its response accordingly.

Config schema (all fields optional):
    tone:                "formal" | "casual" | "technical"
    format:              "prose" | "bullets" | "table"
    language:            any language name, e.g. "Spanish"
    response_length:     "brief" | "standard" | "detailed"
    custom_instructions: free-text string

Example output of build_presentation_hint():
    "Respond in Spanish. Use bullet point format. Keep the response brief.
     Additional instructions: Always start with a one-line cost summary."
"""

import logging
import os

logger = logging.getLogger(__name__)

_CONFIG_FIELDS = {
    "tone": {
        "formal": "Use a formal, professional tone.",
        "casual": "Use a casual, conversational tone.",
        "technical": "Use a technical tone with precise terminology.",
    },
    "format": {
        "prose": "Write in flowing prose paragraphs.",
        "bullets": "Use bullet points for all lists and key information.",
        "table": "Present structured data in markdown tables where possible.",
    },
    "response_length": {
        "brief": "Keep the response concise — one to two sentences per point.",
        "standard": "",
        "detailed": "Provide a thorough, detailed response with full explanations.",
    },
}


def get_client_skill_config(client_id: str, skill: str) -> dict:
    """Return the config dict for a client+skill pair. Returns {} on any error."""
    try:
        from core.db import _get_client
        resp = (
            _get_client()
            .table("client_skill_configs")
            .select("config")
            .eq("client_id", client_id)
            .eq("skill", skill)
            .single()
            .execute()
        )
        config = resp.data.get("config", {}) if resp.data else {}
        if config:
            logger.info(f"[customization] Fetched config for {client_id}/{skill}: {config}")
        return config
    except Exception as exc:
        logger.debug(f"[customization] client_skill_configs fetch skipped for {client_id}/{skill}: {exc}")
        return {}


def set_client_skill_config(client_id: str, skill: str, config: dict) -> None:
    """Upsert a config row. Never raises — failures are logged only."""
    try:
        from core.db import _get_client
        import datetime
        _get_client().table("client_skill_configs").upsert(
            {
                "client_id": client_id,
                "skill": skill,
                "config": config,
                "updated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            },
            on_conflict="client_id,skill",
        ).execute()
    except Exception as exc:
        logger.warning("client_skill_configs upsert failed: %s", exc)


def build_presentation_hint(config: dict) -> str:
    """Convert a config dict into a natural-language instruction string for the LLM."""
    if not config:
        return ""

    parts: list[str] = []

    language = config.get("language", "").strip()
    if language and language.lower() not in ("english", "en"):
        parts.append(f"Respond in {language}.")

    for field, mapping in _CONFIG_FIELDS.items():
        value = config.get(field, "").strip()
        if value and value in mapping and mapping[value]:
            parts.append(mapping[value])

    custom = config.get("custom_instructions", "").strip()
    if custom:
        parts.append(f"Additional instructions: {custom}")

    hint = " ".join(parts)
    if hint:
        logger.info(f"[customization] Built hint: {hint}")
    return hint


def get_presentation_hint(skill: str, client_id: str = None) -> str:
    """Convenience wrapper: read CLIENT_ID via core.config or provided arg, return hint string."""
    if not client_id:
        from core.config import get_client_id
        client_id = get_client_id()
    
    if not client_id:
        return ""
        
    config = get_client_skill_config(client_id, skill)
    return build_presentation_hint(config)
