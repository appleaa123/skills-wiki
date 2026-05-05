"use client";

import { useCallback, useEffect, useState } from "react";
import Link from "next/link";
import { ExternalLink, Trash2, Plus, CheckCircle2, ChevronDown, ChevronUp } from "lucide-react";
import { Button } from "@/components/ui/button";
import { SUPPORTED_SERVICES, isCustomService, type ServiceId } from "@/lib/services";

const CUSTOM_SENTINEL = "__custom__";

interface Connection {
  service: string;
  label: string;
  service_meta?: { url: string } | null;
  created_at: string;
  updated_at: string;
}

interface AddFormState {
  service: ServiceId | typeof CUSTOM_SENTINEL;
  label: string;
  credentials: Record<string, string>;
  customServiceName: string;
}

const EMPTY_FORM: AddFormState = {
  service: "supabase" as ServiceId,
  label: "",
  credentials: {},
  customServiceName: "",
};

function ConnectedCard({ conn, onRemove }: { conn: Connection; onRemove: () => void }) {
  const def = SUPPORTED_SERVICES[conn.service];
  const displayName = def?.label ?? conn.service;
  const subtitle = isCustomService(conn.service) && conn.service_meta?.url
    ? conn.service_meta.url
    : displayName;

  return (
    <div className="rounded-lg border bg-white p-4 flex items-start justify-between gap-4 shadow-sm">
      <div className="flex items-start gap-3">
        <CheckCircle2 className="h-4 w-4 text-primary mt-0.5 shrink-0" />
        <div>
          <p className="text-sm font-medium">{conn.label}</p>
          <p className="text-xs text-muted-foreground">{subtitle}</p>
        </div>
      </div>
      <button
        onClick={onRemove}
        className="text-muted-foreground hover:text-destructive transition-colors"
        aria-label={`Remove ${conn.label}`}
      >
        <Trash2 className="h-4 w-4" />
      </button>
    </div>
  );
}

