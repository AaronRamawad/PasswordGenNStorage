"""
Try to fix the symbols and numbers when they are the only one's choosen. 
"""

import random
import string
from storage import store

random.seed()

def ask_for_answer(trait):
    while True:
        answer = input(f"Do you want {trait}: (Y/N)\nType Here: ").lower()
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("Error: Enter Proper Answer")

def ask_for_number(trait, min_length=12, length=100):
    previous_trait = trait
    while True:
        try:
            trait = int(input(f"How many {trait}? (-1 = random number between 0 and {length})\nType Here: "))
        except ValueError and TypeError:
            print("Error: Enter a proper integer")
        if trait == -1:
            return random.randint(min_length, length)
        if trait > 0 and trait < length:
            return trait
        else:
            trait = previous_trait
    


def generator():
    
    password = []

    #all constant variables that holds the possible characters for the password
    SYMBOLS = ["!", "@", "#", "$", "%", "^", "&", "*"]
    NUMBERS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    UPPER_ALPHABET = []
    for char in string.ascii_uppercase:
        UPPER_ALPHABET.append(char)
    LOWER_ALPHABET = []
    for char in string.ascii_lowercase:
        LOWER_ALPHABET.append(char.lower())

    #need length, symbols, numbers, uppercase, lowercase, minimum symbols, minimum numbers

    length = ask_for_number("characters")

    is_symbol = ask_for_answer("symbol")
    is_number = ask_for_answer("number")
    is_uppercase = ask_for_answer("uppercase")
    is_lowercase = ask_for_answer("lowercase")

    is_letters = is_uppercase or is_lowercase

    #generates symbols
    if is_symbol:
        min_symbols = ask_for_number("symbols", 0, length)
        for _ in range(min_symbols):
            password.append(SYMBOLS[random.randint(0, len(SYMBOLS) - 1)])
    else:
        min_symbols = 0

    #generates numbers
    if is_number:
        if is_letters:
            min_numbers = ask_for_number("numbers", 0, length - min_symbols)
            for _ in range(min_numbers):
                password.append(NUMBERS[random.randint(0, len(NUMBERS) - 1)])
        else:
            min_numbers = length - min_symbols
            for _ in range(min_numbers):
                password.append(NUMBERS[random.randint(0, len(NUMBERS) - 1)])
    else:
        min_numbers = 0

    #Grabs the amount of letters in password
    if is_letters:
        amount_of_letters = length - min_numbers - min_symbols

        amount_of_uppercase = 0
        amount_of_lowercase = 0

        for _ in range(0, amount_of_letters):
            if is_uppercase:
                if not is_lowercase:
                    amount_of_uppercase = amount_of_letters
                else:
                    amount_of_uppercase = random.randint(0, amount_of_letters)
                    amount_of_lowercase = amount_of_letters - amount_of_uppercase
            else:
                amount_of_lowercase = amount_of_letters

        for _ in range(amount_of_uppercase):
            password.append(UPPER_ALPHABET[random.randint(0, len(UPPER_ALPHABET) - 1)])
        for _ in range(amount_of_lowercase):
            password.append(LOWER_ALPHABET[random.randint(0, len(LOWER_ALPHABET) - 1)])

    else:
        amount_of_letters = 0

    final_password = ""

    #generates final password using all the found characters
    for _ in range(len(password)):
        random_char = password.pop(random.randint(0, len(password) - 1))
        final_password = final_password + random_char

    print(f"Password: {final_password}")
    return final_password
    

    
    






    