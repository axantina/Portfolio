from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

stocks = [
    {"name": "PS4", "buy_price": 10000, "sell_price": 13000},
    {"name": "PS5", "buy_price": 20000, "sell_price": 25000}
]

class Stock(BaseModel):
    name: str
    buy_price: int
    sell_price: int

@app.get("/")
def home():
    return {"message": "API is running!"}

@app.get("/stocks")
def get_stocks():
    return stocks

@app.post("/stocks/add", response_model=None)
def add_stock(stock: Stock):
    stocks.append(stock.model_dump())
    return {"message": "added", "data": stocks}

@app.get("/stocks/search")
def search_stock(keyword: str):
    result = []
    for item in stocks:
        if keyword.lower() in item["name"].lower():
            result.append(item)
    return {"total": len(result), "data": result}

@app.put("/stocks/update")
def update_stock(name: str, new_price: int):
    for item in stocks:
        if item["name"] == name:
            item["sell_price"] = new_price
    return {"message": "updated", "data": stocks}

@app.delete("/stocks/delete")
def delete_stock(name: str):
    global stocks
    stocks = [item for item in stocks if item["name"] != name]
    return {"message": "deleted", "data": stocks}