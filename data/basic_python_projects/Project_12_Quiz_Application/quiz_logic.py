class QuizLogic:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1#
        print(f"Q.{self.question_number}: {current_question.text}")
        user_answer = input("0 - False\n1 - True\nYour answer:")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        try:
            user_answer = int(user_answer)
        except ValueError:
            user_answer = -1

        if int(user_answer) == correct_answer:
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {"True" if correct_answer else "False"}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")



