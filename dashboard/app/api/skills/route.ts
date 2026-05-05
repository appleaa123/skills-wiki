import { NextRequest, NextResponse } from "next/server";
import { loadDb, saveDb, getLocalAdminId } from "@/lib/local-db";

// PATCH /api/skills  body: { skills: string[] }
export async function PATCH(req: NextRequest) {
  try {
    const body = await req.json() as { skills?: unknown };
    if (!Array.isArray(body.skills)) {
      return NextResponse.json({ error: "skills must be an array" }, { status: 400 });
    }

    const clientId = getLocalAdminId();
    const selected = (body.skills as string[]).filter((s) => typeof s === "string");
    const finalSkills = Array.from(new Set([...selected, "feedback_skill"]));

    const db = loadDb();
    
    // Find or create client
    let client = db.clients.find(c => c.client_id === clientId);
    if (!client) {
      client = { client_id: clientId, enabled_skills: [] };
      db.clients.push(client);
    }
    
    client.enabled_skills = finalSkills;
    saveDb(db);

    return NextResponse.json({ ok: true, skills: finalSkills });
  } catch (err: unknown) {
    return NextResponse.json({ error: err instanceof Error ? err.message : "Internal error" }, { status: 500 });
  }
}
