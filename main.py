from fastapi import FastAPI, Request
from crew_setup import run_crew

app = FastAPI()

@app.post("/ask")
async def ask_agent(request: Request):
    data = await request.json()
    question = data.get("question")
    if not question:
        return {"error": "No question provided"}
    result = await run_crew(question)
    return {"response": result}
