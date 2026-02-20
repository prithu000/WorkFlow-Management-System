from flask_mail import Message
from extensions import mail

SENDER = "keertipillai49@gmail.com"

def send_mail(subject, to_email, body):
    msg = Message(subject=subject, sender=SENDER, recipients=[to_email])
    msg.body = body
    mail.send(msg)

def send_emp_mail(to_email, username, password):
    body = f"""
Hello {username},

Your employee account has been created.

Username: {username}
Password: {password}

Regards,
Admin Team
"""
    send_mail("Employee Account Created", to_email, body)


def send_manager_mail(to_email, name, password):
    body = f"""
Hello {name},

Your manager account has been created.

Password: {password}

Regards,
Admin Team
"""
    send_mail("Manager Account Created", to_email, body)


def send_task_assignment_mail(to_email, username, task_title, manager_name):
    body = f"""
Hello {username},

A new task has been assigned by {manager_name}.

Task: {task_title}

Regards,
Admin Team
"""
    send_mail("New Task Assigned", to_email, body)


def send_task_completion_mail(to_email, manager_name, task_title, employee_name):
    body = f"""
Hello {manager_name},

Task '{task_title}' has been completed by {employee_name}.

Regards,
Admin Team
"""
    send_mail("Task Completed", to_email, body)
