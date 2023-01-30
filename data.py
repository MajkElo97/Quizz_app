import requests
from question_model import Question

parameters = {
    "amount": 10,
    "type": "boolean"
}


def import_questions():
    response = requests.get(url="https://opentdb.com/api.php?", params=parameters)
    response.raise_for_status()
    question_data = response.json()["results"]
    question_bank = []
    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)
    return question_bank
