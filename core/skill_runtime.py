"""Runtime helpers used by generated skill modules."""

import json
import logging
import re
import time
from pathlib import Path

logger = logging.getLogger(__name__)

# In-memory cache: raw_url → (content, fetched_at_timestamp)
_SKILL_CONTENT_CACHE: dict[str, tuple[str, float]] = {}
_CACHE_TTL = 3600  # seconds (1 hour)


def read_skill_file(skill_main_py_path: str, filename: str) -> str | None:
    """Return the content of a skill file by slug name.

    Resolution order:
    1. Local disk at skill_files/<filename> — allows local overrides.
    2. raw_url from skill_files/_index.json — fetched from GitHub with 1h TTL cache.

    Args:
        skill_main_py_path: Value of __file__ from the calling skill's main.py.
        filename: Slug filename, e.g. "maintenance-triage.md".
    """
    if not filename:
        return None

    skill_files_dir = Path(skill_main_py_path).parent / "skill_files"

    # 1. Local disk (for overrides or legacy copied files)
    local = skill_files_dir / filename
    if local.exists():
        try:
            return local.read_text(errors="replace")
        except Exception:
            pass

    # 2. URL-based fetch via _index.json
    index_path = skill_files_dir / "_index.json"
    if not index_path.exists():
        return None

    try:
        index = json.loads(index_path.read_text())
    except Exception:
        return None

    # Find the slug entry (filename without .md extension is the slug)
    slug = filename[:-3] if filename.endswith(".md") else filename
    entry = index.get(slug)
    if not entry:
        return None

    raw_url = entry.get("raw_url")
    if not raw_url:
        return None

    return _fetch_with_cache(raw_url)


def _fetch_with_cache(url: str) -> str | None:
    """Fetch a URL with an in-memory TTL cache. Returns None on failure."""
    now = time.time()
    cached = _SKILL_CONTENT_CACHE.get(url)
    if cached and (now - cached[1]) < _CACHE_TTL:
        return cached[0]

    content = None
    try:
        import httpx
        resp = httpx.get(url, timeout=10, follow_redirects=True)
        resp.raise_for_status()
        content = resp.text
    except Exception as exc:
        logger.debug("skill file fetch failed for %s: %s", url, exc)
        return None

    _SKILL_CONTENT_CACHE[url] = (content, now)
    return content


def fetch_referenced_files(skill_main_py_path: str, guidance: str, skill_slug: str) -> dict[str, str]:
    """Parse guidance markdown for backtick-wrapped `references/*.md` links and fetch each.

    References live inside the skill's own directory on GitHub, e.g.:
    .../master/client-care-route/references/data-concepts.md

    Derives the skill directory base URL from _index.json using skill_slug, then
    fetches each referenced file through the shared 1h-TTL cache.

    Args:
        skill_main_py_path: Value of __file__ from the calling skill's main.py.
        guidance: Full markdown content of the skill file to scan for references.
        skill_slug: The slug key in _index.json (e.g. "client-care-route").

    Returns:
        Dict mapping filename → content for each successfully fetched reference.
    """
    ref_paths = re.findall(r"`(references/[^`]+\.md)`", guidance)
    if not ref_paths:
        return {}

    skill_files_dir = Path(skill_main_py_path).parent / "skill_files"
    index_path = skill_files_dir / "_index.json"
    if not index_path.exists():
        return {}

    try:
        index = json.loads(index_path.read_text())
    except Exception:
        return {}

    # Use the specific skill's raw_url to get the correct per-skill directory base.
    # e.g. ".../master/client-care-route/SKILL.md" → ".../master/client-care-route/"
    raw_url = index.get(skill_slug, {}).get("raw_url", "")
    if not raw_url:
        return {}

    base_url = raw_url.rsplit("/", 1)[0] + "/"

    result = {}
    for ref_path in dict.fromkeys(ref_paths):  # preserve order, deduplicate
        content = _fetch_with_cache(base_url + ref_path)
        if content:
            filename = ref_path.split("/")[-1]
            result[filename] = content

    return result


def list_client_connections() -> list[str]:
    """Return connected service names for the current client. Never raises."""
    try:
        from fastmcp.server.dependencies import get_http_request
        client_id = get_http_request().headers.get("x-client-id")
    except Exception:
        client_id = None
    if not client_id:
        from core.config import get_client_id
        client_id = get_client_id()
    try:
        from core.credentials import list_configured_services
        return list_configured_services(client_id)
    except Exception:
        return []
