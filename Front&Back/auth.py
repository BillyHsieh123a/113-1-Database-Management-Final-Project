import hashlib
from db_manager import execute_query

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def signup(username, password):
    hashed_pw = hash_password(password)
    query = "INSERT INTO users (username, password) VALUES (%s, %s)"
    execute_query(None, query, (username, hashed_pw))
    print("Account created successfully!")

def login(username, password):
    hashed_pw = hash_password(password)
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    user = execute_query(None, query, (username, hashed_pw))
    return user is not None
