import random
import time
from time import sleep

from art import logo

symbol_to_value = {
    "Ass": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
}

def get_stake_from_user(pocket):
    is_valid = False
    stake = 0
    while not is_valid:
        stake = input("Please enter a stake: ")
        if stake.isnumeric() and 0 < int(stake) <= pocket:
            is_valid = True
        else:
            print("Invalid stake.")
    return int(stake)

def deal_card():
    card_symbols = ["Ass", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    card_symbol = random.choice(card_symbols)
    return card_symbol



def calculate_score(cards):
    card_values = []
    for card in cards:
        card_values.append(symbol_to_value[card])

    if sum(card_values) == 21 and len(card_values) == 2:
        return 21

    while 11 in card_values and sum(card_values) > 21:
        card_values.remove(11)
        card_values.append(1)

    return sum(card_values)


def evaluate(user_score, computer_score, pocket, stake):
    print("")
    sleep(1)
    if user_score == computer_score:
        print("Draw 🙃")
        return pocket + stake
    elif computer_score == 21:
        print("Lose, opponent has Blackjack 😱")
        return pocket - stake
    elif user_score == 21:
        print("Win with a Blackjack 😎")
        return pocket + stake * 2
    elif user_score > 21:
        print("You went over. You lose 😭")
        return pocket - stake
    elif computer_score > 21:
        print("Opponent went over. You win 😁")
        return pocket + stake * 2
    elif user_score > computer_score:
        print("You win 😃")
        return pocket + stake * 2
    else:
        print("You lose 😤")
        return pocket - stake


def play_game(pocket):
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    stake = 0
    is_game_over = False
    stake = get_stake_from_user(pocket)

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"\nYour cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 21 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("\nType 'y' to get another card, type 'n' to pass: ")
            if user_should_deal.lower() == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while user_score <= 21 and computer_score != 21 and computer_score < 17:
        print(f"The computer's hand: {computer_cards}")
        print("Computer is dealt another card...")
        sleep(2)
        card = deal_card()
        print("The computer got: ", card)
        computer_cards.append(card)
        computer_score = calculate_score(computer_cards)

    sleep(1)
    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    return evaluate(user_score, computer_score, pocket, stake)

def main():
    pocket = 100
    game_continue = True
    print(logo)
    while game_continue:
        print(f"Your pocket: {pocket}")
        pocket = play_game(pocket)
        print(f"Your pocket: {pocket}")
        if pocket > 0:
            game_continue = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == "y"
        else:
            print("\nSorry, you're out of money. Game over.")
            game_continue = False

main()




