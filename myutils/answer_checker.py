def check_answer(user_input):
    if "force" in user_input.lower():
        return "✔️ Correct! This involves Newton's Laws."
    elif "wrong" in user_input.lower():
        return "❌ Incorrect. Try reviewing the concept again."
    else:
        return "🤔 Could not verify. Type `explain ache se` for more help."