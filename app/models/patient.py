from app import db

class Patient(db.Model):
    __tablename__ = 'patients'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, unique=True)
    date_of_birth = db.Column(db.Date, nullable=False)
    medical_history = db.Column(db.Text, nullable=True)

    # Establish relationship with Appointment
    appointments = db.relationship('Appointment', backref='patient', lazy=True)

    def __init__(self, user_id, date_of_birth, medical_history=None):
        self.user_id = user_id
        self.date_of_birth = date_of_birth
        self.medical_history = medical_history

    def __repr__(self):
        return f"<Patient {self.id}>"
