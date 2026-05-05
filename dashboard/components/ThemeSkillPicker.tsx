"use client";

import { useState } from "react";
import type { Theme, SkillMeta } from "@/lib/skills";

interface ThemeSkillPickerProps {
  themes: Theme[];
  selectedSkills: Set<string>;
  onChange: (skills: Set<string>) => void;
}

export function ThemeSkillPicker({ themes, selectedSkills, onChange }: ThemeSkillPickerProps) {
  const [expandedTheme, setExpandedTheme] = useState<string | null>(themes[0]?.slug ?? null);

  const toggleSkill = (name: string) => {
    const next = new Set(selectedSkills);
    if (next.has(name)) next.delete(name);
    else next.add(name);
    onChange(next);
  };

  const toggleAllInTheme = (theme: Theme) => {
    const next = new Set(selectedSkills);
    const allSelected = theme.skills.every((s) => next.has(s.name));
    if (allSelected) {
      theme.skills.forEach((s) => next.delete(s.name));
    } else {
      theme.skills.forEach((s) => next.add(s.name));
    }
    onChange(next);
  };

  const countSelected = (theme: Theme) =>
    theme.skills.filter((s) => selectedSkills.has(s.name)).length;

  return (
    <div className="space-y-2">
      {themes.map((theme) => {
        const selected = countSelected(theme);
        const isOpen = expandedTheme === theme.slug;
        const allChecked = selected === theme.skills.length;
        const someChecked = selected > 0 && !allChecked;

        return (
          <div key={theme.slug} className="border rounded-lg overflow-hidden">
            {/* Theme header row */}
            <button
              type="button"
              onClick={() => setExpandedTheme(isOpen ? null : theme.slug)}
              className="w-full flex items-center justify-between px-4 py-3 bg-muted/40 hover:bg-muted/70 transition-colors text-left"
            >
              <div className="flex items-center gap-3">
                {/* Theme-level checkbox */}
                <span
                  role="checkbox"
                  aria-checked={allChecked ? "true" : someChecked ? "mixed" : "false"}
                  onClick={(e) => {
                    e.stopPropagation();
                    toggleAllInTheme(theme);
                  }}
                  className={`flex-shrink-0 h-4 w-4 rounded border transition-colors cursor-pointer
                    ${allChecked ? "bg-primary border-primary" : someChecked ? "bg-primary/40 border-primary/60" : "border-input bg-background"}`}
                />
                <div>
                  <span className="font-medium text-sm">{theme.name}</span>
                  {theme.description && (
                    <span className="text-xs text-muted-foreground ml-2">{theme.description}</span>
                  )}
                </div>
              </div>
              <div className="flex items-center gap-2 text-xs text-muted-foreground">
                {selected > 0 && (
                  <span className="bg-primary/10 text-primary px-1.5 py-0.5 rounded">
                    {selected}/{theme.skills.length}
                  </span>
                )}
                {!selected && (
                  <span className="opacity-50">{theme.skills.length} skills</span>
                )}
                <svg
                  className={`w-4 h-4 transition-transform ${isOpen ? "rotate-180" : ""}`}
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                  strokeWidth={2}
                >
                  <path strokeLinecap="round" strokeLinejoin="round" d="M19 9l-7 7-7-7" />
                </svg>
              </div>
            </button>

            {/* Skill list */}
            {isOpen && (
              <div className="divide-y">
                {theme.skills.map((skill) => (
                  <SkillRow
                    key={skill.name}
                    skill={skill}
                    checked={selectedSkills.has(skill.name)}
                    onToggle={() => toggleSkill(skill.name)}
                  />
                ))}
              </div>
            )}
          </div>
        );
      })}
    </div>
  );
}

function SkillRow({
  skill,
  checked,
  onToggle,
}: {
  skill: SkillMeta;
  checked: boolean;
  onToggle: () => void;
}) {
  return (
    <button
      type="button"
      onClick={onToggle}
      className={`w-full flex items-start gap-3 px-4 py-3 text-left transition-colors hover:bg-muted/30
        ${checked ? "bg-primary/5" : "bg-background"}`}
    >
      <div
        className={`mt-0.5 flex-shrink-0 h-4 w-4 rounded border transition-colors
          ${checked ? "bg-primary border-primary" : "border-input"}`}
      />
      <div className="min-w-0">
        <p className="text-sm font-medium">{skill.displayName}</p>
        {skill.description && (
          <p className="text-xs text-muted-foreground mt-0.5 line-clamp-2">{skill.description}</p>
        )}
      </div>
    </button>
  );
}
