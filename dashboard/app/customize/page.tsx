"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { Button } from "@/components/ui/button";

interface SkillConfig {
  tone?: string;
  format?: string;
  language?: string;
  response_length?: string;
  custom_instructions?: string;
}

interface SkillConfigRow {
  skill: string;
  config: SkillConfig;
  updated_at: string | null;
}

interface Submission {
  id: string;
  skill_name: string;
  repo_url: string;
  status: "pending" | "approved" | "rejected";
  submitted_at: string;
}

const TONE_OPTIONS = ["", "formal", "casual", "technical"];
const FORMAT_OPTIONS = ["", "prose", "bullets", "table"];
const LENGTH_OPTIONS = ["", "brief", "standard", "detailed"];

const REPO_URL_RE = /^https:\/\/github\.com\/[^/]+\/[^/]+/;
const SKILL_NAME_RE = /^[a-z][a-z0-9_]{1,39}$/;

const STATUS_BADGE: Record<string, string> = {
  pending: "bg-yellow-100 text-yellow-800",
  approved: "bg-green-100 text-green-800",
  rejected: "bg-red-100 text-red-800",
};

function ConfigCard({
  skill,
  initial,
  onSaved,
}: {
  skill: string;
  initial: SkillConfig;
  onSaved: () => void;
}) {
  const [cfg, setCfg] = useState<SkillConfig>(initial);
  const [saving, setSaving] = useState(false);
  const [saved, setSaved] = useState(false);

  const update = (field: keyof SkillConfig, value: string) =>
    setCfg((prev) => ({ ...prev, [field]: value }));

  const handleSave = async () => {
    setSaving(true);
    await fetch("/api/config", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ skill, config: cfg }),
    });
    setSaving(false);
    setSaved(true);
    setTimeout(() => setSaved(false), 2000);
    onSaved();
  };

  const handleReset = async () => {
    await fetch(`/api/config?skill=${skill}`, { method: "DELETE" });
    setCfg({});
    onSaved();
  };

  return (
    <div className="rounded-lg border bg-white p-5 shadow-sm space-y-4">
      <div className="flex items-center justify-between">
        <h3 className="font-semibold text-sm">{skill}</h3>
        <button
          onClick={handleReset}
          className="text-xs text-muted-foreground hover:text-destructive"
        >
          Reset to defaults
        </button>
      </div>

      <div className="grid grid-cols-2 gap-3 sm:grid-cols-3">
        <label className="flex flex-col gap-1 text-xs font-medium text-muted-foreground">
          Tone
          <select
            value={cfg.tone ?? ""}
            onChange={(e) => update("tone", e.target.value)}
            className="rounded border px-2 py-1 text-sm font-normal text-foreground"
          >
            {TONE_OPTIONS.map((o) => (
              <option key={o} value={o}>{o || "— default —"}</option>
            ))}
          </select>
        </label>

        <label className="flex flex-col gap-1 text-xs font-medium text-muted-foreground">
          Format
          <select
            value={cfg.format ?? ""}
            onChange={(e) => update("format", e.target.value)}
            className="rounded border px-2 py-1 text-sm font-normal text-foreground"
          >
            {FORMAT_OPTIONS.map((o) => (
              <option key={o} value={o}>{o || "— default —"}</option>
            ))}
          </select>
        </label>

        <label className="flex flex-col gap-1 text-xs font-medium text-muted-foreground">
          Length
          <select
            value={cfg.response_length ?? ""}
            onChange={(e) => update("response_length", e.target.value)}
            className="rounded border px-2 py-1 text-sm font-normal text-foreground"
          >
            {LENGTH_OPTIONS.map((o) => (
              <option key={o} value={o}>{o || "— default —"}</option>
            ))}
          </select>
        </label>

        <label className="flex flex-col gap-1 text-xs font-medium text-muted-foreground col-span-2 sm:col-span-1">
          Language
          <input
            type="text"
            placeholder="e.g. Spanish"
            value={cfg.language ?? ""}
            onChange={(e) => update("language", e.target.value)}
            className="rounded border px-2 py-1 text-sm font-normal text-foreground"
          />
        </label>
      </div>

      <label className="flex flex-col gap-1 text-xs font-medium text-muted-foreground">
        Custom instructions
        <textarea
          rows={2}
          placeholder="e.g. Always start with a one-line summary. Skip the tips section."
          value={cfg.custom_instructions ?? ""}
          onChange={(e) => update("custom_instructions", e.target.value)}
          className="rounded border px-2 py-1 text-sm font-normal text-foreground resize-none"
        />
      </label>

      <Button size="sm" onClick={handleSave} disabled={saving}>
        {saved ? "Saved ✓" : saving ? "Saving…" : "Save"}
      </Button>
    </div>
  );
}

