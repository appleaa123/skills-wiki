import { NextRequest, NextResponse } from "next/server"
import { readLocalConfig, writeLocalConfig } from "@/lib/local-db"
import { SUPPORTED_SERVICES } from "@/lib/services"

const CUSTOM_SERVICE_NAME_RE = /^[a-z0-9][a-z0-9-]{0,62}$/

// GET /api/connections — list connected services (names only, no credential values)
export async function GET(_req: NextRequest) {
  try {
    const config = readLocalConfig()
    const connections = Object.keys(config.connections).map((service) => ({
      service,
      label: service,
      created_at: null,
      updated_at: null,
    }))
    return NextResponse.json({ connections })
  } catch (err: unknown) {
    return NextResponse.json({ error: err instanceof Error ? err.message : "Internal error" }, { status: 500 })
  }
}

// POST /api/connections — add or update a service credential
export async function POST(req: NextRequest) {
  try {
    const body = await req.json() as {
      service?: string
      label?: string
      is_custom?: boolean
      credentials?: Record<string, string>
    }

    if (!body.service || !body.label || typeof body.credentials !== "object") {
      return NextResponse.json({ error: "service, label, and credentials are required" }, { status: 400 })
    }

    if (body.is_custom || !SUPPORTED_SERVICES[body.service]) {
      if (!CUSTOM_SERVICE_NAME_RE.test(body.service)) {
        return NextResponse.json(
          { error: "Service name must be lowercase letters, numbers, or hyphens" },
          { status: 400 }
        )
      }
      if (!body.credentials.url || !body.credentials.token) {
        return NextResponse.json({ error: "url and token are required for custom services" }, { status: 400 })
      }
    } else {
      const serviceDef = SUPPORTED_SERVICES[body.service]
      const missing = serviceDef.fields
        .filter((f) => !f.optional)
        .map((f) => f.key)
        .filter((k) => !body.credentials![k])
      if (missing.length > 0) {
        return NextResponse.json({ error: `Missing fields: ${missing.join(", ")}` }, { status: 400 })
      }
    }

    const data = readLocalConfig()
    data.connections[body.service] = body.credentials
    writeLocalConfig(data)

    return NextResponse.json({ ok: true, service: body.service })
  } catch (err: unknown) {
    return NextResponse.json({ error: err instanceof Error ? err.message : "Internal error" }, { status: 500 })
  }
}

// DELETE /api/connections?service=github
export async function DELETE(req: NextRequest) {
  try {
    const service = req.nextUrl.searchParams.get("service")
    if (!service) return NextResponse.json({ error: "service param required" }, { status: 400 })

    const data = readLocalConfig()
    delete data.connections[service]
    writeLocalConfig(data)

    return NextResponse.json({ ok: true })
  } catch (err: unknown) {
    return NextResponse.json({ error: err instanceof Error ? err.message : "Internal error" }, { status: 500 })
  }
}
