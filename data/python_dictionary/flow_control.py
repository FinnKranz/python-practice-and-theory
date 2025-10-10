def if_else_statement():
    condition = True
    number = 2

    if condition:
        print("True")
    elif not condition:
        print("False")
    else:
        pass    #create an empty if/else block

    #short versions
    if condition: print("True")
    print("True") if condition else print("False")
    print("Greater") if number > 2 else print("Smaller") if number == 2 else print("Equal")
    #Description
    #different ways of using the if_else statement

def logical_operators():
    condition_one = True
    condition_two = False

    print("False: ",condition_one and condition_two)
    print("True: ",condition_one or condition_two)
    print("False ", not condition_one)
    #Description
    #three main logical operators for connecting booleans

def while_loop():
    i = 0
    while i < 5:
        print(i)
        i += 1
    #Description
    #do a certain action while a condition is true

def for_loop():
    for i in range(5):
        print(i)
    #Description
    #do a certain action for a certain number of times