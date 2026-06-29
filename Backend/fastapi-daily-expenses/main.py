from fastapi import FastAPI
from database import cursor, conn
from models import User, Transactions

app = FastAPI()

@app.post("/users")
def add_user(user: User):
    cursor.execute(
        "INSERT INTO users(name) VALUES (?)", (user.name,)
    )
    conn.commit()
    return{"message": "new user added"}

@app.post("/transactions")
def add_transactions(transactions: Transactions):
    cursor.execute(
        "SELECT id FROM users WHERE id=?",(transactions.user_id,)
        )
    user = cursor.fetchone()
    if user:
        cursor.execute(
            "INSERT INTO transactions(user_id,item,price,date) VALUES (?,?,?,?)", 
            (transactions.user_id, transactions.item, transactions.price, transactions.date,)
        )
        conn.commit()
        return{"message": "new transaction added"}
    else:
        return{"error": "the id not exists"}
    
@app.get("/users")
def get_users():
    cursor.execute(
        "SELECT id,name FROM users"
    )
    users= cursor.fetchall()
    if users:
        return[
            {"id": u[0],
            "name": u[1]}
            for u in users
        ]
    else:
        return{"error": "the data is not exist"}
    
@app.get("/users/{user_id}")
def get_transactions(user_id: int):
    cursor.execute(
        "SELECT name FROM users WHERE id=?", (user_id,)
        )    
    user= cursor.fetchone()
    if user:
        cursor.execute(
            "SELECT id, item, price, date FROM transactions WHERE user_id=?", (user_id,)
        )
        txs= cursor.fetchall()
        return{
            "name": user[0],
            "transactions":[
                {
                  "id": t[0],
                   "item": t[1],
                    "price": t[2],
                   "date": t[3]
                }
                for t in txs
            ]
        }
    else:
        return{"error": "the data is not exists"}

@app.get("/transactions")
def get_all_transactions():
    cursor.execute(
        "SELECT id, user_id, item, price, date FROM transactions"
    )  
    txs = cursor.fetchall()
    if txs:
        return[
                {
                "id": t[0],
                "user_id": t[1],
                "item": t[2],
                "price": t[3],
                "date": t[4]
                }
                for t in txs
        ]
    else:
        return[]
    
@app.delete("/transactions/{id}")
def delete_transaction(id: int):
    cursor.execute(
        "SELECT id FROM transactions WHERE id=?",(id,)
    )    
    txs= cursor.fetchone()
    if txs:
        cursor.execute(
        "DELETE FROM transactions WHERE id=?", (id,)
        )
        conn.commit()
        return{"message": "data deleted"}
    else:
        return{"message": "the id is not exist"}
    
@app.put("/transactions/{id}")
def update_transaction(transactions: Transactions, id: int):
    cursor.execute(
        "SELECT * FROM transactions WHERE id=?",(id,)
    )
    txs = cursor.fetchone()
    if txs:
        cursor.execute(
            "UPDATE transactions SET item=?, price=?, date=? WHERE id=?", (transactions.item, transactions.price, transactions.date, id,)
        )
        conn.commit()
        return{"message": "data updated"}
    else:
        return{"error": "the id doess not exist"}
    
@app.get("/transactions")
def get_min_price(min_price: int):
    cursor.execute("SELECT id, user_id, item, price, date FROM transactions WHERE price>=?", (min_price,))
    data = cursor.fetchall()
    if data:
        return[{
            "id": m[0],
            "user_id": m[1],
            "item": m[2],
            "price": m[3],
            "date": m[4]
            }
            for m in data
        ]
    else:
        return[]

