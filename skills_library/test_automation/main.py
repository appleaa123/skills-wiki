"""Skill: test_automation."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("test-automation")


_SKILLS: dict[str, dict] = {
    'what-is-this': {
        "description": 'TestMu AI Skills is a curated collection of **Agent Skills** that teach AI coding assistants how to write production-grade test automation.',
        "guidance": 'TestMu AI Skills is a curated collection of **Agent Skills** that teach AI coding assistants how to write production-grade test automation. Each skill is a self-contained package of instructions, code patterns, debugging guides, and CI/CD configurations for a specific testing framework.\n\nInstead of getting generic test code, your AI agent becomes a **Senior QA automation architect** that knows:\n- The right project structure for each framework\n- Correct dependency versions and configurations\n- Both local and cloud (TestMu AI) execution patterns\n- Common pitfalls and how to debug them\n- CI/CD integration with GitHub Actions\n- Best practices that ship in real-world codebases',
    },
    'quick-start': {
        "description": '### Install All Skills\n\n```bash\nnpx skills add https://github.',
        "guidance": '### Install All Skills\n\n```bash\nnpx skills add https://github.com/LambdaTest/agent-skills.git\n```\n\nThe CLI auto-detects your AI tool and installs to the right directory. You can also specify it explicitly:\n\n```bash\nnpx skills add https://github.com/LambdaTest/agent-skills.git --tool cursor\n```\n\n### Install a Specific Skill\n\n```bash\n# E2E Testing\nnpx skills add https://github.com/LambdaTest/agent-skills.git --skill selenium-skill\nnpx skills add https://github.com/LambdaTest/agent-skills.git --skill playwright-skill\nnpx skills add https://github.com/LambdaTest/agent-skills.git --skill cypress-skill\n\n# Unit Testing\nnpx skills add https://github.com/LambdaTest/agent-skills.git --skill jest-skill\nnpx skills add https://github.com/LambdaTest/agent-skills.git --skill pytest-skill\nnpx skills add https://github.com/LambdaTest/agent-skills.git --skill junit-5-skill\n\n# Mobile Testing\nnpx skills add https://github.com/LambdaTest/agent-skills.git --skill appium-skill\n\n# BDD\nnpx skills add https://github.com/LambdaTest/agent-skills.git --skill cucumber-skill\n```\n\n### Browse Available Skills\n\n```bash\nnpx skills list https://github.com/LambdaTest/agent-skills.git\n```\n\n### CLI Reference\n\n| Flag | Description | Example |\n|------|-------------|---------|\n| `--skill <name>` | Install a single skill | `--skill playwright-skill` |\n| `--tool <name>` | Target a specific AI tool | `--tool claude` |\n| `--dir <path>` | Custom installation directory | `--dir ./my-skills` |\n\n> Supported tools: `claude` · `cursor` · `copilot` · `gemini` · `codex` · `opencode` · `windsurf`\n\n---\n\nOnce installed, just ask your AI assistant naturally:\n\n```\n"Write Playwright tests for the login page and run them on TestMu AI cloud (Chrome + Firefox)"\n\n"Set up Cypress component tests for the React dashboard and upload screenshots on failure"\n\n"Create JUnit 5 tests for the payments service with Mockito and GitHub Actions CI"\n\n"Run Playwright tests locally against http://localhost:3000 with trace and video enabled"\n```\n\n---',
    },
    'compatibility': {
        "description": 'These skills follow the open **[Agent Skills Standard](https://agentskills.',
        "guidance": 'These skills follow the open **[Agent Skills Standard](https://agentskills.io)** (`SKILL.md` format):\n\n| Tool | Type | Support | `--tool` flag |\n|------|------|---------|---------------|\n| **Claude Code** | CLI | ✅ Full | `claude` |\n| **GitHub Copilot** | Extension | ✅ Full | `copilot` |\n| **Cursor** | IDE | ✅ Full | `cursor` |\n| **Gemini CLI** | CLI | ✅ Full | `gemini` |\n| **Codex CLI** | CLI | ✅ Full | `codex` |\n| **OpenCode** | CLI | ✅ Full | `opencode` |\n| **Windsurf** | IDE | ✅ Full | `windsurf` |\n| **Claude.ai** | Web | ✅ Upload | Settings → Features → Skills |\n\n---',
    },
    'features-categories': {
        "description": '| Category | Count | Frameworks |\n|----------|-------|------------|\n| 🌐 **E2E / Browser Testing** | 15 | Selenium, Playwright, Cypress, WebdriverIO, Puppeteer, TestCafe, Nightwatch.',
        "guidance": '| Category | Count | Frameworks |\n|----------|-------|------------|\n| 🌐 **E2E / Browser Testing** | 15 | Selenium, Playwright, Cypress, WebdriverIO, Puppeteer, TestCafe, Nightwatch.js, Capybara, Geb, Selenide, NemoJS, Protractor, Codeception, Laravel Dusk, Robot Framework |\n| 🧪 **Unit Testing** | 15 | Jest, JUnit 5, pytest, TestNG, Vitest, Mocha, Jasmine, Karma, xUnit, NUnit, MSTest, RSpec, PHPUnit, Test::Unit, unittest |\n| 📱 **Mobile Testing** | 5 | Appium, Espresso, XCUITest, Flutter, Detox |\n| 📋 **BDD Testing** | 7 | Cucumber, SpecFlow, Serenity BDD, Behave, Behat, Gauge, Lettuce |\n| 👁️ **Visual Testing** | 1 | SmartUI |\n| ☁️ **Cloud Testing** | 1 | HyperExecute |\n| 🔄 **Migration** | 1 | Selenium ↔ Playwright, Puppeteer, Cypress |\n| 🔄 **DevOps / CI/CD** | 1 | GitHub Actions / Jenkins / GitLab CI |\n\n### Languages Covered\n\n`Java` · `Python` · `JavaScript` · `TypeScript` · `C#` · `Ruby` · `PHP` · `Kotlin` · `Swift` · `Objective-C` · `Dart` · `Groovy` · `YAML` · `XML` · `Robot Framework`\n\n---',
    },
    'full-skill-registry-46-46': {
        "description": '| Skill | Languages | Category | Quick Install |\n|-------|-----------|----------|---------------|\n| **[Selenium Skill](selenium-skill/)** | Java, Python, JS, C#, Ruby | E2E | `npx skills add https://g',
        "guidance": '| Skill | Languages | Category | Quick Install |\n|-------|-----------|----------|---------------|\n| **[Selenium Skill](selenium-skill/)** | Java, Python, JS, C#, Ruby | E2E | `npx skills add https://github.com/LambdaTest/agent-skills.git --skill selenium-skill` |\n| **[Playwright Skill](playwright-skill/)** | JS, TS, Python, Java, C# | E2E | `npx skills add https://github.com/LambdaTest/agent-skills.git --skill playwright-skill` |\n| **[Cypress Skill](cypress-skill/)** | JS, TS | E2E | `npx skills add https://github.com/LambdaTest/agent-skills.git --skill cypress-skill` |\n| **[Jest Skill](jest-skill/)** | JS, TS | Unit | `npx skills add https://github.com/LambdaTest/agent-skills.git --skill jest-skill` |\n| **[JUnit 5 Skill](junit-5-skill/)** | Java | Unit | `npx skills add https://github.com/LambdaTest/agent-skills.git --skill junit-5-skill` |\n| **[pytest Skill](pytest-skill/)** | Python | Unit | `npx skills add https://github.com/LambdaTest/agent-skills.git --skill pytest-skill` |\n| **[TestNG Skill](testng-skill/)** | Java | Unit | `npx skills add https://github.com/LambdaTest/agent-skills.git --skill testng-skill` |\n| **[WebdriverIO Skill](webdriverio-skill/)** | JS, TS | E2E | `npx skills add https://github.com/LambdaTest/agent-skills.git --skill webdriverio-skill` |\n| **[Appium Skill](appium-skill/)** | Java, Python, JS, Ruby, C# | Mobile | `npx skills add https://github.com/LambdaTest/agent-skills.git --skill appium-skill` |\n| **[Puppeteer Skill](puppeteer-skill/)** | JS, TS | E2E | `npx skills add https://github.com/LambdaTest/agent-skills.git --skill puppeteer-skill` |\n| **[Test Framework Migration Skill](test-framework-migration-skill/)** | JS, TS, Java, Python, C# | Migration | `npx skills add https://github.com/LambdaTest/agent-skills.git --skill test-framework-migration-skill` |\n| **[Mocha Skill](mocha-skill/)** | JS, TS | Unit | `npx skills add https://github.com/LambdaTest/agent-skills.git --skill mocha-skill` |\n| **[Vitest Skill](vitest-skill/)** | JS, TS | Unit | `npx skills add https://github.com/LambdaTest/agent-skills.git --skill vitest-skill` |\n| **[Cucumber Skill](cucumber-skill/)** | Java, JS, Ruby, TS | BDD | `npx skills add https://github.com/LambdaTest/agent-skills.git --skill cucumber-skill` |\n| **[Espresso Skill](espresso-skill/)** | Java, Kotlin | Mobile | `npx skills add https://github.com/LambdaTest/agent-skills.git --skill espresso-skill` |\n| **[Nightwatch.js Skill](nightwatchjs-skill/)** | JS, TS | E2E | `npx skills add https://github.com/LambdaTest/agent-skills.git --skill nightwatchjs-skill` |\n| **[Flutter Testing Skill](flutter-testing-skill/)** | Dart | Mobile | `npx skills add https://github.com/LambdaTest/agent-skills.git --skill flutter-testing-skill` |\n| **[XCUITest Skill](xcuitest-skill/)** | Swift, Obj-C | Mobile | `npx skills add https://github.com/LambdaTest/agent-skills.git --skill xcuitest-skill` |\n| **[Detox Skill](detox-skill/)** | JS, TS | Mobile | `npx skills add https://github.com/LambdaTest/agent-skills.git --skill detox-skill` |\n| **[TestCafe Skill](testcafe-skill/)** | JS, TS | E2E | `npx skills add https://github.com/LambdaTest/agent-skills.git --skill testcafe-skill` |\n| **[xUnit Skill](xunit-skill/)** | C# | Unit | `npx skills add https://github.com/LambdaTest/agent-skills.git --skill xunit-skill` |\n| **[RSpec Skill](rspec-skill/)** | Ruby | Unit | `npx skills add https://github.com/LambdaTest/agent-skills.git --skill rspec-skill` |\n| **[NUnit Skill](nunit-skill/)** | C# | Unit | `npx skills add https://github.com/LambdaTest/agent-skills.git --skill nunit-skill` |\n| **[Karma Skill](karma-skill/)** | JS, TS | Unit | `npx skills add https://github.com/LambdaTest/agent-skills.git --skill karma-skill` |\n| **[MSTest Skill](mstest-skill/)** | C# | Unit | `npx skills add https://github.com/LambdaTest/agent-skills.git --skill mstest-skill` |\n| **[Jasmine Skill](jasmine-skill/)** | JS, TS | Unit | `npx skills add https://github.com/LambdaTest/agent-skills.git --skill jasmine-skill` |\n| **[PHPUnit Skill](phpunit-skill/)** | PHP | Unit | `npx skills add https://github.com/LambdaTest/agent-skills.git --skill phpunit-skill` |\n| **[Robot Framework Skill](robot-framework-skill/)** | Python, Robot | E2E | `npx skills add https://github.com/LambdaTest/agent-skills.git --skill robot-framework-skill` |\n| **[Behat Skill](behat-skill/)** | PHP | BDD | `npx skills add https://github.com/LambdaTest/agent-skills.git --skill behat-skill` |\n| **[Behave Skill](behave-skill/)** | Python | BDD | `npx skills add https://github.com/LambdaTest/agent-skills.git --skill behave-skill` |\n| **[Capybara Skill](capybara-skill/)** | Ruby | E2E | `npx skills add https://github.com/LambdaTest/agent-skills.git --skill capybara-skill` |\n| **[Codeception Skill](codeception-skill/)** | PHP | E2E | `npx skills add https://github.com/LambdaTest/agent-skills.git --skill codeception-skill` |\n| **[Gauge Skill](gauge-skill/)** | Java, Python, JS, Ruby, C# | BDD | `npx skills add https://github.com/LambdaTest/agent-skills.git --skill gauge-skill` |\n| **[Geb Skill](geb-skill/)** | Groovy | E2E | `npx skills add https://github.com/LambdaTest/agent-skills.git --skill geb-skill` |\n| **[Laravel Dusk Skill](laravel-dusk-skill/)** | PHP | E2E | `npx skills add https://github.com/LambdaTest/agent-skills.git --skill laravel-dusk-skill` |\n| **[Lettuce Skill](lettuce-skill/)** | Python | BDD | `npx skills add https://github.com/LambdaTest/agent-skills.git --skill lettuce-skill` |\n| **[Nemo.js Skill](nemojs-skill/)** | JS | E2E | `npx skills add https://github.com/LambdaTest/agent-skills.git --skill nemojs-skill` |\n| **[Protractor Skill](protractor-skill/)** | JS, TS | E2E | `npx skills add https://github.com/LambdaTest/agent-skills.git --skill protractor-skill` |\n| **[Selenide Skill](selenide-skill/)** | Java | E2E | `npx skills add https://github.com/LambdaTest/agent-skills.git --skill selenide-skill` |\n| **[Serenity BDD Skill](serenity-bdd-skill/)** | Java | BDD | `npx skills add https://github.com/LambdaTest/agent-skills.git --skill serenity-bdd-skill` |\n| **[SmartUI Skill](smartui-skill/)** | JS, TS, Java | Visual | `npx skills add https://github.com/LambdaTest/agent-skills.git --skill smartui-skill` |\n| **[SpecFlow Skill](specflow-skill/)** | C# | BDD | `npx skills add https://github.com/LambdaTest/agent-skills.git --skill specflow-skill` |\n| **[Test::Unit Skill](testunit-skill/)** | Ruby | Unit | `npx skills add https://github.com/LambdaTest/agent-skills.git --skill testunit-skill` |\n| **[unittest Skill](unittest-skill/)** | Python | Unit | `npx skills add https://github.com/LambdaTest/agent-skills.git --skill unittest-skill` |\n| **[HyperExecute Skill](hyperexecute-skill/)** | YAML | Cloud | `npx skills add https://github.com/LambdaTest/agent-skills.git --skill hyperexecute-skill` |\n| **[CI/CD Pipeline Skill](cicd-pipeline-skill/)** | YAML | DevOps | `npx skills add https://github.com/LambdaTest/agent-skills.git --skill cicd-pipeline-skill` |\n\n---',
    },
    'skill-architecture': {
        "description": 'Each skill follows the Agent Skills Standard with progressive disclosure:\n\n```\nselenium-skill/\n├── SKILL.',
        "guidance": 'Each skill follows the Agent Skills Standard with progressive disclosure:\n\n```\nselenium-skill/\n├── SKILL.md                          # Core instructions (<500 lines)\n│   └── Workflow + decision trees     # When/how to use the skill\n└── reference/\n    ├── playbook.md                   # Complete implementation guide\n    │   ├── Project setup & dependencies\n    │   ├── Code patterns & page objects\n    │   ├── Cloud integration (LambdaTest)\n    │   ├── CI/CD configuration\n    │   ├── Debugging table (12+ common problems)\n    │   └── Best practices checklist (14+ items)\n    ├── advanced-patterns.md          # Advanced topics\n    └── cloud-integration.md          # Cloud-specific patterns\n```\n\n**How it works:**\n1. **Metadata** (name + description) is always loaded — ~100 tokens per skill\n2. **SKILL.md body** loads when triggered — core workflow and patterns\n3. **Reference files** load on-demand — detailed code, debugging, CI/CD\n\n---',
    },
    'cloud-testing-with-testmu-ai': {
        "description": 'Skills that support browser/device testing include **TestMu AI  cloud integration** out of the box.',
        "guidance": 'Skills that support browser/device testing include **TestMu AI  cloud integration** out of the box.\n\n### Get Your TestMu AI Credentials\n\nMake sure you have your TestMu AI credentials with you to run test automation scripts on TestMu AI Selenium Grid. You can obtain these credentials from the [TestMu AI Automation Dashboard](https://automation.lambdatest.com/) or through [TestMu AI Profile](https://accounts.lambdatest.com/security).\n\nSet TestMu AI `USERNAME` and `ACCESS_KEY` in environment variables.\n- Copy `.env.example` to `.env` and fill in your credentials.\n\n\nor add credentials directly from your terminal:\n\n**For Linux/macOS:**\n```bash\nexport LT_USERNAME="YOUR_USERNAME"\nexport LT_ACCESS_KEY="YOUR_ACCESS_KEY"\n```\n\n**For Windows:**\n```bash\nset LT_USERNAME="YOUR_USERNAME"\nset LT_ACCESS_KEY="YOUR_ACCESS_KEY"\n```\n\n### Run Tests on the Cloud\n\nThen ask your AI assistant naturally:\n```\n"Run my Selenium tests on Chrome, Firefox, and Safari on TestMu AI with OS versions Windows 11, macOS Sonoma, and Ubuntu 22.04"\n\n"Execute Playwright tests across 5 browsers in parallel on TestMu AI, tag the build as \'release-1.8.2\', and capture traces on failure"\n\n"Set up Cypress on TestMu AI with video recording and JUnit reports, and upload artifacts to the dashboard"\n\n"Test my localhost app through the TestMu AI tunnel (http://localhost:3000) using Playwright and validate login + checkout flows"\n\n"Run mobile web tests on real devices via TestMu AI tunnel and verify the responsive layout on iPhone 15 and Pixel 8"\n```\n\nView your test results, logs, and video recordings on the [TestMu AI  Automation Dashboard](https://automation.lambdatest.com/).\n\n---',
    },
    'what-each-skill-includes': {
        "description": 'Every playbook follows a consistent structure:\n\n| Section | What It Covers |\n|---------|---------------|\n| **Project Setup** | Dependencies, versions, config files, project structure |\n| **Core Patter',
        "guidance": 'Every playbook follows a consistent structure:\n\n| Section | What It Covers |\n|---------|---------------|\n| **Project Setup** | Dependencies, versions, config files, project structure |\n| **Core Patterns** | Essential code patterns with complete, runnable examples |\n| **Page Objects / Utilities** | Reusable abstractions for real-world projects |\n| **Cloud Integration** | TestMu AI  RemoteWebDriver/capabilities configuration |\n| **CI/CD Integration** | GitHub Actions workflow with reports and parallel execution |\n| **Debugging Table** | 12+ common problems with cause → fix mappings |\n| **Best Practices** | 14+ actionable items for production code |\n\n---',
    },
    'repository-structure': {
        "description": '```\nagent-skills/\n├── README.',
        "guidance": '```\nagent-skills/\n├── README.md                  # This file\n├── LICENSE                    # MIT License\n├── CONTRIBUTING.md            # How to contribute\n├── skills_index.json          # Machine-readable skill registry\n├── scripts/\n│   └── validate_skills.py     # Validation script\n├── shared/\n│   ├── testmu-cloud-reference.md\n│   └── scripts/\n├── evals/                     # Evaluation test cases per skill\n│   └── *-evals.json\n└── <skill-name>/              # 46 skill directories\n    ├── SKILL.md\n    └── reference/\n        ├── playbook.md\n        └── advanced-patterns.md\n```\n\n---',
    },
    'validation': {
        "description": '```bash\npython3 scripts/validate_skills.',
        "guidance": '```bash\npython3 scripts/validate_skills.py\n```\n\nChecks: YAML frontmatter, line counts, reference files, cross-references.\n\n---',
    },
    'how-to-contribute': {
        "description": 'See [CONTRIBUTING.',
        "guidance": 'See [CONTRIBUTING.md](CONTRIBUTING.md) for details.\n\n1. Fork the repository\n2. Create your skill directory with `SKILL.md` and `reference/playbook.md`\n3. Run `python3 scripts/validate_skills.py`\n4. Submit a Pull Request\n\n---',
    },
    'credits': {
        "description": '- **[TestMu AI ](https://www.',
        "guidance": '- **[TestMu AI ](https://www.lambdatest.com)** — Power Your Software Testing with  AI Agents and Cloud\n- **[Anthropic](https://anthropic.com)** — Agent Skills standard and Claude Code\n- **[Agent Skills Standard](https://agentskills.io)** — Open standard for portable AI skills\n\n---',
    },
    'license': {
        "description": 'MIT License.',
        "guidance": 'MIT License. See [LICENSE](LICENSE) for details.',
    },
}


@mcp.tool()
def list_test_automation_skills() -> dict:
    """List all available test_automation skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_test_automation_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific test_automation skill."""
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
    hint = get_presentation_hint('test_automation', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@test_automation",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'test_automation',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
