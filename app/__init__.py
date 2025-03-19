from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import pymysql
from app.config import Config

pymysql.install_as_MySQLdb()

# Initialize database globally
db = SQLAlchemy()
migrate = Migrate()  # Migrate should be initialized globally

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Rickc-137@localhost/healthcare_system'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)  # Initialize database with app
    migrate.init_app(app, db)  # Enable Flask-Migrate

    with app.app_context():
        # Import models to register them with SQLAlchemy
        from app.models import user, doctor, patient, appointment, prescription, receptionist

    return app
