import { NextRequest, NextResponse } from "next/server";
import { SUPPORTED_SERVICES } from "@/lib/services";
import { loadDb, saveDb, getLocalAdminId } from "@/lib/local-db";

// GET /api/connections — list connected services (labels only, no credentials)
export async function GET(req: NextRequest) {
  void req;
  try {
    const clientId = getLocalAdminId();
    const db = loadDb();

    const credentials = db.client_service_credentials.filter(c => c.client_id === clientId).map(c => ({
      service: c.service,
      // Provide generic label if none saved
      label: c.service, 
      created_at: new Date().toISOString(),
      updated_at: new Date().toISOString()
    }));

    return NextResponse.json({ connections: credentials });
  } catch (err: unknown) {
    return NextResponse.json({ error: err instanceof Error ? err.message : JSON.stringify(err) }, { status: 500 });
  }
}

const CUSTOM_SERVICE_NAME_RE = /^[a-z0-9][a-z0-9-]{0,62}$/;

// POST /api/connections — add or update a credential
export async function POST(req: NextRequest) {
  try {
    const body = await req.json() as {
      service?: string;
      label?: string;
      is_custom?: boolean;
      credentials?: Record<string, string>;
    };

    if (!body.service || !body.label || typeof body.credentials !== "object") {
      return NextResponse.json({ error: "service, label, and credentials are required" }, { status: 400 });
    }

    if (body.is_custom || !SUPPORTED_SERVICES[body.service]) {
      if (!CUSTOM_SERVICE_NAME_RE.test(body.service)) {
        return NextResponse.json({ error: "Invalid service name" }, { status: 400 });
      }
      if (!body.credentials.url || !body.credentials.token) {
        return NextResponse.json({ error: "url and token required" }, { status: 400 });
      }
    }

    const clientId = getLocalAdminId();
    const db = loadDb();

    const existingIndex = db.client_service_credentials.findIndex(c => c.client_id === clientId && c.service === body.service);
    
    // For local open-source, we store credentials unencrypted in db.json for simplicity
    const newCred = {
      client_id: clientId,
      service: body.service,
      credentials: body.credentials as Record<string, unknown>
    };

    if (existingIndex >= 0) {
      db.client_service_credentials[existingIndex] = newCred;
    } else {
      db.client_service_credentials.push(newCred);
    }

    saveDb(db);
    return NextResponse.json({ ok: true, service: body.service });
  } catch (err: unknown) {
    const message = err instanceof Error ? err.message : JSON.stringify(err);
    return NextResponse.json({ error: message }, { status: 500 });
  }
}

// DELETE /api/connections?service=supabase
export async function DELETE(req: NextRequest) {
  try {
    const service = req.nextUrl.searchParams.get("service");
    if (!service) return NextResponse.json({ error: "service param required" }, { status: 400 });

    const clientId = getLocalAdminId();
    const db = loadDb();

    db.client_service_credentials = db.client_service_credentials.filter(c => !(c.client_id === clientId && c.service === service));
    saveDb(db);

    return NextResponse.json({ ok: true });
  } catch (err: unknown) {
    return NextResponse.json({ error: err instanceof Error ? err.message : JSON.stringify(err) }, { status: 500 });
  }
}
