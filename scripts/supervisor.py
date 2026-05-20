#!/usr/bin/env python3
"""Evolution Loop supervisor.

Two separate improvement paths:

1. GLOBAL — Crash/error fixing (affects all clients):
   Reads audit_logs where success=False → asks Gemini to rewrite the skill's
   main.py → commits + pushes → Railway auto-redeploys all clients.

2. PER-CLIENT — Feedback-based config improvement (affects only that client):
   Reads feedback_logs where rating <= 2 → asks Gemini to generate an updated
   client_skill_configs row for that specific client → writes to Supabase.
   No git push. No redeploy. Instant. Other clients unaffected.
"""

import json
import os
import subprocess
import sys
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

sys.path.insert(0, str(Path(__file__).parent.parent))

from core.db import (  # noqa: E402
    fetch_failed_logs,
    fetch_low_rated_feedback,
    get_client_skill_config,
    set_client_skill_config,
)

_SKILLS_DIR = Path(__file__).parent.parent / "skills_library"
_REPO_ROOT = Path(__file__).parent.parent
_PATCHES_DIR = _REPO_ROOT / "patches"

GEMINI_MODEL = "gemini-2.5-flash"
MAX_ERRORS_PER_SKILL = 5
MAX_FEEDBACK_PER_SKILL = 5

_CONFIG_SCHEMA = """{
  "tone": "formal | casual | technical",
  "format": "prose | bullets | table",
  "language": "<language name, e.g. Spanish>",
  "response_length": "brief | standard | detailed",
  "custom_instructions": "<free text — specific preferences from the user's feedback>"
}"""


# ── Alerting ──────────────────────────────────────────────────────────────────

def _send_alert(message: str) -> None:
    """POST a plain-text alert to ALERT_WEBHOOK_URL (Discord/Slack compatible). Never raises."""
    webhook_url = os.environ.get("ALERT_WEBHOOK_URL")
    if not webhook_url:
        return
    try:
        payload = json.dumps({"content": message}).encode()
        req = urllib.request.Request(
            webhook_url, data=payload,
            headers={"Content-Type": "application/json"}, method="POST",
        )
        urllib.request.urlopen(req, timeout=5)
    except Exception as exc:
        print(f"[alert] Failed to send alert: {exc}")


# ── Helpers ───────────────────────────────────────────────────────────────────

def _group_by_skill(rows: list[dict]) -> dict[str, list[dict]]:
    groups: dict[str, list[dict]] = {}
    for row in rows:
        groups.setdefault(row["skill"], []).append(row)
    return groups


def _group_by_client_and_skill(rows: list[dict]) -> dict[tuple[str, str], list[dict]]:
    groups: dict[tuple[str, str], list[dict]] = {}
    for row in rows:
        key = (row["client_id"], row["skill"])
        groups.setdefault(key, []).append(row)
    return groups


def _configure_gemini() -> genai.GenerativeModel:
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    return genai.GenerativeModel(GEMINI_MODEL)


# ── Path 1: Global error fixing ───────────────────────────────────────────────

def _ask_gemini_for_fix(skill_name: str, source: str, errors: list[dict]) -> str:
    model = _configure_gemini()
    error_lines = "\n".join(
        f"- tool={r['tool']} error={r['error']} called_at={r['called_at']}"
        for r in errors[:MAX_ERRORS_PER_SKILL]
    )
    prompt = (
        f"You are a senior Python engineer fixing a FastMCP skill named '{skill_name}'.\n\n"
        f"SOURCE CODE:\n```python\n{source}\n```\n\n"
        f"ERRORS (most recent first):\n{error_lines}\n\n"
        "Rewrite the complete fixed main.py that exports a FastMCP instance named `mcp`.\n"
        "Return ONLY the Python source — no explanations, no markdown fences."
    )
    return model.generate_content(prompt).text.strip()


def _write_patch(skill_name: str, fixed_code: str) -> Path:
    """Write proposed fix to patches/ directory for human review. Never auto-pushes."""
    _PATCHES_DIR.mkdir(exist_ok=True)
    patch_path = _PATCHES_DIR / f"{skill_name}_fix.py"
    patch_path.write_text(fixed_code)
    return patch_path


