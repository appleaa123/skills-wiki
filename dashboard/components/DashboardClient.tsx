"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { Button } from "@/components/ui/button";
import { SkillCard } from "@/components/SkillCard";
import { ThemeSkillPicker } from "@/components/ThemeSkillPicker";
import { THEMES, skillByName } from "@/lib/skills";

export function DashboardClient({ enabledSkills }: { enabledSkills: string[] }) {
  const router = useRouter();

  // Skills section state
  const [editing, setEditing] = useState(false);
  const [selected, setSelected] = useState<Set<string>>(
    new Set(enabledSkills.filter((s) => s !== "feedback_skill"))
  );
  const [saving, setSaving] = useState(false);

  // Danger zone state
  const [confirmDelete, setConfirmDelete] = useState(false);
  const [deleting, setDeleting] = useState(false);

  const handleSave = async () => {
    setSaving(true);
    try {
      const res = await fetch("/api/skills", {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ skills: Array.from(selected) }),
      });
      if (!res.ok) throw new Error("Save failed");
      router.refresh();
      setEditing(false);
    } finally {
      setSaving(false);
    }
  };

  const handleCancel = () => {
    setSelected(new Set(enabledSkills.filter((s) => s !== "feedback_skill")));
    setEditing(false);
  };

  const handleDelete = async () => {
    setDeleting(true);
    try {
      await fetch("/api/connection", { method: "DELETE" });
      router.push("/signup");
    } finally {
      setDeleting(false);
    }
  };

  const displaySkills = enabledSkills
    .filter((s) => s !== "feedback_skill")
    .map(skillByName)
    .filter(Boolean) as NonNullable<ReturnType<typeof skillByName>>[];

  return (
    <>
      {/* Skills section */}
      <section>
        <div className="flex items-center justify-between mb-4">
          <h2 className="text-xl font-semibold">
            Your skills {!editing && `(${displaySkills.length})`}
          </h2>
          {!editing && (
            <Button variant="outline" size="sm" onClick={() => setEditing(true)}>
              Edit skills
            </Button>
          )}
        </div>

        {editing ? (
          <>
            <p className="text-sm text-muted-foreground mb-3">
              Select skills by theme. Click a theme to expand its individual skills.
            </p>
            <ThemeSkillPicker
              themes={THEMES}
              selectedSkills={selected}
              onChange={setSelected}
            />
            <div className="flex gap-2 mt-4">
              <Button size="sm" onClick={handleSave} disabled={saving || selected.size === 0}>
                {saving ? "Saving…" : `Save changes (${selected.size} selected)`}
              </Button>
              <Button size="sm" variant="ghost" onClick={handleCancel} disabled={saving}>
                Cancel
              </Button>
            </div>
          </>
        ) : (
          <div className="grid gap-4 sm:grid-cols-2">
            {displaySkills.map((skill) => (
              <SkillCard key={skill.name} skill={skill} assigned />
            ))}
          </div>
        )}
      </section>

      {/* Danger zone */}
      <section className="border-t pt-8">
        <p className="text-xs font-medium text-muted-foreground uppercase tracking-wide mb-3">Danger zone</p>
        {!confirmDelete ? (
          <Button
            variant="outline"
            size="sm"
            className="text-destructive border-destructive/40 hover:bg-destructive/5"
            onClick={() => setConfirmDelete(true)}
          >
            Delete connection
          </Button>
        ) : (
          <div className="rounded-lg border border-destructive/40 bg-destructive/5 p-4 space-y-3">
            <p className="text-sm text-destructive">
              This will delete your API key, all skill settings, and feedback history. You&apos;ll be redirected to re-onboard.
            </p>
            <div className="flex gap-2">
              <Button
                size="sm"
                variant="destructive"
                onClick={handleDelete}
                disabled={deleting}
              >
                {deleting ? "Deleting…" : "Confirm delete"}
              </Button>
              <Button size="sm" variant="ghost" onClick={() => setConfirmDelete(false)} disabled={deleting}>
                Cancel
              </Button>
            </div>
          </div>
        )}
      </section>
    </>
  );
}
