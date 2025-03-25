
def ask_for_answer(trait):
    while True:
        answer = input(f"Do you want {trait}: (Y/N)\nType Here: ").lower()
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("Error: Enter Proper Answer")

def ask_for_number(trait):
    while True:
        try:
            trait = int(input(f"How many {trait}?\nType Here: "))
        except TypeError:
            print("Error: Enter a proper integer")
        if trait > 0:
            return trait
    


def generator():
    
    password = {}

    #need length, symbols, numbers, uppercase, lowercase, minimum symbols, minimum numbers
    length = ask_for_number("characters")
    password["length"] = length
    is_symbol = ask_for_answer("symbol")
    password["is_symbol"] = is_symbol
    is_number = ask_for_answer("number")
    password["is_number"] = is_number
    is_uppercase = ask_for_answer("uppercase")
    password["is_uppercase"] = is_uppercase
    is_lowercase = ask_for_answer("lowercase")
    password["is_lowercase"] = is_lowercase
    min_symbols = ask_for_number("symbols")
    password["min_symbols"] = min_symbols
    min_numbers = ask_for_number("numers")
    password["min_numbers"] = min_numbers



    