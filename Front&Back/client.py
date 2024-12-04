import requests

SERVER_URL = "http://127.0.0.1:5000"

def signup():
    print("Signup:")
    user_data = {
        "user_name": input("Username (max 10 chars): "),
        "password": input("Password (max 20 chars): "),
        "user_description": input("Description (optional): ") or None,
        "profile_pic": input("Profile picture URL (optional): ") or None,
        "profile_background": input("Profile background URL (optional): ") or None,
        "birthday": input("Birthday (YYYY-MM-DD): "),
        "email": input("Email: "),
        "country": input("Country (max 20 chars): "),
        "language": input("Language (max 20 chars): "),
        "filtering": input("Enable filtering? (yes/no): ").lower() == "yes",
        "notification": input("Enable notifications? (yes/no): ").lower() == "yes",
        "cookies": input("Accept cookies? (yes/no): ").lower() == "yes"
    }

    response = requests.post(f"{SERVER_URL}/signup", json=user_data)
    if response.status_code == 201:
        print(response.json()["message"])
    else:
        print(f"Error: {response.json().get('error')}")

def login():
    print("Login:")
    user_data = {
        "user_name": input("Username: "),
        "password": input("Password: ")
    }

    response = requests.post(f"{SERVER_URL}/login", json=user_data)
    if response.status_code == 200:
        print(response.json()["message"])
        return True
    else:
        print(f"Error: {response.json().get('error')}")
        return False

def main_menu():
    print("\nMain Menu:")
    print("1. Browse Games")
    print("2. View Library")
    print("3. Purchase Game")
    print("4. Logout")
    return input("Select an option: ")

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
