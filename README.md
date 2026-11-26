# AI Project Agent Maker

A monorepo of AI agent services and web interfaces, built primarily with FastAPI,
LangGraph, and Next.js.

## Projects

- **`LanGraph_Development_Team/`** — FastAPI and LangGraph service for the
  development-team workflow. It stores runs in PostgreSQL.
- **`Dev-Team-Frontend/`** — Next.js interface for the development-team service.
- **`Backend/`** — FastAPI service for the standalone Xander assistant.
- **`Frontend/`** — Next.js client for the standalone assistant.

Each project may have its own dependencies and configuration. See its README
for project-specific details.

## Run the development-team app

You need Python 3.10 or newer, [uv](https://docs.astral.sh/uv/), Node.js 22.17 or
newer, and a PostgreSQL database.

1. Configure the backend's local environment, including `DATABASE_URL` and the
   credentials required by the model provider. Keep secrets in local
   environment files; do not commit them.
2. Start the backend:

   ```sh
   cd LanGraph_Development_Team
   uv sync
   uv run fastapi dev main.py --host 127.0.0.1 --port 8000
   ```

3. In a second terminal, start the frontend:

   ```sh
   cd Dev-Team-Frontend
   npm install
   npm run dev
   ```

Open [http://localhost:3000](http://localhost:3000). The frontend's server-side
proxy uses `BACKEND_URL` (defaults to `http://localhost:8000`); see
`Dev-Team-Frontend/README.md` for configuration and checks.

## Local configuration

Do not commit credentials, `.env` files, virtual environments, dependency
directories, or generated caches. The root `.gitignore` excludes these local
files while allowing `.env.example` templates.
