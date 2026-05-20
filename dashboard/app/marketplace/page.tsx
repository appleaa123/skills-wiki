import { UserMarketplaceClient } from "@/components/UserMarketplaceClient"
import { AppHeader } from "@/components/AppHeader"
import { THEMES, allSkills } from "@/lib/skills"
import { readLocalConfig } from "@/lib/local-db"

export const revalidate = 0

export default async function MarketplacePage() {
  const config = readLocalConfig()
  const skills = allSkills()
  const themes = THEMES.map((t) => ({ slug: t.slug, name: t.name }))

  return (
    <div className="min-h-screen" style={{ background: "var(--v4-bg)" }}>
      <AppHeader activePage="marketplace" />
      <UserMarketplaceClient skills={skills} themes={themes} initialEnabledSkills={config.enabled_skills} />
    </div>
  )
}
