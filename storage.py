import json
import encodings.base64_codec

with open("passwords.json", "r") as passwords_json:
    passwords = json.load(passwords_json)
    print(passwords)