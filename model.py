from sqlalchemy import Column, Integer, String, Float, Date
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    role = Column(String)  # admin, analyst, viewer

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True)
    amount = Column(Float)
    type = Column(String)  # income / expense
    category = Column(String)
    date = Column(String)
    notes = Column(String)
