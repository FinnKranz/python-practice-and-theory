from question_model import Question
from data import question_data
from quiz_logic import QuizLogic

def main():
    print_greetings()
    question_bank = []
    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

    quiz = QuizLogic(question_bank)

    while quiz.still_has_questions():
        quiz.next_question()

    print_farewell(quiz)


def print_greetings():
    print("Welcome to the Quiz Game!")
    print("You will be presented with a series of questions.")
    print("For each question, you will be presented with a choice of answers.")
    print("Your answer will determine the final score.")
    print("Good luck!")
    print("\n")

def print_farewell(quiz):
    print("You've completed the quiz")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}")
    print("\nThank you for playing the Quiz Game!")


main()