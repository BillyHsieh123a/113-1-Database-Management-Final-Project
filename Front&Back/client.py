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
        print("Succeeded!\n")
        return user_data["user_name"], response.json()["message"]
    else:
        print(f"Error: {response.json().get('error')}")
        return ""

def show_user_profile(user_id):
    response = requests.get(f"{SERVER_URL}/show_user_profile", params={"user_id": user_id})
    
    if response.status_code == 200:
        user_data = response.json()
        print("User Profile:")
        print(f"User ID: {user_data['user_id']}")
        print(f"Username: {user_data['user_name']}")
        print(f"Description: {user_data['user_description']}")
        print(f"Profile Picture: {user_data['profile_pic']}")
        print(f"Profile Background: {user_data['profile_background']}")
        print(f"Birthday: {user_data['birthday']}")
        print(f"Email: {user_data['email']}")
        print(f"Country: {user_data['country']}")
        print(f"Language: {user_data['language']}")
        print(f"Fund: {user_data['fund']}")
        print(f"Filtering: {user_data['filtering']}")
        print(f"Notifications: {user_data['notification']}")
        print(f"Cookies: {user_data['cookies']}")
    else:
        print(f"Error: {response.json().get('error')}")

def search_games(keywords):
    if not isinstance(keywords, str) or not keywords.strip():
        print("Invalid keywords. Keywords must be a non-empty string.")
        return []

    try:
        response = requests.get(f"{SERVER_URL}/search_games", params={"keywords": keywords})
        if response.status_code == 200:
            games = response.json()
            if games:
                print("Found Games:")
                for game in games:
                    print(f"{game['game_id']}: {game['game_name']}")
            else:
                print("No games found for the given keywords.")
        else:
            print(f"Error: {response.json().get('error')}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while trying to connect to the server: {e}")

def add_friend(user_name, friend_name):
    if not all([user_name, friend_name]):
        print("Both user_name and friend_name are required.")
        return

    try:
        response = requests.post(
            f"{SERVER_URL}/add_friend",
            json={"user_name": user_name, "friend_name": friend_name}
        )
        if response.status_code == 200:
            print(response.json()["message"])
        else:
            print(f"Error: {response.json().get('error')}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while trying to connect to the server: {e}")

# Function to make the request
def buy_item(user_id, game_id, item_id):
    headers = {'Content-Type': 'application/json'}
    
    data = {
        'user_id': user_id,
        'game_id': game_id,
        'item_id': item_id,
    }

    response = requests.post(f"{SERVER_URL}/buy_item", json=data, headers=headers)

    if response.status_code == 200:
        print("Item purchased successfully!")
    else:
        print(f"Error: {response.json()['error']}")

# Function to add funds
def add_fund(user_id, amount):
    headers = {'Content-Type': 'application/json'}
    data = {
        "user_id": user_id,
        "amount": amount
    }
    
    try:
        # Send POST request to the server
        response = requests.post(f"{SERVER_URL}/add_fund", json=data, headers=headers)
        
        # Check if the request was successful
        if response.status_code == 200:
            result = response.json()
            print(result['message'])
        else:
            result = response.json()
            print(f"Error: {result['error']}")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")

def adding_games(publisher_id, game_name, game_description, system_requirements, original_price, special_offer):
    headers = {'Content-Type': 'application/json'}
    
    data = {
        'publisher_id': publisher_id,
        'game_name': game_name,
        'game_description': game_description,
        'system_requirements': system_requirements,
        'original_price': original_price,
        'special_offer': special_offer,
    }

    try:
        # Send POST request to the server
        response = requests.post(f"{SERVER_URL}/adding_games", json=data, headers=headers)
        
        # Check if the request was successful
        if response.status_code == 200:
            result = response.json()
            print(result['message'])
        else:
            result = response.json()
            print(f"Error: {result['error']}")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")

def changing_price(publisher_id, game_id, item_id, special_offer):
    headers = {'Content-Type': 'application/json'}
    
    data = {
        'publisher_id': publisher_id,
        'game_id': game_id,
        'item_id': item_id,
        'special_offer': special_offer,
    }

    try:
        # Send POST request to the server
        response = requests.post(f"{SERVER_URL}/changing_price", json=data, headers=headers)
        
        # Check if the request was successful
        if response.status_code == 200:
            result = response.json()
            print(result['message'])
        else:
            result = response.json()
            print(f"Error: {result['error']}")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")

def adding_achievement(publisher_id, game_id, achievement_name, achievement_description):
    headers = {'Content-Type': 'application/json'}
    
    data = {
        'publisher_id': publisher_id,
        'game_id': game_id,
        'achievement_name': achievement_name,
        'achievement_description': achievement_description,
    }

    try:
        # Send POST request to the server
        response = requests.post(f"{SERVER_URL}/adding_achievement", json=data, headers=headers)
        
        # Check if the request was successful
        if response.status_code == 200:
            result = response.json()
            print(result['message'])
        else:
            result = response.json()
            print(f"Error: {result['error']}")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")

def adding_item(publisher_id, game_id, item_id, original_price, special_offer):
    headers = {'Content-Type': 'application/json'}
    
    data = {
        'publisher_id': publisher_id,
        'game_id': game_id,
        'item_id': item_id,
        'original_price': original_price,
        'special_offer': special_offer,
    }

    try:
        # Send POST request to the server
        response = requests.post(f"{SERVER_URL}/adding_item", json=data, headers=headers)
        
        # Check if the request was successful
        if response.status_code == 200:
            result = response.json()
            print(result['message'])
        else:
            result = response.json()
            print(f"Error: {result['error']}")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")

def view_games(publisher_id):
    try:
        response = requests.get(f"{SERVER_URL}/view_games", params={"publisher_id": publisher_id})
        if response.status_code == 200:
            games = response.json()
            if games:
                print("Found Games:")
                for game in games:
                    print(f"{game['game_id']}: {game['game_name']}")
            else:
                print("No games found for the given keywords.")
        else:
            print(f"Error: {response.json().get('error')}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while trying to connect to the server: {e}")

def main():
    is_logged_in = False
    user_name = ""
    user_id = 0

    while True:
        print("\nWelcome to GameHub!")
        if not is_logged_in:
            print("1. Login")
            print("2. Signup")
            print("3. Exit")
            choice = input("Select an option: ")

            if choice == "1":
                user_name, user_id = login()
                if user_name != "":
                    is_logged_in = True
                    print("Login successful!")
                else:
                    print("Login failed. Please try again.")
            elif choice == "2":
                signup()
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid option. Try again.")
        else:
            print("1. Show User Profile")
            print("2. Search for Games")
            print("3. Add Friends")
            print("4. Buy Game Items")
            print("5. Add Fund")
            print("9. Logout")
            print("0. Exit")
            choice = input("Select an option: ")

            if choice == "1":
                user_name = input("Enter User Name to view profile: ")
                show_user_profile(user_name)
            elif choice == "2":
                keywords = input("Enter Keywords to Search for Games: ")
                search_games(keywords)
            elif choice == "3":
                friend_name = input("Enter User's Name: ")
                add_friend(user_name, friend_name)
            elif choice == "4":
                game_id = input("Enter Game ID: ")
                item_id = input("Enter Item ID (1 for the game itself): ")
                buy_item(user_id, game_id, item_id)
            elif choice == "5":
                amount = input("Enter Amount: ")
                add_fund(user_id, amount)
            elif choice == "9":
                print("Logging out...")
                is_logged_in = False
                user_name = None
                user_id = 0
            elif choice == "0":
                print("Goodbye!")
                break
            else:
                print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
