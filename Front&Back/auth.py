from db_manager import execute_query
import hashlib

def hash_password(password):
    """
    Hash the user's password and truncate it to 20 characters.
    """
    full_hash = hashlib.sha256(password.encode()).hexdigest()
    return full_hash[:20]  # Truncate to 20 characters

def signup():
    """
    Handle user registration.
    """
    print("Signup:")
    user_name = input("Username (max 10 chars): ")
    password = input("Password (max 20 chars): ")
    password_hashed = hash_password(password)
    user_description = input("Description (optional): ") or None
    profile_pic = input("Profile picture URL (optional): ") or None
    profile_background = input("Profile background URL (optional): ") or None
    birthday = input("Birthday (YYYY-MM-DD): ")
    email = input("Email: ")
    country = input("Country (max 20 chars): ")
    language = input("Language (max 20 chars): ")
    filtering = input("Enable filtering? (yes/no): ").lower() == "yes"
    notification = input("Enable notifications? (yes/no): ").lower() == "yes"
    cookies = input("Accept cookies? (yes/no): ").lower() == "yes"

    query = """
    INSERT INTO public."user" (
        password_hashed, user_name, user_description, profile_pic,
        profile_background, birthday, email, country, language,
        fund, filtering, notification, cookies
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        password_hashed, user_name, user_description, profile_pic,
        profile_background, birthday, email, country, language,
        0, filtering, notification, cookies
    )

    try:
        execute_query(query, values)
        print("User successfully registered!")
    except Exception as e:
        print(f"Error during registration: {e}")

def login():
    """
    Handle user login.
    """
    print("Login:")
    user_name = input("Username: ")
    password = input("Password: ")
    password_hashed = hash_password(password)

    query = """
    SELECT * FROM public."user"
    WHERE user_name = %s AND password_hashed = %s
    """
    try:
        result = execute_query(query, (user_name, password_hashed))
        if result:
            print("Login successful!")
            return True
        else:
            print("Invalid username or password.")
            return False
    except Exception as e:
        print(f"Error during login: {e}")
        return False
