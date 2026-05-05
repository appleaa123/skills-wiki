"""Skill: agent_scan."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("agent-scan")


_SKILLS: dict[str, dict] = {
    'highlights': {
        "description": '- Auto-discover MCP configurations, agent tools, skills\n- Scanning of Claude, Cursor, Windsurf, Gemini CLI, Amp, Amazon Q, and other agents.',
        "guidance": '- Auto-discover MCP configurations, agent tools, skills\n- Scanning of Claude, Cursor, Windsurf, Gemini CLI, Amp, Amazon Q, and other agents.\n- Detects [15+ distinct security risks](docs/issue-codes.md) across MCP servers and agent skills:\n  - MCP: [Prompt Injection](docs/issue-codes.md#E001), [Tool Poisoning](docs/issue-codes.md#E001), [Tool Shadowing](docs/issue-codes.md#E002), [Toxic Flows](docs/issue-codes.md#ToxicFlows)\n  - Skills: [Prompt Injection](docs/issue-codes.md#E004), [Malware Payloads](docs/issue-codes.md#E006), [Untrusted Content](docs/issue-codes.md#W011), [Credential Handling](docs/issue-codes.md#W007), [Hardcoded Secrets](docs/issue-codes.md#W008)',
    },
    'supported-agents-and-capabilities': {
        "description": 'Agent Scan auto-discovers agents and their capabilities (MCP servers or skills) when their install paths exist.',
        "guidance": 'Agent Scan auto-discovers agents and their capabilities (MCP servers or skills) when their install paths exist. The table reflects [well-known agent definitions](src/agent_scan/well_known_clients.py).\n\n- **✓**: at least one path is defined for that capability.\n- **✗**: the agent is listed for that OS but has no paths for that capability.\n- **—**: that agent is not included for that OS.\n- **Skills** columns apply when using `--skills`.\n\n| Agent | macOS MCP | macOS Skills | Linux MCP | Linux Skills | Windows MCP | Windows Skills |\n| --- | :---: | :---: | :---: | :---: | :---: | :---: |\n| Windsurf | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |\n| Cursor | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |\n| VS Code | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |\n| Claude Desktop | ✓ | ✗ | — | — | ✓ | ✗ |\n| Claude Code | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |\n| Gemini CLI | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |\n| OpenClaw | ✗ | ✓ | ✗ | ✓ | ✗ | ✓ |\n| Amp | ✗ | ✓ | ✗ | ✓ | ✗ | ✓ |\n| Kiro | ✓ | ✗ | ✓ | ✗ | ✓ | ✗ |\n| OpenCode | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |\n| Antigravity | ✓ | ✗ | ✓ | ✗ | ✓ | ✗ |\n| Codex | ✗ | ✓ | ✗ | ✓ | — | — |\n| Amazon Q | ✓ | ✗ | ✓ | ✗ | — | — |',
    },
    'quick-start': {
        "description": 'To get started:\n\n1.',
        "guidance": 'To get started:\n\n1. **Sign up at [Snyk](https://snyk.io)** and get an API token from [https://app.snyk.io/account](https://app.snyk.io/account) (API Token → KEY → click to show).\n2. **Set the token as an environment variable** before running any scan:\n   ```bash\n   export SNYK_TOKEN=your-api-token-here\n   ```\n3. Have [uv](https://docs.astral.sh/uv/getting-started/installation/) installed on your system.\n\n### Scanning\n\nTo run a full scan of your machine (auto-discovers agents, MCP servers, skills), run:\n\n```bash\nuvx snyk-agent-scan@latest\n```\n\n\nThis will scan for security vulnerabilities in MCP servers, tools, prompts, and resources. It will automatically discover a variety of agent configurations, including Claude Code/Desktop, Cursor, Gemini CLI, and Windsurf.\n\nTo also auto-discover and scan agent skills, pass the `--skills` flag:\n\n```bash\nuvx snyk-agent-scan@latest --skills\n```\n\nYou can also scan particular MCP configuration files or skills:\n\n```bash\n# scan a specific mcp configuration\nuvx snyk-agent-scan@latest ~/.vscode/mcp.json\n# scan a single agent skill\nuvx snyk-agent-scan@latest --skills ~/path/to/my/SKILL.md\n# scan all claude skills\nuvx snyk-agent-scan@latest --skills ~/.claude/skills\n```\n\n#### Example Run\n\n[![Agent Scan security vulnerabilities demo](demo.svg)](https://asciinema.org/a/716858)',
    },
    'scanner-capabilities': {
        "description": 'Agent Scan is a security scanning tool to both scan and inspect the supply chain of agent components on your machine.',
        "guidance": 'Agent Scan is a security scanning tool to both scan and inspect the supply chain of agent components on your machine. It scans for common security vulnerabilities like prompt injections, tool poisoning, toxic flows, or vulnerabilities in agent skills.\n\nAgent Scan operates in two main modes which can be used jointly or separately:\n\n1. **Scan Mode**: The CLI command `snyk-agent-scan` scans the current machine for agents and agent components such as skills and MCP servers. Upon completion, it will output a comprehensive report for the user to review.\n\n2. **Background Mode** (MDM, Crowdstrike). Agent Scan scans the machine in regular intervals in the background, and reports the results to a [Snyk Evo](https://evo.ai.snyk.io) instance. This can be used by security teams to monitor the company-wide agent supply chain in a central location. To set this up, please [contact us](https://evo.ai.snyk.io/#contact-us).',
    },
    'how-it-works': {
        "description": "### Scanning\n\nAgent Scan searches through your local agent's configuration files to find agents, skills, and MCP servers.",
        "guidance": "### Scanning\n\nAgent Scan searches through your local agent's configuration files to find agents, skills, and MCP servers. For MCP, it connects to servers and retrieves tool descriptions.\n\n#### Interactive Consent for MCP Servers\n\nBy default, Agent Scan prompts for user consent before starting each stdio MCP server during interactive runs. This consent flow:\n\n- Shows the server name, command, and environment variables (redacted) that will be executed\n- Allows you to approve or decline each server individually\n- Prevents potentially untrusted servers from running without your explicit permission\n- Records declined servers with a `user_declined` error (they are never started)\n\nFor non-interactive environments (e.g., CI/CD pipelines), you must use the `--dangerously-run-mcp-servers` flag to bypass the consent prompt and start all servers automatically.\n\n#### Analysis and Validation\n\nAgent Scan validates the components, both with local checks and by invoking the Agent Scan API. For this, skills, agent applications, tool names, and descriptions are shared with Snyk. By using Agent Scan, you agree to the Snyk [terms of use for Agent Scan](./TERMS.md).\n\nA unique, persistent, and anonymous ID is assigned to your scans for analysis. You can opt out of sending this information using the `--opt-out` flag.\n\nAgent Scan does not store or log any usage data, i.e. the contents and results of your MCP tool calls.",
    },
    'cli-parameters': {
        "description": 'Agent Scan provides the following commands:\n\n```\nsnyk-agent-scan - Security scanner for agents, MCP servers, and skills\n```\n\n### Common Options\n\nThese options are available for all commands:\n\n```\n--st',
        "guidance": 'Agent Scan provides the following commands:\n\n```\nsnyk-agent-scan - Security scanner for agents, MCP servers, and skills\n```\n\n### Common Options\n\nThese options are available for all commands:\n\n```\n--storage-file FILE    Path to store scan results and scanner state (default: ~/.mcp-scan)\n--base-url URL         Base URL for the verification server\n--verbose              Enable detailed logging output\n--print-errors         Show error details and tracebacks\n--json                 Output results in JSON format instead of rich text\n```\n\n### Commands\n\n#### scan (default)\n\nScan MCP configurations for security vulnerabilities in tools, prompts, and resources.\n\n```\nsnyk-agent-scan scan [CONFIG_FILE...]\n```\n\nOptions:\n\n```\n--skills                          Also scan agent skills (default: off)\n--checks-per-server NUM           Number of checks to perform on each server (default: 1)\n--server-timeout SECONDS          Seconds to wait before timing out server connections (default: 10)\n--suppress-mcpserver-io BOOL      Suppress stderr from stdio MCP servers (stdout carries the JSON-RPC protocol\n                                  and is never shown). Default: False for interactive runs (stderr is streamed\n                                  with a [server-name] prefix), True otherwise.\n--dangerously-run-mcp-servers     Skip the interactive consent prompt and start every stdio MCP server listed\n                                  in the scanned configs.\n```\n\n#### inspect\n\nPrint descriptions of tools, prompts, and resources without verification.\n\n```\nsnyk-agent-scan inspect [CONFIG_FILE...]\n```\n\nOptions:\n\n```\n--server-timeout SECONDS          Seconds to wait before timing out server connections (default: 10)\n--suppress-mcpserver-io BOOL      Suppress stderr from stdio MCP servers (stdout carries the JSON-RPC protocol\n                                  and is never shown). Default: False for interactive runs (stderr is streamed\n                                  with a [server-name] prefix), True otherwise.\n--dangerously-run-mcp-servers     Skip the interactive consent prompt and start every stdio MCP server listed\n                                  in the scanned configs.\n```\n\n#### help\n\nDisplay detailed help information and examples.\n\n```bash\nsnyk-agent-scan help\n```\n\n### Examples\n\n```bash\n# Scan all known MCP configs\nsnyk-agent-scan\n\n# Scan all known MCP configs and agent skills\nsnyk-agent-scan --skills\n\n# Scan a specific config file\nsnyk-agent-scan ~/custom/config.json\n\n# Scan a specific skill file\nsnyk-agent-scan --skills ~/path/to/my/SKILL.md\n\n# Scan a directory for skills\nsnyk-agent-scan --skills ~/.claude/skills\n\n# Just inspect tools without verification\nsnyk-agent-scan inspect\n\n# Skip consent prompts and run all servers (for CI/CD or trusted environments)\nsnyk-agent-scan --dangerously-run-mcp-servers\n\n# Suppress MCP server stderr output during scanning\nsnyk-agent-scan --suppress-mcpserver-io=true\n\n# CI mode (requires --dangerously-run-mcp-servers)\nsnyk-agent-scan --ci --dangerously-run-mcp-servers\n```',
    },
    'demo': {
        "description": 'This repository includes a vulnerable MCP server that can demonstrate Model Context Protocol security issues that Agent Scan finds.',
        "guidance": 'This repository includes a vulnerable MCP server that can demonstrate Model Context Protocol security issues that Agent Scan finds.\n\nHow to demo MCP security issues?\n\n1. Clone this repository\n2. Create an `mcp.json` config file in the cloned git repository root directory with the following contents:\n\n```jsonc\n{\n  "mcpServers": {\n    "Demo MCP Server": {\n      "type": "stdio",\n      "command": "uv",\n      "args": ["run", "mcp", "run", "demoserver/server.py"],\n    },\n  },\n}\n```\n\n3. Run Agent Scan: `uvx --python 3.13 snyk-agent-scan@latest scan --full-toxic-flows mcp.json`\n\nNote: if you place the `mcp.json` configuration filepath elsewhere then adjust the `args` path inside the MCP server configuration to reflect the path to the MCP Server (`demoserver/server.py`) as well as the `uvx` command that runs Agent Scan with the correct filepath to `mcp.json`.',
    },
    'agent-scan-is-closed-to-contributions': {
        "description": 'Agent Scan does not accept external contributions at this time.',
        "guidance": 'Agent Scan does not accept external contributions at this time.\n\nWe welcome suggestions, bug reports, or feature requests as GitHub issues.',
    },
    'development-setup': {
        "description": 'To run Agent Scan from source, follow these steps:\n\n```bash\nuv run pip install -e.',
        "guidance": 'To run Agent Scan from source, follow these steps:\n\n```bash\nuv run pip install -e .\nuv run -m src.agent_scan.cli\n```',
    },
    'including-agent-scan-results-in-your-own-project-registry': {
        "description": 'If you want to include Agent Scan results in your own project or registry, please [reach out](https://evo.',
        "guidance": 'If you want to include Agent Scan results in your own project or registry, please [reach out](https://evo.ai.snyk.io/#contact-us). There are designated APIs for this purpose. Using the standard Agent Scan API for large scale scanning is considered abuse and will result in your account being blocked.',
    },
    'documentation': {
        "description": '- [Scanning](docs/scanning.',
        "guidance": '- [Scanning](docs/scanning.md) — How scanning works, CLI parameters, and usage examples.\n- [Issue Codes](docs/issue-codes.md) — Reference for all security issues detected by Agent Scan.',
    },
    'further-reading': {
        "description": '- [Introducing MCP-Scan](https://invariantlabs.',
        "guidance": '- [Introducing MCP-Scan](https://invariantlabs.ai/blog/introducing-mcp-scan)\n- [MCP Security Notification Tool Poisoning Attacks](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)\n- [WhatsApp MCP Exploited](https://invariantlabs.ai/blog/whatsapp-mcp-exploited)\n- [MCP Prompt Injection](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)\n- [Toxic Flow Analysis](https://invariantlabs.ai/blog/toxic-flow-analysis)\n- [Skills Report](.github/reports/skills-report.pdf)',
    },
    'changelog': {
        "description": 'See [CHANGELOG.',
        "guidance": 'See [CHANGELOG.md](CHANGELOG.md).',
    },
}


@mcp.tool()
def list_agent_scan_skills() -> dict:
    """List all available agent_scan skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_agent_scan_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific agent_scan skill."""
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
    hint = get_presentation_hint('agent_scan', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@agent_scan",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'agent_scan',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
