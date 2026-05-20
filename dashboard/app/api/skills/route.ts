import { NextRequest, NextResponse } from "next/server"
import { readLocalConfig, writeLocalConfig } from "@/lib/local-db"

// PATCH /api/skills  body: { skills: string[] }
export async function PATCH(req: NextRequest) {
  try {
    const body = await req.json() as { skills?: unknown }
    if (!Array.isArray(body.skills)) {
      return NextResponse.json({ error: "skills must be an array" }, { status: 400 })
    }

    const selected = (body.skills as string[]).filter((s) => typeof s === "string")
    const finalSkills = Array.from(new Set(selected))

    const config = readLocalConfig()
    writeLocalConfig({ ...config, enabled_skills: finalSkills })

    return NextResponse.json({ ok: true, skills: finalSkills })
  } catch (err: unknown) {
    return NextResponse.json({ error: err instanceof Error ? err.message : "Internal error" }, { status: 500 })
  }
}
