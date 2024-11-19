import random
import faker
from datetime import datetime, timedelta

# Setup Faker for generating mock data
fake = faker.Faker()

# Data stores for unique values
users = {}
games = {}
game_types = {}
game_items = {}
game_developers = {}
game_publishers = {}
game_reviews = {}
user_inventory = {}
user_games = {}
user_game_statistics = {}
user_achievements = {}
game_additions = {}
user_notifications = {}
user_carts = {}
game_tags = {}
user_ratings = {}
game_dlc = {}
user_payments = {}
game_subscriptions = {}
game_suggestions = {}

# Define a function to generate users
def generate_users(num=10):
    for _ in range(num):
        user_id = fake.unique.random_number(digits=10)
        users[user_id] = {
            "user_id": user_id,
            "user_name": fake.user_name(),
            "email": fake.email(),
            "birthday": fake.date_of_birth(minimum_age=18, maximum_age=80),
            "country": fake.country(),
            "language": fake.language_name(),
            "fund": random.randint(100, 1000),
            "notification": random.choice([True, False]),
            "cookies": random.choice([True, False]),
        }
        print(f"INSERT INTO user (user_id, user_name, email, birthday, country, language, fund, notification, cookies) "
              f"VALUES ('{user_id}', '{users[user_id]['user_name']}', '{users[user_id]['email']}', "
              f"'{users[user_id]['birthday']}', '{users[user_id]['country']}', '{users[user_id]['language']}', "
              f"{users[user_id]['fund']}, {users[user_id]['notification']}, {users[user_id]['cookies']});")

# Define a function to generate games
def generate_games(num=10):
    for _ in range(num):
        game_id = fake.unique.random_number(digits=10)
        games[game_id] = {
            "game_id": game_id,
            "game_name": fake.word(),
            "game_description": fake.sentence(),
            "system_requirements": fake.sentence(),
        }
        print(f"INSERT INTO game (game_id, game_name, game_description, system_requirements) "
              f"VALUES ('{game_id}', '{games[game_id]['game_name']}', '{games[game_id]['game_description']}', "
              f"'{games[game_id]['system_requirements']}');")

# Define a function to generate game types
def generate_game_types(num=5):
    for _ in range(num):
        game_type_id = fake.unique.random_number(digits=10)
        game_types[game_type_id] = {
            "game_type_id": game_type_id,
            "game_type_name": fake.word(),
        }
        print(f"INSERT INTO game_types (game_type_id, game_type_name) "
              f"VALUES ('{game_type_id}', '{game_types[game_type_id]['game_type_name']}');")

# Define a function to generate game items
def generate_game_items(num=10):
    for _ in range(num):
        game_item = fake.unique.random_number(digits=10)
        game_id = random.choice(list(games.keys()))
        game_items[game_item] = {
            "item_id": game_item,
            "game_id": game_id,
            "original_price": random.randint(10, 100),
            "current_price": random.randint(10, 100),
            "special_offer": random.uniform(0, 1),
            "release_date": fake.date_this_decade(),
        }
        print(f"INSERT INTO game_items (item_id, game_id, original_price, current_price, special_offer, release_date) "
              f"VALUES ('{game_item}', '{game_id}', {game_items[game_item]['original_price']}, "
              f"{game_items[game_item]['current_price']}, {game_items[game_item]['special_offer']}, "
              f"'{game_items[game_item]['release_date']}');")

# Define a function to generate game developers
def generate_game_developers(num=10):
    for _ in range(num):
        developer_id = fake.unique.random_number(digits=10)
        game_id = random.choice(list(games.keys()))
        print(f"INSERT INTO game_developers (developer_id, game_id) VALUES ('{developer_id}', '{game_id}');")

# Define a function to generate game publishers
def generate_game_publishers(num=10):
    for _ in range(num):
        publisher_id = fake.unique.random_number(digits=10)
        game_id = random.choice(list(games.keys()))
        print(f"INSERT INTO game_publishers (publisher_id, game_id) VALUES ('{publisher_id}', '{game_id}');")

# Define a function to generate user game statistics
def generate_user_game_statistics(num=10):
    for _ in range(num):
        user_id = random.choice(list(users.keys()))
        game_id = random.choice(list(games.keys()))
        playtime = random.randint(1, 1000)
        last_played = fake.date_this_year()
        user_game_statistics_id = fake.unique.random_number(digits=10)
        print(f"INSERT INTO user_game_statistics (user_game_statistics_id, user_id, game_id, playtime, last_played) "
              f"VALUES ('{user_game_statistics_id}', '{user_id}', '{game_id}', {playtime}, '{last_played}');")

