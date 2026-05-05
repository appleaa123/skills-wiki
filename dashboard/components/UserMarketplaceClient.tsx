"use client";

import { useState, useMemo } from "react";
import { UserSkillCard } from "@/components/UserSkillCard";
import type { SkillMeta } from "@/lib/skills";

interface ThemeOption {
  slug: string;
  name: string;
}

interface UserMarketplaceClientProps {
  skills: SkillMeta[];
  themes: ThemeOption[];
  initialEnabledSkills: string[];
}

const ALL_THEMES_LABEL = "All themes";

export function UserMarketplaceClient({ skills, themes, initialEnabledSkills }: UserMarketplaceClientProps) {
  const [enabledSkills, setEnabledSkills] = useState<string[]>(initialEnabledSkills);
  const [search, setSearch] = useState("");
  const [selectedTheme, setSelectedTheme] = useState("");
  const [installingName, setInstallingName] = useState<string | null>(null);

  const themeNameMap = useMemo(() => {
    const map: Record<string, string> = {};
    for (const t of themes) map[t.slug] = t.name;
    return map;
  }, [themes]);

  const filtered = useMemo(() => {
    return skills.filter((s) => {
      if (selectedTheme && s.theme !== selectedTheme) return false;
      if (search) {
        const q = search.toLowerCase();
        if (!s.displayName.toLowerCase().includes(q) && !s.description.toLowerCase().includes(q)) return false;
      }
      return true;
    });
  }, [skills, search, selectedTheme]);

  async function handleInstall(skillName: string) {
    setInstallingName(skillName);
    try {
      const res = await fetch("/api/marketplace/add", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ skillName }),
      });
      if (!res.ok) {
        const { error } = await res.json() as { error: string };
        alert(`Install failed: ${error}`);
        return;
      }
      setEnabledSkills((prev) => Array.from(new Set([...prev, skillName])));
    } finally {
      setInstallingName(null);
    }
  }

  return (
    <div className="space-y-6">
      {/* Filter bar */}
      <div className="flex flex-wrap gap-3 items-center">
        <input
          type="text"
          placeholder="Search skills…"
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          className="h-9 rounded-md border border-input bg-background px-3 text-sm shadow-sm placeholder:text-muted-foreground focus:outline-none focus:ring-1 focus:ring-ring w-full sm:w-56"
        />

        <select
          value={selectedTheme}
          onChange={(e) => setSelectedTheme(e.target.value)}
          className="h-9 rounded-md border border-input bg-background px-3 text-sm shadow-sm focus:outline-none focus:ring-1 focus:ring-ring"
        >
          <option value="">{ALL_THEMES_LABEL}</option>
          {themes.map((t) => (
            <option key={t.slug} value={t.slug}>{t.name}</option>
          ))}
        </select>

        <span className="text-sm text-muted-foreground ml-auto">
          {filtered.length} of {skills.length} skills
        </span>
      </div>

      {/* Grid */}
      {filtered.length === 0 ? (
        <p className="text-center text-muted-foreground py-16">No skills match your filters.</p>
      ) : (
        <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
          {filtered.map((skill) => (
            <UserSkillCard
              key={skill.name}
              skill={skill}
              themeLabel={themeNameMap[skill.theme] ?? skill.theme}
              isInstalled={enabledSkills.includes(skill.name)}
              onInstall={handleInstall}
              installing={installingName === skill.name}
            />
          ))}
        </div>
      )}
    </div>
  );
}
