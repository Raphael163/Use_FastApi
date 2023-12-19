from faker import Faker

fake = Faker()


def generate_fake_user(user_id):
    return {
        "id": user_id,
        "role": fake.random_element(elements=("admin", "user")),
        "name": fake.name(),
        "email": fake.email(),
        "phone_number": fake.phone_number(),
        "address": fake.address(),
    }


# Генерация пользователей
fake_users = [generate_fake_user(user_id) for user_id in range(1, 40)]


def generate_fake_trade(trade_id, user_id):
    return {
        "id": trade_id,
        "user_id": user_id,
        "currency": fake.random_element(elements=("BTC", "ETH", "LTC", "XRP")),
        "side": fake.random_element(elements=("buy", "sell")),
        "price": fake.pyfloat(left_digits=4, right_digits=2, positive=True),
        "amount": fake.pyfloat(left_digits=3, right_digits=2, positive=True),
    }


# Генерация торговых сделок
fake_trades = [generate_fake_trade(trade_id, user_id) for trade_id, user_id in zip(range(1, 41), range(1, 41))]
