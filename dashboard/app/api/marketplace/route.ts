import { NextRequest, NextResponse } from "next/server"
import { allSkills, THEMES } from "@/lib/skills"

export async function GET(_req: NextRequest) {
  try {
    const skills = allSkills()
    const themes = THEMES.map((t) => ({ slug: t.slug, name: t.name }))
    return NextResponse.json(
      { data: skills, themes, count: skills.length },
      { headers: { "Cache-Control": "public, max-age=60" } }
    )
  } catch (err: unknown) {
    return NextResponse.json({ error: err instanceof Error ? err.message : "Internal error" }, { status: 500 })
  }
}
