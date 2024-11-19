import psycopg2
from faker import Faker
import random
import datetime

# Create a Faker instance
fake = Faker()

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname="DB_Final_Project", 
    user="postgres", 
    password="bear123321a", 
    host="localhost"
)
cur = conn.cursor()

# Generate random data for each table

# 1. Insert into "user" table
def insert_user():
    user_id = fake.unique.random_number(digits=10)
    password_hashed = fake.password(length=20)
    user_name = fake.user_name()
    user_description = fake.text(max_nb_chars=300)
    profile_pic = fake.image_url()
    profile_background = fake.image_url()
    birthday = fake.date_of_birth(minimum_age=18, maximum_age=60)
    email = fake.email()
    country = fake.country()
    language = fake.language_name()
    fund = random.randint(0, 10000)
    filtering = random.choice([True, False])
    notification = random.choice([True, False])
    cookies = random.choice([True, False])

    cur.execute(
        "INSERT INTO public.\"user\" (user_id, password_hashed, user_name, user_description, profile_pic, profile_background, birthday, email, country, language, fund, filtering, notification, cookies) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (user_id, password_hashed, user_name, user_description, profile_pic, profile_background, birthday, email, country, language, fund, filtering, notification, cookies)
    )

# 2. Insert into "ACHIEVEMENTS" table
def insert_achievements():
    game_id = fake.unique.random_number(digits=10)
    achievement_id = fake.unique.random_number(digits=10)
    achievement_name = fake.word()  # Generate a random achievement name

    cur.execute(
        "INSERT INTO public.achievements (game_id, achievement_id, achievement_name) "
        "VALUES (%s, %s, %s)",
        (game_id, achievement_id, achievement_name)
    )


# 3. Insert into "add_fund_record" table
def insert_add_fund_record():
    add_fund_record_id = fake.uuid4()
    user_id = fake.random_number(digits=10)
    fund_change = random.randint(0, 1000)
    timestamp = fake.date_time_this_year()

    cur.execute(
        "INSERT INTO public.add_fund_record (add_fund_record_id, user_id, fund_change, timestamp) "
        "VALUES (%s, %s, %s, %s)",
        (add_fund_record_id, user_id, fund_change, timestamp)
    )

# 4. Insert into "buy_item" table
def insert_buy_item():
    buy_item_id = fake.uuid4()
    user_id = fake.random_number(digits=10)
    game_id = fake.unique.random_number(digits=10)
    item_id = fake.unique.random_number(digits=10)
    price = random.randint(1, 100)
    timestamp = fake.date_time_this_year()
    is_cancelled = random.choice([True, False])

    cur.execute(
        "INSERT INTO public.buy_item (buy_item_id, user_id, game_id, item_id, price, timestamp, isCancelled) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (buy_item_id, user_id, game_id, item_id, price, timestamp, is_cancelled)
    )

# 5. Insert into "buy_item_cancel" table
def insert_buy_item_cancel():
    buy_item_id = fake.uuid4()
    game_id = fake.unique.random_number(digits=10)
    item_id = fake.unique.random_number(digits=10)
    timestamp = fake.date_time_this_year()

    cur.execute(
        "INSERT INTO public.buy_item_cancel (buy_item_id, game_id, item_id, timestamp) "
        "VALUES (%s, %s, %s, %s)",
        (buy_item_id, game_id, item_id, timestamp)
    )

# 6. Insert into "CART" table
def insert_cart():
    user_id = fake.random_number(digits=10)
    game_id = fake.unique.random_number(digits=10)
    item_id = fake.unique.random_number(digits=10)

    cur.execute(
        "INSERT INTO public.\"CART\" (user_id, game_id, item_id) "
        "VALUES (%s, %s, %s)",
        (user_id, game_id, item_id)
    )

# 7. Insert into "DEVELOPERS" table
def insert_developers():
    developer_id = fake.unique.random_number(digits=10)
    developer_name = fake.company()
    description = fake.text(max_nb_chars=100)

    cur.execute(
        "INSERT INTO public.\"DEVELOPERS\" (developer_id, developer_name, description) "
        "VALUES (%s, %s, %s)",
        (developer_id, developer_name, description)
    )

# 8. Insert into "GAME" table
def insert_game():
    game_id = fake.unique.random_number(digits=10)
    game_name = fake.word()
    game_description = fake.text(max_nb_chars=100)
    system_requirements = fake.text(max_nb_chars=100)

    cur.execute(
        "INSERT INTO public.\"GAME\" (game_id, game_name, game_description, system_reuirements) "
        "VALUES (%s, %s, %s, %s)",
        (game_id, game_name, game_description, system_requirements)
    )

# 9. Insert into "game_developers" table
def insert_game_developers():
    developer_id = fake.random_number(digits=10)
    game_id = fake.random_number(digits=10)

    cur.execute(
        "INSERT INTO public.game_developers (developer_id, game_id) "
        "VALUES (%s, %s)",
        (developer_id, game_id)
    )

# 10. Insert into "game_game_type" table
def insert_game_game_type():
    game_id = fake.random_number(digits=10)
    game_type_id = fake.random_number(digits=10)

    cur.execute(
        "INSERT INTO public.game_game_type (game_id, game_type_id) "
        "VALUES (%s, %s)",
        (game_id, game_type_id)
    )

# 11. Insert into "game_item" table
def insert_game_item():
    item_id = fake.unique.random_number(digits=10)
    game_id = fake.random_number(digits=10)
    original_price = random.randint(1, 100)
    current_price = random.randint(1, 100)
    special_offer = random.uniform(0, 1)
    release_date = fake.date_this_year()

    cur.execute(
        "INSERT INTO public.game_item (item_id, game_id, original_price, current_price, special_offer, release_date) "
        "VALUES (%s, %s, %s, %s, %s, %s)",
        (item_id, game_id, original_price, current_price, special_offer, release_date)
    )

