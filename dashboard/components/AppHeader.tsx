"use client"

import Link from "next/link"

const NAV_LINKS = [
  { href: "/dashboard", label: "Dashboard", key: "dashboard" },
  { href: "/marketplace", label: "Marketplace", key: "marketplace" },
  { href: "/connections", label: "Connections", key: "connections" },
  { href: "/config", label: "Config", key: "config" },
  { href: "/setup", label: "Setup", key: "setup" },
] as const

type ActivePage = "dashboard" | "marketplace" | "connections" | "config" | "setup"

interface AppHeaderProps {
  activePage?: ActivePage
  appNavLinks?: boolean
  rightSlot?: React.ReactNode
}

export function AppHeader({ activePage, appNavLinks = true, rightSlot }: AppHeaderProps) {
  return (
    <header className="border-b bg-white px-6 h-14 flex items-center justify-between sticky top-0 z-50">
      <Link href="/" className="flex items-center gap-2.5 no-underline">
        <div className="w-7 h-7 bg-primary rounded-md flex items-center justify-center flex-shrink-0">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="white" strokeWidth="2.5">
            <circle cx="12" cy="12" r="3" />
            <path d="M12 1v4M12 19v4M4.22 4.22l2.83 2.83M16.95 16.95l2.83 2.83M1 12h4M19 12h4M4.22 19.78l2.83-2.83M16.95 7.05l2.83-2.83" />
          </svg>
        </div>
        <span className="font-semibold text-sm text-foreground">skills_wiki</span>
      </Link>

      {rightSlot ? (
        <div className="flex items-center gap-2">{rightSlot}</div>
      ) : appNavLinks ? (
        <nav className="flex items-center gap-1 text-sm">
          {NAV_LINKS.map(({ href, label, key }) => (
            <Link
              key={key}
              href={href}
              className={
                activePage === key
                  ? "font-semibold text-foreground px-3 py-1.5 rounded"
                  : "text-muted-foreground hover:text-foreground hover:bg-muted px-3 py-1.5 rounded"
              }
            >
              {label}
            </Link>
          ))}
        </nav>
      ) : null}
    </header>
  )
}
