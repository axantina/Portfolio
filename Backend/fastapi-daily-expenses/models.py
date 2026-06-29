from pydantic import BaseModel

class User(BaseModel):
    name : str

class Transactions(BaseModel):
    user_id : int
    item : str
    price : int
    date : str