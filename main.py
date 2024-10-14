from typing import List

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="Shop app"
)


class Product(BaseModel):
    id: int
    title: str
    price: int = Field(..., gt=0)


fake_product_data = [
    {"id": 1, "title": "Кольцо", "price": 200_000},
    {"id": 2, "title": "Кольцо 3", "price": 210_000},
    {"id": 3, "title": "Кольцо", "price": 254_000},
    {"id": 4, "title": "Кольцо 2", "price": 20_000},
]


@app.get("/product", response_model=List[Product])
def get_product(limit: int = 1, offset: int = 1):
    return fake_product_data[offset:][:limit]


@app.post("/product/{product_id}")
def change_product_price(product_id: int, new_price: int):
    print(product_id)
    current_shop = list(filter(lambda shop: shop.get("id") == product_id, fake_product_data))[0]
    current_shop["price"] = new_price
    return {"statue": 200, "data": current_shop}


@app.post("/product")
def add_product(shop: List[Product]):
    fake_product_data.extend(shop)
    return { "status": 200, "data": fake_product_data }