def multiline_strings ():
    multiline_string = """ 
        First Line
        Second Line
        Third Line
    """
    #Description
    #accesses a character in a string

def raw_strings ():
    strings = {
        "normal": "No need for escaping backslashes \n",
        "raw": r"No need for escaping backslashes \n"
    }
    #Description
    #convert a string to a raw string to include backslashes without escaping

def concatenate_strings ():
    strings = {
        "result": "FirstString" + "SecondString"
    }
    #Description
    #concatenating two strings

def indexing_strings ():
    type_of_indexing = {
        "normal": "String"[0],
        "backwards": "String"[-1]
    }
    #Description
    #accesses a character in a string

def convert_to_string ():
    string_type = {
        "string": str(123)
    }
    #Description
    #converts a variable to a string

def format_strings ():
    formatted_strings = {
        "f_strings": f"This is a integer: {123}",
        "formatted_string": "This is a integer: {}, this is a float: {}".format(123, 23.5)
    }
    #Description
    #use other datatypes or variables in strings

def convert_case_string ():
    convertion = {
        "uppercase": "This is now UPPERCASE".upper(),
        "lowercase": "This is now LOWERCASE".lower()
    }
    #Description
    #convert a string to lowercase
