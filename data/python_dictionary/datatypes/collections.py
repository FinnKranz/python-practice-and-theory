def list_type():
    import random
    example_list = ["First", "Second", "Third"]

    list_operations = {
        "First Element": example_list[0],
        "Last Element": example_list[-1],
        "Index of Element": example_list.index("Second"),
        "Random Element": random.choice(example_list)
    }

    # Modify the list
    example_list[1] = "NewElement"
    example_list.append("NewElement")
    example_list.extend(["NewElement", "NewElement"])
    #Description
    #most important methods and workflows for lists