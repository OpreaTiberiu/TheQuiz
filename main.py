from question_model import Question
from data import question_data
from quiz_brain import Quiz

questions = []
for entry in question_data:
    questions.append(Question(entry))

quiz = Quiz(questions)

while quiz.still_has_questions():
    quiz.next()

print("You have completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")