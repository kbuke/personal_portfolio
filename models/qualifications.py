from db import db 
from datetime import date

class QualificationModel(db.Model):
    __tablename__ = "qualifications"

    id = db.Column(db.Integer, primary_key=True)
    qualification_title = db.Column(db.String, nullable=False, unique=True)
    qualifciation_img = db.Column(db.String, nullable=False, unique=True)
    qualification_date = db.Column(db.Date, nullable=False) #this will only store YY.MM.DD
    
    about_id = db.Column(db.Integer, db.ForeignKey("intro.id"), unique=False, nullable=False)
    about = db.relationship("AboutModel", back_populates="qualifications")

    institute_id = db.Column(db.Integer, db.ForeignKey("institutes.id"), unique=False, nullable=False)
    institute = db.relationship("InstituteModel", back_populates="qualifications")
