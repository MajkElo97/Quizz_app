import ui
from data import import_questions
from quiz_brain import QuizBrain
# from ui import *
question_bank = []
question_bank = import_questions()

quiz = QuizBrain(question_bank)
quiz_ui = ui.QuizInterface(quiz)
# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
