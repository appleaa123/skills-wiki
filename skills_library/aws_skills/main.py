"""Skill: aws_skills."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("aws-skills")


_SKILLS: dict[str, dict] = {
    'plugins': {
        "description": '### 0.',
        "guidance": '### 0. AWS Common Plugin (Dependency)\n\nShared AWS agent skills including AWS Documentation MCP configuration for querying up-to-date AWS knowledge.\n\n**Features**:\n- AWS MCP server configuration guide\n- Documentation MCP setup for querying AWS knowledge\n- Shared by all other AWS plugins as a dependency\n\n**Note**: This plugin is automatically loaded as a dependency by other plugins. Install it first if installing plugins individually.\n\n### 1. AWS CDK Plugin\n\nAWS CDK development skill with integrated MCP server for infrastructure as code.\n\n**Features**:\n- AWS CDK best practices and patterns\n- Pre-deployment validation script\n- Comprehensive CDK patterns reference\n\n**Integrated MCP Server**:\n- AWS CDK MCP (stdio)\n\n### 2. AWS Cost & Operations Plugin\n\nCost optimization, monitoring, and operational excellence with 3 integrated MCP servers.\n\n**Features**:\n- Cost estimation and optimization\n- Monitoring and observability patterns\n- Operational best practices\n\n**Integrated MCP Servers**:\n- AWS Pricing\n- AWS Cost Explorer\n- Amazon CloudWatch\n\n### 3. AWS Serverless & Event-Driven Architecture Plugin\n\nServerless and event-driven architecture patterns based on Well-Architected Framework.\n\n**Features**:\n- Well-Architected serverless design principles\n- Event-driven architecture patterns\n- Orchestration with Step Functions\n- Saga patterns for distributed transactions\n- Event sourcing patterns\n\n### 4. AWS Agentic AI Plugin\n\nAWS Bedrock AgentCore comprehensive expert for deploying and managing AI agents.\n\n**Features**:\n- Gateway service for converting REST APIs to MCP tools\n- Runtime service for deploying and scaling agents\n- Memory service for managing conversation state\n- Identity service for credential and access management\n- Code Interpreter for secure code execution\n- Browser service for web automation\n- Observability for tracing and monitoring',
    },
    'installation': {
        "description": '### Option 1: Claude Code Plugin Marketplace\n\nAdd the marketplace to Claude Code:\n\n```bash\n/plugin marketplace add zxkane/aws-skills\n```\n\nInstall plugins individually:\n\n```bash\n# Install the common de',
        "guidance": '### Option 1: Claude Code Plugin Marketplace\n\nAdd the marketplace to Claude Code:\n\n```bash\n/plugin marketplace add zxkane/aws-skills\n```\n\nInstall plugins individually:\n\n```bash\n# Install the common dependency first\n/plugin install aws-common@aws-skills\n\n# Then install the plugins you need\n/plugin install aws-cdk@aws-skills\n/plugin install aws-cost-ops@aws-skills\n/plugin install serverless-eda@aws-skills\n/plugin install aws-agentic-ai@aws-skills\n```\n\n### Option 2: Install Individual Skills via npx\n\nInstall a single skill directly from the repository using [skills.sh](https://skills.sh):\n\n```bash\n# AWS CDK development skill\nnpx skills add https://github.com/zxkane/aws-skills --skill aws-cdk-development\n\n# AWS cost & operations skill\nnpx skills add https://github.com/zxkane/aws-skills --skill aws-cost-operations\n\n# AWS serverless & event-driven architecture skill\nnpx skills add https://github.com/zxkane/aws-skills --skill aws-serverless-eda\n\n# AWS Bedrock AgentCore skill\nnpx skills add https://github.com/zxkane/aws-skills --skill aws-agentic-ai\n\n# AWS MCP setup (shared dependency)\nnpx skills add https://github.com/zxkane/aws-skills --skill aws-mcp-setup\n```\n\nBrowse all skills at [skills.sh/zxkane/aws-skills](https://skills.sh/zxkane/aws-skills).',
    },
    'core-cdk-principles': {
        "description": '### Resource Naming\n\n**Do NOT explicitly specify resource names** when they are optional in CDK constructs.',
        "guidance": "### Resource Naming\n\n**Do NOT explicitly specify resource names** when they are optional in CDK constructs.\n\n```typescript\n// ✅ GOOD - Let CDK generate unique names\nnew lambda.Function(this, 'MyFunction', {\n  // No functionName specified\n});\n\n// ❌ BAD - Prevents multiple deployments\nnew lambda.Function(this, 'MyFunction', {\n  functionName: 'my-lambda',\n});\n```\n\n### Lambda Functions\n\nUse appropriate constructs for automatic bundling:\n\n- **TypeScript/JavaScript**: `NodejsFunction` from `aws-cdk-lib/aws-lambda-nodejs`\n- **Python**: `PythonFunction` from `@aws-cdk/aws-lambda-python-alpha`\n\n### Pre-Deployment Validation\n\nBefore committing CDK code:\n\n```bash\nnpm run build\nnpm test\nnpm run lint\ncdk synth\n./scripts/validate-stack.sh\n```",
    },
    'usage-examples': {
        "description": '### CDK Development\n\nAsk Claude to help with CDK:\n\n```\nCreate a CDK stack with a Lambda function that processes S3 events\n```\n\nClaude will:\n- Follow CDK best practices\n- Use NodejsFunction for automat',
        "guidance": '### CDK Development\n\nAsk Claude to help with CDK:\n\n```\nCreate a CDK stack with a Lambda function that processes S3 events\n```\n\nClaude will:\n- Follow CDK best practices\n- Use NodejsFunction for automatic bundling\n- Avoid explicit resource naming\n- Grant proper IAM permissions\n- Use MCP servers for latest AWS information\n\n### Cost Optimization\n\nEstimate costs before deployment:\n\n```\nEstimate the monthly cost of running 10 Lambda functions with 1M invocations each\n```\n\nAnalyze current spending:\n\n```\nShow me my AWS costs for the last 30 days broken down by service\n```\n\n### Monitoring and Observability\n\nSet up monitoring:\n\n```\nCreate CloudWatch alarms for my Lambda functions to alert on errors and high duration\n```\n\nInvestigate issues:\n\n```\nShow me CloudWatch logs for my API Gateway errors in the last hour\n```\n\n### Security and Audit\n\nAudit activity:\n\n```\nShow me all IAM changes made in the last 7 days\n```\n\nAssess security:\n\n```\nRun a Well-Architected security assessment on my infrastructure\n```\n\n### Serverless Development\n\nBuild serverless applications:\n\n```\nCreate a serverless API with Lambda and API Gateway for user management\n```\n\nImplement event-driven workflow:\n\n```\nCreate an event-driven order processing system with EventBridge and Step Functions\n```\n\nOrchestrate complex workflows:\n\n```\nImplement a saga pattern for booking flights, hotels, and car rentals with compensation logic\n```\n\n### AI Agent Development\n\nDeploy AI agents with Bedrock AgentCore:\n\n```\nDeploy a REST API as an MCP tool using AgentCore Gateway\n```\n\nManage agent memory:\n\n```\nSet up conversation memory for my AI agent with DynamoDB backend\n```\n\nMonitor agent performance:\n\n```\nConfigure observability for my AgentCore runtime with CloudWatch dashboards\n```',
    },
    'structure': {
        "description": '```.',
        "guidance": '```\n.\n├── .claude-plugin/\n│   └── marketplace.json              # Plugin marketplace configuration\n├── plugins/                          # Each plugin has isolated skills\n│   ├── aws-common/\n│   │   └── skills/\n│   │       └── aws-mcp-setup/        # Shared MCP configuration skill\n│   │           └── SKILL.md\n│   ├── aws-cdk/\n│   │   └── skills/\n│   │       └── aws-cdk-development/  # CDK development skill\n│   │           ├── SKILL.md\n│   │           ├── references/\n│   │           │   └── cdk-patterns.md\n│   │           └── scripts/\n│   │               └── validate-stack.sh\n│   ├── aws-cost-ops/\n│   │   └── skills/\n│   │       └── aws-cost-operations/  # Cost & operations skill\n│   │           ├── SKILL.md\n│   │           └── references/\n│   │               ├── operations-patterns.md\n│   │               └── cloudwatch-alarms.md\n│   ├── serverless-eda/\n│   │   └── skills/\n│   │       └── aws-serverless-eda/   # Serverless & EDA skill\n│   │           ├── SKILL.md\n│   │           └── references/\n│   │               ├── serverless-patterns.md\n│   │               └── eda-patterns.md\n│   └── aws-agentic-ai/\n│       └── skills/\n│           └── aws-agentic-ai/       # Bedrock AgentCore skill\n│               ├── SKILL.md\n│               ├── services/         # Service-specific docs\n│               └── cross-service/    # Cross-service patterns\n└── README.md\n```',
    },
    'mcp-server-names': {
        "description": "MCP server names use short identifiers to comply with Bedrock's 64-character tool name limit.",
        "guidance": "MCP server names use short identifiers to comply with Bedrock's 64-character tool name limit. The naming pattern is: `mcp__plugin_{plugin}_{server}__{tool}`\n\nExamples: `awsdocs` (AWS docs), `cdk` (CDK), `cw` (CloudWatch), `sfn` (Step Functions), `sam` (Serverless), etc.",
    },
    'resources': {
        "description": '- [Claude Agent Skills](https://docs.',
        "guidance": '- [Claude Agent Skills](https://docs.claude.com/en/docs/claude-code/skills)\n- [AWS MCP Servers](https://awslabs.github.io/mcp/)\n- [AWS CDK](https://aws.amazon.com/cdk/)\n- [Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html)\n- [MCP Protocol](https://modelcontextprotocol.io/)',
    },
    'license': {
        "description": 'MIT License - see [LICENSE](LICENSE).',
        "guidance": 'MIT License - see [LICENSE](LICENSE)',
    },
}


@mcp.tool()
def list_aws_skills_skills() -> dict:
    """List all available aws_skills skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_aws_skills_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific aws_skills skill."""
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
    hint = get_presentation_hint('aws_skills', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@aws_skills",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'aws_skills',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
