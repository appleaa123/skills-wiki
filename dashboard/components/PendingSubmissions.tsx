"use client";

import { useEffect, useState } from "react";
import { Button } from "@/components/ui/button";

interface Submission {
  id: string;
  user_email: string | null;
  skill_name: string;
  repo_url: string;
  status: "pending" | "approved" | "rejected";
  submitted_at: string;
  reviewed_at: string | null;
  reviewed_by: string | null;
}

const STATUS_BADGE: Record<string, string> = {
  pending: "bg-yellow-100 text-yellow-800",
  approved: "bg-green-100 text-green-800",
  rejected: "bg-red-100 text-red-800",
};

function timeAgo(iso: string): string {
  const diff = Date.now() - new Date(iso).getTime();
  const m = Math.floor(diff / 60000);
  if (m < 60) return `${m}m ago`;
  const h = Math.floor(m / 60);
  if (h < 24) return `${h}h ago`;
  return `${Math.floor(h / 24)}d ago`;
}

export function PendingSubmissions() {
  const [submissions, setSubmissions] = useState<Submission[]>([]);
  const [loading, setLoading] = useState(true);
  const [actioning, setActioning] = useState<string | null>(null);

  const load = async () => {
    const res = await fetch("/api/skills/submitted");
    if (res.ok) {
      const data = await res.json() as { submissions: Submission[] };
      setSubmissions(data.submissions ?? []);
    }
    setLoading(false);
  };

  useEffect(() => { load(); }, []);

  const act = async (id: string, action: "approve" | "reject") => {
    setActioning(id);
    await fetch(`/api/skills/${action}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ id }),
    });
    setActioning(null);
    await load();
  };

  if (loading) return <p className="text-sm text-muted-foreground">Loading submissions…</p>;
  if (submissions.length === 0) return null;

  return (
    <div className="mb-10">
      <h2 className="text-lg font-semibold mb-3">Pending Submissions</h2>
      <div className="rounded-lg border bg-white overflow-hidden">
        <table className="w-full text-sm">
          <thead className="bg-muted/50 border-b">
            <tr>
              <th className="px-4 py-2.5 text-left font-medium text-xs text-muted-foreground">Submitted by</th>
              <th className="px-4 py-2.5 text-left font-medium text-xs text-muted-foreground">Skill name</th>
              <th className="px-4 py-2.5 text-left font-medium text-xs text-muted-foreground">Repo URL</th>
              <th className="px-4 py-2.5 text-left font-medium text-xs text-muted-foreground">When</th>
              <th className="px-4 py-2.5 text-left font-medium text-xs text-muted-foreground">Status</th>
              <th className="px-4 py-2.5 text-left font-medium text-xs text-muted-foreground">Actions</th>
            </tr>
          </thead>
          <tbody className="divide-y">
            {submissions.map((s) => (
              <tr key={s.id} className="hover:bg-muted/20">
                <td className="px-4 py-3 text-xs text-muted-foreground">{s.user_email ?? "—"}</td>
                <td className="px-4 py-3 font-mono text-xs">{s.skill_name}</td>
                <td className="px-4 py-3">
                  <a
                    href={s.repo_url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-xs text-blue-600 hover:underline truncate max-w-[200px] block"
                  >
                    {s.repo_url.replace("https://github.com/", "")}
                  </a>
                </td>
                <td className="px-4 py-3 text-xs text-muted-foreground whitespace-nowrap">{timeAgo(s.submitted_at)}</td>
                <td className="px-4 py-3">
                  <span className={`rounded px-1.5 py-0.5 text-[10px] font-medium ${STATUS_BADGE[s.status] ?? ""}`}>
                    {s.status}
                  </span>
                </td>
                <td className="px-4 py-3">
                  {s.status === "pending" ? (
                    <div className="flex gap-2">
                      <Button
                        size="sm"
                        variant="outline"
                        className="h-6 text-xs text-green-700 border-green-300 hover:bg-green-50"
                        disabled={actioning === s.id}
                        onClick={() => act(s.id, "approve")}
                      >
                        Approve
                      </Button>
                      <Button
                        size="sm"
                        variant="outline"
                        className="h-6 text-xs text-red-600 border-red-300 hover:bg-red-50"
                        disabled={actioning === s.id}
                        onClick={() => act(s.id, "reject")}
                      >
                        Reject
                      </Button>
                    </div>
                  ) : (
                    <span className="text-xs text-muted-foreground">
                      {s.reviewed_by ?? "—"}
                    </span>
                  )}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
