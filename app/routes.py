from flask import Blueprint, render_template, redirect, url_for, request, session
from extensions import db
from app.models import Employee, Manager, Task
from werkzeug.security import generate_password_hash, check_password_hash
from app.services.mail_services import (
    send_emp_mail,
    send_manager_mail,
    send_task_assignment_mail,
    send_task_completion_mail
)

main = Blueprint("main", __name__)


# Home
@main.route("/")
def index():
    return render_template("index.html")


# ---------------- ADMIN ----------------

@main.route("/admin-login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "1234":
            total_employees = Employee.query.count()
            total_managers = Manager.query.count()
            total_tasks = Task.query.count()

            return render_template(
                "admin_dashboard.html",
                total_employees=total_employees,
                total_managers=total_managers,
                total_tasks=total_tasks,
            )

        return render_template("admin_login.html", error="Invalid credentials")

    return render_template("admin_login.html")


# ---------------- EMPLOYEE ----------------

@main.route("/employee-login", methods=["GET", "POST"])
def employee_login():
    if request.method == "POST":
        name = request.form.get("username")
        password = request.form.get("password")

        employee = Employee.query.filter_by(name=name).first()

        if employee and check_password_hash(employee.password, password):
            session["employee_id"] = employee.id
            tasks = Task.query.filter_by(employee_id=employee.id).all()
            return render_template("employee_dashboard.html", employee=employee, tasks=tasks)

        return render_template("employee_login.html", error="Invalid credentials")

    return render_template("employee_login.html")


# ---------------- MANAGER ----------------

@main.route("/manager-login", methods=["GET", "POST"])
def manager_login():
    if request.method == "POST":
        name = request.form.get("name")
        password = request.form.get("password")

        manager = Manager.query.filter_by(name=name).first()

        if manager and check_password_hash(manager.password, password):
            session["manager_id"] = manager.id
            employees = Employee.query.all()
            tasks = Task.query.all()

            return render_template(
                "manager_dashboard.html",
                manager=manager,
                employees=employees,
                tasks=tasks
            )

        return render_template("manager_login.html", error="Invalid credentials")

    return render_template("manager_login.html")


# ---------------- EMPLOYEE MANAGEMENT ----------------

@main.route("/manage-employees")
def manage_employees():
    employees = Employee.query.all()
    return render_template("employee_manage.html", employees=employees)


@main.route("/add-employee", methods=["POST"])
def add_employee():
    name = request.form.get("employee_name")
    password = request.form.get("employee_password")
    email = request.form.get("emp_email")

    hashed_password = generate_password_hash(password)

    new_employee = Employee(name=name, password=hashed_password, email=email)
    db.session.add(new_employee)
    db.session.commit()

    try:
        send_emp_mail(email, name, password)
    except:
        print("Mail not sent")

    return redirect(url_for("main.manage_employees"))


@main.route("/delete-employee/<int:id>", methods=["POST"])
def del_emp(id):
    employee = Employee.query.get_or_404(id)
    db.session.delete(employee)
    db.session.commit()
    return redirect(url_for("main.manage_employees"))


# ---------------- MANAGER MANAGEMENT ----------------

@main.route("/manage-managers")
def manage_managers():
    managers = Manager.query.all()
    return render_template("manage_manager.html", managers=managers)


@main.route("/add-manager", methods=["POST"])
def add_manager():
    name = request.form.get("manager_name")
    password = request.form.get("manager_password")
    department = request.form.get("manager_department")
    email = request.form.get("manager_email")

    hashed_password = generate_password_hash(password)

    new_manager = Manager(
        name=name,
        password=hashed_password,
        department=department,
        email=email
    )

    db.session.add(new_manager)
    db.session.commit()

    try:
        send_manager_mail(email, name, password)
    except:
        print("Mail not sent")

    return redirect(url_for("main.manage_managers"))


@main.route("/delete-manager/<int:id>", methods=["POST"])
def delete_manager(id):
    manager = Manager.query.get_or_404(id)
    db.session.delete(manager)
    db.session.commit()
    return redirect(url_for("main.manage_managers"))


# ---------------- TASKS ----------------

@main.route("/add-task", methods=["POST"])
def add_task():
    title = request.form.get("title")
    employee_id = request.form.get("employee_id")

    manager_id = session.get("manager_id")

    new_task = Task(
        title=title,
        employee_id=employee_id,
        manager_id=manager_id
    )

    db.session.add(new_task)
    db.session.commit()

    employee = Employee.query.get(employee_id)
    manager = Manager.query.get(manager_id)

    try:
        send_task_assignment_mail(employee.email, employee.name, title, manager.name)
    except:
        print("Mail not sent")

    employees = Employee.query.all()
    tasks = Task.query.all()

    return render_template("manager_dashboard.html",
                           employees=employees,
                           tasks=tasks,
                           manager=manager)


@main.route("/complete-task/<int:id>", methods=["POST"])
def task_done(id):
    task = Task.query.get_or_404(id)
    task.status = "Completed"
    db.session.commit()

    manager = Manager.query.get(task.manager_id)
    employee = Employee.query.get(task.employee_id)

    try:
        send_task_completion_mail(manager.email, manager.name, task.title, employee.name)
    except:
        print("Mail not sent")

    tasks = Task.query.filter_by(employee_id=employee.id).all()

    return render_template("employee_dashboard.html",
                           employee=employee,
                           tasks=tasks)


# ---------------- VIEW ALL ----------------

@main.route("/view-detail")
def view_detail():
    employees = Employee.query.all()
    managers = Manager.query.all()
    return render_template("view.html", employees=employees, managers=managers)
