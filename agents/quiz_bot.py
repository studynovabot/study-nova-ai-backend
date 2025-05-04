from ufrom utils.groq_wrapper import ask_groq
from utils.groq_wrapper import ask_groq

async def quiz_agent(question):
    prompt = f"You are a Quiz Master. Analyze this student response: {question}"
    return await ask_groq(prompt, model="llama-3.3-70b-versatile")
