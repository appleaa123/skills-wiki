export interface ServiceField {
  key: string;
  label: string;
  placeholder: string;
  sensitive: boolean;
  optional?: boolean;
}

export interface ServiceDefinition {
  label: string;
  description: string;
  fields: ServiceField[];
  platformLinks: {
    claude?: string;
    chatgpt?: string;
    gemini?: string;
  };
}

export const SUPPORTED_SERVICES: Record<string, ServiceDefinition> = {
  supabase: {
    label: "Supabase",
    description: "Connect your Supabase project to let skills query your database.",
    fields: [
      { key: "url", label: "Project URL", placeholder: "https://xxxx.supabase.co", sensitive: false },
      { key: "publishable_key", label: "Publishable Key", placeholder: "eyJ...", sensitive: true },
      { key: "secret_key", label: "Secret Key (optional — bypasses RLS)", placeholder: "eyJ...", sensitive: true, optional: true },
    ],
    platformLinks: {},
  },
  github: {
    label: "GitHub",
    description: "GitHub personal access token for repository and issue access.",
    fields: [
      { key: "token", label: "Personal Access Token", placeholder: "ghp_...", sensitive: true },
    ],
    platformLinks: {
      claude: "https://claude.ai/settings/integrations",
    },
  },
  notion: {
    label: "Notion",
    description: "Notion integration token for reading and writing pages.",
    fields: [
      { key: "token", label: "Integration Token", placeholder: "secret_...", sensitive: true },
    ],
    platformLinks: {
      claude: "https://claude.ai/settings/integrations",
    },
  },
  openai: {
    label: "OpenAI",
    description: "OpenAI API key for skills that call GPT models directly.",
    fields: [
      { key: "api_key", label: "API Key", placeholder: "sk-...", sensitive: true },
    ],
    platformLinks: {},
  },
};

export type ServiceId = keyof typeof SUPPORTED_SERVICES;

export function isCustomService(service: string): boolean {
  return !(service in SUPPORTED_SERVICES);
}
