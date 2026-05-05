"use client";

import { useEffect, useState } from "react";
import { CheckCircle, Loader2 } from "lucide-react";

interface StatusBadgeProps {
  clientId: string;
  initialStatus: "pending" | "live";
}

export function StatusBadge({ clientId, initialStatus }: StatusBadgeProps) {
  const [status, setStatus] = useState(initialStatus);

  useEffect(() => {
    if (status === "live") return;

    const interval = setInterval(async () => {
      try {
        const res = await fetch(`/api/status?clientId=${clientId}`);
        if (!res.ok) return;
        const data = await res.json();
        if (data.status === "live") {
          setStatus("live");
          clearInterval(interval);
        }
      } catch {
        // swallow — just try again next tick
      }
    }, 5000);

    return () => clearInterval(interval);
  }, [clientId, status]);

  if (status === "live") {
    return (
      <span className="inline-flex items-center gap-1.5 text-xs font-medium text-green-600">
        <CheckCircle className="h-3.5 w-3.5" />
        Live
      </span>
    );
  }

  return (
    <span className="inline-flex items-center gap-1.5 text-xs font-medium text-amber-600">
      <Loader2 className="h-3.5 w-3.5 animate-spin" />
      Deploying…
    </span>
  );
}
