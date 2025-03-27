from generator import generator
from storage import store, display_passwords
from login import master_login


def main():

    refresh = 0
    while True:

        if refresh == 0:
            master_login()
        elif refresh % 10 == 0:
            print("Session Expired")
            master_login()
    
        application_choice = 0

        while application_choice != 1 or application_choice != 2:
            application_choice = int(input("Welcome to Password Generator/Storage\n\nChoose Option Below:\n1. Generator\n2. Storage\nChoice: "))
            if application_choice == 1 or application_choice == 2:
                break
            else:
                print("Error: Improper Response")
            
        if application_choice == 1:
            login = input("Login Username: ")
            
            password = generator()
            while True:
                confirmation_input = input("Do you want to keep password? (Y/N)\nType Here: ")
                if confirmation_input.lower() == "y":
                    confirmation = True
                    break
                if confirmation_input.lower() == "n":
                    confirmation = False
                    break
            
            if confirmation:
                store(login, password)
            
        elif application_choice == 2:
            display_passwords()    
        
        refresh += 1
    

if __name__ == "__main__":
    main()