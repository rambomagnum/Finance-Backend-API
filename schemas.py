from pydantic import BaseModel

class TransactionCreate(BaseModel):
    amount: float
    type: str
    category: str
    date: str
    notes: str

class UserCreate(BaseModel):
    name: str
    role: str
