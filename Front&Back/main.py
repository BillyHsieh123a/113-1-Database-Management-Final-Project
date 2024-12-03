from auth import signup, login

def main_menu():
    """
    Display the main menu options for the user.
    """
    print("\nMain Menu:")
    print("1. Browse Games")
    print("2. View Library")
    print("3. Purchase Game")
    print("4. Logout")
    choice = input("Select an option: ")
    return choice

def main():
    while True:
        print("\nWelcome to GameHub!")
        print("1. Login")
        print("2. Signup")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            if login():
                while True:
                    choice = main_menu()
                    if choice == "1":
                        print("Browsing games...")
                    elif choice == "2":
                        print("Viewing library...")
                    elif choice == "3":
                        print("Purchasing a game...")
                    elif choice == "4":
                        print("Logging out...")
                        break
                    else:
                        print("Invalid option. Try again.")
        elif choice == "2":
            signup()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
