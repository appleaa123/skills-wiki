import ConnectionsClient from "@/components/ConnectionsClient"
import { AppHeader } from "@/components/AppHeader"

export default function ConnectionsPage() {
  return (
    <div style={{ minHeight: "100vh", background: "var(--v4-bg)" }}>
      <AppHeader activePage="connections" />
      <ConnectionsClient />
    </div>
  )
}
