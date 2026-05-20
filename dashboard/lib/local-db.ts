import fs from "fs"
import path from "path"

const CONFIG_PATH = path.join(process.cwd(), "..", "data", "local_config.json")

export interface LocalConfig {
  client_id: string
  api_key: string
  enabled_skills: string[]
  skill_configs: Record<string, Record<string, string>>
  connections: Record<string, Record<string, string>>
}

const DEFAULT_CONFIG: LocalConfig = {
  client_id: "",
  api_key: "",
  enabled_skills: [],
  skill_configs: {},
  connections: {},
}

function generateApiKey(): string {
  const bytes = new Uint8Array(16)
  crypto.getRandomValues(bytes)
  return Array.from(bytes).map((b) => b.toString(16).padStart(2, "0")).join("")
}

export function readLocalConfig(): LocalConfig {
  let config: LocalConfig = { ...DEFAULT_CONFIG }

  if (fs.existsSync(CONFIG_PATH)) {
    try {
      config = { ...DEFAULT_CONFIG, ...JSON.parse(fs.readFileSync(CONFIG_PATH, "utf-8")) }
    } catch {
      config = { ...DEFAULT_CONFIG }
    }
  }

  let dirty = false
  if (!config.client_id) {
    config.client_id = crypto.randomUUID()
    dirty = true
  }
  if (!config.api_key) {
    config.api_key = generateApiKey()
    dirty = true
  }
  if (dirty) writeLocalConfig(config)

  return config
}

export function writeLocalConfig(data: LocalConfig): void {
  const dir = path.dirname(CONFIG_PATH)
  if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true })
  fs.writeFileSync(CONFIG_PATH, JSON.stringify(data, null, 2))
}
