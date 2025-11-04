from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def get_product_selection():
    while True:
        decision = input(
            "\nWhat would you like?\n1 - espresso\n2 - latte\n3 - cappuccino\n4 - off\n5 - report\nYour input:"
        )
        try:
            decision = int(decision)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if not 0 <= decision < 6:
            print("Invalid input. Please enter a number between 1 and 4.")
        else:
            break
    match decision:
        case 1:
            return "espresso"
        case 2:
            return "latte"
        case 3:
            return "cappuccino"
        case 4:
            return "off"
        case 5:
            return "report"

def main():
    money_machine = MoneyMachine()
    coffee_maker = CoffeeMaker()
    menu = Menu()

    is_on = True
    while is_on:
        choice = get_product_selection()
        if choice == "off":
            is_on = False
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(choice)
            print(f"{drink.name}: {drink.cost}")
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

main()