"""Skill: stripe_stripe_skills."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("stripe-stripe-skills")


_SKILLS: dict[str, dict] = {
    'model-context-protocol-mcp': {
        "description": 'Stripe hosts a remote MCP server at `https://mcp.',
        "guidance": 'Stripe hosts a remote MCP server at `https://mcp.stripe.com`. This allows secure MCP client access via OAuth. View the docs [here](https://docs.stripe.com/mcp#remote).\n\nThe Stripe Agent Toolkit also exposes tools in the [Model Context Protocol (MCP)](https://modelcontextprotocol.com/) format. Or, to run a local Stripe MCP server using npx, use the following command:\n\n```sh\nnpx -y @stripe/mcp --api-key=YOUR_STRIPE_SECRET_KEY\n```\n\nTool permissions are controlled by your Restricted API Key (RAK). Create a RAK with the desired permissions at https://dashboard.stripe.com/apikeys\n\nSee [MCP](/tools/modelcontextprotocol) for more details.',
    },
    'agent-toolkit': {
        "description": "Stripe's Agent Toolkit enables popular agent frameworks including OpenAI's Agent SDK, LangChain, CrewAI, and Vercel's AI SDK to integrate with Stripe APIs through function calling.",
        "guidance": 'Stripe\'s Agent Toolkit enables popular agent frameworks including OpenAI\'s Agent SDK, LangChain, CrewAI, and Vercel\'s AI SDK to integrate with Stripe APIs through function calling. The library is not exhaustive of the entire Stripe API. It includes support for Python and TypeScript, and is built directly on top of the Stripe [Python][python-sdk] and [Node][node-sdk] SDKs.\n\nIncluded below are basic instructions, but refer to [Python](/tools/python) and [TypeScript](/tools/typescript) packages for more information.\n\n### Python\n\n#### Installation\n\nYou don\'t need this source code unless you want to modify the package. If you just\nwant to use the package run:\n\n```sh\npip install stripe-agent-toolkit\n```\n\n##### Requirements\n\n- Python 3.11+\n\n#### Usage\n\nThe library needs to be configured with your account\'s secret key which is\navailable in your [Stripe Dashboard][api-keys]. We strongly recommend using a [Restricted API Key][restricted-keys] (`rk_*`) for better security and granular permissions. Tool availability is determined by the permissions you configure on the restricted key.\n\n```python\nfrom stripe_agent_toolkit.openai.toolkit import create_stripe_agent_toolkit\n\nasync def main():\n    toolkit = await create_stripe_agent_toolkit(secret_key="rk_test_...")\n    tools = toolkit.get_tools()\n    # ... use tools ...\n    await toolkit.close()  # Clean up when done\n```\n\nThe toolkit works with OpenAI\'s Agent SDK, LangChain, and CrewAI and can be passed as a list of tools. For example:\n\n```python\nfrom agents import Agent\n\nasync def main():\n    toolkit = await create_stripe_agent_toolkit(secret_key="rk_test_...")\n\n    stripe_agent = Agent(\n        name="Stripe Agent",\n        instructions="You are an expert at integrating with Stripe",\n        tools=toolkit.get_tools()\n    )\n    # ... use agent ...\n    await toolkit.close()\n```\n\nExamples for OpenAI\'s Agent SDK,LangChain, and CrewAI are included in [/examples](/tools/python/examples).\n\n##### Context\n\nIn some cases you will want to provide values that serve as defaults when making requests. Currently, the `account` context value enables you to make API calls for your [connected accounts](https://docs.stripe.com/connect/authentication).\n\n```python\ntoolkit = await create_stripe_agent_toolkit(\n    secret_key="rk_test_...",\n    configuration={\n        "context": {\n            "account": "acct_123"\n        }\n    }\n)\n```\n\n### TypeScript\n\n#### Installation\n\nYou don\'t need this source code unless you want to modify the package. If you just\nwant to use the package run:\n\n```sh\nnpm install @stripe/agent-toolkit\n```\n\n##### Requirements\n\n- Node 18+\n\n##### Migrating from v0.8.x\n\nIf you\'re upgrading from v0.8.x, see the [Migration Guide](/tools/typescript/MIGRATION.md) for breaking changes.\n\n#### Usage\n\nThe library needs to be configured with your account\'s secret key which is available in your [Stripe Dashboard][api-keys]. We strongly recommend using a [Restricted API Key][restricted-keys] (`rk_*`) for better security and granular permissions. Tool availability is determined by the permissions you configure on the restricted key.\n\n```typescript\nimport { createStripeAgentToolkit } from "@stripe/agent-toolkit/langchain";\n\nconst toolkit = await createStripeAgentToolkit({\n  secretKey: process.env.STRIPE_SECRET_KEY!,\n  configuration: {},\n});\n\nconst tools = toolkit.getTools();\n// ... use tools ...\n\nawait toolkit.close(); // Clean up when done\n```\n\n##### Tools\n\nThe toolkit works with LangChain and Vercel\'s AI SDK and can be passed as a list of tools. For example:\n\n```typescript\nimport { AgentExecutor, createStructuredChatAgent } from "langchain/agents";\nimport { createStripeAgentToolkit } from "@stripe/agent-toolkit/langchain";\n\nconst toolkit = await createStripeAgentToolkit({\n  secretKey: process.env.STRIPE_SECRET_KEY!,\n  configuration: {},\n});\n\nconst tools = toolkit.getTools();\n\nconst agent = await createStructuredChatAgent({\n  llm,\n  tools,\n  prompt,\n});\n\nconst agentExecutor = new AgentExecutor({\n  agent,\n  tools,\n});\n```\n\n##### Context\n\nIn some cases you will want to provide values that serve as defaults when making requests. Currently, the `account` context value enables you to make API calls for your [connected accounts](https://docs.stripe.com/connect/authentication).\n\n```typescript\nconst toolkit = await createStripeAgentToolkit({\n  secretKey: process.env.STRIPE_SECRET_KEY!,\n  configuration: {\n    context: {\n      account: "acct_123",\n    },\n  },\n});\n```',
    },
    'supported-api-methods': {
        "description": 'See the [Stripe MCP](https://docs.',
        "guidance": 'See the [Stripe MCP](https://docs.stripe.com/mcp) docs for a list of supported methods.\n\n[python-sdk]: https://github.com/stripe/stripe-python\n[node-sdk]: https://github.com/stripe/stripe-node\n[api-keys]: https://dashboard.stripe.com/account/apikeys\n[restricted-keys]: https://docs.stripe.com/keys#create-restricted-api-keys',
    },
    'license': {
        "description": '[MIT](LICENSE).',
        "guidance": '[MIT](LICENSE)',
    },
}


@mcp.tool()
def list_stripe_stripe_skills_skills() -> dict:
    """List all available stripe_stripe_skills skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_stripe_stripe_skills_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific stripe_stripe_skills skill."""
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
    hint = get_presentation_hint('stripe_stripe_skills', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@stripe_stripe_skills",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'stripe_stripe_skills',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
