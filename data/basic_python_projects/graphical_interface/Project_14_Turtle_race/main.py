from turtle import Turtle, Screen
from tkinter import messagebox
import random

def init_screen():
    screen = Screen()
    screen.setup(width=500, height=400)
    return screen

def init_turtles(colors):
    y_positions = [80, 50, 20, -10, -40, -70]
    all_turtles = []
    for turtle_index in range(0, 6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(colors[turtle_index])
        new_turtle.goto(x=-230, y=y_positions[turtle_index])
        all_turtles.append(new_turtle)
    return all_turtles

def get_user_bet(screen, colors):
    message = "Which turtle will win the race? Choose a color:"
    for number in range(0,len(colors)):
        message += f"\n{number} - {colors[number]}"
    while True:
            try:
                chosen_clr = screen.textinput(title="Make your bet", prompt=message)
                index = int(chosen_clr)
                if 0 <= index < len(colors):
                    return colors[index]
                else:
                    raise ValueError
            except:
                messagebox.showinfo("Error", "Invalid number. Try again.")

def get_tutle_rank(all_turtles, target_turtle):
    turtles_sorted = sorted(all_turtles, key=lambda t: t.xcor(), reverse=True)
    return turtles_sorted.index(target_turtle) + 1


def start_race(all_turtles):
    while True:
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                winning_color = turtle.pencolor()
                return winning_color
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)

def evaluate_race_result(user_bet, winning_color, rank ):
    messagebox.showinfo(
        "You win!" if user_bet == winning_color else "You lose!",
        f"Your turtle finished in {rank} place."
    )

def main():
    screen = init_screen()
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    all_turtles = init_turtles(colors)
    user_bet = get_user_bet(screen, colors)
    winning_color= start_race(all_turtles)
    rank = get_tutle_rank(all_turtles, all_turtles[colors.index(user_bet)])
    evaluate_race_result(user_bet, winning_color, rank)

main()


