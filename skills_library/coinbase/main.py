"""Skill: coinbase."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("coinbase")


_SKILLS: dict[str, dict] = {
    'available-skills': {
        "description": '| Skill                                                        | Description                                                    |\n| ------------------------------------------------------------ | -----',
        "guidance": '| Skill                                                        | Description                                                    |\n| ------------------------------------------------------------ | -------------------------------------------------------------- |\n| [authenticate-wallet](./skills/authenticate-wallet/SKILL.md) | Sign in to the wallet via email OTP                            |\n| [fund](./skills/fund/SKILL.md)                               | Add money to the wallet via Coinbase Onramp                    |\n| [send-usdc](./skills/send-usdc/SKILL.md)                     | Send USDC to Ethereum addresses or ENS names                   |\n| [trade](./skills/trade/SKILL.md)                             | Swap/trade tokens on Base (USDC, ETH, WETH)                    |\n| [search-for-service](./skills/search-for-service/SKILL.md)   | Search the x402 bazaar for paid API services                   |\n| [pay-for-service](./skills/pay-for-service/SKILL.md)         | Make paid API requests via x402                                |\n| [monetize-service](./skills/monetize-service/SKILL.md)       | Build and deploy a paid API that other agents can use via x402 |\n| [query-onchain-data](./skills/query-onchain-data/SKILL.md)   | Query onchain data on Base using the CDP SQL API via x402      |',
    },
    'installation': {
        "description": "Install with [Vercel's Skills CLI](https:/skills.",
        "guidance": "Install with [Vercel's Skills CLI](https:/skills.sh):\n\n```bash\nnpx skills add coinbase/agentic-wallet-skills\n```",
    },
    'usage': {
        "description": 'Skills are automatically available once installed.',
        "guidance": 'Skills are automatically available once installed. The agent will use them when relevant tasks are detected.\n\n**Examples:**\n\n```text\nSign-in to my wallet with me@email.com\n```\n\n```text\nSend 10 USDC to barmstrong.eth\n```',
    },
    'contributing': {
        "description": 'To add a new skill:\n\n1.',
        "guidance": "To add a new skill:\n\n1. Create a folder in `./skills/` with a lowercase, hyphenated name\n2. Add a `SKILL.md` file with YAML frontmatter and instructions\n\nSee the [Agent Skills specification](https://agentskills.io/specification) for the complete format.\n\n### Updating the `awal` version\n\nAll skills pin a specific version of the `awal` CLI. When a new version is published to npm, run:\n\n```bash\n# Make sure you're using Node v22+\nnode ./scripts/bump-awal.js\n```\n\nThis fetches the latest version from the npm registry and updates all skill files automatically.",
    },
    'license': {
        "description": 'MIT.',
        "guidance": 'MIT',
    },
}


@mcp.tool()
def list_coinbase_skills() -> dict:
    """List all available coinbase skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_coinbase_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific coinbase skill."""
    if not skill_name or str(skill_name).lower() in ["null", "none"]:
        skill_name = "start-here" if "start-here" in _SKILLS else next(iter(_SKILLS))
    skill_data = _SKILLS.get(skill_name, {"error": f"Unknown skill: {skill_name}"})
    try:
        from fastmcp.server.dependencies import get_http_request
        client_id = get_http_request().headers.get("x-client-id")
    except Exception:
        client_id = None
    if not client_id:
        from core.config import get_client_id
        client_id = get_client_id()
    hint = get_presentation_hint('coinbase', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@coinbase",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'coinbase',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
