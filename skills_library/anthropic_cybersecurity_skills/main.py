"""Skill: anthropic_cybersecurity_skills."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("anthropic-cybersecurity-skills")


_SKILLS: dict[str, dict] = {
    'give-any-ai-agent-the-security-skills-of-a-senior-analyst': {
        "description": 'A junior analyst knows which Volatility3 plugin to run on a suspicious memory dump, which Sigma rules catch Kerberoasting, and how to scope a cloud breach across three providers.',
        "guidance": "A junior analyst knows which Volatility3 plugin to run on a suspicious memory dump, which Sigma rules catch Kerberoasting, and how to scope a cloud breach across three providers. **Your AI agent doesn't — unless you give it these skills.**\n\nThis repo contains **754 structured cybersecurity skills** spanning **26 security domains**, each following the [agentskills.io](https://agentskills.io) open standard.  Every skill is mapped to **five industry frameworks** — MITRE ATT&CK, NIST CSF 2.0, MITRE ATLAS, MITRE D3FEND, and NIST AI RMF  — making this the only open-source skills library with unified cross-framework coverage.  Clone it, point your agent at it, and your next security investigation gets expert-level guidance in seconds.",
    },
    'five-frameworks-one-skill-library': {
        "description": 'No other open-source skills library maps every skill to all five frameworks.',
        "guidance": 'No other open-source skills library maps every skill to all five frameworks.  One skill, five compliance checkboxes. \n\n| Framework | Version | Scope in this repo | What it maps |\n|---|---|---|---|\n| [MITRE ATT&CK](https://attack.mitre.org) | v18 | 14 tactics · 200+ techniques | Adversary behaviors and TTPs |\n| [NIST CSF 2.0](https://www.nist.gov/cyberframework) | 2.0 | 6 functions · 22 categories | Organizational security posture |\n| [MITRE ATLAS](https://atlas.mitre.org) | v5.4 | 16 tactics · 84 techniques | AI/ML adversarial threats |\n| [MITRE D3FEND](https://d3fend.mitre.org) | v1.3 | 7 categories · 267 techniques | Defensive countermeasures |\n| [NIST AI RMF](https://airc.nist.gov/AI_RMF) | 1.0 | 4 functions · 72 subcategories | AI risk management |\n\n**Example — a single skill maps across all five:**\n\n| Skill | ATT&CK | NIST CSF | ATLAS | D3FEND | AI RMF |\n|---|---|---|---|---|---|\n| `analyzing-network-traffic-of-malware` | T1071 | DE.CM | AML.T0047 | D3-NTA | MEASURE-2.6 |',
    },
    'quick-start': {
        "description": '```bash\n# Option 1: npx (recommended)\nnpx skills add mukul975/Anthropic-Cybersecurity-Skills\n\n# Option 2: Git clone\ngit clone https://github.',
        "guidance": '```bash\n# Option 1: npx (recommended)\nnpx skills add mukul975/Anthropic-Cybersecurity-Skills\n\n# Option 2: Git clone\ngit clone https://github.com/mukul975/Anthropic-Cybersecurity-Skills.git\ncd Anthropic-Cybersecurity-Skills\n```\n\nWorks immediately with Claude Code, GitHub Copilot, OpenAI Codex CLI, Cursor, Gemini CLI, and any [agentskills.io](https://agentskills.io)-compatible platform.',
    },
    'try-it-on-the-playground': {
        "description": 'Experience Casky.',
        "guidance": 'Experience Casky.ai hands-on — no setup required.\n\n**[→ Launch Playground on Casky.ai](https://casky.ai/?utm_source=github&utm_medium=readme&utm_campaign=cohort_launch#waitlist)**\n\nThe playground lets you:\n- Run live cybersecurity skill exercises against real targets\n- See AI agents execute structured skills in real time\n- Explore MITRE ATT&CK mapped workflows interactively\n- Test threat hunting, DFIR, and penetration testing scenarios\n\nNo installation. No configuration. Just open and start.',
    },
    'why-this-exists': {
        "description": 'The cybersecurity workforce gap hit **4.',
        "guidance": "The cybersecurity workforce gap hit **4.8 million unfilled roles** globally in 2024 (ISC2). AI agents can help close that gap — but only if they have structured domain knowledge to work from. Today's agents can write code and search the web, but they lack the practitioner playbooks that turn a generic LLM into a capable security analyst.\n\nExisting security tool repos give you wordlists, payloads, or exploit code. None of them give an AI agent the structured decision-making workflow a senior analyst follows: when to use each technique, what prerequisites to check, how to execute step-by-step, and how to verify results. That is the gap this project fills.\n\n**Anthropic Cybersecurity Skills** is not a collection of scripts or checklists. It is an **AI-native knowledge base** built from the ground up for the agentskills.io standard  — YAML frontmatter for sub-second discovery, structured Markdown for step-by-step execution, and reference files for deep technical context.  Every skill encodes real practitioner workflows, not generated summaries.",
    },
    'what-s-inside-26-security-domains': {
        "description": '| Domain | Skills | Key capabilities |\n|---|---|---|\n| Cloud Security | 60 | AWS, Azure, GCP hardening · CSPM · cloud forensics |\n| Threat Hunting | 55 | Hypothesis-driven hunts · LOTL detection · beh',
        "guidance": '| Domain | Skills | Key capabilities |\n|---|---|---|\n| Cloud Security | 60 | AWS, Azure, GCP hardening · CSPM · cloud forensics |\n| Threat Hunting | 55 | Hypothesis-driven hunts · LOTL detection · behavioral analytics |\n| Threat Intelligence | 50 | STIX/TAXII · MISP · feed integration · actor profiling |\n| Web Application Security | 42 | OWASP Top 10 · SQLi · XSS · SSRF · deserialization |\n| Network Security | 40 | IDS/IPS · firewall rules · VLAN segmentation · traffic analysis |\n| Malware Analysis | 39 | Static/dynamic analysis · reverse engineering · sandboxing |\n| Digital Forensics | 37 | Disk imaging · memory forensics · timeline reconstruction |\n| Security Operations | 36 | SIEM correlation · log analysis · alert triage |\n| Identity & Access Management | 35 | IAM policies · PAM · zero trust identity · Okta · SailPoint |\n| SOC Operations | 33 | Playbooks · escalation workflows · metrics · tabletop exercises |\n| Container Security | 30 | K8s RBAC · image scanning · Falco · container forensics |\n| OT/ICS Security | 28 | Modbus · DNP3 · IEC 62443 · historian defense · SCADA |\n| API Security | 28 | GraphQL · REST · OWASP API Top 10 · WAF bypass |\n| Vulnerability Management | 25 | Nessus · scanning workflows · patch prioritization · CVSS |\n| Incident Response | 25 | Breach containment · ransomware response · IR playbooks |\n| Red Teaming | 24 | Full-scope engagements · AD attacks · phishing simulation |\n| Penetration Testing | 23 | Network · web · cloud · mobile · wireless pentesting |\n| Endpoint Security | 17 | EDR · LOTL detection · fileless malware · persistence hunting |\n| DevSecOps | 17 | CI/CD security · code signing · Terraform auditing |\n| Phishing Defense | 16 | Email authentication · BEC detection · phishing IR |\n| Cryptography | 14 | TLS · Ed25519 · certificate transparency · key management |\n| Zero Trust Architecture | 13 | BeyondCorp · CISA maturity model · microsegmentation |\n| Mobile Security | 12 | Android/iOS analysis · mobile pentesting · MDM forensics |\n| Ransomware Defense | 7 | Precursor detection · response · recovery · encryption analysis |\n| Compliance & Governance | 5 | CIS benchmarks · SOC 2 · regulatory frameworks |\n| Deception Technology | 2 | Honeytokens · breach detection canaries |',
    },
    'how-ai-agents-use-these-skills': {
        "description": 'Each skill costs **~30 tokens to scan** (frontmatter only)  and **500–2,000 tokens to fully load** (complete workflow).',
        "guidance": 'Each skill costs **~30 tokens to scan** (frontmatter only)  and **500–2,000 tokens to fully load** (complete workflow). This progressive disclosure architecture lets agents search all 754 skills in a single pass without blowing context windows. \n\n```\nUser prompt: "Analyze this memory dump for signs of credential theft"\n\nAgent\'s internal process:\n\n  1. Scans 754 skill frontmatters (~30 tokens each)\n     → identifies 12 relevant skills by matching tags, description, domain\n\n  2. Loads top 3 matches:\n     • performing-memory-forensics-with-volatility3\n     • hunting-for-credential-dumping-lsass\n     • analyzing-windows-event-logs-for-credential-access\n\n  3. Executes the structured Workflow section step-by-step\n     → runs Volatility3 plugins, checks LSASS access patterns,\n        correlates with event log evidence\n\n  4. Validates results using the Verification section\n     → confirms IOCs, maps findings to ATT&CK T1003 (Credential Dumping)\n```\n\n**Without these skills**, the agent guesses at tool commands and misses critical steps. **With them**, it follows the same playbook a senior DFIR analyst would use.',
    },
    'skill-anatomy': {
        "description": 'Every skill follows a consistent directory structure:\n\n```\nskills/performing-memory-forensics-with-volatility3/\n├── SKILL.',
        "guidance": 'Every skill follows a consistent directory structure:\n\n```\nskills/performing-memory-forensics-with-volatility3/\n├── SKILL.md              ← Skill definition (YAML frontmatter + Markdown body)\n├── references/\n│   ├── standards.md      ← MITRE ATT&CK, ATLAS, D3FEND, NIST mappings\n│   └── workflows.md      ← Deep technical procedure reference\n├── scripts/\n│   └── process.py        ← Working helper scripts\n└── assets/\n    └── template.md       ← Filled-in checklists and report templates\n```\n\n\n### YAML frontmatter (real example)\n\n```yaml\n---\nname: performing-memory-forensics-with-volatility3\ndescription: >-\n  Analyze memory dumps to extract running processes, network connections,\n  injected code, and malware artifacts using the Volatility3 framework.\ndomain: cybersecurity\nsubdomain: digital-forensics\ntags: [forensics, memory-analysis, volatility3, incident-response, dfir]\natlas_techniques: [AML.T0047]\nd3fend_techniques: [D3-MA, D3-PSMD]\nnist_ai_rmf: [MEASURE-2.6]\nnist_csf: [DE.CM-01, RS.AN-03]\nversion: "1.2"\nauthor: mukul975\nlicense: Apache-2.0\n---\n```\n\n\n### Markdown body sections\n\n```markdown',
    },
    'when-to-use': {
        "description": 'Trigger conditions — when should an AI agent activate this skill?.',
        "guidance": 'Trigger conditions — when should an AI agent activate this skill?',
    },
    'prerequisites': {
        "description": 'Required tools, access levels, and environment setup.',
        "guidance": 'Required tools, access levels, and environment setup.',
    },
    'workflow': {
        "description": 'Step-by-step execution guide with specific commands and decision points.',
        "guidance": 'Step-by-step execution guide with specific commands and decision points.',
    },
    'verification': {
        "description": 'How to confirm the skill was executed successfully.',
        "guidance": "How to confirm the skill was executed successfully.\n```\n\nFrontmatter fields: `name` (kebab-case, 1–64 chars), `description` (keyword-rich for agent discovery), `domain`, `subdomain`, `tags`,  `atlas_techniques` (MITRE ATLAS IDs), `d3fend_techniques` (MITRE D3FEND IDs), `nist_ai_rmf` (NIST AI RMF references), `nist_csf` (NIST CSF 2.0 categories).  MITRE ATT&CK technique mappings are documented in each skill's `references/standards.md` file and in the ATT&CK Navigator layer included with releases. \n\n<details>\n<summary><strong>📊 MITRE ATT&CK Enterprise coverage — all 14 tactics</strong></summary>\n\n&nbsp;\n\n| Tactic | ID | Coverage | Key skills |\n|---|---|---|---|\n| Reconnaissance | TA0043 | Strong | OSINT, subdomain enumeration, DNS recon |\n| Resource Development | TA0042 | Moderate | Phishing infrastructure, C2 setup detection |\n| Initial Access | TA0001 | Strong | Phishing simulation, exploit detection, forced browsing |\n| Execution | TA0002 | Strong | PowerShell analysis, fileless malware, script block logging |\n| Persistence | TA0003 | Strong | Scheduled tasks, registry, service accounts, LOTL |\n| Privilege Escalation | TA0004 | Strong | Kerberoasting, AD attacks, cloud privilege escalation |\n| Defense Evasion | TA0005 | Strong | Obfuscation, rootkit analysis, evasion detection |\n| Credential Access | TA0006 | Strong | Mimikatz detection, pass-the-hash, credential dumping |\n| Discovery | TA0007 | Moderate | BloodHound, AD enumeration, network scanning |\n| Lateral Movement | TA0008 | Strong | SMB exploits, lateral movement detection with Splunk |\n| Collection | TA0009 | Moderate | Email forensics, data staging detection |\n| Command and Control | TA0011 | Strong | C2 beaconing, DNS tunneling, Cobalt Strike analysis |\n| Exfiltration | TA0010 | Strong | DNS exfiltration, DLP controls, data loss detection |\n| Impact | TA0040 | Strong | Ransomware defense, encryption analysis, recovery |\n\nAn **ATT&CK Navigator layer file** is included in the [v1.0.0 release assets](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/releases/tag/v1.0.0) for visual coverage mapping. \n\n> **Note:** ATT&CK v19 lands April 28, 2026 — splitting Defense Evasion (TA0005) into two new tactics: *Stealth* and *Impair Defenses*.  Skill mappings will be updated in a forthcoming release.\n\n</details>\n\n<details>\n<summary><strong>📊 NIST CSF 2.0 alignment — all 6 functions</strong></summary>\n\n&nbsp;\n\n| Function | Skills | Examples |\n|---|---|---|\n| **Govern (GV)** | 30+ | Risk strategy, policy frameworks, roles & responsibilities |\n| **Identify (ID)** | 120+ | Asset discovery, threat landscape assessment, risk analysis |\n| **Protect (PR)** | 150+ | IAM hardening, WAF rules, zero trust, encryption |\n| **Detect (DE)** | 200+ | Threat hunting, SIEM correlation, anomaly detection |\n| **Respond (RS)** | 160+ | Incident response, forensics, breach containment |\n| **Recover (RC)** | 40+ | Ransomware recovery, BCP, disaster recovery |\n\nNIST CSF 2.0 (February 2024) added the **Govern** function  and expanded scope from critical infrastructure to all organizations.  Skill mappings align to all 22 categories and reference 106 subcategories. \n\n</details>\n\n<details>\n<summary><strong>📊 Framework deep dive — ATLAS, D3FEND, AI RMF</strong></summary>\n\n&nbsp;\n\n### MITRE ATLAS v5.4 — AI/ML adversarial threats\nATLAS maps adversarial tactics, techniques, and case studies specific to AI and machine learning systems. Version 5.4 covers **16 tactics and 84 techniques** including agentic AI attack vectors added in late 2025: AI agent context poisoning, tool invocation abuse, MCP server compromises, and malicious agent deployment.  Skills mapped to ATLAS help agents identify and defend against threats to ML pipelines, model weights, inference APIs, and autonomous workflows. \n\n### MITRE D3FEND v1.3 — Defensive countermeasures\nD3FEND is an NSA-funded knowledge graph of **267 defensive techniques** organized across 7 tactical categories: Model, Harden, Detect, Isolate, Deceive, Evict, and Restore.  Built on OWL 2 ontology, it uses a shared Digital Artifact layer to bidirectionally map defensive countermeasures to ATT&CK offensive techniques.  Skills tagged with D3FEND identifiers let agents recommend specific countermeasures for detected threats.\n\n### NIST AI RMF 1.0 + GenAI Profile (AI 600-1)\nThe AI Risk Management Framework defines 4 core functions — Govern, Map, Measure, Manage — with **72 subcategories** for trustworthy AI development.  The GenAI Profile (AI 600-1, July 2024) adds **12 risk categories** specific to generative AI, from confabulation and data privacy to prompt injection and supply chain risks.  Colorado's AI Act (effective February 2026) provides a **legal safe harbor** for organizations complying with NIST AI RMF, making these mappings directly relevant to regulatory compliance.\n\n</details>",
    },
    'compatible-platforms': {
        "description": '**AI code assistants**\nClaude Code (Anthropic) · GitHub Copilot (Microsoft) · Cursor · Windsurf · Cline · Aider · Continue · Roo Code · Amazon Q Developer · Tabnine · Sourcegraph Cody · JetBrains AI \n',
        "guidance": '**AI code assistants**\nClaude Code (Anthropic) · GitHub Copilot (Microsoft) · Cursor · Windsurf · Cline · Aider · Continue · Roo Code · Amazon Q Developer · Tabnine · Sourcegraph Cody · JetBrains AI \n\n**CLI agents**\nOpenAI Codex CLI · Gemini CLI (Google) \n\n**Autonomous agents**\nDevin · Replit Agent · SWE-agent · OpenHands \n\n**Agent frameworks & SDKs**\nLangChain · CrewAI · AutoGen · Semantic Kernel · Haystack · Vercel AI SDK · Any MCP-compatible agent \n\nAll platforms that support the [agentskills.io](https://agentskills.io) standard can load these skills with zero configuration.',
    },
    'what-people-are-saying': {
        "description": '> *"A database of real, organized security skills that any AI agent can plug into and use.',
        "guidance": '> *"A database of real, organized security skills that any AI agent can plug into and use. Not tutorials. Not blog posts."* \n> — **[Hasan Toor (@hasantoxr)](https://x.com/hasantoxr/status/2033193922349179249)**, AI/tech creator\n\n> *"This is not a random collection of security scripts. It\'s a structured operational knowledge base designed for AI-driven security workflows."* \n> — **[fazal-sec](https://fazal-sec.medium.com/claude-skills-ai-powered-cybersecurity-the-complete-guide-to-building-intelligent-security-7bb7e9d14c8e)**,  Medium',
    },
    'featured-in': {
        "description": '| Where | Type | Link |\n|---|---|---|\n| **awesome-agent-skills** | Awesome List (1,000+ skills index) | [VoltAgent/awesome-agent-skills](https://github.',
        "guidance": '| Where | Type | Link |\n|---|---|---|\n| **awesome-agent-skills** | Awesome List (1,000+ skills index) | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) |\n| **awesome-ai-security** | Awesome List (AI security tools) | [ottosulin/awesome-ai-security](https://github.com/ottosulin/awesome-ai-security) |\n| **awesome-codex-cli** | Awesome List (Codex CLI resources) | [RoggeOhta/awesome-codex-cli](https://github.com/RoggeOhta/awesome-codex-cli) |\n| **SkillsLLM** | Skills directory & marketplace | [skillsllm.com/skill/anthropic-cybersecurity-skills](https://skillsllm.com/skill/anthropic-cybersecurity-skills) |\n| **Openflows** | Signal analysis & tracking | [openflows.org](https://openflows.org/currency/currents/anthropic-cybersecurity-skills/) |\n| **NeverSight skills_feed** | Automated skills index | [NeverSight/skills_feed](https://github.com/NeverSight/skills_feed) |',
    },
    'star-history': {
        "description": '<a href="https://star-history.',
        "guidance": '<a href="https://star-history.com/#mukul975/Anthropic-Cybersecurity-Skills&Date">\n <picture>\n   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=mukul975/Anthropic-Cybersecurity-Skills&type=Date&theme=dark" />\n   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=mukul975/Anthropic-Cybersecurity-Skills&type=Date" />\n   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=mukul975/Anthropic-Cybersecurity-Skills&type=Date" width="100%" />\n </picture>\n</a>',
    },
    'releases': {
        "description": '| Version | Date | Highlights |\n|---|---|---|\n| [v1.',
        "guidance": '| Version | Date | Highlights |\n|---|---|---|\n| [v1.0.0](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/releases/tag/v1.0.0) | March 11, 2026 | 734 skills · 26 domains · MITRE ATT&CK + NIST CSF 2.0 mapping · ATT&CK Navigator layer |\n\nSkills have continued to grow on `main` since v1.0.0 — the library now contains **754 skills** with **5-framework mapping**  (MITRE ATLAS, D3FEND, and NIST AI RMF added post-release).  Check [Releases](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/releases) for the latest tagged version.',
    },
    'contributing': {
        "description": 'This project grows through community contributions.',
        "guidance": 'This project grows through community contributions. Here is how to get involved:\n\n**Add a new skill** — Domains like Deception Technology (2 skills) and Compliance & Governance (5 skills) need the most help. Follow the template in [CONTRIBUTING.md](CONTRIBUTING.md) and submit a PR with the title `Add skill: your-skill-name`.\n\n**Improve existing skills** — Add framework mappings, fix workflows, update tool references, or contribute scripts and templates.\n\n**Report issues** — Found an inaccurate procedure or broken script? [Open an issue](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/issues).\n\nEvery PR is reviewed for technical accuracy and agentskills.io standard compliance within 48 hours.  Check [good first issues](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) for a starting point.\n\nThis project follows the [Contributor Covenant](https://www.contributor-covenant.org/). By participating, you agree to uphold this code.',
    },
    'community': {
        "description": '💬 [Discussions](https://github.',
        "guidance": '💬 [Discussions](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/discussions) — Questions, ideas, and roadmap conversations\n🐛 [Issues](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/issues) — Bug reports and feature requests\n🔒 [Security Policy](SECURITY.md) — Responsible disclosure process (48-hour acknowledgment)',
    },
    'citation': {
        "description": 'If you use this project in research or publications:\n\n```bibtex\n@software{anthropic_cybersecurity_skills,\n  author       = {Jangra, Mahipal},\n  title        = {Anthropic Cybersecurity Skills},\n  year ',
        "guidance": 'If you use this project in research or publications:\n\n```bibtex\n@software{anthropic_cybersecurity_skills,\n  author       = {Jangra, Mahipal},\n  title        = {Anthropic Cybersecurity Skills},\n  year         = {2026},\n  url          = {https://github.com/mukul975/Anthropic-Cybersecurity-Skills},\n  license      = {Apache-2.0},\n  note         = {754 structured cybersecurity skills for AI agents,\n                  mapped to MITRE ATT\\&CK, NIST CSF 2.0, MITRE ATLAS,\n                  MITRE D3FEND, and NIST AI RMF}\n}\n```',
    },
    'license': {
        "description": 'This project is licensed under the [Apache License 2.',
        "guidance": 'This project is licensed under the [Apache License 2.0](LICENSE). You are free to use, modify, and distribute these skills in both personal and commercial projects. \n\n---\n\n<div align="center">\n\n**If this project helps your security work, consider giving it a ⭐**\n\n[⭐ Star](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/stargazers) · [🍴 Fork](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/fork) · [💬 Discuss](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/discussions) · [📝 Contribute](CONTRIBUTING.md)\n\nCommunity project by [@mukul975](https://github.com/mukul975). Not affiliated with Anthropic PBC.\n\n</div>',
    },
}


@mcp.tool()
def list_anthropic_cybersecurity_skills_skills() -> dict:
    """List all available anthropic_cybersecurity_skills skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_anthropic_cybersecurity_skills_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific anthropic_cybersecurity_skills skill."""
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
    hint = get_presentation_hint('anthropic_cybersecurity_skills', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@anthropic_cybersecurity_skills",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'anthropic_cybersecurity_skills',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
