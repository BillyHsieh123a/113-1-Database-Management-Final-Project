from flask import Flask, request, jsonify
from psycopg2 import sql, OperationalError, IntegrityError, DataError, InterfaceError
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
        if conn:
            conn.rollback() 
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
            return jsonify({"message": f"{result[0][0]}"}), 200
        else:
            return jsonify({"error": "Invalid username or password."}), 401
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Function to show user profile
def show_user_profile(user_name):
    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            """
            SELECT user_id, user_name, user_description, profile_pic, 
                   profile_background, birthday, email, country, 
                   language, fund, filtering, notification, cookies
            FROM public."user"
            WHERE user_name = %s
            """,
            (user_name,)
        )

        if cur.rowcount == 0:
            return None
        
        user_data = cur.fetchall()
        return user_data[0]  # Assuming user_name is unique

    except OperationalError as e:
        if conn:
            conn.rollback() 
        print(f"Database connection error: {e}")
        return None
    except IntegrityError as e:
        if conn:
            conn.rollback() 
        print(f"Integrity error: {e}")
        return None
    except DataError as e:
        if conn:
            conn.rollback() 
        print(f"Invalid input data: {e}")
        return None
    except Exception as e:
        if conn:
            conn.rollback() 
        print(f"An unexpected error occurred: {e}")
        return None
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

@app.route('/show_user_profile', methods=['GET'])
def get_user_profile():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({"error": "user_id is required"}), 400
    
    user_data = show_user_profile(user_id)
    
    if user_data:
        return jsonify({
            "user_id": user_data[0],
            "user_name": user_data[1],
            "user_description": user_data[2],
            "profile_pic": user_data[3],
            "profile_background": user_data[4],
            "birthday": user_data[5],
            "email": user_data[6],
            "country": user_data[7],
            "language": user_data[8],
            "fund": user_data[9],
            "filtering": user_data[10],
            "notification": user_data[11],
            "cookies": user_data[12]
        })
    else:
        return jsonify({"error": "User not found"}), 404

# Game search function
def search_games(keywords):
    conn = None
    cur = None
    try:
        # Establish database connection
        conn = get_connection()
        cur = conn.cursor()

        # Execute the query to search for games
        cur.execute(
            """
            SELECT game_id, game_name
            FROM public."game"
            WHERE game_name ILIKE %s
            """, 
            (f"%{keywords}%",)
        )

        # Fetch all matching rows
        related_games = cur.fetchall()

        return related_games

    except OperationalError as e:
        if conn:
            conn.rollback() 
        return {"error": f"Database connection error: {e}"}
    except DataError as e:
        if conn:
            conn.rollback() 
        return {"error": f"Invalid input data: {e}"}
    except Exception as e:
        if conn:
            conn.rollback() 
        return {"error": f"An unexpected error occurred: {e}"}
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

@app.route('/search_games', methods=['GET'])
def search_for_games():
    keywords = request.args.get('keywords', '')
    if not keywords:
        return jsonify({"error": "Keywords are required"}), 400

    search_results = search_games(keywords)
    if "error" in search_results:
        return jsonify(search_results), 400
    
    # Return game results
    games = [{"game_id": game[0], "game_name": game[1]} for game in search_results]
    return jsonify(games)

def add_friend(user_name, friend_name):
    conn = None
    cur = None

    try:
        # Validate inputs
        if not all([user_name, friend_name]):
            raise ValueError("Both user_name and friend_name are required.")
        if user_name == friend_name:
            raise ValueError("A user cannot add themselves as a friend.")

        # Establish database connection
        conn = get_connection()
        cur = conn.cursor()

        # Get user_id for user_name
        cur.execute(
            """
            SELECT user_id FROM public."user" WHERE user_name = %s;
            """,
            (user_name,)
        )
        user_result = cur.fetchone()
        if not user_result:
            raise ValueError(f"User with user_name {user_name} not found.")
        user_id = user_result[0]

        # Get user_id for friend_name
        cur.execute(
            """
            SELECT user_id FROM public."user" WHERE user_name = %s;
            """,
            (friend_name,)
        )
        friend_result = cur.fetchone()
        if not friend_result:
            raise ValueError(f"User with friend_name {friend_name} not found.")
        friend_id = friend_result[0]

        # Add friendship in both directions
        cur.execute(
            """
            INSERT INTO public."user_friends" (user_id, friend_id)
            VALUES (%s, %s)
            ON CONFLICT (user_id, friend_id) DO NOTHING;
            """,
            (user_id, friend_id)
        )
        cur.execute(
            """
            INSERT INTO public."user_friends" (user_id, friend_id)
            VALUES (%s, %s)
            ON CONFLICT (user_id, friend_id) DO NOTHING;
            """,
            (friend_id, user_id)
        )

        # Commit transaction
        conn.commit()
        return {"message": f"Friendship added successfully between user_name: {user_name} and friend_name: {friend_name}."}

    except ValueError as e:
        if conn:
            conn.rollback() 
        return {"error": f"Validation error: {e}"}
    except OperationalError as e:
        if conn:
            conn.rollback() 
        return {"error": f"Database connection error: {e}"}
    except IntegrityError as e:
        if conn:
            conn.rollback() 
        return {"error": f"Integrity error: {e}"}
    except DataError as e:
        if conn:
            conn.rollback() 
        return {"error": f"Invalid input data: {e}"}
    except Exception as e:
        if conn:
            conn.rollback() 
        return {"error": f"An unexpected error occurred: {e}"}
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

# Route to add friends
@app.route('/add_friend', methods=['POST'])
def handle_add_friend():
    data = request.json
    user_name = data.get('user_name')
    friend_name = data.get('friend_name')

    if not user_name or not friend_name:
        return jsonify({"error": "Both user_name and friend_name are required."}), 400

    result = add_friend(user_name, friend_name)
    if "error" in result:
        return jsonify(result), 400
    
    return jsonify(result), 200

