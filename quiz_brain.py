class Quiz:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def next(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        self.ask_question(current_question)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def ask_question(self, q):
        res = input(f"Q.{self.question_number} {q.text} (True/False):").lower()
        if res == q.answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer is {q.answer}")
        print("\n")
