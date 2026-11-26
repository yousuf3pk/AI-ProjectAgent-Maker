# Backend

FastAPI service for the standalone Xander assistant.

## Run locally

Requires Python 3.11 or newer and [uv](https://docs.astral.sh/uv/). Configure
the required local environment variables before starting the service. Keep
credentials in a local `.env` file and never commit them.

```sh
uv sync
uv run fastapi dev main.py
```

By default, FastAPI serves the application on `http://127.0.0.1:8000`.