# 12. Insert into "game_publishers" table
def insert_game_publishers():
    publisher_id = fake.unique.random_number(digits=10)
    game_id = fake.random_number(digits=10)

    cur.execute(
        "INSERT INTO public.\"GAME_PUBLISHERS\" (publisher_id, game_id) "
        "VALUES (%s, %s)",
        (publisher_id, game_id)
    )

# 13. Insert into "game_reviews" table
def insert_game_reviews():
    review_id = fake.uuid4()
    game_id = fake.random_number(digits=10)
    user_id = fake.random_number(digits=10)
    rating = random.randint(1, 5)
    text = fake.text(max_nb_chars=100)
    review_timestamp = fake.date_time_this_year()

    cur.execute(
        "INSERT INTO public.game_reviews (review_id, game_id, user_id, rating, text, review_timestamp) "
        "VALUES (%s, %s, %s, %s, %s, %s)",
        (review_id, game_id, user_id, rating, text, review_timestamp)
    )

# 14. Insert into "game_types" table
def insert_game_types():
    game_type_id = fake.unique.random_number(digits=10)
    game_type_name = fake.word()

    cur.execute(
        "INSERT INTO public.game_types (game_type_id, game_type_name) "
        "VALUES (%s, %s)",
        (game_type_id, game_type_name)
    )

# 15. Insert into "publishers" table
def insert_publishers():
    publisher_id = fake.unique.random_number(digits=10)
    publisher_name = fake.company()
    description = fake.text(max_nb_chars=100)

    cur.execute(
        "INSERT INTO public.publishers (publisher_id, publisher_name, description) "
        "VALUES (%s, %s, %s)",
        (publisher_id, publisher_name, description)
    )

# 16. Insert into "user_achievements" table
def insert_user_achievements():
    user_id = fake.random_number(digits=10)
    achievement_id = fake.random_number(digits=10)

    cur.execute(
        "INSERT INTO public.user_achievements (user_id, achievement_id) "
        "VALUES (%s, %s)",
        (user_id, achievement_id)
    )

# 17. Insert into "user_games" table
def insert_user_games():
    user_id = fake.random_number(digits=10)
    game_id = fake.random_number(digits=10)
    installed_date = fake.date_this_decade()
    uninstalled_date = fake.date_this_decade() if random.choice([True, False]) else None

    cur.execute(
        "INSERT INTO public.user_games (user_id, game_id, installed_date, uninstalled_date) "
        "VALUES (%s, %s, %s, %s)",
        (user_id, game_id, installed_date, uninstalled_date)
    )

# 18. Insert into "user_game_statistics" table
def insert_user_game_statistics():
    user_id = fake.random_number(digits=10)
    game_id = fake.random_number(digits=10)
    played_time = str(random.randint(1, 100)) + ' hours'  # Example format: 5 hours
    achievement_num = random.randint(0, 100)

    cur.execute(
        "INSERT INTO public.user_game_statistics (user_id, game_id, played_time, achievement_num) "
        "VALUES (%s, %s, %s, %s)",
        (user_id, game_id, played_time, achievement_num)
    )

# 19. Insert into "user_game_types" table
def insert_user_game_types():
    user_id = fake.random_number(digits=10)
    game_type_id = fake.random_number(digits=10)

    cur.execute(
        "INSERT INTO public.user_game_types (user_id, game_type_id) "
        "VALUES (%s, %s)",
        (user_id, game_type_id)
    )

# 20. Insert into "user_inventory" table
def insert_user_inventory():
    user_id = fake.random_number(digits=10)
    game_id = fake.random_number(digits=10)
    item_id = fake.random_number(digits=10)
    acquired_date = fake.date_this_year()
    not_owned_date = fake.date_this_year() if random.choice([True, False]) else None

    cur.execute(
        "INSERT INTO public.user_inventory (user_id, game_id, item_id, acquired_date, not_owned_date) "
        "VALUES (%s, %s, %s, %s, %s)",
        (user_id, game_id, item_id, acquired_date, not_owned_date)
    )

# 21. Insert into "user_friends" table
def insert_user_friends():
    user_id = fake.random_number(digits=10)
    friend_id = fake.random_number(digits=10)

    cur.execute(
        "INSERT INTO public.user_friends (user_id, friend_id) "
        "VALUES (%s, %s)",
        (user_id, friend_id)
    )

# Number of records to insert
num_records = 100

# Insert data for all tables
for _ in range(num_records):
    insert_user()  # Insert into "user"
    insert_achievements()  # Insert into "achievements"
    insert_add_fund_record()  # Insert into "add_fund_record"
    insert_buy_item()  # Insert into "buy_item"
    insert_buy_item_cancel()  # Insert into "buy_item_cancel"
    insert_cart()  # Insert into "cart"
    insert_developers()  # Insert into "developers"
    insert_game()  # Insert into "game"
    insert_game_developers()  # Insert into "game_developers"
    insert_game_game_type()  # Insert into "game_game_type"
    insert_game_item()  # Insert into "game_item"
    insert_game_publishers()  # Insert into "game_publishers"
    insert_game_reviews()  # Insert into "game_reviews"
    insert_game_types()  # Insert into "game_types"
    insert_publishers()  # Insert into "publishers"
    insert_user_achievements()  # Insert into "user_achievements"
    insert_user_games()  # Insert into "user_games"
    insert_user_game_statistics()  # Insert into "user_game_statistics"
    insert_user_game_types()  # Insert into "user_game_types"
    insert_user_inventory()  # Insert into "user_inventory"
    insert_user_friends()  # Insert into "user_friends"

# Commit all the inserts
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
