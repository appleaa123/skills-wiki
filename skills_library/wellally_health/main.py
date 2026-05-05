"""Skill: wellally_health."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("wellally-health")


_SKILLS: dict[str, dict] = {
    'project-developer': {
        "description": 'This project is developed and maintained by [WellAlly Tech](https://www.',
        "guidance": 'This project is developed and maintained by [WellAlly Tech](https://www.wellally.tech/).',
    },
    'system-features': {
        "description": '- 📁 Pure file-based storage, no database required\n- 🖼️ Intelligent medical report image recognition\n- 📊 Automatic biochemical test data and reference range extraction\n- 🔍 Structured medical imaging da',
        "guidance": '- 📁 Pure file-based storage, no database required\n- 🖼️ Intelligent medical report image recognition\n- 📊 Automatic biochemical test data and reference range extraction\n- 🔍 Structured medical imaging data extraction\n- 🔪 Surgical history and implant management\n- 📋 Structured discharge summary storage\n- 👨\u200d⚕️ Multi-Disciplinary Team (MDT) consultation system\n- 🔬 13 medical specialist intelligent analysis\n- ☢️ Medical radiation dose tracking and management\n- 💊 **Intelligent drug interaction detection** (New)\n- 🚨 **Five-level severity warning system** (A/B/C/D/X)\n- 👤 User basic profile management\n- 💾 Local storage, completely private data\n- 🚀 Claude Code command operations, no programming required',
    },
    'directory-structure': {
        "description": '```\nmy-his/\n├──.',
        "guidance": '```\nmy-his/\n├── .claude/\n│   ├── commands/\n│   │   ├── save-report.md    # Save medical report command\n│   │   ├── query.md          # Query records command\n│   │   ├── profile.md        # User profile settings command\n│   │   ├── radiation.md      # Radiation exposure management command\n│   │   ├── surgery.md        # Surgery history record command\n│   │   ├── discharge.md      # Discharge summary management command\n│   │   ├── medication.md     # Medication record management command\n│   │   ├── interaction.md    # Drug interaction detection command\n│   │   ├── consult.md        # Multi-disciplinary consultation command\n│   │   └── specialist.md     # Single specialist consultation command\n│   └── specialists/\n│       ├── cardiology.md            # Cardiology specialist Skill\n│       ├── endocrinology.md         # Endocrinology specialist Skill\n│       ├── gastroenterology.md      # Gastroenterology specialist Skill\n│       ├── nephrology.md            # Nephrology specialist Skill\n│       ├── hematology.md            # Hematology specialist Skill\n│       ├── respiratory.md           # Respiratory medicine specialist Skill\n│       ├── neurology.md             # Neurology specialist Skill\n│       ├── oncology.md              # Oncology specialist Skill\n│       ├── general.md               # General practice specialist Skill\n│       └── consultation-coordinator.md # Consultation coordinator\n├── data/\n│   ├── profile.json          # User basic profile\n│   ├── radiation-records.json # Radiation exposure records\n│   ├── allergies.json        # Allergy history records\n│   ├── interactions/         # Drug interaction database\n│   │   ├── interaction-db.json      # Interaction rules main database\n│   │   └── interaction-logs/        # Check history records\n│   ├── medications/          # Medication record data\n│   ├── 生化检查/             # Biochemical test data\n│   │   └── YYYY-MM/\n│   │       └── YYYY-MM-DD_test_name.json\n│   ├── 影像检查/             # Medical imaging data\n│   │   └── YYYY-MM/\n│   │       ├── YYYY-MM-DD_test_name_body_part.json\n│   │       └── images/       # Original image backup\n│   ├── 手术记录/             # Surgery history data\n│   │   └── YYYY-MM/\n│   │       └── YYYY-MM-DD_surgery_name.json\n│   ├── 出院小结/             # Discharge summary data\n│   │   └── YYYY-MM/\n│   │       └── YYYY-MM-DD_main_diagnosis.json\n│   └── index.json            # Global index file\n└── README.md\n```',
    },
    'quick-navigation': {
        "description": '- 📖 [Complete User Guide](docs/user-guide.',
        "guidance": '- 📖 [Complete User Guide](docs/user-guide.md) (Chinese) | [docs/user-guide.en.md](docs/user-guide.en.md) (English) - Detailed command usage instructions and examples\n- 📋 [Data Structure Specification](docs/data-structures.md) (Chinese) | [docs/data-structures.en.md](docs/data-structures.en.md) (English) - JSON data format and field descriptions\n- 🔧 [Technical Implementation Details](docs/technical-details.md) (Chinese) - System architecture and technical details\n- ⚠️ [Safety Guidelines and Usage Limitations](docs/safety-guidelines.md) (Chinese) - Safety principles and disclaimer',
    },
    'quick-start': {
        "description": '1.',
        "guidance": '1. Ensure Claude Code is installed\n2. Open Claude Code in the current directory\n3. First-time setup: `/profile set 175 70 1990-01-01`\n4. Save first report: `/save-report /path/to/image.jpg`\n5. Record radiation: `/radiation add CT chest`\n6. Record surgery: `/surgery Gallbladder removal surgery in August last year due to gallstones`\n7. Save discharge summary: `/discharge @医疗报告/出院小结.jpg`\n8. Query all records: `/query all`\n9. Start MDT consultation: `/consult`',
    },
    'data-privacy': {
        "description": '- All data stored on local filesystem\n- No uploads to any cloud services\n- No external database dependencies\n- Completely private management.',
        "guidance": '- All data stored on local filesystem\n- No uploads to any cloud services\n- No external database dependencies\n- Completely private management',
    },
    'core-commands-overview': {
        "description": '| Command | Function | Description |\n|---------|----------|-------------|\n| `/profile` | User basic parameters | Set height, weight, birth date |\n| `/save-report` | Save medical report | Support bioch',
        "guidance": '| Command | Function | Description |\n|---------|----------|-------------|\n| `/profile` | User basic parameters | Set height, weight, birth date |\n| `/save-report` | Save medical report | Support biochemical and imaging tests |\n| `/radiation` | Radiation management | Record and track radiation exposure |\n| `/surgery` | Surgery history | Record surgery information and implants |\n| `/discharge` | Discharge summary | Save and structure discharge summaries |\n| `/medication` | Medication management | Manage medication plans and records |\n| `/interaction` | Interaction detection | Detect drug interactions |\n| `/allergy` | Allergy history management | Record and manage allergy history |\n| `/query` | Query records | Multi-condition medical data queries |\n| `/consult` | Multi-disciplinary consultation | Comprehensive analysis across 13 specialties |\n| `/specialist` | Single specialist consultation | Consult specific specialty experts |\n\n> 💡 For detailed usage, refer to [Complete User Guide](docs/user-guide.en.md)',
    },
    'technical-features': {
        "description": '- **Storage Method**: JSON files + filesystem directory structure\n- **Command System**: Claude Code Slash Commands\n- **Expert System**: Multi-specialty Skill definitions + Subagent architecture\n- **Co',
        "guidance": '- **Storage Method**: JSON files + filesystem directory structure\n- **Command System**: Claude Code Slash Commands\n- **Expert System**: Multi-specialty Skill definitions + Subagent architecture\n- **Consultation Coordination**: Parallel processing + opinion integration algorithms\n- **Image Recognition**: AI visual analysis\n- **Data Extraction**: Intelligent text recognition and structuring\n- **Radiation Calculation**: Body surface area adjustment + exponential decay model\n\n> 🔧 For more technical details, refer to [Technical Implementation Details](docs/technical-details.md) (Chinese)',
    },
    'important-safety-statement': {
        "description": 'This system strictly follows medical safety principles:\n\n1.',
        "guidance": 'This system strictly follows medical safety principles:\n\n1. **Does not provide specific medication dosages**\n2. **Does not directly prescribe prescription drugs**\n3. **Does not predict life prognosis**\n4. **Does not replace doctor diagnosis**\n\nAll analysis reports from this system are for reference only and should not be used as a basis for medical diagnosis. All medical decisions require consultation with professional doctors. In case of emergency, seek immediate medical attention.\n\n> ⚠️ For complete safety principles and usage limitations, refer to [Safety Guidelines Document](docs/safety-guidelines.md) (Chinese)',
    },
    'drug-interaction-database': {
        "description": 'The system includes intelligent drug interaction detection, supporting drug-drug, drug-disease, drug-dose, and drug-food interaction detection using a five-level severity classification system (A/B/C/',
        "guidance": 'The system includes intelligent drug interaction detection, supporting drug-drug, drug-disease, drug-dose, and drug-food interaction detection using a five-level severity classification system (A/B/C/D/X).\n\n**Core Features:**\n- 🔍 Automatically detect interactions in current medication combinations\n- 🚨 Severity-graded warnings (A/B/C/D/X)\n- 📋 Provide detailed management recommendations and monitoring indicators\n- 💾 Support custom rules and history records\n\n**Quick Start:**\n```bash\n# Check interactions for current medications\n/interaction check\n\n# List all interaction rules\n/interaction list\n\n# View absolute contraindication rules\n/interaction list X\n```\n\n> 📖 **Detailed Documentation**: [Drug Interaction Database Complete Guide](docs/drug-interaction-database.md) (Chinese)\n>\n> 🩺 **Professional Contributions**: Medical professionals are welcome to help improve the database → [Contribution Guidelines](docs/drug-interaction-database.md#专业人员贡献指南-) (Chinese)',
    },
    'license': {
        "description": 'This project is open-sourced under the [MIT License](LICENSE).',
        "guidance": 'This project is open-sourced under the [MIT License](LICENSE).\n\n**Important Disclaimer**: This system is for personal health management only and should not be used as a basis for medical diagnosis.',
    },
}


@mcp.tool()
def list_wellally_health_skills() -> dict:
    """List all available wellally_health skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_wellally_health_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific wellally_health skill."""
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
    hint = get_presentation_hint('wellally_health', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@wellally_health",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'wellally_health',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
