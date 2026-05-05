"use client";

import Link from "next/link";
import { AlertCircle, CheckCircle, ExternalLink, Loader2, Wrench } from "lucide-react";
import { Button } from "@/components/ui/button";
import type { SkillMeta } from "@/lib/skills";

interface UserSkillCardProps {
  skill: SkillMeta;
  themeLabel: string;
  isInstalled: boolean;
  onInstall: (name: string) => Promise<void>;
  installing: boolean;
  connectedServices?: string[];
}

export function UserSkillCard({ skill, themeLabel, isInstalled, onInstall, installing, connectedServices = [] }: UserSkillCardProps) {
  const missingServices = (skill.requires ?? []).filter((s) => !connectedServices.includes(s));
  return (
    <div className="rounded-lg border bg-card p-4 flex flex-col gap-3">
      {/* Top row: installed badge */}
      <div className="flex items-start justify-between gap-2 min-h-[24px]">
        <span className="rounded-md bg-muted px-2 py-0.5 text-xs text-muted-foreground">
          {themeLabel}
        </span>
        {isInstalled && (
          <span className="flex items-center gap-1 rounded-full bg-primary/10 px-2 py-0.5 text-xs font-medium text-primary">
            <CheckCircle className="h-3 w-3" />
            Installed
          </span>
        )}
      </div>

      {/* Name + description */}
      <div>
        <p className="font-medium text-sm">{skill.displayName}</p>
        <p className="mt-2 text-xs text-muted-foreground leading-relaxed line-clamp-3">
          {skill.description}
        </p>
      </div>

      {/* Tools count */}
      {skill.tools.length > 0 && (
        <div className="flex items-center gap-1 text-xs text-muted-foreground">
          <Wrench className="h-3 w-3" />
          {skill.tools.length} {skill.tools.length === 1 ? "tool" : "tools"}
        </div>
      )}

      {/* Service setup badge */}
      {isInstalled && missingServices.length > 0 && (
        <Link
          href="/connections"
          className="flex items-center gap-1 text-xs text-amber-600 hover:text-amber-700 transition-colors"
        >
          <AlertCircle className="h-3 w-3" />
          Needs setup →
        </Link>
      )}

      {/* GitHub source link */}
      {skill.githubUrl && (
        <a
          href={skill.githubUrl}
          target="_blank"
          rel="noopener noreferrer"
          className="flex items-center gap-1 text-xs text-muted-foreground hover:text-foreground transition-colors"
        >
          <ExternalLink className="h-3 w-3" />
          GitHub
        </a>
      )}

      {/* Install action */}
      <div className="mt-auto pt-1">
        <Button
          size="sm"
          variant={isInstalled ? "outline" : "default"}
          className="h-7 text-xs w-full"
          disabled={isInstalled || installing}
          onClick={() => onInstall(skill.name)}
        >
          {installing ? (
            <>
              <Loader2 className="h-3 w-3 animate-spin mr-1" />
              Adding…
            </>
          ) : isInstalled ? (
            "Added"
          ) : (
            "Add to Skills"
          )}
        </Button>
      </div>
    </div>
  );
}
