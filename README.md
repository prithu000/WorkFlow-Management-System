# Workflow Management System (WMS)

A Role-Based Employee Task Management Platform built using Flask and SQLite.

## 📖 Project Overview

Workflow Management System (WMS) is a web-based application that allows organizations to manage employees, managers, and task assignments efficiently.

The system provides role-based authentication and enables managers to assign tasks while employees can track and complete assigned tasks.

---

## 🚀 Features

- 🔐 Role-Based Authentication (Admin, Manager, Employee)
- 👥 Employee & Manager Management
- 📋 Task Assignment System
- 📊 Dashboard with Task Overview
- 📧 Email Notifications for:
  - Account Creation
  - Task Assignment
  - Task Completion
- 🗂 SQLite Database Integration
- 🎨 Responsive Modern UI (Glassmorphism Design)

---

## 🏗 Tech Stack

- **Backend:** Flask (Python)
- **Database:** SQLite
- **Frontend:** HTML, CSS
- **ORM:** SQLAlchemy
- **Authentication:** Werkzeug Security
- **Email Service:** Flask-Mail
- **Version Control:** Git & GitHub

---

## 🗃 Project Structure
workflow-management-system/
│
├── app/
│ ├── init.py
│ ├── models.py
│ ├── routes.py
│ └── services/
│ └── mail_services.py
│
├── templates/
│ ├── base.html
│ ├── index.html
│ ├── admin_dashboard.html
│ ├── employee_dashboard.html
│ ├── manager_dashboard.html
│ └── ...
│
├── static/
│ └── css/
│ └── style.css
│
├── config.py
├── extensions.py
├── run.py
├── requirements.txt
└── README.md
