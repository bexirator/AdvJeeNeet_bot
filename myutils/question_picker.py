import json
import random
import os

def get_questions(exam_name, count):
    exam_files = {
        "jeemains": "data/jeemains_questions.json",
        "jeeadv": "data/jeeadv_questions.json",
        "neet": "data/neet_questions.json"
    }

    filepath = exam_files.get(exam_name.lower())
    if not filepath or not os.path.exists(filepath):
        return ["❌ Question data not found for this exam."]

    with open(filepath, "r", encoding="utf-8") as f:
        all_questions = json.load(f)

    if count > len(all_questions):
        count = len(all_questions)

    return random.sample(all_questions, count)
