"""Skill: service_bridge — query user-connected services from chat."""

import ipaddress
import logging
import re
import time
from collections import defaultdict
from typing import Any

from fastmcp import FastMCP

logger = logging.getLogger(__name__)

mcp = FastMCP("service-bridge")

# In-process rate limiting: client_id → list of call timestamps (last 60s)
_rate_limit_window: dict[str, list[float]] = defaultdict(list)
_RATE_LIMIT = 30  # calls per minute per client

# Headers that must never be returned to the LLM
_SENSITIVE_HEADERS = {"authorization", "apikey", "api-key", "x-api-key", "x-service-key"}

# Private IP ranges for SSRF defense
_PRIVATE_NETS = [
    ipaddress.ip_network("127.0.0.0/8"),
    ipaddress.ip_network("10.0.0.0/8"),
    ipaddress.ip_network("172.16.0.0/12"),
    ipaddress.ip_network("192.168.0.0/16"),
    ipaddress.ip_network("169.254.0.0/16"),
    ipaddress.ip_network("::1/128"),
    ipaddress.ip_network("fc00::/7"),
]

_PLACEHOLDER_VALUES = frozenset({"n/a", "none", "null", "placeholder", "todo", ""})


def _valid_key(val: str | None) -> str | None:
    """Return val if it looks like a real API key (any format), else None."""
    if not val or len(val) < 10 or val.lower().strip() in _PLACEHOLDER_VALUES:
        return None
    return val


def _build_supabase_auth(c: dict) -> dict:
    pub = c.get("publishable_key") or c.get("anon_key", "")
    sec = _valid_key(c.get("secret_key")) or _valid_key(c.get("service_role_key"))
    bearer = sec or pub

    if bearer and bearer.startswith("sb_"):
        # New sb_ format: role is determined solely by the apikey header value.
        # Use the highest-privilege key (service_role > anon) as apikey.
        # Do NOT send Authorization: Bearer — PostgREST rejects non-JWT tokens (PGRST301).
        return {"apikey": bearer}
    else:
        # Legacy JWT format: anon key as apikey, service_role JWT in Authorization.
        headers: dict = {"apikey": pub}
        if bearer:
            headers["Authorization"] = f"Bearer {bearer}"
        return headers


# Per-service adapter configuration
_SERVICE_ADAPTERS: dict[str, dict] = {
    "supabase": {
        "base_url_key": "url",
        "base_path": "/rest/v1",
        "auth": _build_supabase_auth,
        "examples": [
            {"endpoint": "properties", "method": "GET", "description": "List all rows in the properties table"},
            {"endpoint": "properties?status=eq.occupied", "method": "GET", "description": "Filter rows"},
        ],
    },
    "github": {
        "base_url": "https://api.github.com",
        "base_path": "",
        "auth": lambda c: {"Authorization": f"Bearer {c.get('token', '')}"},
        "examples": [
            {"endpoint": "user", "method": "GET", "description": "Get authenticated user"},
            {"endpoint": "repos/owner/repo/issues", "method": "GET", "description": "List issues"},
        ],
    },
    "notion": {
        "base_url": "https://api.notion.com/v1",
        "base_path": "",
        "auth": lambda c: {
            "Authorization": f"Bearer {c.get('token', '')}",
            "Notion-Version": "2022-06-28",
        },
        "examples": [
            {"endpoint": "users/me", "method": "GET", "description": "Get current user"},
            {"endpoint": "databases", "method": "POST", "description": "List databases"},
        ],
    },
    "openai": {
        "base_url": "https://api.openai.com/v1",
        "base_path": "",
        "auth": lambda c: {"Authorization": f"Bearer {c.get('api_key', '')}"},
        "examples": [
            {"endpoint": "models", "method": "GET", "description": "List available models"},
        ],
    },
}

_GUIDANCE = {
    "display_name": "Service Bridge",
    "description": (
        "Query your connected services (Supabase, GitHub, Notion, OpenAI, custom APIs) "
        "directly from chat using stored credentials."
    ),
    "tools": {
        "list_connected_services": "Show which services you have connected in the dashboard.",
        "describe_service_schema": "Get the base URL, auth format, and example calls for a service.",
        "query_connected_service": "Execute a real HTTP request against a connected service.",
    },
    "usage_example": (
        "1. Call list_connected_services() to see what's available.\n"
        "2. Call describe_service_schema('supabase') to understand the API shape.\n"
        "3. Call query_connected_service(service='supabase', endpoint='properties', method='GET') "
        "to fetch real data.\n"
        "Combine with skill guidance: first call get_<skill>_skill() to get the workflow, "
        "then use service_bridge tools to execute the steps."
    ),
}


