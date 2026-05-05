"use client";

import { Wrench } from "lucide-react";
import type { SkillMeta } from "@/lib/skills";

interface SkillCardProps {
  skill: SkillMeta;
  assigned?: boolean;
}

export function SkillCard({ skill, assigned = false }: SkillCardProps) {
  const label = skill.displayName || skill.name.replace(/_/g, " ").replace(/\b\w/g, (c) => c.toUpperCase());

  return (
    <div className={`rounded-lg border p-4 ${assigned ? "border-primary/40 bg-primary/5" : "border-border bg-card"}`}>
      <div className="flex items-start justify-between gap-2">
        <div>
          <p className="font-medium text-sm">{label}</p>
          <p className="mt-1 text-xs text-muted-foreground leading-relaxed">
            {skill.description}
          </p>
        </div>
        {assigned && (
          <span className="shrink-0 rounded-full bg-primary/10 px-2 py-0.5 text-xs font-medium text-primary">
            Active
          </span>
        )}
      </div>
      <div className="mt-3 flex flex-wrap gap-1">
        {skill.tools.map((tool) => (
          <span
            key={tool}
            className="inline-flex items-center gap-1 rounded-md bg-muted px-2 py-0.5 text-xs text-muted-foreground"
          >
            <Wrench className="h-3 w-3" />
            {tool}
          </span>
        ))}
      </div>
    </div>
  );
}
