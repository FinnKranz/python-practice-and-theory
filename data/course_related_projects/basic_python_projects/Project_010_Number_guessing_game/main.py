from random import randint
from art import logo


EASY_LEVEL_TURNS = 12
MEDIUM_LEVEL_TURNS = 8
HARD_LEVEL_TURNS = 4


def is_correct_answer(user_guess, actual_answer):
    if user_guess > actual_answer:
        print("Too high.")
        return False
    elif user_guess < actual_answer:
        print("Too low.")
        return False
    else:
        print(f"You got it! The answer was {actual_answer}")
        return True


# Function to set difficulty
def set_difficulty():
    is_invalid = True
    level = ""
    while is_invalid:
        print("Choose a difficulty.\n1 - easy\n2 - medium\n3 - hard")
        level = input("Type your choice:")
        if level.isnumeric() and 1 <= int(level) <= 3:
            is_invalid = False
        else:
            print("Invalid choice. Try again.")

    match level:
        case "1":
            return EASY_LEVEL_TURNS
        case "2":
            return MEDIUM_LEVEL_TURNS
        case "3":
            return HARD_LEVEL_TURNS


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("\nI'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    turns = set_difficulty()
    continue_game = True

    while continue_game:
        print(f"\nYou have {turns} attempts remaining to guess the number.")

        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if is_correct_answer(guess, answer):
            return
        else :
            turns -= 1

        if turns == 0:
            print("You've run out of guesses, you lose.")
            continue_game = False
        elif guess != answer:
            print("Guess again.")


game()


