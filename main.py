"""Root MCP server entry point.

Mounts every skill found in skills_library/ at startup. The Cloudflare Worker
filters exposed tools by each client's enabled_skills list, so enabling or
disabling a skill in the dashboard takes effect immediately without a redeploy.

Usage:
    # Local dev (MCP Inspector):
    fastmcp dev main.py

    # Production (Streamable HTTP):
    python main.py
"""

import importlib.util
import os
from pathlib import Path

from dotenv import load_dotenv
from fastmcp import FastMCP

from core.config import get_client_id

load_dotenv()

client_id = get_client_id()
mcp = FastMCP(f"Agency-{client_id}")

_skills_dir = Path(__file__).parent / "skills_library"

for skill_dir in sorted(_skills_dir.iterdir()):
    if not skill_dir.is_dir() or skill_dir.name.startswith("."):
        continue
    skill_path = skill_dir / "main.py"
    if not skill_path.exists():
        continue
    try:
        spec = importlib.util.spec_from_file_location(f"skill_{skill_dir.name}", skill_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        if not hasattr(module, "mcp"):
            print(f"[warn] {skill_dir.name}: no `mcp` export — skipped")
            continue
        mcp.mount(module.mcp, namespace=skill_dir.name)
    except Exception as exc:
        print(f"[warn] {skill_dir.name}: failed to load — {exc}")

if __name__ == "__main__":
    port = int(os.getenv("PORT", "0"))
    if port:
        # HTTP mode: PORT is set by Railway (and other hosting platforms)
        mcp.run(transport="streamable-http", host="0.0.0.0", port=port)
    else:
        # Stdio mode: no PORT set — spawned by Inspector, Claude Desktop, etc.
        mcp.run(transport="stdio")
