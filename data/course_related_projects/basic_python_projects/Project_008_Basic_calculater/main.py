import art


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def little_calculator():
    print(art.logo)
    should_continue = True
    number_one = get_number_from_user()

    while should_continue:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        if operation_symbol not in operations:
            print("Invalid operation symbol")
            continue

        number_two = get_number_from_user()
        try:
            answer = operations[operation_symbol](number_one, number_two)
        except Exception as e:
            print(f"Invalid math operation! {e}")
            return False
        print(f"{number_one} {operation_symbol} {number_two} = {answer}")

        message = f"Choose an option:\n"
        message += f"1 - Continue calculating with {answer}\n"
        message += "2 - Start a new calculation\n"
        message += "q - Quit"
        decision = input(message)

        match decision:
            case "1":
                number_one = answer
            case "2":
                return False
            case "q":
                should_continue = False
            case _:
                print("Invalid choice! Close program.")
                should_continue = False
    return True


def main():
    is_finished = False

    while not is_finished:
        is_finished = little_calculator()

def get_number_from_user():
    while True:
        try:
            return float(input("Enter a number: "))
        except ValueError:
            print("Enter a valid number!")



main()