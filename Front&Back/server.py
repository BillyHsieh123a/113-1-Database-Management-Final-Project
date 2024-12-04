from flask import Flask, request, jsonify
import psycopg2
import hashlib

app = Flask(__name__)

# Database connection function
def get_connection():
    return psycopg2.connect(
        dbname="DB_Final_Project",
        user="postgres",
        password="bear123321a",
        host="localhost",
    )

# Query execution function
def execute_query(query, values=None):
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(query, values)
        if query.strip().upper().startswith("SELECT"):
            return cursor.fetchall()
        conn.commit()
    except Exception as e:
        raise e
    finally:
        if conn:
            conn.close()

# Hashing function
def hash_password(password):
    full_hash = hashlib.sha256(password.encode()).hexdigest()
    return full_hash[:20]

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    password_hashed = hash_password(data['password'])

    query = """
    INSERT INTO public."user" (
        password_hashed, user_name, user_description, profile_pic,
        profile_background, birthday, email, country, language,
        fund, filtering, notification, cookies
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        password_hashed, data['user_name'], data.get('user_description'), data.get('profile_pic'),
        data.get('profile_background'), data['birthday'], data['email'], data['country'],
        data['language'], 0, data['filtering'], data['notification'], data['cookies']
    )

    try:
        execute_query(query, values)
        return jsonify({"message": "User successfully registered!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    password_hashed = hash_password(data['password'])

    query = """
    SELECT * FROM public."user"
    WHERE user_name = %s AND password_hashed = %s
    """
    try:
        result = execute_query(query, (data['user_name'], password_hashed))
        if result:
            return jsonify({"message": "Login successful!"}), 200
        else:
            return jsonify({"error": "Invalid username or password."}), 401
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
