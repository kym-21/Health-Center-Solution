from app import db

class Prescription(db.Model):
    __tablename__ = 'prescriptions'

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'), nullable=False)
    medication = db.Column(db.String(255), nullable=False)
    dosage = db.Column(db.String(100), nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    date_issued = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __init__(self, patient_id, doctor_id, medication, dosage, instructions):
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.medication = medication
        self.dosage = dosage
        self.instructions = instructions

    def __repr__(self):
        return f"<Prescription {self.id} - {self.medication}>"
