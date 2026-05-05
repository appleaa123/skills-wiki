import Link from "next/link";
import { CredentialsPopup } from "@/components/CredentialsPopup";
import { gatewayUrl } from "@/lib/utils";
import { DashboardClient } from "@/components/DashboardClient";
import { loadDb, getLocalAdminId } from "@/lib/local-db";

export default async function DashboardPage() {
  const clientId = getLocalAdminId();
  const db = loadDb();
  
  let client = db.clients.find(c => c.client_id === clientId);
  if (!client) {
    client = { client_id: clientId, enabled_skills: [] };
  }

  const credentials = {
    clientId: client.client_id,
    apiKey: "sk-local-dev-key",
    claudeUrl: gatewayUrl(client.client_id, "mcp"),
    chatgptUrl: gatewayUrl(client.client_id, "openapi"),
    geminiUrl: gatewayUrl(client.client_id, "mcp"),
    status: "live" as "live",
    username: "Local User",
  };

  return (
    <div className="min-h-screen bg-background">
      <header className="border-b px-6 py-4 flex items-center justify-between">
        <span className="font-semibold">Skills Portal</span>
        <div className="flex items-center gap-4">
          <Link href="/marketplace" className="text-sm text-muted-foreground hover:text-foreground transition-colors">
            Marketplace
          </Link>
          <Link href="/customize" className="text-sm text-muted-foreground hover:text-foreground transition-colors">
            Customize
          </Link>
          <Link href="/connections" className="text-sm text-muted-foreground hover:text-foreground transition-colors">
            Connections
          </Link>
        </div>
      </header>

      <main className="mx-auto max-w-3xl px-6 py-10 space-y-10">
        <section>
          <h2 className="text-xl font-semibold mb-4">Your connections</h2>
          <CredentialsPopup credentials={credentials} enabledSkills={client.enabled_skills} />
        </section>

        <DashboardClient enabledSkills={client.enabled_skills} />
      </main>
    </div>
  );
}
