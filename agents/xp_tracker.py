from utils.xp_evaluator import evaluate_xp

async def xp_agent(question, answer):
    score, reason = evaluate_xp(answer)
    return f"XP Awarded: {score} - Reason: {reason}"
