"use client";

import { useState } from "react";
import { Download, Copy, Check, Smartphone, User } from "lucide-react";
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";
import { Button } from "@/components/ui/button";
import { allSkills } from "@/lib/skills";

export type Platform = "claude" | "chatgpt" | "gemini" | "username";

const USERNAME_PLATFORM_USAGE: { platform: string; icon: string; usage: string }[] = [
  {
    platform: "Claude.ai",
    icon: "claude",
    usage: 'Go to Settings → Integrations → Add integration → expand Advanced settings → paste your User Name into the "OAuth Client ID" field.',
  },
  {
    platform: "ChatGPT",
    icon: "chatgpt",
    usage: "Your User Name is already embedded in the ChatGPT URL you copied — no extra step needed. It uniquely routes requests to your skill server.",
  },
  {
    platform: "Gemini",
    icon: "gemini",
    usage: "Your User Name is already embedded in the Gemini URL you copied — no extra step needed. The Chrome Extension uses it to connect to your skills.",
  },
];

const GUIDES: Record<Exclude<Platform, "username">, { title: string; steps: string[] }> = {
  claude: {
    title: "Connect to Claude.ai",
    steps: [
      "Open claude.ai and sign in.",
      "Go to Settings → Integrations → Add integration.",
      'Paste your Claude.ai URL into the "Remote MCP Server URL" field.',
      'Enter your API key (sk-…) when prompted for authentication.',
      "Click Connect — your skills will appear as tools immediately.",
    ],
  },
  chatgpt: {
    title: "Connect to ChatGPT (Custom GPT Actions)",
    steps: [
      "Go to chatgpt.com → Explore GPTs → Create → Configure → Actions → Add action.",
      'Click "Import from URL" and paste your ChatGPT URL to load the OpenAPI schema.',
      'Under Authentication, select "API Key", set Auth Type to "Bearer", and paste your sk-… key.',
      'Click "Save" to confirm authentication.',
      "Save the GPT — your skills appear as available actions.",
    ],
  },
  gemini: {
    title: "Connect to Gemini (Chrome Extension)",
    steps: [
      "Download the Skills Chrome Extension zip using the button below.",
      "Unzip into a permanent folder (do not delete after install).",
      "Open Chrome → chrome://extensions → toggle Developer Mode ON.",
      "Click Load Unpacked → select the unzipped folder.",
      "Click the extension icon → enter your Gemini URL + API key → Connect.",
      "Open gemini.google.com — the Skills panel appears bottom-right.",
    ],
  },
};

function buildMobileSkillJSON(enabledSkills: string[]): string {
  const skills = allSkills().filter((s) => enabledSkills.includes(s.name));
  if (skills.length === 0) return "{}";

  const output: Record<string, Record<string, { skill: string; description: string }>> = {};
  for (const s of skills) {
    output[s.name] = {};
    for (const tool of s.tools) {
      output[s.name][tool] = { skill: s.name, description: s.description };
    }
  }
  return JSON.stringify(output, null, 2);
}

interface SetupGuideProps {
  platform: Platform | null;
  onClose: () => void;
  enabledSkills?: string[];
}

export function SetupGuide({ platform, onClose, enabledSkills = [] }: SetupGuideProps) {
  const [jsonCopied, setJsonCopied] = useState(false);

  if (!platform) return null;
  const skillJson = buildMobileSkillJSON(enabledSkills);

  const copyJson = async () => {
    await navigator.clipboard.writeText(skillJson);
    setJsonCopied(true);
    setTimeout(() => setJsonCopied(false), 2000);
  };

  if (platform === "username") {
    return (
      <Dialog open onOpenChange={(open) => !open && onClose()}>
        <DialogContent className="max-w-md overflow-y-auto max-h-[90vh]">
          <DialogHeader>
            <DialogTitle className="flex items-center gap-2">
              <User className="h-4 w-4" />
              Your User Name
            </DialogTitle>
          </DialogHeader>
          <p className="text-sm text-muted-foreground mt-1">
            Your User Name is your unique identifier on SkillsHub. It tells each platform which skill server to connect to.
          </p>
          <div className="mt-4 space-y-4">
            {USERNAME_PLATFORM_USAGE.map(({ platform: name, usage }) => (
              <div key={name} className="rounded-lg border p-4 space-y-1.5">
                <p className="text-sm font-semibold">{name}</p>
                <p className="text-sm text-muted-foreground leading-relaxed">{usage}</p>
              </div>
            ))}
          </div>
        </DialogContent>
      </Dialog>
    );
  }

  const guide = GUIDES[platform];

  return (
    <Dialog open={!!platform} onOpenChange={(open) => !open && onClose()}>
      <DialogContent className="max-w-md overflow-y-auto max-h-[90vh]">
        <DialogHeader>
          <DialogTitle>{guide.title}</DialogTitle>
        </DialogHeader>

        <ol className="mt-2 space-y-3">
          {guide.steps.map((step, i) => (
            <li key={i} className="flex gap-3 text-sm">
              <span className="flex h-5 w-5 shrink-0 items-center justify-center rounded-full bg-primary text-primary-foreground text-xs font-semibold">
                {i + 1}
              </span>
              <span className="text-muted-foreground leading-relaxed break-words min-w-0">{step}</span>
            </li>
          ))}
        </ol>

        {platform === "gemini" && (
          <>
            <a href="/chrome-extension.zip" download className="mt-4 block">
              <Button variant="outline" className="w-full gap-2">
                <Download className="h-4 w-4" />
                Download Chrome Extension (.zip)
              </Button>
            </a>

            <div className="mt-6 border-t pt-5">
              <div className="flex items-center gap-2 mb-3">
                <Smartphone className="h-4 w-4 text-muted-foreground" />
                <p className="text-sm font-medium">On mobile (Gemini App)</p>
              </div>
              <ol className="space-y-3 mb-4">
                {[
                  "Copy your skill JSON using the button below.",
                  "Open the Gemini app and start a new conversation.",
                  "Paste the JSON as your first message — Gemini will use your skills as context.",
                ].map((step, i) => (
                  <li key={i} className="flex gap-3 text-sm">
                    <span className="flex h-5 w-5 shrink-0 items-center justify-center rounded-full bg-muted text-muted-foreground text-xs font-semibold">
                      {i + 1}
                    </span>
                    <span className="text-muted-foreground leading-relaxed break-words min-w-0">{step}</span>
                  </li>
                ))}
              </ol>
              <pre className="mb-3 rounded-md border bg-muted p-3 text-xs overflow-auto max-h-48 whitespace-pre">
                {skillJson}
              </pre>
              <Button variant="outline" className="w-full gap-2" onClick={copyJson}>
                {jsonCopied ? (
                  <><Check className="h-4 w-4 text-green-600" /> Copied!</>
                ) : (
                  <><Copy className="h-4 w-4" /> Copy skill JSON for Gemini App</>
                )}
              </Button>
            </div>
          </>
        )}
      </DialogContent>
    </Dialog>
  );
}
