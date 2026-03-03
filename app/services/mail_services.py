import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

SENDGRID_API_KEY = os.environ.get("MAIL_PASSWORD")
FROM_EMAIL = "rahul.business940@gmai.com"

def send_mail(subject, to_email, body):
    message = Mail(
        from_email=FROM_EMAIL,
        to_emails=to_email,
        subject=subject,
        plain_text_content=body
    )

    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print("Email sent:", response.status_code)
    except Exception as e:
        print("SendGrid error:", str(e))
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
