# Finance-Backend-API(Data Processing)

 
## 🚀 Overview
This project is a backend system for managing financial records with role-based access control and dashboard analytics.

## 🧠 Features
- User & Role Management (Admin, Analyst, Viewer)
- CRUD operations for transactions
- Filtering transactions
- Summary APIs:
  - Total Income
  - Total Expense
  - Net Balance
  - Category-wise breakdown

## ⚙️ Tech Stack
- Python (FastAPI)
- SQLite (can be replaced with PostgreSQL)
- SQLAlchemy

## 🔐 Roles
- Admin → Full access
- Analyst → Read + analytics
- Viewer → Read only

## 📌 API Endpoints

### Users
- POST /users

### Transactions
- POST /transactions
- GET /transactions
- DELETE /transactions/{id}

### Summary
- GET /summary
- GET /summary/category

## ▶️ How to Run

```bash
pip install -r requirements.txt
uvicorn main:app --reload
