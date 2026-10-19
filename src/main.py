from fastapi import FastAPI

from .config import settings

app = FastAPI(title="Enterprise AI Project Template")


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "env": settings.app_env}
