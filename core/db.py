"""Local JSON persistence layer — replaces Supabase for the open-source version."""

import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

_CONFIG_PATH = Path(__file__).parent.parent / "data" / "local_config.json"

_DEFAULT: dict = {"enabled_skills": [], "skill_configs": {}, "connections": {}}


def _read() -> dict:
    if not _CONFIG_PATH.exists():
        return dict(_DEFAULT)
    try:
        return json.loads(_CONFIG_PATH.read_text())
    except Exception as exc:
        logger.warning("Failed to read local_config.json: %s", exc)
        return dict(_DEFAULT)


def _write(data: dict) -> None:
    try:
        _CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
        _CONFIG_PATH.write_text(json.dumps(data, indent=2))
    except Exception as exc:
        logger.warning("Failed to write local_config.json: %s", exc)


def fetch_enabled_skills(_client_id: str | None = None) -> list[str]:
    return _read().get("enabled_skills", [])


def get_client_skill_config(_client_id: str, skill: str) -> dict:
    return _read().get("skill_configs", {}).get(skill, {})


def set_client_skill_config(_client_id: str, skill: str, config: dict) -> None:
    data = _read()
    data.setdefault("skill_configs", {})[skill] = config
    _write(data)
