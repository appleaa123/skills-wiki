"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { CredentialsPopup, type Credentials } from "@/components/CredentialsPopup";
import { skillByName, type SkillMeta } from "@/lib/skills";

const MONO = "var(--font-mono, 'JetBrains Mono', monospace)";

function formatFusionResults(
  results: Array<{ skill: string; tool: string; result: string }>
): string {
  return [
    "# Skills Context",
    `// generated ${new Date().toISOString()}`,
    "",
    ...results.flatMap(({ skill, tool, result }) => [
      `## ${skill} / ${tool}`,
      result.trim(),
      "",
    ]),
  ].join("\n");
}

function Spinner() {
  return <span style={{ display: "inline-block", width: 10, height: 10, border: "1.5px solid currentColor", borderTopColor: "transparent", borderRadius: "50%", animation: "spin 0.5s linear infinite" }} />;
}

interface ActiveSkillCardProps {
  skill: SkillMeta;
  isSelected: boolean;
  isEditing: boolean;
  onToggle: () => void;
  isExpanded: boolean;
  onExpandToggle: () => void;
  skillTools: Record<string, string> | null;
  isLoading: boolean;
  checkedTools: Map<string, Record<string, string>>;
  onToolCheck: (toolKey: string, checked: boolean) => void;
}

function ActiveSkillCard({
  skill,
  isSelected,
  isEditing,
  onToggle,
  isExpanded,
  onExpandToggle,
  skillTools,
  isLoading,
  checkedTools,
  onToolCheck,
}: ActiveSkillCardProps) {
  return (
    <div style={{
      borderRadius: 4, border: "1px solid", overflow: "hidden",
      background: isSelected ? "var(--v4-primary-10)" : "var(--v4-bg)",
      borderColor: isSelected ? "var(--v4-primary-20)" : "var(--v4-border)",
      transition: "all 0.12s",
    }}>
      <div
        style={{
          display: "flex", alignItems: "center", justifyContent: "space-between",
          padding: "8px 10px",
          cursor: isEditing ? "default" : "pointer",
        }}
        onClick={isEditing ? undefined : onExpandToggle}
      >
        <div style={{ flex: 1, minWidth: 0 }}>
          <p style={{ fontFamily: MONO, fontSize: 13, fontWeight: 500, color: "var(--v4-fg)" }}>{skill.name}</p>
          <p style={{ fontFamily: MONO, fontSize: 12, color: "var(--v4-fg-4)" }}>{skill.tools.length} functions loaded</p>
        </div>
        {isEditing ? (
          <button
            onClick={(e) => { e.stopPropagation(); onToggle(); }}
            style={{
              width: 32, height: 16, borderRadius: 8, border: "none", cursor: "pointer",
              background: isSelected ? "var(--v4-primary)" : "var(--v4-muted)",
              position: "relative", transition: "background 0.2s", flexShrink: 0,
            }}
          >
            <span style={{
              position: "absolute", top: 2, width: 12, height: 12,
              background: isSelected ? "white" : "#cbd5e1",
              borderRadius: "50%", transition: "left 0.2s",
              left: isSelected ? 18 : 2,
              boxShadow: "var(--v4-shadow-sm)",
            }} />
          </button>
        ) : (
          <span style={{ fontFamily: MONO, fontSize: 10, color: "var(--v4-fg-4)", flexShrink: 0, userSelect: "none" }}>
            {isExpanded ? "▼" : "▶"}
          </span>
        )}
      </div>

      {isExpanded && !isEditing && (
        <div style={{ borderTop: "1px solid var(--v4-border)", padding: "8px 10px", display: "flex", flexDirection: "column", gap: 4 }}>
          {isLoading && !skillTools && (
            <span style={{ fontFamily: MONO, fontSize: 12, color: "var(--v4-fg-4)" }}>// loading tools…</span>
          )}
          {!isLoading && skillTools && Object.keys(skillTools).length === 0 && (
            <span style={{ fontFamily: MONO, fontSize: 12, color: "var(--v4-fg-4)" }}>// no tools found for this skill</span>
          )}
          {skillTools && Object.entries(skillTools).map(([slug]) => {
            const toolKey = `${skill.name}/${slug}`;
            const isChecked = checkedTools.has(toolKey);
            return (
              <label key={toolKey} style={{ display: "flex", alignItems: "flex-start", gap: 7, cursor: "pointer", padding: "3px 0" }}>
                <input
                  type="checkbox"
                  checked={isChecked}
                  onChange={(e) => onToolCheck(toolKey, e.target.checked)}
                  style={{ marginTop: 1, flexShrink: 0, cursor: "pointer" }}
                />
                <span style={{ fontFamily: MONO, fontSize: 13, fontWeight: 500, color: "var(--v4-fg)" }}>{slug}</span>
              </label>
            );
          })}
        </div>
      )}
    </div>
  );
}

