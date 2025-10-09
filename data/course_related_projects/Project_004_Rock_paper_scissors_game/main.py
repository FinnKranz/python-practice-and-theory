import random

rock = """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
"""

paper = """
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

def main():
    options = [rock, paper, scissors]
    print("Welcome to the Rock Paper Scissors Game!")
    print("Choose one of the following options:\n"
          "0 - Stone\n1 - Paper\n2 - Scissors")

    user_number = int(input("Enter a number: "))
    if not 0 <= user_number <= 2:
        print("Invalid number!")
    print(f"You:\n{options[user_number]}")

    computer_number = random.randint(0, 2)
    print(f"The computer: {options[computer_number]}")

    print("\n")

    if user_number == computer_number:
        print("Draw!")
    elif (computer_number + 1) % 3 == user_number:
        print("You win!")
    else:
        print("You lose!")

main()





