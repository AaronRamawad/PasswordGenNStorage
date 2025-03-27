import hashlib

def master_login():

    master_password = "c634325291b48a90f29fc7090d73781a0445d4918b73389e6f572b09713a0ac4"

    tries = 5
    while tries > 0:
        password = input("Enter Password: ").encode("utf-8")
        if hashlib.sha256(password).hexdigest() == master_password:
            print("LOGIN APPROVED")
            break
        tries -= 1
    if tries == 0:
        print("Login Failed")
        exit()
