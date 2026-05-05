"use client";

import { useState, useMemo } from "react";
import { MarketplaceSkillCard, type CatalogSkill } from "@/components/MarketplaceSkillCard";
import { SkillMetaEditModal } from "@/components/SkillMetaEditModal";

const RANKS = ["S", "A", "B", "C"] as const;
const ALL_CATEGORIES_LABEL = "All categories";

interface MarketplaceClientProps {
  initialSkills: CatalogSkill[];
  categories: string[];
  isAdmin: boolean;
  mode?: "admin" | "user";
}

export function MarketplaceClient({ initialSkills, categories, isAdmin }: MarketplaceClientProps) {
  const [skills, setSkills] = useState<CatalogSkill[]>(initialSkills);
  const [search, setSearch] = useState("");
  const [selectedCategory, setSelectedCategory] = useState("");
  const [selectedRanks, setSelectedRanks] = useState<string[]>([]);
  const [installingSlug, setInstallingSlug] = useState<string | null>(null);
  const [blockingSlug, setBlockingSlug] = useState<string | null>(null);
  const [editingSkill, setEditingSkill] = useState<string | null>(null);

  const filtered = useMemo(() => {
    return skills.filter((s) => {
      if (selectedCategory && s.category !== selectedCategory) return false;
      if (selectedRanks.length > 0 && !selectedRanks.includes(s.rank ?? "")) return false;
      if (search) {
        const q = search.toLowerCase();
        if (!s.name.toLowerCase().includes(q) && !(s.description ?? "").toLowerCase().includes(q)) return false;
      }
      return true;
    });
  }, [skills, search, selectedCategory, selectedRanks]);

  function toggleRank(rank: string) {
    setSelectedRanks((prev) =>
      prev.includes(rank) ? prev.filter((r) => r !== rank) : [...prev, rank]
    );
  }

  async function handleInstall(slug: string) {
    setInstallingSlug(slug);
    try {
      const res = await fetch("/api/marketplace/install", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ slug }),
      });
      if (!res.ok) {
        const { error } = await res.json() as { error: string };
        alert(`Install failed: ${error}`);
        return;
      }
      setSkills((prev) =>
        prev.map((s) => s.slug === slug ? { ...s, installed_at: new Date().toISOString() } : s)
      );
    } finally {
      setInstallingSlug(null);
    }
  }

  async function handleBlock(slug: string) {
    if (!confirm("Block this skill? It won't appear in the marketplace or be crawled again.")) return;
    setBlockingSlug(slug);
    try {
      const res = await fetch("/api/marketplace/block", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ slug }),
      });
      if (!res.ok) {
        const { error } = await res.json() as { error: string };
        alert(`Block failed: ${error}`);
        return;
      }
      setSkills((prev) => prev.filter((s) => s.slug !== slug));
    } finally {
      setBlockingSlug(null);
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
          value={selectedCategory}
          onChange={(e) => setSelectedCategory(e.target.value)}
          className="h-9 rounded-md border border-input bg-background px-3 text-sm shadow-sm focus:outline-none focus:ring-1 focus:ring-ring"
        >
          <option value="">{ALL_CATEGORIES_LABEL}</option>
          {categories.map((c) => (
            <option key={c} value={c}>{c}</option>
          ))}
        </select>

        <div className="flex items-center gap-2">
          {RANKS.map((rank) => (
            <label key={rank} className="flex items-center gap-1 cursor-pointer select-none">
              <input
                type="checkbox"
                checked={selectedRanks.includes(rank)}
                onChange={() => toggleRank(rank)}
                className="rounded"
              />
              <span className="text-sm font-medium">{rank}</span>
            </label>
          ))}
        </div>

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
            <MarketplaceSkillCard
              key={skill.slug}
              skill={skill}
              onInstall={handleInstall}
              onBlock={handleBlock}
              onEditMeta={isAdmin ? setEditingSkill : undefined}
              installing={installingSlug === skill.slug}
              blocking={blockingSlug === skill.slug}
              isAdmin={isAdmin}
            />
          ))}
        </div>
      )}
      {editingSkill && (
        <SkillMetaEditModal
          skillName={editingSkill}
          open={!!editingSkill}
          onClose={() => setEditingSkill(null)}
          onSaved={() => setEditingSkill(null)}
        />
      )}
    </div>
  );
}
