# 🚀 FastAPI CRUD App – Employee Management

A simple and scalable **CRUD (Create, Read, Update, Delete)** application built using **FastAPI** to manage employee records with an SQLite database.

---

## 📌 Tech Stack

* ⚡ FastAPI
* 🛢️ SQLAlchemy
* ✅ Pydantic
* 🚀 Uvicorn
* 🗄️ SQLite

---

## 📋 Prerequisites

Make sure you have the following installed:

* Python **3.10+**
* pip (Python package manager)

---

## ⚙️ Getting Started

Follow these steps to set up and run the project locally:

---

# Clone the repository
```bash
git clone https://github.com/Sakshamsinha23/FastApi-Crud.git
```
# Navigate into the project directory
```bash
cd FastApi-Crud
```
---

### 2️⃣ Create Virtual Environment

```bash
python3 -m venv venv
```

---

### 3️⃣ Activate Virtual Environment

**macOS/Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

---

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 5️⃣ Run the Server

```bash
uvicorn main:app --reload
```

---

### 6️⃣ Open API Docs (Swagger UI)

👉 Open in browser:

```
http://127.0.0.1:8000/docs
```

---

## 🔗 API Endpoints

| Method | Endpoint              | Description           |
| ------ | --------------------- | --------------------- |
| POST   | `/employees`          | Create a new employee |
| GET    | `/employees`          | Get all employees     |
| GET    | `/employees/{emp_id}` | Get employee by ID    |
| PUT    | `/employees/{emp_id}` | Update employee by ID |
| DELETE | `/employees/{emp_id}` | Delete employee by ID |

---

## 📁 Project Structure

```bash
FastApi-Crud-2/
│
├── main.py          # 🚀 Entry point of the app (API routes)
├── models.py        # 🛢️ SQLAlchemy models (Employee table)
├── schemas.py       # ✅ Pydantic schemas (validation)
├── crud.py          # 🔄 CRUD operations logic
├── database.py      # 🔌 DB connection & session setup
├── requirements.txt # 📦 Dependencies
└── test.db          # 🗄️ SQLite database (auto-created)
```

---

## 💡 Key Features

* ✔️ Clean and modular architecture
* ✔️ RESTful API design
* ✔️ Automatic interactive API docs (Swagger UI)
* ✔️ Data validation using Pydantic
* ✔️ Lightweight database (SQLite)

---


