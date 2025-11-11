import random

from hangman_words import word_list
from hangman_asci2_art import stages, logo

def main():
    lives = len(stages) -1
    print(logo)

    chosen_word = random.choice(word_list)
    placeholder = "_" * len(chosen_word)
    print("Word to guess: " + placeholder)
    print(chosen_word)
    correct_letters = list(placeholder)

    while lives > 0:
        lives = invoke_next_round(lives, correct_letters, chosen_word)
        if "".join(correct_letters) == chosen_word:
            print("****************************YOU WIN****************************")
            return

    print(f"***********************IT WAS { str(chosen_word)}! YOU LOSE**********************")


def invoke_next_round(lives, correct_letters, chosen_word):
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess != "_" and guess in correct_letters:
        print(f"You've already guessed {guess}")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
    else:
        for i, letter in enumerate(chosen_word):
            if letter == guess:
                correct_letters[i] = guess

    print("Word to guess: " + "".join(correct_letters))
    print(stages[lives])

    return lives

main()