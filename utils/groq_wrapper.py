import httpx
import os

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

async def ask_groq(prompt, model="gemma2-9b-it"):
    headers = {
        "Authorization": f"Bearer {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}",
        "Content-Type": "application/json"
    }
    json_data = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}]
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(GROQ_API_URL, headers=headers, json=json_data)
        res = response.json()
        return res["choices"][0]["message"]["content"]
