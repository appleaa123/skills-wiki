# Skills Wiki — Open Source Local Platform

> A locally runnable, self-contained multi-LLM assistant platform that delivers specialized AI skill packs to your favorite AI interfaces.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Skills Wiki fills the gap between what your AI assistant can do out of the box and what your business actually needs. This open-source version allows you to run the entire stack locally via Docker, giving you full control over your tools and data.

---

## 🚀 Quick Start

Run the entire platform with a single command:

```bash
npm start
```

*This command orchestrates `docker compose up --build` to launch the Python backend and Next.js dashboard.*

Once started:
- **Dashboard**: Access [http://localhost:3000](http://localhost:3000)
- **FastMCP Backend**: Running on [http://localhost:8000](http://localhost:8000)

---

## ✨ Features

- **Local Skill Library** — Access 100+ community-contributed skill packs (Amazon, SEO, Marketing, Engineering, etc.) natively from your local machine.
- **FastMCP Architecture** — High-performance Python backend built for low-latency tool execution and modular skill management.
- **Universal Connection** — Seamlessly connect to Claude Desktop, Claude.ai, ChatGPT, and Gemini using a single local endpoint.
- **Zero-Config Database** — No external Supabase or Postgres required. Uses a local JSON-based persistence layer (`db.json`) that stays on your machine.
- **Docker-First** — Fully containerized services ensuring a consistent environment and easy deployment.

---

## 🛠 Prerequisites

- [Docker](https://www.docker.com/products/docker-desktop/) & Docker Compose
- [Node.js](https://nodejs.org/) (v18+)

---

## 📖 How to Use

### 1. Configure Your Skills
Open the **Dashboard** at `http://localhost:3000`. Browse the **Marketplace** and click **Install** to enable specific skill packs. Your choices are saved instantly to your local `db.json`.

### 2. Connect Your Assistant

#### Claude Desktop
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "local-skills": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-http", "--url", "http://localhost:8000/sse"]
    }
  }
}
```

#### ChatGPT (Custom GPTs)
1. In GPT Actions, use **Import from URL**: `http://localhost:8000/openapi.json`.
2. (Note: Requires a local tunnel like `ngrok` if you are using the ChatGPT web interface).

#### Gemini (Web)
Use the included Chrome Extension files to bridge Gemini's web interface to your local skill server.

---

## 🏗 Architecture

```
User Browser (Next.js Dashboard) <───> Local JSON DB (~/.skills-wiki/db.json)
                                              │
                                              ▼
LLM Assistant (Claude/GPT/Gemini) <───> FastMCP Server (Python)
                                              │
                                              ▼
                                       Skill Library (100+ Skills)
```

---

## 🤝 Contributing

We welcome contributions!
1. Add new skill packs to `skills_library/`.
2. Improve the dashboard in `dashboard/`.
3. Enhance the core runtime in `core/`.

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
