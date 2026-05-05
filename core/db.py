"""Local JSON persistence layer for Skills Wiki Open Source."""

import json
import logging
import os
from datetime import datetime, timezone
from pathlib import Path

logger = logging.getLogger(__name__)

def _get_db_path() -> Path:
    # Use a local db.json in ~/.skills-wiki directory
    # We create the directory if it doesn't exist
    home_dir = Path.home() / ".skills-wiki"
    home_dir.mkdir(parents=True, exist_ok=True)
    return home_dir / "db.json"

def _load_db() -> dict:
    db_path = _get_db_path()
    if not db_path.exists():
        return {
            "clients": [{"client_id": "local-admin", "enabled_skills": []}],
            "audit_logs": [],
            "feedback_logs": [],
            "client_skill_configs": []
        }
    try:
        with open(db_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as exc:
        logger.warning("Failed to load db.json: %s", exc)
        return {
            "clients": [{"client_id": "local-admin", "enabled_skills": []}],
            "audit_logs": [],
            "feedback_logs": [],
            "client_skill_configs": []
        }

def _save_db(data: dict) -> None:
    try:
        with open(_get_db_path(), "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except Exception as exc:
        logger.warning("Failed to save db.json: %s", exc)

def fetch_enabled_skills(client_id: str) -> list[str]:
    """Return enabled skill names for a client from db.json.
    Defaults to returning all skills or empty list if admin doesn't exist.
    """
    db = _load_db()
    for client in db.get("clients", []):
        if client.get("client_id") == client_id:
            return client.get("enabled_skills", [])
    
    # If client doesn't exist, create default local-admin
    if client_id == "local-admin":
        db.setdefault("clients", []).append({"client_id": "local-admin", "enabled_skills": []})
        _save_db(db)
        return []
    
    return []

def log_tool_call(
    client_id: str,
    skill: str,
    tool: str,
    success: bool,
    error: str | None = None,
) -> None:
    """Insert one row into audit_logs."""
    db = _load_db()
    db.setdefault("audit_logs", []).append({
        "client_id": client_id,
        "skill": skill,
        "tool": tool,
        "success": success,
        "error": error,
        "called_at": datetime.now(timezone.utc).isoformat()
    })
    _save_db(db)

def fetch_failed_logs(since: datetime) -> list[dict]:
    """Return all failed audit_log rows since the given UTC timestamp."""
    db = _load_db()
    failed = []
    for log in db.get("audit_logs", []):
        if not log.get("success"):
            log_time = datetime.fromisoformat(log["called_at"])
            if log_time >= since:
                failed.append(log)
    return sorted(failed, key=lambda x: x["called_at"], reverse=True)

def log_feedback(
    client_id: str,
    skill: str,
    rating: int,
    tool: str | None = None,
    comment: str | None = None,
    tool_args: dict | None = None,
    result_preview: str | None = None,
) -> None:
    """Insert one row into feedback_logs."""
    db = _load_db()
    db.setdefault("feedback_logs", []).append({
        "client_id": client_id,
        "skill": skill,
        "tool": tool,
        "rating": rating,
        "comment": comment,
        "tool_args": tool_args,
        "result_preview": result_preview,
        "submitted_at": datetime.now(timezone.utc).isoformat()
    })
    _save_db(db)

def fetch_low_rated_feedback(since: datetime, max_rating: int = 2) -> list[dict]:
    """Return feedback_logs rows with rating <= max_rating since the given UTC timestamp."""
    db = _load_db()
    low_rated = []
    for log in db.get("feedback_logs", []):
        if log.get("rating", 5) <= max_rating:
            log_time = datetime.fromisoformat(log["submitted_at"])
            if log_time >= since:
                low_rated.append(log)
    return sorted(low_rated, key=lambda x: x["submitted_at"], reverse=True)

def get_client_skill_config(client_id: str, skill: str) -> dict:
    """Return the config dict for a client+skill pair. Returns {} if not found."""
    db = _load_db()
    for conf in db.get("client_skill_configs", []):
        if conf.get("client_id") == client_id and conf.get("skill") == skill:
            return conf.get("config", {})
    return {}

def set_client_skill_config(client_id: str, skill: str, config: dict) -> None:
    """Upsert a per-client skill config row."""
    db = _load_db()
    configs = db.setdefault("client_skill_configs", [])
    found = False
    for conf in configs:
        if conf.get("client_id") == client_id and conf.get("skill") == skill:
            conf["config"] = config
            conf["updated_at"] = datetime.now(timezone.utc).isoformat()
            found = True
            break
    
    if not found:
        configs.append({
            "client_id": client_id,
            "skill": skill,
            "config": config,
            "updated_at": datetime.now(timezone.utc).isoformat()
        })
    _save_db(db)
