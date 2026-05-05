"""Skill: resume_skills."""

from fastmcp import FastMCP
from core.skill_config import get_presentation_hint

mcp = FastMCP("resume-skills")


_SKILLS: dict[str, dict] = {
    'what-are-skills': {
        "description": 'Skills are markdown files that give AI agents specialized knowledge and workflows for specific tasks.',
        "guidance": "Skills are markdown files that give AI agents specialized knowledge and workflows for specific tasks. When you add these to your project, Claude Code can recognize when you're working on resume and job search tasks and apply the right frameworks and best practices.",
    },
    'available-skills': {
        "description": '| Skill | Description |\n|-------|-------------|\n| [resume-ats-optimizer](/skills/resume-ats-optimizer) | Optimize resumes for Applicant Tracking Systems, check ATS compatibility, analyze keyword match',
        "guidance": '| Skill | Description |\n|-------|-------------|\n| [resume-ats-optimizer](/skills/resume-ats-optimizer) | Optimize resumes for Applicant Tracking Systems, check ATS compatibility, analyze keyword match |\n| [resume-bullet-writer](/skills/resume-bullet-writer) | Transform weak bullets into achievement-focused statements with metrics and impact |\n| [job-description-analyzer](/skills/job-description-analyzer) | Analyze job postings, calculate match scores, identify gaps, create application strategy |\n| [resume-tailor](/skills/resume-tailor) | Customize resume for specific job postings while maintaining truthfulness |\n| [cover-letter-generator](/skills/cover-letter-generator) | Create personalized, compelling cover letters from resume + job description |\n| [linkedin-profile-optimizer](/skills/linkedin-profile-optimizer) | Sync resume with LinkedIn, optimize for searchability and engagement |\n| [interview-prep-generator](/skills/interview-prep-generator) | Generate STAR stories, practice questions, talking points from resume |\n| [salary-negotiation-prep](/skills/salary-negotiation-prep) | Research market rates, build negotiation strategy, create counter-offer scripts |\n| [tech-resume-optimizer](/skills/tech-resume-optimizer) | Optimize resumes for software engineering, PM, and technical roles |\n| [executive-resume-writer](/skills/executive-resume-writer) | Create C-suite and VP level resumes emphasizing strategic leadership |\n| [career-changer-translator](/skills/career-changer-translator) | Translate skills from one industry to another, identify transferable skills |\n| [resume-quantifier](/skills/resume-quantifier) | Find opportunities to add metrics, estimate when numbers unknown |\n| [resume-formatter](/skills/resume-formatter) | Ensure ATS-friendly formatting, create clean scannable layouts |\n| [portfolio-case-study-writer](/skills/portfolio-case-study-writer) | Transform resume bullets into detailed portfolio case studies |\n| [academic-cv-builder](/skills/academic-cv-builder) | Format CVs for academic positions with publications, grants, teaching |\n| [reference-list-builder](/skills/reference-list-builder) | Format professional references properly and prepare reference materials |\n| [offer-comparison-analyzer](/skills/offer-comparison-analyzer) | Compare multiple job offers side-by-side with total compensation analysis |\n| [resume-version-manager](/skills/resume-version-manager) | Track different resume versions, maintain master resume, manage tailored versions |\n| [creative-portfolio-resume](/skills/creative-portfolio-resume) | Balance visual design with ATS compatibility for creative roles |\n| [resume-section-builder](/skills/resume-section-builder) | Create targeted sections optimized for different experience levels and roles |',
    },
    'installation': {
        "description": '### Option 1: CLI Install (Recommended)\n\n```bash\n# Install all 20 skills globally (works across all projects)\nnpx skills add Paramchoudhary/ResumeSkills -g -y\n\n# Install to current project only\nnpx sk',
        "guidance": "### Option 1: CLI Install (Recommended)\n\n```bash\n# Install all 20 skills globally (works across all projects)\nnpx skills add Paramchoudhary/ResumeSkills -g -y\n\n# Install to current project only\nnpx skills add Paramchoudhary/ResumeSkills -y\n\n# List installed skills\nnpx skills list\n\n# List global skills\nnpx skills list --global\n```\n\n### Option 2: Manual Install\n\n```bash\n# Clone and copy to skills folder\ngit clone https://github.com/Paramchoudhary/ResumeSkills.git\nmkdir -p ~/.cursor/skills\ncp -r ResumeSkills/skills/* ~/.cursor/skills/\n```\n\n### Option 3: Direct Download\n\nDownload individual skill files from the `/skills` directory and add them to your AI agent's skills folder.\n\n### Uninstall\n\n```bash\n# Remove individual skills by name\nnpx skills remove resume-ats-optimizer\nnpx skills remove resume-bullet-writer\n\n# Or remove all skills from a directory\nrm -rf ~/.agents/skills/resume-*\nrm -rf ~/.cursor/skills/resume-*\n```",
    },
    'supported-ai-agents': {
        "description": 'These skills work with multiple AI coding assistants:\n\n- **Cursor** (IDE)\n- **Claude Code** (CLI)\n- **Windsurf**\n- **Codex**\n- **Gemini CLI**\n- **Amp, Antigravity, Augment** and 30+ more.',
        "guidance": 'These skills work with multiple AI coding assistants:\n\n- **Cursor** (IDE)\n- **Claude Code** (CLI)\n- **Windsurf**\n- **Codex**\n- **Gemini CLI**\n- **Amp, Antigravity, Augment** and 30+ more',
    },
    'usage': {
        "description": 'Once installed, just ask your AI assistant to help with resume tasks:\n\n```\n"Optimize my resume for ATS"\n→ Uses resume-ats-optimizer skill\n\n"Improve my resume bullets"\n→ Uses resume-bullet-writer skill',
        "guidance": 'Once installed, just ask your AI assistant to help with resume tasks:\n\n```\n"Optimize my resume for ATS"\n→ Uses resume-ats-optimizer skill\n\n"Improve my resume bullets"\n→ Uses resume-bullet-writer skill\n\n"Should I apply to this job?" + paste job description\n→ Uses job-description-analyzer skill\n\n"Write me a cover letter for this role"\n→ Uses cover-letter-generator skill\n\n"Prep me for an interview at Google"\n→ Uses interview-prep-generator skill\n```',
    },
    'skill-categories': {
        "description": '### Resume Optimization\n- `resume-ats-optimizer` - Pass ATS systems\n- `resume-bullet-writer` - Write achievement-focused bullets\n- `resume-quantifier` - Add metrics and numbers\n- `resume-formatter` - ',
        "guidance": '### Resume Optimization\n- `resume-ats-optimizer` - Pass ATS systems\n- `resume-bullet-writer` - Write achievement-focused bullets\n- `resume-quantifier` - Add metrics and numbers\n- `resume-formatter` - Clean, scannable formatting\n- `resume-section-builder` - Targeted section creation\n\n### Job Search Strategy\n- `job-description-analyzer` - Match analysis and strategy\n- `resume-tailor` - Customize for specific jobs\n- `resume-version-manager` - Track multiple versions\n- `offer-comparison-analyzer` - Compare job offers\n\n### Supporting Documents\n- `cover-letter-generator` - Personalized cover letters\n- `linkedin-profile-optimizer` - LinkedIn optimization\n- `portfolio-case-study-writer` - Portfolio content\n- `reference-list-builder` - Professional references\n\n### Interview & Negotiation\n- `interview-prep-generator` - STAR stories and practice\n- `salary-negotiation-prep` - Negotiation strategy\n\n### Specialized Roles\n- `tech-resume-optimizer` - Engineering/PM/technical\n- `executive-resume-writer` - C-suite/VP\n- `academic-cv-builder` - Academic positions\n- `creative-portfolio-resume` - Design/creative roles\n- `career-changer-translator` - Career transitions',
    },
    'why-these-skills-matter': {
        "description": '**The Problem:**\n- 75% of resumes rejected by ATS before humans see them\n- Average job gets 250 applications\n- Most resumes have weak bullets with no metrics\n- Job seekers apply to wrong jobs, waste t',
        "guidance": '**The Problem:**\n- 75% of resumes rejected by ATS before humans see them\n- Average job gets 250 applications\n- Most resumes have weak bullets with no metrics\n- Job seekers apply to wrong jobs, waste time\n\n**The Solution:**\n- Pass ATS with optimized formatting and keywords\n- Stand out with achievement-focused bullets\n- Apply strategically to right-fit roles\n- Get interviews faster with tailored applications\n\n**The Results:**\n- 2-3x more interviews per application\n- Higher quality responses\n- Faster job search (2 months saved on average)\n- Better salary negotiations ($10K+ higher offers)',
    },
    'quick-start-examples': {
        "description": "### Example 1: Full Resume Optimization\n\n```\nUser: Here's my resume [paste].",
        "guidance": "### Example 1: Full Resume Optimization\n\n```\nUser: Here's my resume [paste]. I'm applying to data scientist roles. Help me optimize it.\n\nClaude will:\n1. Run ATS compatibility check\n2. Analyze against common data scientist job requirements\n3. Improve bullet points with metrics\n4. Suggest keyword additions\n5. Format for ATS compatibility\n```\n\n### Example 2: Job-Specific Tailoring\n\n```\nUser: Here's a job description [paste] and my resume [paste]. Should I apply?\n\nClaude will:\n1. Calculate match score\n2. Identify gaps and strengths\n3. Flag any red flags in posting\n4. Provide resume customization strategy\n5. Generate cover letter talking points\n```\n\n### Example 3: Interview Preparation\n\n```\nUser: I have an interview at [Company] for [Role]. Here's my resume. Help me prepare.\n\nClaude will:\n1. Generate STAR stories from your experience\n2. Predict likely interview questions\n3. Create talking points for each bullet\n4. Research company-specific prep\n5. Prepare questions to ask\n```",
    },
    'contributing': {
        "description": 'Found a way to improve a skill? Have a new skill to suggest? PRs and issues welcome!\n\nSee [CONTRIBUTING.',
        "guidance": 'Found a way to improve a skill? Have a new skill to suggest? PRs and issues welcome!\n\nSee [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.\n\n### Ways to Contribute\n- Improve existing skill instructions\n- Add industry-specific examples\n- Create new skills for specialized use cases\n- Fix typos or clarify language\n- Add translations',
    },
    'license': {
        "description": 'MIT License - Use these skills however you want.',
        "guidance": 'MIT License - Use these skills however you want.\n\nSee [LICENSE](LICENSE) for details.',
    },
    'about': {
        "description": 'Resume skills for Claude Code.',
        "guidance": 'Resume skills for Claude Code. ATS optimization, bullet writing, job matching, interview prep, and career development.\n\n**Keywords:** resume, CV, ATS, job search, career, interview, cover letter, LinkedIn, salary negotiation, job application\n\n---\n\n*Built with care for job seekers everywhere. Good luck with your search!*',
    },
}


@mcp.tool()
def list_resume_skills_skills() -> dict:
    """List all available resume_skills skills."""
    return {k: v["description"] for k, v in _SKILLS.items()}


@mcp.tool()
def get_resume_skills_skill(skill_name: str = None) -> dict:
    """Get full guidance for a specific resume_skills skill."""
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
    hint = get_presentation_hint('resume_skills', client_id=client_id)
    if hint:
        skill_data = {**skill_data, "_presentation_hint": hint}
    return {
        "id": f"{skill_name}@resume_skills",
        "skill_name": skill_name,
        "status": skill_data.get("status", "production"),
        "metadata": {
            "folder": 'resume_skills',
            "client_id": client_id,
            "source": "community-library"
        },
        "interface": {
            "commands": [f"/{skill_name}"]
        },
        "content": skill_data
    }
