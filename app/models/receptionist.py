from app import db

class Receptionist(db.Model):
    __tablename__ = 'receptionists'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, unique=True)
    hire_date = db.Column(db.Date, nullable=False)

    def __init__(self, user_id, hire_date):
        self.user_id = user_id
        self.hire_date = hire_date

    def __repr__(self):
        return f"<Receptionist {self.id}>"
