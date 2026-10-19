from fastapi import FastAPI
from pydantic import BaseModel

from .config import settings
from .llm import chat

app = FastAPI(title="Enterprise AI Project Template")


class Prompt(BaseModel):
    prompt: str


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "env": settings.app_env}


@app.post("/chat")
async def chat_endpoint(body: Prompt) -> dict:
    return {"reply": await chat(body.prompt)}
