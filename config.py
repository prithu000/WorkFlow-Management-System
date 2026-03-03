import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev_secret_key")

    SQLALCHEMY_DATABASE_URI = "sqlite:///company.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = "smtp.sendgrid.net"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "apikey"
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = "rahul.business940@gmail.com"
