from app import db

class Appointment(db.Model):
    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), nullable=False, default='pending')

    def __init__(self, patient_id, doctor_id, date, status='pending'):
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date = date
        self.status = status

    def __repr__(self):
        return f"<Appointment {self.id} - {self.status}>"
