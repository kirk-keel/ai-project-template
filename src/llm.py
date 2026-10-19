import httpx

from .config import settings


async def chat(prompt: str) -> str:
    """Send a prompt to the LiteLLM gateway and return the reply."""
    async with httpx.AsyncClient(timeout=120) as client:
        resp = await client.post(
            f"{settings.litellm_base}/v1/chat/completions",
            headers={"Authorization": f"Bearer {settings.litellm_key}"},
            json={
                "model": settings.llm_model,
                "messages": [{"role": "user", "content": prompt}],
            },
        )
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"]
