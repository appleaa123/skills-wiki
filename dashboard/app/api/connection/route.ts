import { NextResponse } from "next/server";
import { loadDb, saveDb, getLocalAdminId, LocalDb } from "@/lib/local-db";

// DELETE /api/connection  — full reset: removes client row + all associated data
export async function DELETE() {
  try {
    const clientId = getLocalAdminId();
    const db = loadDb();

    db.clients = db.clients.filter(c => c.client_id !== clientId);
    db.client_skill_configs = db.client_skill_configs.filter(c => c.client_id !== clientId);
    db.client_service_credentials = db.client_service_credentials.filter(c => c.client_id !== clientId);
    // also clean feedback/audit if needed, but they don't block anything
    
    saveDb(db);

    return NextResponse.json({ ok: true });
  } catch (err: unknown) {
    return NextResponse.json({ error: err instanceof Error ? err.message : "Internal error" }, { status: 500 });
  }
}
