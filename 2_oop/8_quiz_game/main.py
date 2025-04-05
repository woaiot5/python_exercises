from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from os import system, name


def clear_screen():
    system('cls' if name == 'nt' else 'clear')


question_bank = []
for q in question_data:
    question_bank.append(Question(q["text"], q["answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    clear_screen()
