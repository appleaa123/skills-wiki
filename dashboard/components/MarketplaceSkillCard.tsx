"use client";

import { Star, ExternalLink, CheckCircle, Loader2, Ban, Pencil } from "lucide-react";
import { Button } from "@/components/ui/button";

export interface DimensionScores {
  practicality: number;
  clarity: number;
  automation: number;
  quality: number;
  impact: number;
}

export interface CatalogSkill {
  id: string;
  slug: string;
  name: string;
  author: string;
  repo_url: string;
  stars: number;
  category: string | null;
  rank: "S" | "A" | "B" | "C" | null;
  description: string | null;
  installed_at: string | null;
  library_name: string | null;
  scores: DimensionScores | null;
  blocked: boolean;
}

interface MarketplaceSkillCardProps {
  skill: CatalogSkill;
  onInstall: (slug: string) => Promise<void>;
  onBlock: (slug: string) => Promise<void>;
  onEditMeta?: (libraryName: string) => void;
  installing: boolean;
  blocking: boolean;
  isAdmin: boolean;
}

const RANK_STYLES: Record<string, string> = {
  S: "bg-yellow-400/20 text-yellow-700 border border-yellow-400",
  A: "bg-green-400/20 text-green-700 border border-green-400",
  B: "bg-blue-400/20 text-blue-700 border border-blue-400",
  C: "bg-gray-200 text-gray-600 border border-gray-300",
};

const DIMENSION_LABELS: (keyof DimensionScores)[] = [
  "practicality", "clarity", "automation", "quality", "impact",
];

function ScoreBar({ label, value }: { label: string; value: number }) {
  const pct = (value / 10) * 100;
  const color = value >= 8 ? "bg-green-500" : value >= 6 ? "bg-blue-500" : "bg-gray-400";
  return (
    <div className="flex items-center gap-2">
      <span className="w-20 shrink-0 text-xs text-muted-foreground capitalize">{label}</span>
      <div className="flex-1 h-1.5 rounded-full bg-muted overflow-hidden">
        <div className={`h-full rounded-full ${color}`} style={{ width: `${pct}%` }} />
      </div>
      <span className="w-4 text-xs text-right text-muted-foreground">{value}</span>
    </div>
  );
}

export function MarketplaceSkillCard({ skill, onInstall, onBlock, onEditMeta, installing, blocking, isAdmin }: MarketplaceSkillCardProps) {
  const rankStyle = RANK_STYLES[skill.rank ?? "C"];
  const isInstalled = skill.installed_at !== null;
  const label = skill.name.replace(/[-_]/g, " ").replace(/\b\w/g, (c) => c.toUpperCase());

  return (
    <div className="rounded-lg border bg-card p-4 flex flex-col gap-3">
      {/* Top row: rank + installed badge */}
      <div className="flex items-start justify-between gap-2">
        <span className={`shrink-0 rounded-md px-2 py-0.5 text-xs font-bold ${rankStyle}`}>
          {skill.rank ?? "?"}-Rank
        </span>
        {isInstalled && (
          <span className="flex items-center gap-1 rounded-full bg-primary/10 px-2 py-0.5 text-xs font-medium text-primary">
            <CheckCircle className="h-3 w-3" />
            Installed
          </span>
        )}
      </div>

      {/* Name + author + description */}
      <div>
        <p className="font-medium text-sm">{label}</p>
        <p className="text-xs text-muted-foreground mt-0.5">by {skill.author}</p>
        {skill.description && (
          <p className="mt-2 text-xs text-muted-foreground leading-relaxed line-clamp-3">
            {skill.description}
          </p>
        )}
      </div>

      {/* 5-dimension score bars */}
      {skill.scores && (
        <div className="flex flex-col gap-1.5 py-1">
          {DIMENSION_LABELS.map((dim) => (
            <ScoreBar key={dim} label={dim} value={skill.scores![dim]} />
          ))}
        </div>
      )}

      {/* Stars + category */}
      <div className="flex items-center gap-3 text-xs text-muted-foreground">
        <span className="flex items-center gap-1">
          <Star className="h-3 w-3" />
          {skill.stars.toLocaleString()}
        </span>
        {skill.category && (
          <span className="rounded-md bg-muted px-2 py-0.5">{skill.category}</span>
        )}
      </div>

      {/* Actions */}
      <div className="flex items-center gap-2 mt-auto pt-1">
        <a
          href={skill.repo_url}
          target="_blank"
          rel="noopener noreferrer"
          className="flex items-center gap-1 text-xs text-muted-foreground hover:text-foreground transition-colors"
        >
          <ExternalLink className="h-3 w-3" />
          GitHub
        </a>

        <div className="ml-auto flex items-center gap-2">
          {isAdmin && skill.library_name && (
            <Button
              size="sm"
              variant="ghost"
              className="h-7 text-xs"
              onClick={() => onEditMeta?.(skill.library_name!)}
              title="Edit skill metadata"
            >
              <Pencil className="h-3 w-3" />
            </Button>
          )}
          {isAdmin && (
            <Button
              size="sm"
              variant="ghost"
              className="h-7 text-xs text-destructive hover:text-destructive hover:bg-destructive/10"
              disabled={blocking}
              onClick={() => onBlock(skill.slug)}
              title="Block this skill — won't appear again"
            >
              {blocking ? <Loader2 className="h-3 w-3 animate-spin" /> : <Ban className="h-3 w-3" />}
            </Button>
          )}

          <Button
            size="sm"
            variant={isInstalled ? "outline" : "default"}
            className="h-7 text-xs"
            disabled={isInstalled || installing}
            onClick={() => onInstall(skill.slug)}
          >
            {installing ? (
              <>
                <Loader2 className="h-3 w-3 animate-spin mr-1" />
                Installing…
              </>
            ) : isInstalled ? (
              "Installed"
            ) : (
              "Install"
            )}
          </Button>
        </div>
      </div>
    </div>
  );
}
