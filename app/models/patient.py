from app import db

class Patient(db.Model):
    __tablename__ = 'patients'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, unique=True)
    name = db.Column(db.String(100), nullable=False)  # Added Name
    phone = db.Column(db.String(15), nullable=False, unique=True)  # Added Phone Number
    address = db.Column(db.String(255), nullable=False)  # Added Address
    date_of_birth = db.Column(db.Date, nullable=False)
    medical_history = db.Column(db.Text, nullable=True)

    # Establish relationship with Appointment
    appointments = db.relationship('Appointment', backref='patient', lazy='dynamic')  # Changed to dynamic

    def __init__(self, user_id, name, phone, address, date_of_birth, medical_history=None):
        self.user_id = user_id
        self.name = name
        self.phone = phone
        self.address = address
        self.date_of_birth = date_of_birth
        self.medical_history = medical_history

    def __repr__(self):
        return f"<Patient {self.id} - {self.name}>"
