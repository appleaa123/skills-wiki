import { NextResponse } from "next/server";
import { loadDb, getLocalAdminId } from "@/lib/local-db";

export async function GET() {
  try {
    const clientId = getLocalAdminId();
    const db = loadDb();
    
    let client = db.clients.find(c => c.client_id === clientId);
    if (!client) {
      client = { client_id: clientId, enabled_skills: [] };
    }

    // For local open-source, the Gateway URL is the local MCP server.
    const baseUrl = process.env.NEXT_PUBLIC_GATEWAY_BASE_URL || "http://localhost:8000";

    return NextResponse.json({
      clientId: client.client_id,
      skills: client.enabled_skills,
      status: "active",
      maskedApiKey: "sk-local-dev-key",
      claudeUrl: `${baseUrl}/sse`, // Example FastMCP SSE endpoint
      chatgptUrl: `${baseUrl}/openapi.json`,
      geminiUrl: `${baseUrl}/sse`,
    });
  } catch (err: unknown) {
    const message = err instanceof Error ? err.message : "Internal error";
    return NextResponse.json({ error: message }, { status: 500 });
  }
}
