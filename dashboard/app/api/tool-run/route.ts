import { NextRequest, NextResponse } from "next/server"
import fs from "fs"
import path from "path"

const MCP_BASE = process.env.NEXT_PUBLIC_GATEWAY_BASE_URL ?? "http://localhost:8000"

export async function POST(req: NextRequest) {
  try {
    const body = await req.json() as { skill?: unknown; tool?: unknown; args?: unknown }
    const skill = typeof body?.skill === "string" ? body.skill : ""
    const tool = typeof body?.tool === "string" ? body.tool : ""
    const args = (body?.args && typeof body.args === "object" && !Array.isArray(body.args))
      ? body.args as Record<string, unknown>
      : {}

    if (!skill || !tool) {
      return NextResponse.json({ error: "skill and tool are required" }, { status: 400 })
    }

    // Stage 1: try calling the local MCP server
    const mcpResult = await tryMcpCall(skill, tool, args)
    if (mcpResult !== null) {
      return NextResponse.json({ result: mcpResult })
    }

    // Stage 2: parse guidance from main.py on filesystem
    const fsResult = parseGuidanceFromFile(skill, args.skill_name as string | undefined)
    if (fsResult !== null) {
      return NextResponse.json({ result: fsResult })
    }

    // Stage 3: fall back to skill_meta description
    const metaResult = readSkillMetaDescription(skill)
    if (metaResult !== null) {
      return NextResponse.json({ result: metaResult })
    }

    return NextResponse.json({ error: "No result available — ensure the Python server is running" }, { status: 502 })
  } catch (err: unknown) {
    return NextResponse.json({ error: err instanceof Error ? err.message : "Internal error" }, { status: 500 })
  }
}

async function tryMcpCall(
  skill: string,
  tool: string,
  args: Record<string, unknown>
): Promise<string | null> {
  try {
    const toolName = `${skill}_${tool}`
    const controller = new AbortController()
    const timeout = setTimeout(() => controller.abort(), 5000)

    const resp = await fetch(`${MCP_BASE}/mcp`, {
      method: "POST",
      headers: { "Content-Type": "application/json", "Accept": "application/json, text/event-stream" },
      body: JSON.stringify({
        jsonrpc: "2.0",
        id: 1,
        method: "tools/call",
        params: { name: toolName, arguments: args },
      }),
      signal: controller.signal,
    })
    clearTimeout(timeout)

    if (!resp.ok) return null

    const text = await resp.text()
    // Handle SSE response: find the JSON data line
    if (text.includes("data:")) {
      for (const line of text.split("\n")) {
        if (line.startsWith("data:")) {
          try {
            const data = JSON.parse(line.slice(5).trim()) as { result?: { content?: Array<{ text?: string }> } }
            const content = data?.result?.content
            if (Array.isArray(content) && content[0]?.text) return content[0].text
          } catch { continue }
        }
      }
      return null
    }

    // Handle plain JSON response
    try {
      const data = JSON.parse(text) as { result?: { content?: Array<{ text?: string }> } }
      const content = data?.result?.content
      if (Array.isArray(content) && content[0]?.text) return content[0].text
    } catch { /* ignore */ }

    return null
  } catch {
    return null
  }
}

function parseGuidanceFromFile(skill: string, skillName: string | undefined): string | null {
  if (!skillName) return null
  try {
    const src = fs.readFileSync(
      path.join(process.cwd(), "..", "skills_library", skill, "main.py"),
      "utf-8"
    )

    // Match: 'skill-name': { ... "guidance": """...""" ... }
    // Also handles single-quoted guidance values
    const escapedName = skillName.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")
    const blockRe = new RegExp(
      `(?:'${escapedName}'|"${escapedName}")\\s*:\\s*\\{([\\s\\S]*?)\\}(?=\\s*[,}])`,
    )
    const blockMatch = blockRe.exec(src)
    if (!blockMatch) return null

    const block = blockMatch[1]

    // Extract guidance value — handles triple-quoted and regular strings
    const tripleDoubleMatch = /["\s]guidance["']?\s*:\s*"""([\s\S]*?)"""/.exec(block)
    if (tripleDoubleMatch) return tripleDoubleMatch[1].trim()

    const tripleSingleMatch = /["\s]guidance["']?\s*:\s*'''([\s\S]*?)'''/.exec(block)
    if (tripleSingleMatch) return tripleSingleMatch[1].trim()

    const singleLineDouble = /guidance["']?\s*:\s*"((?:[^"\\]|\\.)*)"/.exec(block)
    if (singleLineDouble) return singleLineDouble[1]

    const singleLineSingle = /guidance["']?\s*:\s*'((?:[^'\\]|\\.)*)'/.exec(block)
    if (singleLineSingle) return singleLineSingle[1]

    // If no guidance, return description
    const descDouble = /description["']?\s*:\s*"((?:[^"\\]|\\.)*)"/.exec(block)
    if (descDouble) return descDouble[1]

    const descSingle = /description["']?\s*:\s*'((?:[^'\\]|\\.)*)'/.exec(block)
    if (descSingle) return descSingle[1]

    return null
  } catch {
    return null
  }
}

function readSkillMetaDescription(skill: string): string | null {
  try {
    const meta = JSON.parse(
      fs.readFileSync(
        path.join(process.cwd(), "..", "skills_library", skill, "skill_meta.json"),
        "utf-8"
      )
    ) as { description?: string; display_name?: string }
    if (meta.description) return meta.description
    return null
  } catch {
    return null
  }
}
