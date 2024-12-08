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

# 
user_num = 2000
friend_min = 0
friedn_max = 5
add_fund_min = 1
add_fund_max = 10
add_fund_value_min = 100
add_fund_value_max = 1000
publisher_num = 100
game_num_for_each_publisher_min = 1
game_num_for_each_publisher_max = 8
game_original_price_min = 10
game_original_price_max = 50
rate_of_games_have_special_offer = 0.95
special_offer_min = 0.6
systems = ["Win 10", "Mac", "GameHub"]
item_num_min = 0
item_num_max = 5
item_original_price_min = 1
item_original_price_max = 30
rate_of_items_have_special_offer = 0.95
rate_not_to_buy_a_game_min = 0.85
rate_to_buy_other_item_min = 0.6
achievements_num_min = 1
achievements_num_max = 3
rate_of_games_not_having_achievements = 0.8
# generate user

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
        random_frined_names = random.sample(fake_names, random.randint(friend_min, friedn_max))
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

    add_fund_times = random.randint(add_fund_min, add_fund_max)
    for i in range(add_fund_times):
        amount = random.randint(add_fund_value_min, add_fund_value_max)
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
fake_publisher_names = []
for i in range(publisher_num):
    fake_publisher_names.append(f"{fake.user_name()[:6]}{uuid.uuid4().hex[:4]}")
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


# add games
game_publisher = []
game_data = []
game_ids = []
game_item_data = {}
with open("fake_game_name.txt", encoding="utf-8") as file:
    fake_game_name_list = file.read()
fake_game_names = fake_game_name_list.splitlines()
i_game = 0
for publisher_id in publisher_ids:
    if not fake_game_names:
        break
    game_num = random.randint(game_num_for_each_publisher_min, game_num_for_each_publisher_max)
    for _ in range(game_num):
        if not fake_game_names:
            break
        game_data.append({
            "game_name": fake_game_names[0],
            "game_description": fake.text(max_nb_chars=100),
            "system_requirements": random.choice(systems),
            "original_price" : random.randint(game_original_price_min, game_original_price_max),
            "special_offer" : round(random.uniform(special_offer_min, 1), 2) if round(random.uniform(0, 1), 2) > rate_of_games_have_special_offer else 1,
        })
        del fake_game_names[0]
        query = """
        INSERT INTO public."game" (game_name, game_description, system_requirements)
        VALUES (%s, %s, %s) 
        RETURNING game_id
        """
        values = (game_data[i_game]['game_name'], game_data[i_game]['game_description'], game_data[i_game]['system_requirements'])
        
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
            if cursor:
                cursor.close()
            if conn:
                conn.close()

        game_id = game_id_result[0][0]
        game_ids.append(game_id)

        current_price = int(game_data[i_game]['original_price'] * game_data[i_game]['special_offer'])
        
        # Insert into game_item with game_id and item_id set to 1
        query = """
        INSERT INTO public."game_item" (game_id, item_id, original_price, current_price, special_offer, release_date)
        VALUES (%s, %s, %s, %s, %s, NOW())
        """
        values = (game_id, 1, game_data[i_game]['original_price'], current_price, game_data[i_game]['special_offer'])
        execute_query(query, values)
        game_item_data[game_id] = {}
        game_item_data[game_id][1] = {
            "original_price" : game_data[i_game]['original_price'],
            "special_offer" : game_data[i_game]['special_offer'],
        }

        # Insert into game_publisher with game_id and publisher_id
        query = """
        INSERT INTO public."game_publishers" (game_id, publisher_id)
        VALUES (%s, %s)
        """
        values = (game_id, publisher_id)
        execute_query(query, values)
        i_game += 1
print("finish adding games")


