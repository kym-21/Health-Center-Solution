from flask_sqlalchemy import SQLAlchemy
from app import db

db = SQLAlchemy

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primaryKey=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password =db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), nullable=False)

    def __init__(self, name, email, password, role):
        self.name = name
        self.email= email
        self.password= password
        self.role = role

    def __repr__(self):
        return f"<User.{self.name} - {self.role}>"
