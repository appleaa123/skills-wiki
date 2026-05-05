"use client";

import { useEffect, useState } from "react";
import { Dialog, DialogContent, DialogHeader, DialogTitle } from "@/components/ui/dialog";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";

interface LocalMeta {
  display_name: string;
  description: string;
  source_repo: string;
  theme: string;
}

interface SkillMetaEditModalProps {
  skillName: string;
  open: boolean;
  onClose: () => void;
  onSaved: (meta: LocalMeta) => void;
}

const EMPTY: LocalMeta = { display_name: "", description: "", source_repo: "", theme: "" };

export function SkillMetaEditModal({ skillName, open, onClose, onSaved }: SkillMetaEditModalProps) {
  const [fields, setFields] = useState<LocalMeta>(EMPTY);
  const [loading, setLoading] = useState(false);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!open) return;
    setError(null);
    setLoading(true);
    fetch(`/api/admin/skill-meta?name=${encodeURIComponent(skillName)}`)
      .then((r) => r.json())
      .then((data: Partial<LocalMeta>) => {
        setFields({
          display_name: data.display_name ?? "",
          description: data.description ?? "",
          source_repo: data.source_repo ?? "",
          theme: data.theme ?? "",
        });
      })
      .catch(() => setError("Failed to load metadata."))
      .finally(() => setLoading(false));
  }, [open, skillName]);

  function set(key: keyof LocalMeta, value: string) {
    setFields((prev) => ({ ...prev, [key]: value }));
  }

  async function handleSave() {
    setSaving(true);
    setError(null);
    try {
      const res = await fetch("/api/admin/skill-meta", {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name: skillName, fields }),
      });
      if (!res.ok) {
        const { error: msg } = await res.json() as { error: string };
        setError(msg ?? "Save failed.");
        return;
      }
      const { meta } = await res.json() as { meta: LocalMeta };
      onSaved(meta);
      onClose();
    } catch {
      setError("Network error — save failed.");
    } finally {
      setSaving(false);
    }
  }

  return (
    <Dialog open={open} onOpenChange={(v) => { if (!v) onClose(); }}>
      <DialogContent className="max-w-lg">
        <DialogHeader>
          <DialogTitle>Edit Skill Metadata — {skillName}</DialogTitle>
        </DialogHeader>

        {loading ? (
          <p className="py-6 text-center text-sm text-muted-foreground">Loading…</p>
        ) : (
          <div className="flex flex-col gap-4 py-2">
            <div className="flex flex-col gap-1.5">
              <Label htmlFor="sme-display-name">Display Name</Label>
              <Input
                id="sme-display-name"
                value={fields.display_name}
                onChange={(e) => set("display_name", e.target.value)}
                placeholder="Human-readable skill name"
              />
            </div>

            <div className="flex flex-col gap-1.5">
              <Label htmlFor="sme-description">Description</Label>
              <Textarea
                id="sme-description"
                value={fields.description}
                onChange={(e) => set("description", e.target.value)}
                placeholder="Short description of what this skill does"
                rows={3}
              />
            </div>

            <div className="flex flex-col gap-1.5">
              <Label htmlFor="sme-source-repo">Source Repo</Label>
              <Input
                id="sme-source-repo"
                value={fields.source_repo}
                onChange={(e) => set("source_repo", e.target.value)}
                placeholder="https://github.com/…"
              />
            </div>

            <div className="flex flex-col gap-1.5">
              <Label htmlFor="sme-theme">Theme</Label>
              <Input
                id="sme-theme"
                value={fields.theme}
                onChange={(e) => set("theme", e.target.value)}
                placeholder="e.g. engineering, seo, _unthemed"
              />
            </div>

            {error && <p className="text-sm text-destructive">{error}</p>}
          </div>
        )}

        <div className="flex justify-end gap-2 pt-2">
          <Button variant="outline" onClick={onClose} disabled={saving}>Cancel</Button>
          <Button onClick={handleSave} disabled={loading || saving}>
            {saving ? "Saving…" : "Save"}
          </Button>
        </div>
      </DialogContent>
    </Dialog>
  );
}
