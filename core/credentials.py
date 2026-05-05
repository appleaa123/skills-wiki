"""Service credential resolver for MCP skill servers."""

import json
import logging
import os

logger = logging.getLogger(__name__)


def get_service_credential(service: str, client_id: str | None = None) -> dict | None:
    """Return decrypted credentials for a service for the given client.

    Args:
        service: Service identifier, e.g. "supabase", "github", "notion".
        client_id: Client identifier. Defaults to CLIENT_ID env var.

    Returns:
        Dict of credential fields, or None if not configured.
    """
    if client_id is None:
        client_id = os.getenv("CLIENT_ID", "dev-client")

    if not os.getenv("SUPABASE_URL"):
        return _load_from_local(client_id, service)

    try:
        from core.db import _get_client
        row = (
            _get_client()
            .table("client_service_credentials")
            .select("credentials")
            .eq("client_id", client_id)
            .eq("service", service)
            .single()
            .execute()
        )
        if not row.data:
            return None
        return _decrypt(row.data["credentials"])
    except Exception as exc:
        logger.debug("credential fetch skipped for %s/%s: %s", client_id, service, exc)
        return None


def _decrypt(ciphertext: str) -> dict:
    """AES-256-GCM decrypt — mirrors dashboard/lib/encryption.ts."""
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM

    key_hex = os.getenv("CREDENTIALS_ENCRYPTION_KEY")
    if not key_hex:
        raise RuntimeError("CREDENTIALS_ENCRYPTION_KEY is not set")

    key = bytes.fromhex(key_hex)
    iv_hex, tag_hex, enc_hex = ciphertext.split(".")
    iv = bytes.fromhex(iv_hex)
    tag = bytes.fromhex(tag_hex)
    enc = bytes.fromhex(enc_hex)

    aesgcm = AESGCM(key)
    plaintext = aesgcm.decrypt(iv, enc + tag, None)
    return json.loads(plaintext)


def _load_from_local(client_id: str, service: str) -> dict | None:
    """Dev fallback: read credentials from local db.json."""
    from core.db import _load_db
    
    db = _load_db()
    for cred in db.get("client_service_credentials", []):
        if cred.get("client_id") == client_id and cred.get("service") == service:
            return cred.get("credentials")
    return None


def list_configured_services(client_id: str | None = None) -> list[str]:
    """Return service names the client has saved credentials for.

    Args:
        client_id: Client identifier. Defaults to CLIENT_ID env var.

    Returns:
        Sorted list of service names (e.g. ["github", "supabase"]).
    """
    if client_id is None:
        client_id = os.getenv("CLIENT_ID", "local-admin")

    if not os.getenv("SUPABASE_URL"):
        return _list_local_services(client_id)

    try:
        from core.db import _get_client
        rows = (
            _get_client()
            .table("client_service_credentials")
            .select("service")
            .eq("client_id", client_id)
            .execute()
        )
        return sorted({r["service"] for r in (rows.data or [])})
    except Exception as exc:
        logger.debug("list_configured_services failed for %s: %s", client_id, exc)
        return []


def _list_local_services(client_id: str) -> list[str]:
    """Dev fallback: list service names from local db.json."""
    from core.db import _load_db
    
    db = _load_db()
    services = []
    for cred in db.get("client_service_credentials", []):
        if cred.get("client_id") == client_id:
            services.append(cred.get("service"))
    return sorted(services)
