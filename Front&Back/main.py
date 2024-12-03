from auth import signup, login
from menu import main_menu

def main():
    while True:
        print("\nWelcome to GameHub!")
        print("1. Login")
        print("2. Signup")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            username = input("Username: ")
            password = input("Password: ")
            if login(username, password):
                print("Login successful!")
                user_dashboard()
            else:
                print("Invalid credentials.")
        elif choice == "2":
            username = input("Choose a username: ")
            password = input("Choose a password: ")
            signup(username, password)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

def user_dashboard():
    while True:
        choice = main_menu()
        if choice == 1:
            print("Browsing games...")
        elif choice == 2:
            print("Viewing library...")
        elif choice == 3:
            print("Purchasing a game...")
        elif choice == 4:
            print("Logging out...")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
