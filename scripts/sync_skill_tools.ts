#!/usr/bin/env npx tsx
// Syncs tool definitions from skills_library/{skill}/main.py into skill_catalog.tools.
// Local skills have no crawler-generated rows, so this script upserts them using
// library_name as the key (slug = folder name for locally-added skills).
//
// Run after adding new skills:
//   NODE_PATH=dashboard/node_modules npx tsx scripts/sync_skill_tools.ts

import fs from "fs";
import path from "path";
import { createClient } from "@supabase/supabase-js";
import { config } from "dotenv";

config({ path: path.join(__dirname, "../dashboard/.env.local") });

const SUPABASE_URL = process.env.NEXT_PUBLIC_SUPABASE_URL;
const SUPABASE_SERVICE_KEY = process.env.SUPABASE_SERVICE_ROLE_KEY;

if (!SUPABASE_URL || !SUPABASE_SERVICE_KEY) {
  console.error("Missing NEXT_PUBLIC_SUPABASE_URL or SUPABASE_SERVICE_ROLE_KEY in dashboard/.env.local");
  process.exit(1);
}

const supabase = createClient(SUPABASE_URL, SUPABASE_SERVICE_KEY);
const SKILLS_DIR = path.join(__dirname, "../skills_library");

function parseTools(src: string): Record<string, string> {
  const tools: Record<string, string> = {};
  const re =
    /(?:'([^']+)'|"([^"]+)"):\s*\{[^}]*?"description":\s*(?:'((?:[^'\\]|\\.)*)'|"((?:[^"\\]|\\.)*)")/g;
  let m: RegExpExecArray | null;
  while ((m = re.exec(src)) !== null) {
    const slug = m[1] ?? m[2] ?? "";
    const desc = m[3] ?? m[4] ?? "";
    if (slug) tools[slug] = desc;
  }
  return tools;
}

function authorFromRepoUrl(repoUrl: string): string {
  const m = repoUrl.match(/github\.com\/([^/]+)/);
  return m ? m[1] : "unknown";
}

async function main() {
  if (!fs.existsSync(SKILLS_DIR)) {
    console.error(`skills_library not found at ${SKILLS_DIR}`);
    process.exit(1);
  }

  const skillDirs = fs.readdirSync(SKILLS_DIR).filter((name) =>
    fs.existsSync(path.join(SKILLS_DIR, name, "main.py"))
  );

  console.log(`Found ${skillDirs.length} skills with main.py`);

  let inserted = 0;
  let updated = 0;
  let skipped = 0;

  for (const skillName of skillDirs) {
    const src = fs.readFileSync(path.join(SKILLS_DIR, skillName, "main.py"), "utf-8");
    const tools = parseTools(src);

    if (Object.keys(tools).length === 0) {
      skipped++;
      continue;
    }

    // Check if row already exists for this local skill
    const { data: existing } = await supabase
      .from("skill_catalog")
      .select("slug")
      .eq("library_name", skillName)
      .maybeSingle();

    if (existing) {
      const { error } = await supabase
        .from("skill_catalog")
        .update({ tools })
        .eq("library_name", skillName);
      if (error) { console.error(`  ✗ ${skillName}: ${error.message}`); }
      else { console.log(`  ✓ ${skillName}: ${Object.keys(tools).length} tools (updated)`); updated++; }
      continue;
    }

    // No existing row — insert one using skill_meta.json for required fields
    const metaPath = path.join(SKILLS_DIR, skillName, "skill_meta.json");
    const meta = fs.existsSync(metaPath)
      ? JSON.parse(fs.readFileSync(metaPath, "utf-8"))
      : {};

    const repoUrl = meta.source_repo ?? `https://github.com/local/${skillName}`;
    const { error } = await supabase.from("skill_catalog").insert({
      slug: skillName,
      name: meta.display_name ?? skillName,
      author: authorFromRepoUrl(repoUrl),
      repo_url: repoUrl,
      stars: 0,
      description: meta.description ?? "",
      category: meta.theme ?? null,
      library_name: skillName,
      tools,
    });

    if (error) {
      // slug conflict means a crawler row exists with slug = skillName — update it instead
      if (error.code === "23505") {
        const { error: e2 } = await supabase
          .from("skill_catalog")
          .update({ tools, library_name: skillName })
          .eq("slug", skillName);
        if (e2) { console.error(`  ✗ ${skillName}: ${e2.message}`); }
        else { console.log(`  ✓ ${skillName}: ${Object.keys(tools).length} tools (updated existing slug)`); updated++; }
      } else {
        console.error(`  ✗ ${skillName}: ${error.message}`);
      }
    } else {
      console.log(`  ✓ ${skillName}: ${Object.keys(tools).length} tools (inserted)`);
      inserted++;
    }
  }

  console.log(`\nDone. Inserted: ${inserted}, Updated: ${updated}, Skipped (no tools): ${skipped}`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