def _get_client_id() -> str:
    try:
        from fastmcp.server.dependencies import get_http_request
        client_id = get_http_request().headers.get("x-client-id")
        if client_id:
            return client_id
    except Exception:
        pass
    from core.config import get_client_id
    return get_client_id()


def _check_rate_limit(client_id: str) -> bool:
    """Return True if the call is allowed, False if rate-limited."""
    now = time.time()
    window = _rate_limit_window[client_id]
    # Drop timestamps older than 60 seconds
    _rate_limit_window[client_id] = [t for t in window if now - t < 60]
    if len(_rate_limit_window[client_id]) >= _RATE_LIMIT:
        return False
    _rate_limit_window[client_id].append(now)
    return True


def _is_private_host(host: str) -> bool:
    """Return True if the host resolves to a private/loopback address."""
    try:
        addr = ipaddress.ip_address(host)
        return any(addr in net for net in _PRIVATE_NETS)
    except ValueError:
        pass
    private_patterns = ("localhost", "127.", "10.", "192.168.", "169.254.", "::1")
    return any(host.startswith(p) or host == p.rstrip(".") for p in private_patterns)


def _sanitize_response_headers(headers: dict) -> dict:
    return {k: v for k, v in headers.items() if k.lower() not in _SENSITIVE_HEADERS}


def _resolve_adapter(service: str, creds: dict) -> tuple[str, dict] | None:
    """Return (base_url, auth_headers) or None if service is unknown."""
    adapter = _SERVICE_ADAPTERS.get(service)
    if adapter:
        if "base_url_key" in adapter:
            base = creds.get(adapter["base_url_key"], "").rstrip("/") + adapter.get("base_path", "")
        else:
            base = adapter["base_url"].rstrip("/") + adapter.get("base_path", "")
        return base, adapter["auth"](creds)

    # Custom service: expects creds["url"] and creds["token"]
    url = creds.get("url", "").rstrip("/")
    token = creds.get("token", "")
    if url:
        return url, {"Authorization": f"Bearer {token}"}
    return None


@mcp.tool()
def get_service_bridge_guidance() -> dict:
    """Get usage instructions for the service_bridge skill."""
    return _GUIDANCE


@mcp.tool()
def list_connected_services() -> dict:
    """List all services the user has connected in their dashboard."""
    client_id = _get_client_id()
    try:
        from core.credentials import list_configured_services
        services = list_configured_services(client_id)
    except Exception as exc:
        logger.debug("list_configured_services failed: %s", exc)
        services = []
    return {"services": services, "count": len(services)}


@mcp.tool()
def describe_service_schema(service: str) -> dict:
    """Get adapter hints for a connected service: base URL pattern, auth header format, example calls.

    Args:
        service: Service name, e.g. "supabase", "github", "notion", "openai", or a custom name.
    """
    adapter = _SERVICE_ADAPTERS.get(service)
    if not adapter:
        return {
            "service": service,
            "note": "Custom service — uses credentials.url as base URL and credentials.token as Bearer token.",
            "auth_format": "Authorization: Bearer <token>",
            "examples": [{"endpoint": "your/endpoint", "method": "GET"}],
        }
    base_desc = (
        f"credentials.{adapter['base_url_key']} + {repr(adapter['base_path'])}"
        if "base_url_key" in adapter
        else adapter["base_url"]
    )
    return {
        "service": service,
        "base_url": base_desc,
        "auth_format": "See service documentation — credentials resolved from dashboard connections.",
        "examples": adapter.get("examples", []),
    }


