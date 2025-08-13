from db import db 
from datetime import date

class QualificationModel(db.Model):
    __tablename__ = "qualifications"

    id = db.Column(db.Integer, primary_key=True)
    qualification_title = db.Column(db.String, nullable=False, unique=True)
    qualifciation_img = db.Column(db.String, nullable=False, unique=True)
    qualification_date = db.Column(db.Date, nullable=False) #this will only store YY.MM.DD
