import json
import base64

passwords = {}

with open("passwords.json", "r") as passwords_json:
    passwords = json.load(passwords_json)
    
def store(login, password):
    password_bytes = password.encode("utf-8")
    passwords[login.lower()] = base64.b64encode(password_bytes).decode("utf-8")
    
    with open("passwords.json", "w") as passwords_json:
        json.dump(passwords, passwords_json)

def display_passwords():
    for index, item in (enumerate(list(passwords.keys()))):
        print(f"{index}: {item.capitalize()}")
    login = input("Which login do you want to access?\n").lower()
    try:
        password = passwords[login].encode("utf-8")
        password = base64.b64decode(password)
        print(password.decode("utf-8"))
    except TypeError:
        print("Incorrect Login Name")