@mcp.tool()
def query_connected_service(
    service: str,
    endpoint: str,
    method: str = "GET",
    body: str | dict | None = None,
    query_params: str | dict | None = None,
) -> dict:
    """Execute an HTTP request against a user-connected service using stored credentials.

    Args:
        service: Service name matching a connection in the dashboard (e.g. "supabase", "github").
        endpoint: Path relative to the service base URL (e.g. "properties", "repos/owner/repo/issues").
        method: HTTP method — GET, POST, PATCH, PUT, or DELETE.
        body: JSON request body for POST/PATCH/PUT requests.
        query_params: URL query parameters as a dict (e.g. {"id": "eq.123"}).
            REQUIRED for PATCH/PUT: without a filter the request will be rejected to prevent
            silent no-ops. Use standard filter syntax: "eq.value" (equals), "gt.value"
            (greater than), "like.pattern" (LIKE). Alternatively, embed the filter directly
            in the endpoint string (e.g. "tablename?id=eq.123").

    Returns:
        Dict with keys: status (int), ok (bool), data (response body), headers (safe subset).
        On error: {"error": str, "available": [service names]}.
    """
    try:
        import httpx
    except ImportError:
        return {"error": "httpx is not installed — add it to requirements"}

    if body == "null" or body == "":
        body = None
    elif isinstance(body, str):
        try:
            body = __import__("json").loads(body)
        except Exception:
            pass

    if query_params == "null" or query_params == "":
        query_params = None
    elif isinstance(query_params, str):
        try:
            query_params = __import__("json").loads(query_params)
        except Exception:
            pass

    client_id = _get_client_id()

    if not _check_rate_limit(client_id):
        return {"error": "rate_limited", "retry_after_seconds": 60}

    method = method.upper()
    if method not in {"GET", "POST", "PATCH", "PUT", "DELETE"}:
        return {"error": f"Invalid method: {method}. Must be GET, POST, PATCH, PUT, or DELETE."}

    _filter_warning: str | None = None
    if method in {"PATCH", "PUT"}:
        has_inline_filter = "?" in endpoint
        has_param_filter = bool(query_params)
        if not has_inline_filter and not has_param_filter:
            _filter_warning = (
                "No row filter detected — this may update all rows. "
                'Add query_params (e.g. {"id": "eq.123"}) or include a filter '
                'in the endpoint (e.g. "tablename?id=eq.123") to target specific rows.'
            )

    # Resolve credentials using the per-request client_id from HTTP header
    from core.credentials import get_service_credential, list_configured_services
    creds = get_service_credential(service, client_id=client_id)
    if creds is None:
        available = list_configured_services(client_id)
        return {"error": f"Service '{service}' is not connected.", "available": available}

    adapter_result = _resolve_adapter(service, creds)
    if not adapter_result:
        return {"error": f"Cannot resolve base URL for service '{service}'. Check credentials.url is set."}

    base_url, auth_headers = adapter_result

    # Build full URL
    endpoint = endpoint.lstrip("/")
    url = f"{base_url}/{endpoint}" if endpoint else base_url

    # SSRF defense — check the host portion
    host_match = re.match(r"https?://([^/:?#]+)", url)
    if host_match and _is_private_host(host_match.group(1)):
        return {"error": "Blocked: endpoint resolves to a private/loopback address."}

    headers = {**auth_headers, "Content-Type": "application/json"}
    # Ask Supabase/PostgREST to return the affected rows so callers can confirm
    # how many rows were actually updated (204 + content-range:*/* = 0 rows matched).
    if method in {"POST", "PATCH", "PUT"}:
        headers["Prefer"] = "return=representation"

    success = False
    error_msg = None
    try:
        with httpx.Client(timeout=30) as client:
            resp = client.request(
                method=method,
                url=url,
                headers=headers,
                params=query_params,
                json=body,
            )
        success = resp.is_success

        # Parse response body
        try:
            data: Any = resp.json()
        except Exception:
            data = resp.text

        # Cap large responses to prevent overwhelming the caller
        truncated = False
        if isinstance(data, str) and len(data) > 50_000:
            data = data[:50_000]
            truncated = True

        result = {
            "status": resp.status_code,
            "ok": resp.is_success,
            "data": data,
            "headers": _sanitize_response_headers(dict(resp.headers)),
        }
        if truncated:
            result["_truncated"] = True
        if _filter_warning:
            result["filter_warning"] = _filter_warning
        if method in {"PATCH", "PUT", "DELETE"} and isinstance(data, list) and len(data) == 0:
            result["rows_affected"] = 0
            result["warning"] = "0 rows matched your filter — no rows were updated. Verify the filter values."
        return result

    except httpx.TimeoutException:
        error_msg = "Request timed out after 30 seconds."
        return {"error": error_msg, "ok": False}
    except httpx.RequestError as exc:
        error_msg = str(exc)
        return {"error": f"Request failed: {error_msg}", "ok": False}
    except Exception as exc:
        error_msg = str(exc)
        return {"error": f"Unexpected error: {error_msg}", "ok": False}
    finally:
        try:
            from core.db import log_tool_call
            log_tool_call(client_id, "service_bridge", "query_connected_service", success, error_msg)
        except Exception:
            pass
