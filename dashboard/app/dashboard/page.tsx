import { gatewayUrl } from "@/lib/utils"
import { DashboardClient } from "@/components/DashboardClient"
import { AppHeader } from "@/components/AppHeader"
import { readLocalConfig } from "@/lib/local-db"

export const dynamic = "force-dynamic"

export default async function DashboardPage() {
  const config = readLocalConfig()

  const credentials = {
    clientId: config.client_id,
    apiKey: config.api_key,
    claudeUrl: gatewayUrl("mcp"),
    chatgptUrl: gatewayUrl("openapi"),
    geminiUrl: gatewayUrl("mcp"),
    status: "live" as const,
  }

  return (
    <div style={{ minHeight: "100vh", background: "var(--v4-bg)" }}>
      <AppHeader activePage="dashboard" />

      <main style={{ maxWidth: 960, margin: "0 auto", padding: "24px 20px" }}>
        <div className="v4-cmd-prompt" style={{ marginBottom: 16, display: "flex", alignItems: "center", justifyContent: "space-between" }}>
          <span><span className="v4-p">$</span> skills-wiki status --verbose</span>
          <div style={{ display: "flex", gap: 14 }}>
            <span><span style={{ color: "var(--v4-primary)" }}>●</span> gateway: live</span>
            <span><span style={{ color: "var(--v4-amber)" }}>●</span> plan: local</span>
          </div>
        </div>

        <div style={{ marginBottom: 20 }}>
          <h1 style={{ fontSize: 22, fontWeight: 700, letterSpacing: "-0.4px", marginBottom: 3, color: "var(--v4-fg)" }}>Your Workflow Control Center.</h1>
          <p style={{ fontSize: 12, color: "var(--v4-fg-3)" }}>Manage active skills, credentials, and connect to your AI assistant.</p>
        </div>

        <DashboardClient
          enabledSkills={config.enabled_skills}
          installedSkills={config.enabled_skills}
          credentials={credentials}
        />
      </main>
    </div>
  )
}
