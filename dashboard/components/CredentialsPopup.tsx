"use client";

import { useState } from "react";
import Link from "next/link";
import { maskApiKey } from "@/lib/utils";

const MONO = "var(--font-mono, 'JetBrains Mono', monospace)";

export interface Credentials {
  clientId: string;
  apiKey: string;
  claudeUrl: string;
  chatgptUrl: string;
  geminiUrl: string;
  status: "pending" | "live";
}

function CopyBtn({ value }: { value: string }) {
  const [ok, setOk] = useState(false);
  function go() {
    navigator.clipboard?.writeText(value);
    setOk(true);
    setTimeout(() => setOk(false), 1800);
  }
  return (
    <button
      onClick={go}
      title="copy"
      style={{ background: "none", border: "none", cursor: "pointer", padding: "0 4px", color: ok ? "var(--v4-primary)" : "var(--v4-fg-4)", display: "flex", alignItems: "center" }}
    >
      {ok ? (
        <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5"><polyline points="20 6 9 17 4 12" /></svg>
      ) : (
        <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><rect x="9" y="9" width="13" height="13" rx="1" /><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1" /></svg>
      )}
    </button>
  );
}

function CredRow({ label, value, secret = false }: { label: string; value: string; secret?: boolean }) {
  const [show, setShow] = useState(false);
  const display = secret && !show ? maskApiKey(value) : value;

  return (
    <div style={{ marginBottom: 10 }}>
      <span className="v4-mono-label">{label}</span>
      <div style={{ display: "flex", alignItems: "center", gap: 6 }}>
        <code style={{ flex: 1, background: "var(--v4-muted)", border: "1px solid var(--v4-border)", borderRadius: 3, padding: "6px 10px", fontSize: 13, fontFamily: MONO, color: "var(--v4-primary)", overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" }}>
          {display}
        </code>
        {secret && (
          <button
            onClick={() => setShow((v) => !v)}
            style={{ fontFamily: MONO, fontSize: 12, color: "var(--v4-fg-3)", background: "none", border: "none", cursor: "pointer", padding: "0 6px", whiteSpace: "nowrap" }}
          >
            {show ? "[hide]" : "[show]"}
          </button>
        )}
        <CopyBtn value={value} />
      </div>
    </div>
  );
}

export function CredentialsPopup({ credentials }: { credentials: Credentials }) {
  return (
    <div className="v4-card" style={{ padding: 16 }}>
      <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", marginBottom: 12 }}>
        <div>
          <div style={{ fontFamily: MONO, fontWeight: 600, color: "var(--v4-primary)", fontSize: 15 }}>gateway_credentials</div>
          <div style={{ fontFamily: MONO, fontSize: 12, color: "var(--v4-fg-4)", marginTop: 1 }}>// paste into your AI assistant</div>
        </div>
        <span style={{ fontFamily: MONO, fontSize: 12, display: "flex", alignItems: "center", gap: 5, color: "var(--v4-primary)" }}>
          <span style={{ width: 6, height: 6, borderRadius: "50%", background: "var(--v4-primary)", display: "inline-block" }} />
          live
        </span>
      </div>

      <CredRow label="CLIENT_ID" value={credentials.clientId} />
      <CredRow label="API_KEY" value={credentials.apiKey} secret />
      <CredRow label="CLAUDE_URL" value={credentials.claudeUrl} />
      <CredRow label="CHATGPT_URL" value={credentials.chatgptUrl} />
      <CredRow label="GEMINI_URL" value={credentials.geminiUrl} />

      <Link
        href="/setup"
        style={{ display: "flex", alignItems: "center", justifyContent: "center", marginTop: 12, fontFamily: MONO, fontSize: 13, fontWeight: 500, padding: "6px 14px", borderRadius: 4, border: "1px solid var(--v4-border)", background: "var(--v4-surface)", color: "var(--v4-fg-2)", textDecoration: "none", boxShadow: "var(--v4-shadow-sm)" }}
      >
        cat ./setup_guide →
      </Link>
    </div>
  );
}
