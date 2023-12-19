from fastapi import FastAPI
from fake_Base import fake_users
from fake_Base import fake_trades

app = FastAPI(
    title='Trading app'
)

base_user = fake_users
trade_base = fake_trades


@app.get("/users/{user_id}")
def get_user(user_id: int):
    """ Вывод пользователей по id """
    return [user for user in base_user if user.get("id") == user_id]


@app.get("/trades")
def get_trades(limit: int, offset: int):
    """ Вывод пользователей через slize (срезы), limit- указываем сколько показываем, offset с какого"""
    return trade_base[offset:][:limit]