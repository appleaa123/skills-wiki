import fs from "fs";
import path from "path";
import os from "os";

// Helper to get local DB path mirroring Python's logic
function getDbPath(): string {
  const homeDir = path.join(os.homedir(), ".skills-wiki");
  if (!fs.existsSync(homeDir)) {
    fs.mkdirSync(homeDir, { recursive: true });
  }
  return path.join(homeDir, "db.json");
}

export interface Client {
  client_id: string;
  enabled_skills: string[];
}

export interface ClientSkillConfig {
  client_id: string;
  skill: string;
  config: Record<string, unknown>;
  updated_at: string;
}

export interface ClientServiceCredential {
  client_id: string;
  service: string;
  credentials: Record<string, unknown>;
}

export interface LocalDb {
  clients: Client[];
  audit_logs: unknown[];
  feedback_logs: unknown[];
  client_skill_configs: ClientSkillConfig[];
  client_service_credentials: ClientServiceCredential[];
}

const defaultDb: LocalDb = {
  clients: [{ client_id: "local-admin", enabled_skills: [] }],
  audit_logs: [],
  feedback_logs: [],
  client_skill_configs: [],
  client_service_credentials: [],
};

export function loadDb(): LocalDb {
  const dbPath = getDbPath();
  if (!fs.existsSync(dbPath)) {
    return defaultDb;
  }
  try {
    const data = fs.readFileSync(dbPath, "utf-8");
    return JSON.parse(data) as LocalDb;
  } catch (err) {
    console.error("Failed to load db.json:", err);
    return defaultDb;
  }
}

export function saveDb(data: LocalDb): void {
  const dbPath = getDbPath();
  try {
    fs.writeFileSync(dbPath, JSON.stringify(data, null, 2), "utf-8");
  } catch (err) {
    console.error("Failed to save db.json:", err);
  }
}

export function getLocalAdminId(): string {
  // Hardcoded for open-source local usage
  return process.env.CLIENT_ID || "local-admin";
}
