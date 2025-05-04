from utils.groq_wrapper import ask_groq

async def planner_agent(question):
    prompt = f"You are a Study Planner. Help the student with this: {question}"
    return await ask_groq(prompt, model="gemma-7b-it")