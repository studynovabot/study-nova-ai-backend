from agents.planner import planner_agent
from agents.xp_tracker import xp_agent
from agents.quiz_bot import quiz_agent

async def run_crew(question):
    # Simple round-robin agent simulation for now
    responses = []
    responses.append(await planner_agent(question))
    responses.append(await quiz_agent(question))
    responses.append(await xp_agent(question, responses[-1]))
    return " | ".join(responses)