export function DashboardClient({
  enabledSkills,
  installedSkills,
  credentials,
}: {
  enabledSkills: string[];
  installedSkills: string[];
  credentials: Credentials;
}) {
  const router = useRouter();

  const [editing, setEditing] = useState(false);
  const [selected, setSelected] = useState<Set<string>>(
    new Set(enabledSkills.filter((s) => s !== "feedback_skill"))
  );
  const [saving, setSaving] = useState(false);
  const [confirmDelete, setConfirmDelete] = useState(false);
  const [deleting, setDeleting] = useState(false);

  const [skillToolsCache, setSkillToolsCache] = useState<Map<string, Record<string, string>>>(new Map());
  const [skillLoadingSet, setSkillLoadingSet] = useState<Set<string>>(new Set());
  const [expandedSkills, setExpandedSkills] = useState<Set<string>>(new Set());
  const [checkedTools, setCheckedTools] = useState<Map<string, Record<string, string>>>(new Map());
  const [running, setRunning] = useState(false);
  const [runError, setRunError] = useState("");
  const [fusionResults, setFusionResults] = useState<string | null>(null);
  const [copied, setCopied] = useState(false);

  const displaySkills = installedSkills
    .filter((s) => s !== "feedback_skill")
    .map(skillByName)
    .filter(Boolean) as NonNullable<ReturnType<typeof skillByName>>[];

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
    setExpandedSkills(new Set());
  };

  const handleToggleExpand = (skill: SkillMeta) => {
    const skillName = skill.name;
    setExpandedSkills((prev) => {
      const next = new Set(prev);
      next.has(skillName) ? next.delete(skillName) : next.add(skillName);
      return next;
    });
    if (!skillToolsCache.has(skillName) && !skillLoadingSet.has(skillName)) {
      setSkillLoadingSet((prev) => new Set([...prev, skillName]));
      fetch(`/api/skill-tools?skill=${encodeURIComponent(skillName)}`)
        .then((r) => r.json())
        .then((d) => {
          const tools =
            d.tools && typeof d.tools === "object" && !Array.isArray(d.tools)
              ? (d.tools as Record<string, string>)
              : {};
          setSkillToolsCache((prev) => new Map([...prev, [skillName, tools]]));
        })
        .catch(() => setSkillToolsCache((prev) => new Map([...prev, [skillName, {}]])))
        .finally(() =>
          setSkillLoadingSet((prev) => {
            const n = new Set(prev);
            n.delete(skillName);
            return n;
          })
        );
    }
  };

  const handleToolCheck = (toolKey: string, checked: boolean) => {
    setCheckedTools((prev) => {
      const next = new Map(prev);
      checked ? next.set(toolKey, {}) : next.delete(toolKey);
      return next;
    });
    setFusionResults(null);
    setRunError("");
  };

  const handleRunAll = async () => {
    if (checkedTools.size === 0) return;
    setRunning(true);
    setRunError("");
    setFusionResults(null);
    setCopied(false);
    const out: Array<{ skill: string; tool: string; result: string }> = [];
    for (const [toolKey] of checkedTools.entries()) {
      const slashIdx = toolKey.indexOf("/");
      const skillFolder = toolKey.slice(0, slashIdx);
      const slug = toolKey.slice(slashIdx + 1);
      const skillMeta = displaySkills.find((s) => s.name === skillFolder);
      const getTool = skillMeta?.tools.find((t) => t.startsWith("get_"));
      if (!getTool) continue;
      try {
        const resp = await fetch("/api/tool-run", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ skill: skillFolder, tool: getTool, args: { skill_name: slug } }),
        });
        const data = await resp.json() as { result?: unknown; error?: string };
        if (resp.ok && !data.error) {
          out.push({
            skill: skillFolder,
            tool: slug,
            result: typeof data.result === "string" ? data.result : JSON.stringify(data.result, null, 2),
          });
        } else {
          setRunError(`${slug}: ${data.error ?? "failed"}`);
        }
      } catch {
        setRunError(`${slug}: network error`);
      }
    }
    if (out.length > 0) setFusionResults(formatFusionResults(out));
    setRunning(false);
  };

  const handleFusionCopy = () => {
    if (!fusionResults) return;
    navigator.clipboard.writeText(fusionResults);
    setCopied(true);
    setTimeout(() => setCopied(false), 1800);
  };

  const handleToggle = (skillName: string) => {
    setSelected((prev) => {
      const next = new Set(prev);
      if (next.has(skillName)) next.delete(skillName);
      else next.add(skillName);
      return next;
    });
  };

  const handleDelete = async () => {
    setDeleting(true);
    try {
      await fetch("/api/skills", {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ skills: [] }),
      });
      router.refresh();
      setConfirmDelete(false);
    } finally {
      setDeleting(false);
    }
  };

  return (
    <>
      {/* 1. Plan strip — full width */}
      <div className="v4-card" style={{ padding: "10px 14px", display: "flex", alignItems: "center", justifyContent: "space-between", marginBottom: 16 }}>
        <div style={{ fontFamily: MONO, fontSize: 12 }}>
          <span style={{ color: "var(--v4-fg-4)" }}>plan = </span>
          <span style={{ color: "var(--v4-amber)" }}>&quot;local&quot;</span>
          <span style={{ color: "var(--v4-fg-4)", marginLeft: 12 }}>// running fully local — no cloud required</span>
        </div>
      </div>

      {/* 2. Two-column grid: active skills | credentials */}
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 16, marginBottom: 16 }}>
        {/* Active skills card */}
        <div className="v4-card" style={{ padding: 16 }}>
          <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", marginBottom: 12 }}>
            <div>
              <div style={{ fontFamily: MONO, fontWeight: 600, color: "var(--v4-primary)", fontSize: 15 }}>active_skills[]</div>
              <div style={{ fontFamily: MONO, fontSize: 12, color: "var(--v4-fg-4)", marginTop: 1 }}>
                // {displaySkills.length} skill{displaySkills.length !== 1 ? "s" : ""} loaded · toggle on/off instantly
              </div>
            </div>
            {!editing ? (
              <button
                onClick={() => setEditing(true)}
                style={{ fontFamily: MONO, fontSize: 11, fontWeight: 500, height: 28, padding: "0 10px", borderRadius: 4, border: "1px solid var(--v4-border)", background: "var(--v4-muted)", color: "var(--v4-fg-2)", cursor: "pointer", boxShadow: "var(--v4-shadow-sm)" }}
              >
                --edit
              </button>
            ) : (
              <div style={{ display: "flex", gap: 5 }}>
                <button
                  onClick={handleSave}
                  disabled={saving || selected.size === 0}
                  style={{ fontFamily: MONO, fontSize: 11, fontWeight: 700, height: 28, padding: "0 10px", borderRadius: 4, border: "1px solid var(--v4-primary)", background: "var(--v4-primary)", color: "#fff", cursor: "pointer", display: "inline-flex", alignItems: "center", gap: 5 }}
                >
                  {saving ? <><Spinner /> …</> : "--save"}
                </button>
                <button
                  onClick={handleCancel}
                  disabled={saving}
                  style={{ fontFamily: MONO, fontSize: 11, fontWeight: 500, height: 28, padding: "0 10px", borderRadius: 4, border: "1px solid transparent", background: "transparent", color: "var(--v4-fg-3)", cursor: "pointer" }}
                >
                  --cancel
                </button>
              </div>
            )}
          </div>

          <div style={{ display: "flex", flexDirection: "column", gap: 5 }}>
            {displaySkills.map((s) => (
              <ActiveSkillCard
                key={s.name}
                skill={s}
                isSelected={selected.has(s.name)}
                isEditing={editing}
                onToggle={() => handleToggle(s.name)}
                isExpanded={expandedSkills.has(s.name)}
                onExpandToggle={() => handleToggleExpand(s)}
                isLoading={skillLoadingSet.has(s.name)}
                skillTools={skillToolsCache.get(s.name) ?? null}
                checkedTools={checkedTools}
                onToolCheck={handleToolCheck}
              />
            ))}

            {displaySkills.length === 0 && !editing && (
              <p style={{ fontFamily: MONO, fontSize: 13, color: "var(--v4-fg-4)", padding: "16px 0", textAlign: "center" }}>
                // no skills active — browse marketplace
              </p>
            )}

            {editing && (() => {
              const deselected = displaySkills.filter((s) => !selected.has(s.name));
              if (deselected.length === 0) return null;
              return (
                <div style={{ marginTop: 8, borderTop: "1px solid var(--v4-border)", paddingTop: 8 }}>
                  <div style={{ fontFamily: MONO, fontSize: 12, color: "var(--v4-fg-4)", marginBottom: 6 }}>
                    // installed but inactive — click to re-enable:
                  </div>
                  <div style={{ maxHeight: 200, overflowY: "auto", display: "flex", flexDirection: "column", gap: 2 }}>
                    {deselected.map((s) => (
                      <button
                        key={s.name}
                        onClick={() => handleToggle(s.name)}
                        style={{
                          fontFamily: MONO, fontSize: 13, textAlign: "left",
                          padding: "5px 8px", borderRadius: 4,
                          border: "1px solid var(--v4-border)",
                          background: "var(--v4-surface)", color: "var(--v4-fg-3)",
                          cursor: "pointer", display: "flex", alignItems: "center", gap: 6,
                        }}
                      >
                        <span style={{ color: "var(--v4-primary)" }}>+</span> {s.name}
                      </button>
                    ))}
                  </div>
                </div>
              );
            })()}

            <div style={{ display: "flex", gap: 6, marginTop: 4 }}>
              <button
                onClick={handleRunAll}
                disabled={running}
                style={{
                  flex: 1, padding: "6px 12px",
                  background: running ? "var(--v4-muted)" : "var(--v4-primary)",
                  color: running ? "var(--v4-fg-4)" : "#fff",
                  border: "1px solid var(--v4-border)", borderRadius: 4,
                  fontFamily: MONO, fontSize: 13, fontWeight: 700,
                  cursor: running ? "default" : "pointer",
                  display: "inline-flex", alignItems: "center", justifyContent: "center", gap: 5,
                }}
              >
                {running ? <><Spinner /> running…</> : checkedTools.size > 0 ? `▶ run (${checkedTools.size} selected)` : "▶ run"}
              </button>
              <button
                onClick={handleFusionCopy}
                disabled={!fusionResults}
                style={{
                  padding: "6px 12px", background: "none",
                  border: `1px solid ${fusionResults ? "var(--v4-primary)" : "var(--v4-border)"}`,
                  borderRadius: 4, fontFamily: MONO, fontSize: 13, fontWeight: 600,
                  color: fusionResults ? "var(--v4-primary)" : "var(--v4-fg-4)",
                  cursor: fusionResults ? "pointer" : "default",
                  display: "inline-flex", alignItems: "center", gap: 5,
                  transition: "color 0.2s, border-color 0.2s",
                }}
              >
                {copied ? (
                  <>
                    <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5">
                      <polyline points="20 6 9 17 4 12" />
                    </svg>
                    tools are copied
                  </>
                ) : (
                  <>
                    <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                      <rect x="9" y="9" width="13" height="13" rx="1" />
                      <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1" />
                    </svg>
                    copy
                  </>
                )}
              </button>
            </div>
            {runError && (
              <div style={{ fontFamily: MONO, fontSize: 12, color: "#ef4444", marginTop: 2 }}>{runError}</div>
            )}

            {fusionResults && (
              <div style={{ marginTop: 8, padding: "10px 12px", background: "var(--v4-muted)", border: "1px solid var(--v4-border)", borderRadius: 4, fontFamily: MONO, fontSize: 12, color: "var(--v4-fg-3)", whiteSpace: "pre-wrap", maxHeight: 200, overflowY: "auto" }}>
                {fusionResults}
              </div>
            )}

            <a
              href="/marketplace"
              style={{
                display: "flex", alignItems: "center", justifyContent: "center", gap: 6,
                padding: "8px 10px", border: "1px dashed #cbd5e1", borderRadius: 4,
                background: "transparent", textDecoration: "none", fontFamily: MONO, fontSize: 13, color: "var(--v4-fg-4)",
                marginTop: 2,
              }}
            >
              + install more from ./marketplace
            </a>
          </div>
        </div>

        {/* Credentials card */}
        <CredentialsPopup credentials={credentials} />
      </div>

      {/* 3. Danger zone — full width */}
      <div style={{ borderTop: "1px solid var(--v4-border)", paddingTop: 16 }}>
        <span className="v4-mono-label"># danger_zone — destructive actions</span>
        {!confirmDelete ? (
          <button
            onClick={() => setConfirmDelete(true)}
            style={{ fontFamily: MONO, fontSize: 11, fontWeight: 500, height: 28, padding: "0 10px", borderRadius: 4, border: "1px solid rgba(239,68,68,0.3)", background: "rgba(239,68,68,0.06)", color: "var(--v4-destructive)", cursor: "pointer", marginTop: 8, display: "block" }}
          >
            rm -rf ./connection
          </button>
        ) : (
          <div style={{ background: "var(--v4-destructive-bg)", border: "1px solid rgba(239,68,68,0.25)", borderRadius: 3, padding: 12, marginTop: 8 }}>
            <p style={{ fontFamily: MONO, fontSize: 13, color: "var(--v4-destructive)", lineHeight: 1.6, marginBottom: 10 }}>
              // clears all active skills and connections from local config. irreversible.
            </p>
            <div style={{ display: "flex", gap: 8 }}>
              <button
                onClick={handleDelete}
                disabled={deleting}
                style={{ fontFamily: MONO, fontSize: 11, fontWeight: 700, height: 28, padding: "0 10px", borderRadius: 4, border: "1px solid var(--v4-destructive)", background: "var(--v4-destructive)", color: "#fff", cursor: "pointer", display: "inline-flex", alignItems: "center", gap: 5 }}
              >
                {deleting ? <><Spinner /> …</> : "--confirm"}
              </button>
              <button
                onClick={() => setConfirmDelete(false)}
                disabled={deleting}
                style={{ fontFamily: MONO, fontSize: 11, fontWeight: 500, height: 28, padding: "0 10px", borderRadius: 4, border: "1px solid transparent", background: "transparent", color: "var(--v4-fg-3)", cursor: "pointer" }}
              >
                --cancel
              </button>
            </div>
          </div>
        )}
      </div>
    </>
  );
}