# add items
for game_id in game_ids:
    item_num = random.randint(item_num_min, item_num_max)
    for i in range(item_num):
        game_item_data[game_id][i + 2] = {
            "original_price" : random.randint(item_original_price_min, item_original_price_max),
            "special_offer" : round(random.uniform(special_offer_min, 1), 2) if round(random.uniform(0, 1), 2) > rate_of_items_have_special_offer else 1,
        }

        current_price = int(game_item_data[game_id][i + 2]['original_price'] * game_item_data[game_id][i + 2]['special_offer'])

        query = """
        INSERT INTO public."game_item" (game_id, item_id, original_price, current_price, special_offer, release_date)
        VALUES (%s, %s, %s, %s, %s, NOW())
        """
        values = (game_id, i + 2, game_item_data[game_id][i + 2]['original_price'], current_price, game_item_data[game_id][i + 2]['special_offer'])
        execute_query(query, values)
print("finish adding items")


# buy item
for user_name in fake_names:
    query = """
        SELECT user_id FROM public."user" WHERE user_name = %s;
        """
    values = (user_name,)
    user_result = execute_query(query, values)
    user_id = user_result[0][0]
    
    query = """
        SELECT fund 
        FROM public."user" 
        WHERE user_id = %s FOR UPDATE;
        """
    values = (user_id,)
    user_result = execute_query(query, values)
    user_fund = user_result[0][0]

    rate_not_to_buy_a_game = round(random.uniform(rate_not_to_buy_a_game_min, 1), 2)    
    rate_to_buy_other_item = round(random.uniform(rate_to_buy_other_item_min, 1), 2)
    for game_id in game_item_data:
        if round(random.uniform(0, 1), 2) < rate_not_to_buy_a_game:
            continue
        for item_id in game_item_data[game_id]:
            if item_id != 1 and round(random.uniform(0, 1), 2) < rate_to_buy_other_item:
                continue
            current_price = int(game_item_data[game_id][item_id]['original_price'] * game_item_data[game_id][item_id]['special_offer'])

            # Check if the user has sufficient funds
            if user_fund < current_price and item_id == 1:
                break
            elif user_fund < current_price:
                continue

            # Deduct the item price from user funds
            query = """
                UPDATE public."user" 
                SET fund = fund - %s 
                WHERE user_id = %s;
                """
            values = (current_price, user_id)
            execute_query(query, values)

            # Add transaction
            query = """
                INSERT INTO public."buy_item" 
                (user_id, game_id, item_id, price, timestamp, "isCancelled") 
                VALUES (%s, %s, %s, %s, NOW(), %s)
                """
            values = (user_id, game_id, item_id, current_price, False)
            execute_query(query, values)

            # Add record to user_games
            if item_id == 1:
                query = """
                    INSERT INTO public."user_games" 
                    (user_id, game_id, installed_date) 
                    VALUES (%s, %s, NOW())
                    """
                values = (user_id, game_id)
                execute_query(query, values)

            user_fund -= current_price

            if user_fund <= 0:
                break

        if user_fund <= 0:
                break
print("finish buy items")


# add achievements
with open("achievement_names_and_descriptions.txt", encoding="utf-8") as file:
    achievement_names_and_descriptions_list = file.read()
achievements = achievement_names_and_descriptions_list.splitlines()

# Splitting the list into name and description
achievement_names_and_descriptions = [achievement.split(": ", 1) for achievement in achievements]

# Insert achievement into the achievements table with an auto-generated achievement_id
for game_id in game_ids:
    if not achievement_names_and_descriptions:
        break
    achievements_num = random.randint(achievements_num_min, achievements_num_max) if round(random.uniform(0, 1), 2) > rate_of_games_not_having_achievements else 0
    for _ in range(achievements_num):
        if not achievement_names_and_descriptions:
            break
        achievement_name = achievement_names_and_descriptions[0][0]
        achievement_description = achievement_names_and_descriptions[0][1]

        query = """
            INSERT INTO public."achievements" (game_id, achievement_name, achievement_description)
            VALUES (%s, %s, %s)
            """
        values = (game_id, achievement_name, achievement_description)
        execute_query(query, values)
        del achievement_names_and_descriptions[0]

print("finish add achievements")