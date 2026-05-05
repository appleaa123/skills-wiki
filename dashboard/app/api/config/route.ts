import { NextRequest, NextResponse } from "next/server";
import { loadDb, saveDb, getLocalAdminId } from "@/lib/local-db";

interface SkillConfig {
  tone?: "formal" | "casual" | "technical";
  format?: "prose" | "bullets" | "table";
  language?: string;
  response_length?: "brief" | "standard" | "detailed";
  custom_instructions?: string;
}

// GET /api/config?skill=amazon_skills  — returns config for one skill
// GET /api/config                       — returns all configs for the client
export async function GET(req: NextRequest) {
  try {
    const clientId = getLocalAdminId();
    const db = loadDb();
    
    const skill = req.nextUrl.searchParams.get("skill");
    if (skill) {
      const configRecord = db.client_skill_configs.find(c => c.client_id === clientId && c.skill === skill);
      return NextResponse.json({ 
        skill, 
        config: configRecord?.config ?? {}, 
        updated_at: configRecord?.updated_at ?? null 
      });
    }

    const clientConfigs = db.client_skill_configs.filter(c => c.client_id === clientId);
    return NextResponse.json({ configs: clientConfigs });
  } catch (err: unknown) {
    return NextResponse.json({ error: err instanceof Error ? err.message : "Internal error" }, { status: 500 });
  }
}

// POST /api/config  body: { skill: string, config: SkillConfig }
export async function POST(req: NextRequest) {
  try {
    const body = await req.json() as { skill?: string; config?: SkillConfig };
    if (!body.skill || typeof body.config !== "object") {
      return NextResponse.json({ error: "skill and config are required" }, { status: 400 });
    }

    const clientId = getLocalAdminId();
    const db = loadDb();
    
    const existingIndex = db.client_skill_configs.findIndex(c => c.client_id === clientId && c.skill === body.skill);
    const updatedRecord = {
      client_id: clientId,
      skill: body.skill,
      config: body.config as Record<string, unknown>,
      updated_at: new Date().toISOString()
    };

    if (existingIndex >= 0) {
      db.client_skill_configs[existingIndex] = updatedRecord;
    } else {
      db.client_skill_configs.push(updatedRecord);
    }
    
    saveDb(db);
    return NextResponse.json({ ok: true });
  } catch (err: unknown) {
    return NextResponse.json({ error: err instanceof Error ? err.message : "Internal error" }, { status: 500 });
  }
}

// DELETE /api/config?skill=amazon_skills  — resets a skill back to defaults
export async function DELETE(req: NextRequest) {
  try {
    const skill = req.nextUrl.searchParams.get("skill");
    if (!skill) return NextResponse.json({ error: "skill param required" }, { status: 400 });

    const clientId = getLocalAdminId();
    const db = loadDb();
    
    db.client_skill_configs = db.client_skill_configs.filter(c => !(c.client_id === clientId && c.skill === skill));
    saveDb(db);
    
    return NextResponse.json({ ok: true });
  } catch (err: unknown) {
    return NextResponse.json({ error: err instanceof Error ? err.message : "Internal error" }, { status: 500 });
  }
}
