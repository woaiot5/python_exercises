class QuizBrain:
    def __init__(self, all_questions):
        self.question_number = 0
        self.question_list = all_questions
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)


    def keep_score(self, result):
        if result:
            self.score += 1
            print("That's correct!")
        else:
            print("Incorrect :(")
        input(f"Your score: {self.score}\n")



    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        player_answer = input(f"Q.{self.question_number}/{len(self.question_list)}: {current_question.text} (True/False): ").capitalize()
        result = current_question.answer == player_answer
        self.keep_score(result)


