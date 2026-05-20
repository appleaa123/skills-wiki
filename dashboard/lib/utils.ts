import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

export function maskApiKey(key: string): string {
  if (key.length <= 8) return "sk-" + "*".repeat(8);
  return key.slice(0, 6) + "*".repeat(Math.max(key.length - 6, 10));
}

export function gatewayUrl(platform: "mcp" | "openapi") {
  const base = process.env.NEXT_PUBLIC_GATEWAY_BASE_URL || "http://localhost:8000"
  return platform === "openapi" ? `${base}/openapi.json` : `${base}/mcp`
}