function AddServiceForm({ onAdded }: { onAdded: () => void }) {
  const [open, setOpen] = useState(false);
  const [form, setForm] = useState<AddFormState>(EMPTY_FORM);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const isCustom = form.service === CUSTOM_SENTINEL;
  const serviceDef = isCustom ? null : SUPPORTED_SERVICES[form.service as ServiceId];

  const setField = (key: string, value: string) =>
    setForm((prev) => ({ ...prev, credentials: { ...prev.credentials, [key]: value } }));

  const handleServiceChange = (value: string) =>
    setForm({ service: value as AddFormState["service"], label: "", credentials: {}, customServiceName: "" });

  const handleSubmit = async () => {
    setSaving(true);
    setError(null);

    const payload = isCustom
      ? {
          service: form.customServiceName,
          label: form.label,
          is_custom: true,
          credentials: { url: form.credentials.url ?? "", token: form.credentials.token ?? "" },
        }
      : { service: form.service, label: form.label, credentials: form.credentials };

    const res = await fetch("/api/connections", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
    const data = await res.json();
    setSaving(false);
    if (!res.ok) {
      setError(data.error ?? "Failed to save");
      return;
    }
    setForm(EMPTY_FORM);
    setOpen(false);
    onAdded();
  };

  const canSave = !saving && !!form.label && (
    isCustom
      ? !!form.customServiceName && !!form.credentials.url && !!form.credentials.token
      : serviceDef?.fields.filter((f) => !f.optional).every((f) => !!form.credentials[f.key])
  );

  return (
    <div className="rounded-lg border bg-white shadow-sm">
      <button
        onClick={() => setOpen((v) => !v)}
        className="w-full flex items-center justify-between px-4 py-3 text-sm font-medium hover:bg-muted/30 transition-colors"
      >
        <span className="flex items-center gap-2">
          <Plus className="h-4 w-4" />
          Add a service
        </span>
        {open ? <ChevronUp className="h-4 w-4" /> : <ChevronDown className="h-4 w-4" />}
      </button>

      {open && (
        <div className="border-t px-4 py-4 space-y-4">
          <label className="flex flex-col gap-1 text-xs font-medium text-muted-foreground">
            Service
            <select
              value={form.service}
              onChange={(e) => handleServiceChange(e.target.value)}
              className="rounded border px-2 py-1.5 text-sm font-normal text-foreground"
            >
              {Object.entries(SUPPORTED_SERVICES).map(([id, def]) => (
                <option key={id} value={id}>{def.label}</option>
              ))}
              <option value={CUSTOM_SENTINEL}>Custom service…</option>
            </select>
          </label>

          {isCustom ? (
            <>
              <p className="text-xs text-muted-foreground">
                Add any external service. Skills can fetch its credentials by the service name you set.
              </p>
              <label className="flex flex-col gap-1 text-xs font-medium text-muted-foreground">
                Service name
                <input
                  type="text"
                  placeholder="e.g. my-api (lowercase, hyphens allowed)"
                  value={form.customServiceName}
                  onChange={(e) => setForm((prev) => ({ ...prev, customServiceName: e.target.value.toLowerCase() }))}
                  className="rounded border px-2 py-1.5 text-sm font-normal text-foreground"
                />
              </label>
            </>
          ) : (
            <p className="text-xs text-muted-foreground">{serviceDef?.description}</p>
          )}

          <label className="flex flex-col gap-1 text-xs font-medium text-muted-foreground">
            Label
            <input
              type="text"
              placeholder='e.g. "My Production DB"'
              value={form.label}
              onChange={(e) => setForm((prev) => ({ ...prev, label: e.target.value }))}
              className="rounded border px-2 py-1.5 text-sm font-normal text-foreground"
            />
          </label>

          {isCustom ? (
            <>
              <label className="flex flex-col gap-1 text-xs font-medium text-muted-foreground">
                URL / Endpoint
                <input
                  type="text"
                  placeholder="https://api.example.com"
                  value={form.credentials.url ?? ""}
                  onChange={(e) => setField("url", e.target.value)}
                  className="rounded border px-2 py-1.5 text-sm font-normal text-foreground"
                />
              </label>
              <label className="flex flex-col gap-1 text-xs font-medium text-muted-foreground">
                API Key / Token
                <input
                  type="password"
                  placeholder="your-secret-token"
                  value={form.credentials.token ?? ""}
                  onChange={(e) => setField("token", e.target.value)}
                  className="rounded border px-2 py-1.5 text-sm font-normal text-foreground"
                />
              </label>
            </>
          ) : (
            serviceDef?.fields.map((field) => (
              <label key={field.key} className="flex flex-col gap-1 text-xs font-medium text-muted-foreground">
                {field.label}
                <input
                  type={field.sensitive ? "password" : "text"}
                  placeholder={field.placeholder}
                  value={form.credentials[field.key] ?? ""}
                  onChange={(e) => setField(field.key, e.target.value)}
                  className="rounded border px-2 py-1.5 text-sm font-normal text-foreground"
                />
              </label>
            ))
          )}

          {error && <p className="text-xs text-destructive">{error}</p>}

          <Button size="sm" onClick={handleSubmit} disabled={!canSave}>
            {saving ? "Saving…" : "Save"}
          </Button>
        </div>
      )}
    </div>
  );
}

function PlatformAlternatives() {
  const withPlatformLinks = Object.entries(SUPPORTED_SERVICES).filter(
    ([, def]) => Object.keys(def.platformLinks).length > 0
  );

  if (withPlatformLinks.length === 0) return null;

  return (
    <div className="rounded-lg border bg-muted/40 p-4 space-y-3">
      <p className="text-xs font-semibold text-muted-foreground uppercase tracking-wide">
        Platform native alternatives
      </p>
      <p className="text-xs text-muted-foreground">
        Some services can also be connected directly in your LLM platform. Skills work either way —
        the vault above is for services that platforms don&apos;t support natively (like Supabase).
      </p>
      <div className="space-y-2">
        {withPlatformLinks.map(([id, def]) => (
          <div key={id} className="flex flex-wrap gap-2 items-center">
            <span className="text-xs font-medium w-16">{def.label}</span>
            {def.platformLinks.claude && (
              <a
                href={def.platformLinks.claude}
                target="_blank"
                rel="noopener noreferrer"
                className="flex items-center gap-1 text-xs text-muted-foreground hover:text-foreground transition-colors border rounded px-2 py-0.5"
              >
                <ExternalLink className="h-3 w-3" />
                Connect in Claude.ai
              </a>
            )}
            {def.platformLinks.chatgpt && (
              <a
                href={def.platformLinks.chatgpt}
                target="_blank"
                rel="noopener noreferrer"
                className="flex items-center gap-1 text-xs text-muted-foreground hover:text-foreground transition-colors border rounded px-2 py-0.5"
              >
                <ExternalLink className="h-3 w-3" />
                Connect in ChatGPT
              </a>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}

export default function ConnectionsClient() {
  const [connections, setConnections] = useState<Connection[]>([]);
  const [loading, setLoading] = useState(true);

  const load = useCallback(async () => {
    const res = await fetch("/api/connections");
    const data = await res.json();
    setConnections(data.connections ?? []);
    setLoading(false);
  }, []);

  useEffect(() => { load(); }, [load]);

  const handleRemove = async (service: string) => {
    await fetch(`/api/connections?service=${service}`, { method: "DELETE" });
    await load();
  };

  return (
    <div className="min-h-screen bg-muted/30">
      <header className="border-b bg-white px-6 py-4 flex items-center justify-between">
        <span className="font-semibold">Connected Services</span>
        <nav className="flex gap-4 text-sm">
          <Link href="/dashboard" className="text-muted-foreground hover:text-foreground">Dashboard</Link>
          <Link href="/marketplace" className="text-muted-foreground hover:text-foreground">Marketplace</Link>
          <Link href="/customize" className="text-muted-foreground hover:text-foreground">Customize</Link>
        </nav>
      </header>

      <main className="mx-auto max-w-2xl px-4 py-8 space-y-6">
        <p className="text-sm text-muted-foreground">
          Connect external services so your installed skills can act on your behalf —
          query your database, read your repos, or call APIs. Credentials are encrypted
          and only readable by your skills.
        </p>

        {loading ? (
          <p className="text-sm text-muted-foreground">Loading…</p>
        ) : (
          <>
            {connections.length === 0 ? (
              <p className="text-sm text-muted-foreground">No services connected yet.</p>
            ) : (
              <div className="space-y-3">
                {connections.map((conn) => (
                  <ConnectedCard
                    key={conn.service}
                    conn={conn}
                    onRemove={() => handleRemove(conn.service)}
                  />
                ))}
              </div>
            )}

            <AddServiceForm onAdded={load} />
            <PlatformAlternatives />
          </>
        )}
      </main>
    </div>
  );
}