# Function to handle item purchase
def user_buy_items(user_id, game_id, item_id):
    conn = None
    cur = None

    try:
        if not all([user_id, game_id, item_id]):
            raise ValueError("Invalid input. Please ensure all inputs are valid.")

        conn = get_connection()
        cur = conn.cursor()

        # Fetch user fund with row locking
        cur.execute(
            """
            SELECT fund 
            FROM public."user" 
            WHERE user_id = %s FOR UPDATE;
            """,
            (user_id,)
        )
        user_result = cur.fetchone()
        if user_result is None:
            raise ValueError("User not found.")
        user_fund = user_result[0]

        # Fetch item price with shared lock
        cur.execute(
            """
            SELECT current_price 
            FROM public."game_item" 
            WHERE game_id = %s AND item_id = %s FOR SHARE;
            """,
            (game_id, item_id)
        )
        item_result = cur.fetchone()
        if item_result is None:
            raise ValueError("Game item not found.")
        current_price = item_result[0]

        # Check if the user has sufficient funds
        if user_fund < current_price:
            raise ValueError("Insufficient funds.")

        # Deduct the item price from user funds
        cur.execute(
            """
            UPDATE public."user" 
            SET fund = fund - %s 
            WHERE user_id = %s;
            """,
            (current_price, user_id)
        )

        # Add transaction
        cur.execute(
            """
            INSERT INTO public."buy_item" 
            (user_id, game_id, item_id, price, timestamp, "isCancelled") 
            VALUES (%s, %s, %s, %s, NOW(), %s)
            """,
            (user_id, game_id, item_id, current_price, False)
        )

        # Add record to user_games
        cur.execute(
            """
            INSERT INTO public."user_games" 
            (user_id, game_id, installed_date) 
            VALUES (%s, %s, NOW())
            """,
            (user_id, game_id)
        )

        conn.commit()
        return True

    except ValueError as e:
        if conn:
            conn.rollback() 
        return {"error": f"Validation error: {e}"}
    except OperationalError as e:
        if conn:
            conn.rollback() 
        return {"error": f"Database connection error: {e}"}
    except IntegrityError as e:
        if conn:
            conn.rollback() 
        return {"error": f"Integrity error: {e}"}
    except DataError as e:
        if conn:
            conn.rollback() 
        return {"error": f"Invalid input data: {e}"}
    except Exception as e:
        if conn:
            conn.rollback() 
        return {"error": f"An unexpected error occurred: {e}"}
    finally:
        if cur:
            try:
                cur.close()
            except Exception as cleanup_error:
                print(f"Error closing cursor: {cleanup_error}")
        if conn:
            try:
                conn.close()
            except Exception as cleanup_error:
                print(f"Error closing connection: {cleanup_error}")

# API route for buying an item
@app.route('/buy_item', methods=['POST'])
def buy_item():
    data = request.json

    print(data)
    user_id = data.get('user_id')
    game_id = data.get('game_id')
    item_id = data.get('item_id')

    if not all([user_id, game_id, item_id]):
        return jsonify({"error": "Missing required fields."}), 400

    result = user_buy_items(user_id, game_id, item_id)

    if isinstance(result, dict) and result.get('error'):
        return jsonify(result), 400

    return jsonify({"message": "Item purchased successfully!"}), 200

# Function to add funds to the user's account
def user_add_fund(user_id, amount):
    conn = None
    cur = None

    amount = int(amount)

    try:
        # Validate input
        if not isinstance(amount, (int, float)) or amount <= 0:
            return {"error": "Invalid amount. Amount must be a positive number."}

        conn = get_connection()
        cur = conn.cursor()

        # Execute the UPDATE query with row locking (FOR UPDATE)
        cur.execute(
            """
            UPDATE public."user" 
            SET fund = fund + %s
            WHERE user_id = %s
            RETURNING fund;
            """,
            (amount, user_id)
        )

        # Check if the user exists and the update was successful
        updated_row = cur.fetchone()
        if updated_row is None:
            return {"error": "User ID not found."}

        cur.execute(
            """
            INSERT INTO public."add_fund_record"
            (user_id, fund_change, timestamp)
            VALUES (%s, %s, NOW())
            """, 
            (user_id, amount)
        )

        # Commit the transaction
        conn.commit()
        return {"message": f"Fund updated successfully. New fund balance: {updated_row[0]}"}

    except OperationalError as e:
        if conn:
            conn.rollback() 
        return {"error": f"Database connection error: {e}"}
    except IntegrityError as e:
        if conn:
            conn.rollback() 
        return {"error": f"Integrity error (e.g., constraint violation): {e}"}
    except DataError as e:
        if conn:
            conn.rollback() 
        return {"error": f"Invalid input data: {e}"}
    except Exception as e:
        if conn:
            conn.rollback() 
        return {"error": f"An unexpected error occurred: {e}"}
    finally:
        # Cleanup resources
        if cur:
            try:
                cur.close()
            except Exception as cleanup_error:
                print(f"Error closing cursor: {cleanup_error}")
        if conn:
            try:
                conn.close()
            except Exception as cleanup_error:
                print(f"Error closing connection: {cleanup_error}")

# API route to add funds
@app.route('/add_fund', methods=['POST'])
def add_fund():
    data = request.get_json()
    user_id = data.get('user_id')
    amount = data.get('amount')

    if not user_id or not amount:
        return jsonify({"error": "user_id and amount are required"}), 400

    result = user_add_fund(user_id, amount)

    if "error" in result:
        return jsonify(result), 400
    return jsonify(result), 200


if __name__ == "__main__":
    app.run(debug=True)
