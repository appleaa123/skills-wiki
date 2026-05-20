import { NextRequest, NextResponse } from "next/server"
import fs from "fs"
import path from "path"

export async function GET(req: NextRequest) {
  const skill = req.nextUrl.searchParams.get("skill") ?? ""
  if (!skill || !/^[a-z0-9_]+$/.test(skill)) {
    return NextResponse.json({ tools: {} })
  }

  const skillDir = path.join(process.cwd(), "..", "skills_library", skill)

  // Primary: parse _SKILLS-style dict from main.py
  try {
    const src = fs.readFileSync(path.join(skillDir, "main.py"), "utf-8")
    const tools = parseSkills(src)
    if (Object.keys(tools).length > 0) {
      return NextResponse.json({ tools })
    }
  } catch {
    // fall through
  }

  // Fallback: use skill_meta.json description as single entry
  try {
    const meta = JSON.parse(fs.readFileSync(path.join(skillDir, "skill_meta.json"), "utf-8")) as { description?: string }
    if (meta.description) {
      return NextResponse.json({ tools: { [skill]: meta.description } })
    }
  } catch {
    // fall through
  }

  return NextResponse.json({ tools: {} })
}

function parseSkills(src: string): Record<string, string> {
  const tools: Record<string, string> = {}
  // Matches both 'slug': and "slug": dict keys with a "description" field
  const re =
    /(?:'([^']+)'|"([^"]+)"):\s*\{[^}]*?"description":\s*(?:'((?:[^'\\]|\\.)*)'|"((?:[^"\\]|\\.)*)")/g
  let m: RegExpExecArray | null
  while ((m = re.exec(src)) !== null) {
    const slug = m[1] ?? m[2] ?? ""
    const desc = m[3] ?? m[4] ?? ""
    if (slug) tools[slug] = desc
  }
  return tools
}