function LinkSkillSection({ onLinked }: { onLinked: () => void }) {
  const [open, setOpen] = useState(false);
  const [repoUrl, setRepoUrl] = useState("");
  const [skillName, setSkillName] = useState("");
  const [submitting, setSubmitting] = useState(false);
  const [statusMsg, setStatusMsg] = useState<{ type: "success" | "error"; text: string } | null>(null);
  const [submissions, setSubmissions] = useState<Submission[]>([]);

  const loadSubmissions = async () => {
    const res = await fetch("/api/skills/my-submissions");
    if (res.ok) {
      const data = await res.json() as { submissions: Submission[] };
      setSubmissions(data.submissions ?? []);
    }
  };

  useEffect(() => { loadSubmissions(); }, []);

  const validate = (): string | null => {
    if (!REPO_URL_RE.test(repoUrl)) return "Repo URL must be https://github.com/org/repo";
    if (!SKILL_NAME_RE.test(skillName)) return "Skill name must be snake_case, 2–40 chars, start with a letter";
    return null;
  };

  const handleSubmit = async () => {
    const err = validate();
    if (err) { setStatusMsg({ type: "error", text: err }); return; }

    setSubmitting(true);
    setStatusMsg(null);

    const res = await fetch("/api/skills/submit", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ repoUrl, skillName }),
    });
    const data = await res.json() as { error?: string };

    setSubmitting(false);

    if (!res.ok) {
      setStatusMsg({ type: "error", text: data.error ?? "Submission failed" });
    } else {
      setStatusMsg({ type: "success", text: `Queued — "${skillName}" will be active in your account once installed (~2 min).` });
      setRepoUrl("");
      setSkillName("");
      await loadSubmissions();
      onLinked();
    }
  };

  return (
    <div className="rounded-lg border bg-white p-5 shadow-sm space-y-4">
      <button
        className="flex w-full items-center justify-between text-sm font-semibold"
        onClick={() => setOpen((v) => !v)}
      >
        <span>Link a Skill from GitHub</span>
        <span className="text-muted-foreground">{open ? "▲" : "▼"}</span>
      </button>

      {open && (
        <div className="space-y-3 pt-1">
          <p className="text-xs text-muted-foreground">
            Paste a public GitHub repo URL and choose a unique snake_case name. The skill will be added to
            your account immediately and submitted for admin review before appearing in the public marketplace.
          </p>

          <label className="flex flex-col gap-1 text-xs font-medium text-muted-foreground">
            GitHub Repository URL
            <input
              type="url"
              placeholder="https://github.com/org/repo"
              value={repoUrl}
              onChange={(e) => setRepoUrl(e.target.value)}
              className="rounded border px-2 py-1.5 text-sm font-normal text-foreground"
            />
          </label>

          <label className="flex flex-col gap-1 text-xs font-medium text-muted-foreground">
            Skill Name (snake_case)
            <input
              type="text"
              placeholder="my_skill_name"
              value={skillName}
              onChange={(e) => setSkillName(e.target.value)}
              className="rounded border px-2 py-1.5 text-sm font-normal text-foreground"
            />
          </label>

          {statusMsg && (
            <p className={`text-xs ${statusMsg.type === "error" ? "text-destructive" : "text-green-700"}`}>
              {statusMsg.text}
            </p>
          )}

          <Button size="sm" onClick={handleSubmit} disabled={submitting}>
            {submitting ? "Submitting…" : "Link Skill"}
          </Button>
        </div>
      )}

      {submissions.length > 0 && (
        <div className="pt-2">
          <p className="text-xs font-medium text-muted-foreground mb-2">Your submissions</p>
          <div className="space-y-1.5">
            {submissions.map((s) => (
              <div key={s.id} className="flex items-center justify-between text-xs">
                <span className="font-mono">{s.skill_name}</span>
                <span className={`rounded px-1.5 py-0.5 text-[10px] font-medium ${STATUS_BADGE[s.status] ?? ""}`}>
                  {s.status}
                </span>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

export default function CustomizePage() {
  const [skills, setSkills] = useState<string[]>([]);
  const [configs, setConfigs] = useState<Record<string, SkillConfig>>({});
  const [loading, setLoading] = useState(true);

  const load = async () => {
    const [meRes, cfgRes] = await Promise.all([
      fetch("/api/me"),
      fetch("/api/config"),
    ]);
    const me = await meRes.json() as { skills?: string[] };
    const cfgData = await cfgRes.json() as { configs?: SkillConfigRow[] };

    setSkills(me.skills ?? []);
    const map: Record<string, SkillConfig> = {};
    for (const row of cfgData.configs ?? []) {
      map[row.skill] = row.config;
    }
    setConfigs(map);
    setLoading(false);
  };

  useEffect(() => { load(); }, []);

  const enabledSkills = skills.filter((s) => s !== "feedback_skill");

  return (
    <div className="min-h-screen bg-muted/30">
      <header className="border-b bg-white px-6 py-4 flex items-center justify-between">
        <span className="font-semibold">Customize Skills</span>
        <nav className="flex gap-4 text-sm">
          <Link href="/dashboard" className="text-muted-foreground hover:text-foreground">Dashboard</Link>
          <Link href="/marketplace" className="text-muted-foreground hover:text-foreground">Marketplace</Link>
          <Link href="/connections" className="text-muted-foreground hover:text-foreground">Connections</Link>
        </nav>
      </header>

      <main className="mx-auto max-w-3xl px-4 py-8">
        <p className="text-sm text-muted-foreground mb-6">
          Set presentation preferences per skill. Changes apply instantly to your account only —
          other clients are unaffected. These settings can also be updated automatically
          when you submit low-rated feedback.
        </p>

        <div className="space-y-4">
          <LinkSkillSection onLinked={load} />

          {loading ? (
            <p className="text-sm text-muted-foreground">Loading…</p>
          ) : enabledSkills.length === 0 ? (
            <p className="text-sm text-muted-foreground">No skills enabled yet.</p>
          ) : (
            enabledSkills.map((skill) => (
              <ConfigCard
                key={skill}
                skill={skill}
                initial={configs[skill] ?? {}}
                onSaved={load}
              />
            ))
          )}
        </div>
      </main>
    </div>
  );
}
