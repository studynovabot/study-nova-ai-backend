def evaluate_xp(answer: str):
    if "excellent" in answer.lower():
        return 30, "Amazing answer"
    elif "good" in answer.lower():
        return 20, "Decent answer"
    elif "okay" in answer.lower() or "average" in answer.lower():
        return 10, "Needs improvement"
    return 0, "Incorrect or irrelevant"