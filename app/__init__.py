from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()  # flask_sqlalchemy db


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)  # connecting GCP MySQL with ConnStr in config_class

    from app.routes import main
    app.register_blueprint(main)  # register main route in routes.py

    return app
