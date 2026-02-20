from extensions import db
from datetime import datetime

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

class Manager(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    department = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True, nullable=False)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(20), default="Pending")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    employee_id = db.Column(db.Integer, db.ForeignKey("employee.id"), nullable=False)
    manager_id = db.Column(db.Integer, db.ForeignKey("manager.id"))

    employee = db.relationship("Employee", backref="tasks")
    manager = db.relationship("Manager", backref="tasks")
