import { NextRequest, NextResponse } from "next/server"
import { readLocalConfig, writeLocalConfig } from "@/lib/local-db"

interface SkillConfig {
  tone?: "formal" | "casual" | "technical"
  format?: "prose" | "bullets" | "table"
  language?: string
  response_length?: "brief" | "standard" | "detailed"
  custom_instructions?: string
}

// GET /api/config?skill=amazon_skills  — returns config for one skill
// GET /api/config                       — returns all configs
export async function GET(req: NextRequest) {
  try {
    const config = readLocalConfig()
    const skill = req.nextUrl.searchParams.get("skill")
    if (skill) {
      return NextResponse.json({
        skill,
        config: config.skill_configs[skill] ?? {},
        updated_at: null,
      })
    }
    const configs = Object.entries(config.skill_configs).map(([s, c]) => ({
      skill: s,
      config: c,
      updated_at: null,
    }))
    return NextResponse.json({ configs })
  } catch (err: unknown) {
    return NextResponse.json({ error: err instanceof Error ? err.message : "Internal error" }, { status: 500 })
  }
}

// POST /api/config  body: { skill: string, config: SkillConfig }
export async function POST(req: NextRequest) {
  try {
    const body = await req.json() as { skill?: string; config?: SkillConfig }
    if (!body.skill || typeof body.config !== "object") {
      return NextResponse.json({ error: "skill and config are required" }, { status: 400 })
    }
    const data = readLocalConfig()
    data.skill_configs[body.skill] = body.config as Record<string, string>
    writeLocalConfig(data)
    return NextResponse.json({ ok: true })
  } catch (err: unknown) {
    return NextResponse.json({ error: err instanceof Error ? err.message : "Internal error" }, { status: 500 })
  }
}

// DELETE /api/config?skill=amazon_skills  — resets a skill to defaults
export async function DELETE(req: NextRequest) {
  try {
    const skill = req.nextUrl.searchParams.get("skill")
    if (!skill) return NextResponse.json({ error: "skill param required" }, { status: 400 })
    const data = readLocalConfig()
    delete data.skill_configs[skill]
    writeLocalConfig(data)
    return NextResponse.json({ ok: true })
  } catch (err: unknown) {
    return NextResponse.json({ error: err instanceof Error ? err.message : "Internal error" }, { status: 500 })
  }
}
