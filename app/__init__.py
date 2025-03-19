from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
import pymysql

pymysql.install_as_MySQLdb()


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)  # Initialize database with app

    with app.app_context():
        from app.models import user  # Import models
        db.create_all()  # Create tables if they don’t exist

    return app
