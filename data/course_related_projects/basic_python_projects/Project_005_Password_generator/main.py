import random

def main ():
    password = ""
    print("Welcome to password generator!")
    print("What kind of password would you like to generate?"
          "\n1 - Custom password\n2 - Standard password"
          )
    user_decision = int(input("Choose an option:"))

    match user_decision:
        case 1:
            password = generate_custom_password()
        case 2:
             password = generate_standard_password()

    print(f"\nYour password is: {password}")


def generate_custom_password ():
    password_list = []
    number_of_characters = int(input("How many characters do you want your password to have?"))
    number_of_numbers = int(input("How many numbers do you want in your password?"))
    number_of_symbols= int(input("How many special characters do you want in your password?"))

    password_list += get_random_character(number_of_characters)
    password_list += get_random_symbols(number_of_symbols)
    password_list += get_random_numbers(number_of_numbers)

    return "".join(password_list)


def generate_standard_password ():
    password_list = []
    password_list += get_random_character(10)
    password_list += get_random_symbols(5)
    password_list += get_random_numbers(5)
    random.shuffle(password_list)

    return "".join(password_list)

def get_random_character (count):
    characters = []
    for i in range(count):
        characters += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    return characters

def get_random_symbols (count):
    symbols = []
    for i in range(count):
        symbols += random.choice("!@#$%^&*()_+=-")
    return symbols

def get_random_numbers (count):
    numbers = []
    for i in range(count):
        numbers += str(random.randint(0,9))
    return numbers

main()