from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, schemas
from auth import check_role

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Dummy user (simulate login)
CURRENT_USER = {"role": "admin"}  # change to viewer/analyst to test

# ---------------- USERS ----------------

@app.post("/users")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    check_role(CURRENT_USER["role"], ["admin"])
    new_user = models.User(name=user.name, role=user.role)
    db.add(new_user)
    db.commit()
    return {"message": "User created"}

# ---------------- TRANSACTIONS ----------------

@app.post("/transactions")
def create_transaction(tx: schemas.TransactionCreate, db: Session = Depends(get_db)):
    check_role(CURRENT_USER["role"], ["admin", "analyst"])

    if tx.amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be positive")

    new_tx = models.Transaction(**tx.dict())
    db.add(new_tx)
    db.commit()
    return {"message": "Transaction added"}

@app.get("/transactions")
def get_transactions(db: Session = Depends(get_db)):
    return db.query(models.Transaction).all()

@app.delete("/transactions/{tx_id}")
def delete_transaction(tx_id: int, db: Session = Depends(get_db)):
    check_role(CURRENT_USER["role"], ["admin"])

    tx = db.query(models.Transaction).filter(models.Transaction.id == tx_id).first()
    if not tx:
        raise HTTPException(status_code=404, detail="Not found")

    db.delete(tx)
    db.commit()
    return {"message": "Deleted"}

# ---------------- SUMMARY APIs ----------------

@app.get("/summary")
def summary(db: Session = Depends(get_db)):
    txs = db.query(models.Transaction).all()

    income = sum(t.amount for t in txs if t.type == "income")
    expense = sum(t.amount for t in txs if t.type == "expense")

    return {
        "total_income": income,
        "total_expense": expense,
        "net_balance": income - expense
    }

@app.get("/summary/category")
def category_summary(db: Session = Depends(get_db)):
    txs = db.query(models.Transaction).all()
    result = {}

    for t in txs:
        result[t.category] = result.get(t.category, 0) + t.amount

    return result
