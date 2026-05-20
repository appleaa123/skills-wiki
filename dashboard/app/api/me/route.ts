import { NextResponse } from "next/server"
import { readLocalConfig } from "@/lib/local-db"
import { gatewayUrl } from "@/lib/utils"

export async function GET() {
  try {
    const config = readLocalConfig()
    return NextResponse.json({
      skills: config.enabled_skills,
      status: "live",
      claudeUrl: gatewayUrl("mcp"),
      chatgptUrl: gatewayUrl("openapi"),
      geminiUrl: gatewayUrl("mcp"),
    })
  } catch (err: unknown) {
    const message = err instanceof Error ? err.message : "Internal error"
    return NextResponse.json({ error: message }, { status: 500 })
  }
}
