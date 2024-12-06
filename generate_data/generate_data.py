from psycopg2 import sql, OperationalError, IntegrityError, DataError, InterfaceError
import psycopg2
import hashlib
import random
import faker
import pytz
from datetime import datetime, timedelta
from pytz import timezone
import uuid

# Database connection function
def get_connection():
    return psycopg2.connect(
        dbname="DB_Final_Project",
        user="postgres",
        password="000000",
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


# generate user
user_num = 200
fake = faker.Faker()
fake_names = []
for i in range(user_num):
    fake_names.append(f"{fake.user_name()[:6]}{uuid.uuid4().hex[:4]}")
# print(fake_names)
user_data = []
with open("user_login_data.txt", "w") as file:
    for i in range(user_num):
        password = fake.password(length=20)
        user_data.append({
            "password_hashed": hash_password(password),
            "user_name": fake_names[i],
            "user_description": fake.text(max_nb_chars=300),
            "profile_pic": fake.image_url(),
            "profile_background": fake.image_url(),
            "birthday": fake.date_of_birth(minimum_age=18, maximum_age=80),
            "email": fake.email(),
            "country": fake.country()[:20],
            "language": fake.language_name()[:20],
            "fund": random.randint(1000, 10000),
            "filtering": random.choice([True, False]),
            "notification": random.choice([True, False]),
            "cookies": random.choice([True, False]),
        })

        query = """
        INSERT INTO public."user" (
            password_hashed, user_name, user_description, profile_pic,
            profile_background, birthday, email, country, language,
            fund, filtering, notification, cookies
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            user_data[i]['password_hashed'], user_data[i]['user_name'], user_data[i]['user_description'], user_data[i]['profile_pic'],
            user_data[i]['profile_background'], user_data[i]['birthday'], user_data[i]['email'], user_data[i]['country'],
            user_data[i]['language'], user_data[i]['fund'], user_data[i]['filtering'], user_data[i]['notification'], user_data[i]['cookies']
        )
        execute_query(query, values)

        file.write(f"{fake_names[i]} {password}\n")

print("finish generating user")

# generate friends
for user_name in fake_names:
    random_frined_names =[]
    while True:
        random_frined_names = random.sample(fake_names, random.randint(1, 2))
        if user_name not in random_frined_names:
            break

    for friend_name in random_frined_names:
        query = """
        SELECT user_id FROM public."user" WHERE user_name = %s;
        """
        values = (user_name,)
        user_result = execute_query(query, values)
        user_id = user_result[0][0]

        # Get user_id for friend_name
        query = """
        SELECT user_id FROM public."user" WHERE user_name = %s;
        """
        values = (friend_name,)
        friend_result = execute_query(query, values)
        friend_id = friend_result[0][0]

        # Add friendship in both directions
        query = """
        INSERT INTO public."user_friends" (user_id, friend_id)
        VALUES (%s, %s)
        ON CONFLICT (user_id, friend_id) DO NOTHING;
        """
        values = (user_id, friend_id)
        execute_query(query, values)

        query = """
        INSERT INTO public."user_friends" (user_id, friend_id)
        VALUES (%s, %s)
        ON CONFLICT (user_id, friend_id) DO NOTHING;
        """
        values = (friend_id, user_id)
        execute_query(query, values)

print("finish generating user_friends")

# generate user add fund
for user_name in fake_names:
    query = """
    SELECT user_id 
    FROM public."user" 
    WHERE user_name = %s;
    """
    values = (user_name,)
    user_result = execute_query(query, values)
    user_id = user_result[0][0]

    add_fund_times = random.randint(1, 3)
    for i in range(add_fund_times):
        amount = random.randint(1000, 5000)
        query = """
        UPDATE public."user" 
        SET fund = fund + %s
        WHERE user_id = %s;
        """
        values = (amount, user_id)
        execute_query(query, values)

        query = """
        INSERT INTO public."add_fund_record"
        (user_id, fund_change, timestamp)
        VALUES (%s, %s, NOW())
        """
        values = (user_id, amount)
        execute_query(query, values)

print("finish generating add_fund_record")


#generate publisher
publisher_num = 100
fake_publisher_names = []
for i in range(publisher_num):
    fake_publisher_names.append(f"{fake.user_name()[:6]}{uuid.uuid4().hex[:4]}")
# print(fake_names)
publisher_data = []
with open("publisher_login_data.txt", "w") as file:
    for i in range(publisher_num):
        publisher_data.append({
            "publisher_name": fake_publisher_names[i],
            "description": fake.text(max_nb_chars=100),
        })

        query = """
        INSERT INTO public."publishers" (publisher_name, description)
        VALUES (%s, %s)
        """
        values = (publisher_data[i]['publisher_name'], publisher_data[i]['description'])
        execute_query(query, values)

        file.write(f"{fake_publisher_names[i]} {password}\n")

publisher_ids = []
query = """
SELECT publisher_id
FROM public."publishers"
"""
publisher_ids_result = execute_query(query, ())
for publisher_id in publisher_ids_result:
    publisher_ids.append(publisher_id[0])
print("finish generating publisher")
# print(publisher_ids[0])


game_publisher = []
game_data = []
systems = ["Win 10", "Mac", "GameHub"]
with open("fake_game_name.txt") as file:
    fake_game_name_list = file.read()
fake_game_names = fake_game_name_list.splitlines()

for publisher_id in publisher_ids:
    game_num = random.randint(1, 2)
    for i in range(game_num):
        game_data.append({
            "game_name": random.choice(fake_game_names[0]),
            "game_description": fake.text(max_nb_chars=100),
            "system_requirements": random.choice(systems),
            "original_price" : random.randint(10, 100),
            "special_offer" : round(random.uniform(0, 1), 2),
        })
        del fake_game_names[0]
        query = """
        INSERT INTO public."game" (game_name, game_description, system_requirements)
        VALUES (%s, %s, %s) 
        RETURNING game_id
        """
        values = (game_data[i]['game_name'], game_data[i]['game_description'], game_data[i]['system_requirements'])
        
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(query, values)
            game_id_result = cursor.fetchall()
            conn.commit()
        except Exception as e:
            if conn:
                conn.rollback() 
            raise e
        finally:
            if conn:
                conn.close()

        game_id = game_id_result[0][0]

        current_price = int(game_data[i]['original_price'] * game_data[i]['special_offer'])
        
        # Insert into game_item with game_id and item_id set to 1
        query = """
        INSERT INTO public."game_item" (game_id, item_id, original_price, current_price, special_offer, release_date)
        VALUES (%s, %s, %s, %s, %s, NOW())
        """
        values = (game_id, 1, game_data[i]['original_price'], current_price, game_data[i]['special_offer'])
        execute_query(query, values)

         # Insert into game_publisher with game_id and publisher_id
        query = """
        INSERT INTO public."game_publishers" (game_id, publisher_id)
        VALUES (%s, %s)
        """
        values = (game_id, publisher_id)
        execute_query(query, values)

print("finish adding games")