def run_global_fixes(since: datetime) -> None:
    """Path 1: identify broken skills and write proposed patches for human review.

    Patches are written to patches/{skill}_fix.py — a human must review and
    apply them to skills_library/{skill}/main.py before they affect production.
    Auto-push to Railway has been disabled to prevent unreviewed LLM code from
    reaching production.
    """
    error_logs = fetch_failed_logs(since)
    if not error_logs:
        print("[global] No failed tool calls in the past 7 days.")
        return

    groups = _group_by_skill(error_logs)
    proposed: list[str] = []

    for skill_name, rows in groups.items():
        if skill_name == "feedback_skill":
            continue
        path = _SKILLS_DIR / skill_name / "main.py"
        if not path.exists():
            print(f"[global] Skipping {skill_name}: source not found")
            continue
        print(f"[global] Generating patch for {skill_name} ({len(rows)} error(s))...")
        fixed = _ask_gemini_for_fix(skill_name, path.read_text(), rows)
        patch_path = _write_patch(skill_name, fixed)
        proposed.append(skill_name)
        print(f"[global]   → patch written to {patch_path} (review before applying)")

    if proposed:
        summary = f"[supervisor] {len(proposed)} patch(es) ready for review: {', '.join(proposed)}. Check patches/ directory."
        print(f"[global] {summary}")
        _send_alert(summary)
    else:
        print("[global] No skills needed patching.")


# ── Path 2: Per-client config improvement ─────────────────────────────────────

def _ask_gemini_for_config(
    skill_name: str,
    current_config: dict,
    feedback_rows: list[dict],
) -> dict:
    model = _configure_gemini()
    feedback_lines = "\n".join(
        f"- rating={r['rating']}/5 tool={r.get('tool') or '(any)'} "
        f"comment={r.get('comment') or '(no comment)'}"
        for r in feedback_rows[:MAX_FEEDBACK_PER_SKILL]
    )
    current_str = str(current_config) if current_config else "none (default settings)"
    prompt = (
        f"A client uses an AI skill called '{skill_name}' and submitted low-rated feedback.\n\n"
        f"CURRENT CONFIG: {current_str}\n\n"
        f"FEEDBACK:\n{feedback_lines}\n\n"
        f"Generate an updated config JSON that addresses the feedback. "
        f"Use only these fields (all optional):\n{_CONFIG_SCHEMA}\n\n"
        "Merge with the current config — keep fields not mentioned in feedback. "
        "Return ONLY valid JSON — no explanation, no markdown fences."
    )
    import json
    raw = model.generate_content(prompt).text.strip()
    raw = raw.removeprefix("```json").removeprefix("```").removesuffix("```").strip()
    return json.loads(raw)


def run_per_client_configs(since: datetime) -> None:
    """Path 2: update per-client configs from low-rated feedback. Only affects the specific client."""
    feedback_logs = fetch_low_rated_feedback(since, max_rating=2)
    if not feedback_logs:
        print("[per-client] No low-rated feedback in the past 7 days.")
        return

    groups = _group_by_client_and_skill(feedback_logs)
    updated = 0

    for (client_id, skill_name), rows in groups.items():
        if skill_name == "feedback_skill":
            continue
        print(f"[per-client] Updating config for client={client_id} skill={skill_name} "
              f"({len(rows)} feedback item(s))...")
        current = get_client_skill_config(client_id, skill_name)
        try:
            new_config = _ask_gemini_for_config(skill_name, current, rows)
            set_client_skill_config(client_id, skill_name, new_config)
            print(f"[per-client]   → config updated: {new_config}")
            updated += 1
        except Exception as exc:
            msg = f"[per-client]   → failed for {client_id}/{skill_name}: {exc}"
            print(msg)
            _send_alert(f"[supervisor] Config update failed — client={client_id} skill={skill_name}: {exc}")

    print(f"[per-client] {updated} config(s) updated. No code changes. No redeployment needed.")


# ── Entry point ───────────────────────────────────────────────────────────────

def run() -> None:
    since = datetime.now(timezone.utc) - timedelta(days=7)
    run_global_fixes(since)
    print()
    run_per_client_configs(since)


if __name__ == "__main__":
    run()
