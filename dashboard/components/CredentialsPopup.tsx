"use client";

import { useState } from "react";
import { Check, Copy, Eye, EyeOff, BookOpen } from "lucide-react";
import { Button } from "@/components/ui/button";
import { SetupGuide, type Platform } from "@/components/SetupGuide";
import { StatusBadge } from "@/components/StatusBadge";
import { maskApiKey } from "@/lib/utils";

interface Credentials {
  clientId: string;
  apiKey: string;
  claudeUrl: string;
  chatgptUrl: string;
  geminiUrl: string;
  status: "pending" | "live";
  username?: string;
}

interface CredentialsPopupProps {
  credentials: Credentials;
  enabledSkills?: string[];
}

function CopyRow({
  label,
  value,
  onGuide,
}: {
  label: string;
  value: string;
  onGuide: () => void;
}) {
  const [copied, setCopied] = useState(false);

  const copy = async () => {
    await navigator.clipboard.writeText(value);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className="space-y-1">
      <p className="text-xs font-medium text-muted-foreground">{label}</p>
      <div className="flex items-center gap-2">
        <code className="flex-1 truncate rounded-md bg-muted px-3 py-2 text-xs font-mono">
          {value}
        </code>
        <Button variant="outline" size="icon" className="h-8 w-8 shrink-0" onClick={copy}>
          {copied ? <Check className="h-3.5 w-3.5 text-green-600" /> : <Copy className="h-3.5 w-3.5" />}
        </Button>
        <Button variant="outline" size="icon" className="h-8 w-8 shrink-0" onClick={onGuide} title="Setup guide">
          <BookOpen className="h-3.5 w-3.5" />
        </Button>
      </div>
    </div>
  );
}

function ApiKeyRow({ apiKey }: { apiKey: string }) {
  const [revealed, setRevealed] = useState(false);
  const [copied, setCopied] = useState(false);

  const copy = async () => {
    await navigator.clipboard.writeText(apiKey);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className="space-y-1">
      <p className="text-xs font-medium text-muted-foreground">API Key</p>
      <div className="flex items-center gap-2">
        <code className="flex-1 truncate rounded-md bg-muted px-3 py-2 text-xs font-mono">
          {revealed ? apiKey : maskApiKey(apiKey)}
        </code>
        <Button
          variant="outline"
          size="icon"
          className="h-8 w-8 shrink-0"
          onClick={() => setRevealed((v) => !v)}
          title={revealed ? "Hide" : "Reveal"}
        >
          {revealed ? <EyeOff className="h-3.5 w-3.5" /> : <Eye className="h-3.5 w-3.5" />}
        </Button>
        <Button variant="outline" size="icon" className="h-8 w-8 shrink-0" onClick={copy}>
          {copied ? <Check className="h-3.5 w-3.5 text-green-600" /> : <Copy className="h-3.5 w-3.5" />}
        </Button>
      </div>
    </div>
  );
}

export function CredentialsPopup({ credentials, enabledSkills = [] }: CredentialsPopupProps) {
  const [guideOpen, setGuideOpen] = useState<Platform | null>(null);

  return (
    <>
      <div className="rounded-xl border bg-card p-6 shadow-lg space-y-5">
        <div className="flex items-center justify-between">
          <div>
            <h2 className="text-lg font-semibold">Your skills are ready!</h2>
            <p className="text-sm text-muted-foreground mt-0.5">
              Copy a URL and API key to connect your preferred platform.
            </p>
          </div>
          <StatusBadge
            clientId={credentials.clientId}
            initialStatus={credentials.status}
          />
        </div>

        <div className="space-y-4">
          <CopyRow
            label="User Name"
            value={credentials.clientId}
            onGuide={() => setGuideOpen("username")}
          />
          <CopyRow
            label="Claude.ai URL"
            value={credentials.claudeUrl}
            onGuide={() => setGuideOpen("claude")}
          />
          <CopyRow
            label="ChatGPT URL"
            value={credentials.chatgptUrl}
            onGuide={() => setGuideOpen("chatgpt")}
          />
          <CopyRow
            label="Gemini URL"
            value={credentials.geminiUrl}
            onGuide={() => setGuideOpen("gemini")}
          />
          <ApiKeyRow apiKey={credentials.apiKey} />
        </div>

        <p className="text-xs text-muted-foreground">
          Store your API key safely — you can view it again from your dashboard.
        </p>
      </div>

      <SetupGuide platform={guideOpen} onClose={() => setGuideOpen(null)} enabledSkills={enabledSkills} />
    </>
  );
}
