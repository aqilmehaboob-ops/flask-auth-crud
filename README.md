# Flask Expense Tracker (Authentication + Relational Database)

A backend-focused Flask web application that implements user authentication and a relational expense tracking system using SQLAlchemy ORM.

This project demonstrates backend fundamentals required for entry-level backend roles, including authentication, session management, relational database design, CRUD operations, and ownership validation.

---

## 🚀 Features

### 🔐 Authentication System
- User Registration (with unique username validation)
- Password hashing using Werkzeug
- Secure Login system
- Session-based authentication
- Protected routes
- Logout functionality

### 💾 Relational Database Design
- One-to-Many relationship (User → Multiple Expenses)
- ForeignKey implementation (`user_id`)
- Ownership validation for security

### 📊 Expense Tracker
- Add new expense
- Update expense
- Delete individual expense
- View only logged-in user's expenses
- Calculate total expenses
- Secure expense editing with ownership check

---

## 🛠 Tech Stack

- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- WTForms
- Werkzeug Security
- Jinja2 Templates
- Git & GitHub

---

## 🧠 Concepts Implemented

- Object-Oriented Programming (OOP)
- ORM (Object Relational Mapping)
- One-to-Many Relationships
- Primary Key & Foreign Key usage
- Session Management
- POST-Redirect-GET pattern
- Form handling & validation
- Secure CRUD operations
- Basic backend security practices

---

## 📂 Project Structure


project/
│
├── app.py
├── createaccountform.py
├── templates/
│ ├── home.html
│ ├── loginaccountpage.html
│ ├── createaccountpage.html
│ ├── successloginpage.html
│ └── accountcreatedpage.html
│
├── users.sqlite3 (ignored in git)
└── README.md


---

## 🔗 Database Schema

### Users Table
- id (Primary Key)
- name (Unique)
- password (Hashed)
- age
- height
- weight
- date

### Expense Table
- id (Primary Key)
- title
- amount
- user_id (Foreign Key → users.id)

Relationship:

One User → Many Expenses


---

## ▶️ How To Run Locally

1. Clone the repository:


git clone https://github.com/https://github.com/aqilmehaboob-ops/flask-auth-crud

cd flask-auth-crud


2. Create virtual environment:


python -m venv venv


3. Activate virtual environment:

**Windows:**

venv\Scripts\activate


**Mac/Linux:**

source venv/bin/activate


4. Install dependencies:


pip install flask flask_sqlalchemy flask_wtf werkzeug


5. Run the application:


python app.py


6. Open in browser:


http://127.0.0.1:5000/


---

## 🔒 Security Practices Used

- Password hashing (never storing plain passwords)
- Session-based authentication
- Ownership validation before update/delete
- POST method for destructive actions
- Avoided direct SQL queries (used ORM)

---

## 🎯 Why This Project Matters

This project demonstrates:

- Backend system design
- Relational database understanding
- Secure CRUD operations
- Real-world authentication flow
- Clean separation of concerns

It represents a strong foundation for backend internship and junior backend roles.

---

## 📌 Future Improvements

- REST API version of this project
- PostgreSQL migration
- Deployment to production server
- Pagination and sorting
- Token-based authentication (JWT)

---

## 👨‍💻 Author

Built as part of a backend development learning journey toward entry-level backend roles.
