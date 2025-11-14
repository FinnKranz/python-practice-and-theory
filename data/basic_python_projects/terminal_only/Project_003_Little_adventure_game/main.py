
def main ():
    print_start()

    survived = print_first_level()
    if not survived:
        return

    survived = print_second_level()
    if not survived:
        return

    print("You've survived. Well done!")

def print_start ():
    print("Welcome to escape room.\nWill you survive?\n")

def print_first_level ():
    print("You are locked in a dark room. "
          "Above you hangs a lamp with a dimly flickering light bulb.\n"
          "A few meters in front of you, you hear the menacing growl of an animal, "
          "while behind you there is a strange rustling sound.\n\n"
          "What would you like to do?\n"
          "A: Turn the light bulb to make it light up again.\n"
          "B: Carefully approach the growling animal.\n"
          "C: Turn around to look for the source of the rustling sound."
    )

    decision = input("Your decision:").lower()
    print("")
    if decision == "a":
        print("You carefully twist the light bulb and receive a strong electric shock.\n"
              "You fall to the floor, convulsing.\n"
              "Game over."
        )
        return False
    elif decision == "b":
        print("You walk purposefully towards the growling sound.\n"
              "Suddenly, something sprints out of the darkness...and...licks you happily, barking.\n"
              "It's a dog. There's a small button on its collar.\n"
              "You press it and it starts to glow. Now you can finally see some."
        )
        return True
    elif decision == "c":
        print("You turn around and slowly crawl towards the rustling sound.\n"
              "Suddenly, you feel a sharp pain in your hand. It's a bite.\n"
              "You grab your hand and feel the head of a snake.\n"
              "You crawl through the darkness, trembling, for a few more minutes. Then it's quiet.\n"
              "Game over."
        )
        return False
    else:
        print("You can't do that. Game over.")
        return False

def print_second_level ():
    print("\n")
    print(
        "With the glowing light, you notice a door to your left, a ladder leading upward, and a tunnel behind the dog.\n"
        "What would you like to do?\n"
        "A: Open the door and step through.\n"
        "B: Climb the ladder to see where it leads.\n"
        "C: Crawl into the tunnel behind the dog."
        )

    decision = input("Your decision:").lower()
    print("")
    if decision == "a":
        print("You enter a bright room.\n"
              "Slowly, your eyes adjust to the brightness\n"
              "and you see a large crowd of people smiling at you and applauding.\n"
              "Someone hands you a trophy.\n"
        )
        return True
    elif decision == "b":
        print("You climb the ladder and emerge into a forest clearing.\n"
              "The air is cold and damp, and the trees stretch endlessly in every direction.\n"
              "You start walking, hoping to find help,\n"
              "but after hours of wandering, the forest offers no signs of life—no paths, no sounds, no shelter.\n"
              "Night falls, and the temperature drops sharply.\n"
              "Exhausted and disoriented, you collapse under a tree.\n"
              "Game over."
            )
        return False
    elif decision == "c":
        print("You crawl into the tunnel, but it narrows quickly.\n"
              "You're stuck. The dog barks anxiously.\n"
              "Game over."
        )
        return False
    else:
        print("You can't do that. Game over.")
        return False

main()

