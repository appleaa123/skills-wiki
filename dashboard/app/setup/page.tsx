"use client"

import { useState } from "react"
import { AppHeader } from "@/components/AppHeader"

const MONO = "var(--font-mono, 'JetBrains Mono', monospace)"
const MCP_URL = process.env.NEXT_PUBLIC_GATEWAY_BASE_URL
  ? `${process.env.NEXT_PUBLIC_GATEWAY_BASE_URL}/mcp`
  : "http://localhost:8000/mcp"
const OPENAPI_URL = process.env.NEXT_PUBLIC_GATEWAY_BASE_URL
  ? `${process.env.NEXT_PUBLIC_GATEWAY_BASE_URL}/openapi.json`
  : "http://localhost:8000/openapi.json"

const GUIDES = [
  {
    key: "claude",
    title: "Claude Desktop",
    steps: [
      'Open Claude Desktop → Settings → Developer → Edit Config.',
      'Add this to your "mcpServers" section:',
      JSON.stringify({ "skills-wiki": { command: "npx", args: ["-y", "mcp-remote", "http://localhost:8000/mcp"] } }, null, 2),
      "Save and restart Claude Desktop — your skills appear as tools.",
    ],
    url: MCP_URL,
    urlLabel: "MCP URL",
  },
  {
    key: "claude-web",
    title: "Claude.ai (Web)",
    steps: [
      "Open claude.ai → Settings → Integrations → Add integration.",
      `Paste the MCP URL: ${MCP_URL}`,
      "Click Connect — your skills will appear as tools immediately.",
    ],
    url: MCP_URL,
    urlLabel: "MCP URL",
  },
  {
    key: "chatgpt",
    title: "ChatGPT (Custom GPT)",
    steps: [
      "Go to chatgpt.com → Explore GPTs → Create → Configure → Actions → Add action.",
      `Click "Import from URL" and paste: ${OPENAPI_URL}`,
      "Save the GPT — your skills appear as available actions.",
    ],
    url: OPENAPI_URL,
    urlLabel: "OpenAPI URL",
  },
  {
    key: "gemini",
    title: "Gemini / Google AI Studio",
    steps: [
      "Open Google AI Studio → Extensions.",
      `Add a new MCP server with URL: ${MCP_URL}`,
      "Your skills will be available as tools in conversations.",
    ],
    url: MCP_URL,
    urlLabel: "MCP URL",
  },
]

function CopyButton({ text }: { text: string }) {
  const [copied, setCopied] = useState(false)
  return (
    <button
      onClick={() => { navigator.clipboard.writeText(text); setCopied(true); setTimeout(() => setCopied(false), 2000) }}
      style={{ fontFamily: MONO, fontSize: 11, padding: "2px 8px", borderRadius: 3, border: "1px solid var(--v4-border)", background: "var(--v4-surface)", color: copied ? "var(--v4-primary)" : "var(--v4-fg-3)", cursor: "pointer" }}
    >
      {copied ? "✓ copied" : "copy"}
    </button>
  )
}

export default function SetupPage() {
  const [active, setActive] = useState("claude")
  const guide = GUIDES.find((g) => g.key === active)!

  return (
    <div style={{ minHeight: "100vh", background: "var(--v4-bg)" }}>
      <AppHeader activePage="setup" />

      <main style={{ maxWidth: 860, margin: "0 auto", padding: "24px 20px" }}>
        <div className="v4-cmd-prompt" style={{ marginBottom: 16 }}>
          <span><span className="v4-p">$</span> cat ./docs/connect_once_use_everywhere.md</span>
        </div>

        <div style={{ marginBottom: 24 }}>
          <h1 style={{ fontSize: 22, fontWeight: 700, letterSpacing: "-0.4px", marginBottom: 4, color: "var(--v4-fg)" }}>Connect Once. Use Everywhere.</h1>
          <p style={{ fontSize: 12, color: "var(--v4-fg-3)" }}>Add your local Skills Wiki server to your favourite AI assistant in under 60 seconds.</p>
        </div>

        {/* Server URL card */}
        <div className="v4-card" style={{ padding: "14px 16px", marginBottom: 24, display: "flex", alignItems: "center", justifyContent: "space-between", gap: 12 }}>
          <div>
            <p style={{ fontFamily: MONO, fontSize: 11, color: "var(--v4-fg-4)", marginBottom: 3 }}>Local MCP server</p>
            <p style={{ fontFamily: MONO, fontSize: 14, color: "var(--v4-primary)", fontWeight: 600 }}>http://localhost:8000/mcp</p>
          </div>
          <CopyButton text="http://localhost:8000/mcp" />
        </div>

        {/* Platform tabs */}
        <div style={{ display: "flex", gap: 6, marginBottom: 20, flexWrap: "wrap" }}>
          {GUIDES.map((g) => (
            <button
              key={g.key}
              onClick={() => setActive(g.key)}
              style={{
                fontFamily: MONO, fontSize: 12, padding: "6px 14px", borderRadius: 4, cursor: "pointer",
                border: "1px solid var(--v4-border)",
                background: active === g.key ? "var(--v4-primary)" : "var(--v4-surface)",
                color: active === g.key ? "#fff" : "var(--v4-fg-2)",
              }}
            >
              {g.title}
            </button>
          ))}
        </div>

        {/* Guide steps */}
        <div className="v4-card" style={{ padding: "20px 24px" }}>
          <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", marginBottom: 16 }}>
            <h2 style={{ fontFamily: MONO, fontSize: 14, fontWeight: 700, color: "var(--v4-fg)" }}>{guide.title}</h2>
            <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
              <span style={{ fontFamily: MONO, fontSize: 11, color: "var(--v4-fg-4)" }}>{guide.urlLabel}:</span>
              <CopyButton text={guide.url} />
            </div>
          </div>
          <ol style={{ paddingLeft: 20, margin: 0 }}>
            {guide.steps.map((step, i) => (
              <li key={i} style={{ marginBottom: 12 }}>
                {step.startsWith("{") ? (
                  <pre style={{ fontFamily: MONO, fontSize: 11, background: "var(--v4-muted)", padding: "10px 14px", borderRadius: 4, overflow: "auto", margin: "8px 0 0", color: "var(--v4-fg-2)" }}>{step}</pre>
                ) : (
                  <span style={{ fontSize: 13, color: "var(--v4-fg-2)", lineHeight: 1.7 }}>{step}</span>
                )}
              </li>
            ))}
          </ol>
        </div>
      </main>
    </div>
  )
}
