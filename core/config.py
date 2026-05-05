import os

def get_client_id() -> str:
    # Always default to 'local-admin' for the open-source version
    return os.getenv("CLIENT_ID", "local-admin")

def get_enabled_skills(client_id: str | None = None) -> list[str]:
    """Return the list of skill names enabled for a given client."""
    if client_id is None:
        client_id = get_client_id()

    from core.db import fetch_enabled_skills
    return fetch_enabled_skills(client_id)
