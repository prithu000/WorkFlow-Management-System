from flask import Flask
from config import Config
from extensions import db, mail
import os

def create_app():
    app = Flask(__name__,
    template_folder=os.path.join(os.getcwd(), "templates"),
    static_folder=os.path.join(os.getcwd(), "static")
)
    app.config.from_object(Config)

    db.init_app(app)
    mail.init_app(app)

    from app.routes import main
    app.register_blueprint(main)

    return app
