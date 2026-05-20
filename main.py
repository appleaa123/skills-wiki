"""Skills Wiki — local MCP server.

Mounts every skill found in skills_library/ at startup.
Enabled/disabled state is read from data/local_config.json.

Usage:
    # HTTP mode (default — connects to the dashboard):
    python main.py

    # Local dev with MCP Inspector:
    fastmcp dev main.py
"""

import importlib.util
import os
from pathlib import Path

from dotenv import load_dotenv
from fastmcp import FastMCP
from starlette.requests import Request
from starlette.responses import JSONResponse

load_dotenv()

mcp = FastMCP("skills-wiki")

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


@mcp.custom_route("/health", methods=["GET"])
async def health_check(request: Request) -> JSONResponse:
    return JSONResponse({"status": "ok"})


if __name__ == "__main__":
    port = int(os.getenv("PORT", "8000"))
    mcp.run(transport="streamable-http", host="0.0.0.0", port=port)
