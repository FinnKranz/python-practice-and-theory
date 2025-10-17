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
    # Description
    # most important methods and workflows for lists


def dictionary_type():
    dictinary = {}  # create empty dictionary

    dictinary["First"] = 0
    dictinary["Second"] = 1

    value = dictinary.get("First")  # get value safely
    direct_value = dictinary["Second"]  # get value directly

    dictinary["First"] = 100  # update existing key
    dictinary.update({"Third": 3})  # add/update multiple keys

    del dictinary["Second"]  # delete by key
    removed_value = dictinary.pop("Third", None)  # remove and return value
    last_item = dictinary.popitem()  # remove and return last inserted item

    exists = "First" in dictinary  # check if key exists

    for key in dictinary:
        print(f"Key: {key}, Value: {dictinary[key]}")

    for key, value in dictinary.items():
        print(f"{key}: {value}")

    length = len(dictinary)
    dictinary.clear()
    new_dict = dictinary.copy()

    # Create dictionary from keys
    keys = ["a", "b", "c"]
    default_dict = dict.fromkeys(keys, 0)

