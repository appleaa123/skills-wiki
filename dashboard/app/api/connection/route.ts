import { NextResponse } from "next/server"
import { writeLocalConfig } from "@/lib/local-db"

// DELETE /api/connection  — full reset: clears all local config
export async function DELETE() {
  try {
    writeLocalConfig({ client_id: "", api_key: "", enabled_skills: [], skill_configs: {}, connections: {} })
    return NextResponse.json({ ok: true })
  } catch (err: unknown) {
    return NextResponse.json({ error: err instanceof Error ? err.message : "Internal error" }, { status: 500 })
  }
}
