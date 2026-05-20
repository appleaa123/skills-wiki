import json
from pathlib import Path

_CONFIG_PATH = Path(__file__).parent.parent / "data" / "local_config.json"


def _read_config() -> dict:
    if not _CONFIG_PATH.exists():
        return {"enabled_skills": [], "skill_configs": {}, "connections": {}}
    return json.loads(_CONFIG_PATH.read_text())


def get_enabled_skills(_client_id: str | None = None) -> list[str]:
    return _read_config().get("enabled_skills", [])
