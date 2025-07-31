import random

tips = [
    "💡 Use spaced repetition to improve memory recall.",
    "🧘 Breathe deeply before tests to calm anxiety.",
    "⏱️ Practice mock tests under timed conditions.",
    "📌 Review your mistakes after every test attempt.",
    "🎯 Focus on concepts, not just formulas."
]

def get_tip():
    return random.choice(tips)