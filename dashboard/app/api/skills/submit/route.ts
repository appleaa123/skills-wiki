import { NextRequest, NextResponse } from "next/server"
import { execFile } from "child_process"
import { promisify } from "util"
import path from "path"
import { readLocalConfig, writeLocalConfig } from "@/lib/local-db"

const execFileAsync = promisify(execFile)

const REPO_URL_RE = /^https:\/\/github\.com\/[^/]+\/[^/]+/
const SKILL_NAME_RE = /^[a-z][a-z0-9_]{1,39}$/

export async function POST(req: NextRequest) {
  try {
    const { repoUrl, skillName } = await req.json() as {
      repoUrl?: string
      skillName?: string
    }

    if (!repoUrl || !REPO_URL_RE.test(repoUrl)) {
      return NextResponse.json({ error: "repoUrl must be a valid https://github.com/org/repo URL" }, { status: 400 })
    }
    if (!skillName || !SKILL_NAME_RE.test(skillName)) {
      return NextResponse.json({ error: "skillName must be snake_case, 2–40 chars, starting with a letter" }, { status: 400 })
    }

    const repoRoot = path.join(process.cwd(), "..")
    const addSkillScript = path.join(repoRoot, "scripts", "add_skill.py")

    try {
      await execFileAsync("python", [addSkillScript, "--url", repoUrl, "--name", skillName, "--llm"], {
        cwd: repoRoot,
        timeout: 120000,
      })
    } catch (scriptErr) {
      console.error("add_skill.py failed:", scriptErr)
      return NextResponse.json({ error: "Failed to install skill from GitHub. Check the repo URL and try again." }, { status: 500 })
    }

    // Add to enabled_skills
    const config = readLocalConfig()
    if (!config.enabled_skills.includes(skillName)) {
      writeLocalConfig({ ...config, enabled_skills: [...config.enabled_skills, skillName] })
    }

    return NextResponse.json({ ok: true, skillName }, { status: 201 })
  } catch (err: unknown) {
    return NextResponse.json({ error: err instanceof Error ? err.message : "Internal error" }, { status: 500 })
  }
}
