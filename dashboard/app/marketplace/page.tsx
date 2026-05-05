import Link from "next/link";
import { UserMarketplaceClient } from "@/components/UserMarketplaceClient";
import { THEMES, allSkills } from "@/lib/skills";
import { loadDb, getLocalAdminId } from "@/lib/local-db";

export const revalidate = 0;

export default async function MarketplacePage() {
  const clientId = getLocalAdminId();
  const db = loadDb();
  
  let client = db.clients.find(c => c.client_id === clientId);
  let enabledSkills = client?.enabled_skills || [];

  const skills = allSkills();
  const themes = THEMES.map((t) => ({ slug: t.slug, name: t.name }));

  return (
    <div className="min-h-screen bg-background">
      <header className="border-b px-6 py-4 flex items-center justify-between">
        <span className="font-semibold">Skills Portal</span>
        <nav className="flex items-center gap-4">
          <Link href="/dashboard" className="text-sm text-muted-foreground hover:text-foreground transition-colors">
            Dashboard
          </Link>
          <Link href="/marketplace" className="text-sm font-medium">
            Marketplace
          </Link>
          <Link href="/connections" className="text-sm text-muted-foreground hover:text-foreground transition-colors">
            Connections
          </Link>
        </nav>
      </header>

      <main className="mx-auto max-w-6xl px-6 py-10">
        <div className="mb-8">
          <h1 className="text-2xl font-bold">Skill Marketplace</h1>
          <p className="mt-1 text-muted-foreground">
            Browse available skills. Click Install to add a skill to your dashboard.
          </p>
        </div>

        <UserMarketplaceClient skills={skills} themes={themes} initialEnabledSkills={enabledSkills} />
      </main>
    </div>
  );
}