# Define a function to generate user achievements
def generate_user_achievements(num=10):
    for _ in range(num):
        user_id = random.choice(list(users.keys()))
        game_id = random.choice(list(games.keys()))
        achievement_id = fake.unique.random_number(digits=10)
        print(f"INSERT INTO user_achievements (user_id, game_id, achievement_id) "
              f"VALUES ('{user_id}', '{game_id}', '{achievement_id}');")

# Define a function to generate user inventories
def generate_user_inventory(num=10):
    for _ in range(num):
        user_id = random.choice(list(users.keys()))
        game_item = random.choice(list(game_items.keys()))
        game_id = game_items[game_item]["game_id"]
        acquired_date = fake.date_this_century()
        not_owned_date = fake.date_this_century() if random.choice([True, False]) else None
        print(f"INSERT INTO user_inventory (user_id, game_id, item_id, acquired_date, not_owned_date) "
              f"VALUES ('{user_id}', '{game_id}', '{game_item}', '{acquired_date}', '{not_owned_date}');")

# Define a function to generate user games
def generate_user_games(num=10):
    for _ in range(num):
        user_id = random.choice(list(users.keys()))
        game_id = random.choice(list(games.keys()))
        installed_date = fake.date_this_decade()
        uninstalled_date = fake.date_this_decade() if random.choice([True, False]) else None
        print(f"INSERT INTO user_games (user_id, game_id, installed_date, uninstalled_date) "
              f"VALUES ('{user_id}', '{game_id}', '{installed_date}', '{uninstalled_date}');")

# Define a function to generate game reviews
def generate_game_reviews(num=10):
    for _ in range(num):
        user_id = random.choice(list(users.keys()))
        game_id = random.choice(list(games.keys()))
        review_id = fake.unique.random_number(digits=10)
        rating = random.randint(1, 5)
        text = fake.sentence()
        print(f"INSERT INTO game_reviews (review_id, game_id, user_id, rating, text) "
              f"VALUES ('{review_id}', '{game_id}', '{user_id}', {rating}, '{text}');")

# Define a function to generate user payments
def generate_user_payments(num=10):
    for _ in range(num):
        user_id = random.choice(list(users.keys()))
        payment_id = fake.unique.random_number(digits=10)
        amount = random.randint(10, 100)
        payment_date = fake.date_this_year()
        print(f"INSERT INTO user_payments (payment_id, user_id, amount, payment_date) "
              f"VALUES ('{payment_id}', '{user_id}', {amount}, '{payment_date}');")

# Define a function to generate user cart items
def generate_user_carts(num=10):
    for _ in range(num):
        user_id = random.choice(list(users.keys()))
        game_item = random.choice(list(game_items.keys()))
        added_to_cart = fake.date_this_century()
        print(f"INSERT INTO user_carts (user_id, item_id, added_to_cart) "
              f"VALUES ('{user_id}', '{game_item}', '{added_to_cart}');")

# Define a function to generate game tags
def generate_game_tags(num=10):
    for _ in range(num):
        game_id = random.choice(list(games.keys()))
        tag = fake.word()
        print(f"INSERT INTO game_tags (game_id, tag) "
              f"VALUES ('{game_id}', '{tag}');")

# Define a function to generate game downloadable content (DLC)
def generate_game_dlc(num=10):
    for _ in range(num):
        game_id = random.choice(list(games.keys()))
        dlc_id = fake.unique.random_number(digits=10)
        dlc_name = fake.word()
        print(f"INSERT INTO game_dlc (game_id, dlc_id, dlc_name) "
              f"VALUES ('{game_id}', '{dlc_id}', '{dlc_name}');")

# Define a function to generate game subscriptions
def generate_game_subscriptions(num=10):
    for _ in range(num):
        user_id = random.choice(list(users.keys()))
        game_id = random.choice(list(games.keys()))
        subscription_date = fake.date_this_year()
        print(f"INSERT INTO game_subscriptions (user_id, game_id, subscription_date) "
              f"VALUES ('{user_id}', '{game_id}', '{subscription_date}');")

# Define a function to generate game suggestions
def generate_game_suggestions(num=10):
    for _ in range(num):
        user_id = random.choice(list(users.keys()))
        game_id = random.choice(list(games.keys()))
        suggestion_date = fake.date_this_year()
        print(f"INSERT INTO game_suggestions (user_id, game_id, suggestion_date) "
              f"VALUES ('{user_id}', '{game_id}', '{suggestion_date}');")

# Generate the data for all tables
generate_users(5)
generate_games(3)
generate_game_types(3)
generate_game_items(5)
generate_game_developers(5)
generate_game_publishers(5)
generate_user_game_statistics(5)
generate_user_achievements(5)
generate_user_inventory(5)
generate_user_games(5)
generate_game_reviews(5)
generate_user_payments(5)
generate_user_carts(5)
generate_game_tags(5)
generate_game_dlc(5)
generate_game_subscriptions(5)
generate_game_suggestions(5)
