import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key_here'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Rickc-137@localhost/healthcare_system'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
