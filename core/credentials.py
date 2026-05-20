"""Service credential resolver — reads plaintext from data/local_config.json."""

import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

_CONFIG_PATH = Path(__file__).parent.parent / "data" / "local_config.json"


def _read() -> dict:
    if not _CONFIG_PATH.exists():
        return {}
    try:
        return json.loads(_CONFIG_PATH.read_text())
    except Exception:
        return {}


def get_service_credential(service: str, _client_id: str | None = None) -> dict | None:
    return _read().get("connections", {}).get(service) or None


def list_configured_services(_client_id: str | None = None) -> list[str]:
    return sorted(_read().get("connections", {}).keys())
