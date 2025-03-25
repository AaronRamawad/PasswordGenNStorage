from generator import generator

def main():
    
    application_choice = 0

    while application_choice != 1 or application_choice != 2:
        application_choice = int(input("Welcome to Password Generator/Storage\n\nChoose Option Below:\n1. Generator\n2. Storage\nChoice: "))
        if application_choice == 1 or application_choice == 2:
            break
        else:
            print("Error: Improper Response")
        
    if application_choice == 1:
        generator()
    elif application_choice == 2:
        pass



if __name__ == "__main__":
    main()