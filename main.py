from fastapi import FastAPI

app = FastAPI(
    title="Shop app2"
)

fake_users = [
    {"id": 1, "name": "Oleg"},
    {"id": 2, "name": "Daniil"}
]


@app.get("/users")
def get_users():
    return fake_users


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return [user for user in fake_users if user.get('id') == user_id]


fake_shop = [
    {"id": 1, "title": "Кольцо", "price": 200_000},
    {"id": 2, "title": "Кольцо 3", "price": 210_000},
    {"id": 3, "title": "Кольцо", "price": 254_000},
    {"id": 4, "title": "Кольцо 2", "price": 20_000},
]


@app.get("/shop")
def get_shop(limit: int = 1, offset: int = 1):
    return fake_shop[offset:][:limit]


@app.post("/shop/{shop_id}")
def change_shop_price(shop_id: int, new_price: int):
    print(shop_id)
    current_shop = list(filter(lambda shop: shop.get("id") == shop_id, fake_shop))[0]
    current_shop["price"] = new_price
    return {"statue": 200, "data": current_shop}
