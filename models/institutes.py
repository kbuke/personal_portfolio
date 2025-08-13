from db import db
from datetime import date

class InstituteModel(db.Model):
    __tablename__ = "institutes"

    id = db.Column(db.Integer, primary_key=True)
    institute_name = db.Column(db.String, nullable=False, unique=True)
    institute_img = db.Column(db.String, nullable=False)
    position = db.Column(db.String, nullable=True)
    start_date = db.Column(db.Date, nullable=True)
    end_date = db.Column(db.Date, nullable=True)

    about_id = db.Column(db.Integer, db.ForeignKey("intro.id"), unique=False, nullable=False)
    about = db.relationship("AboutModel", back_populates="institutes")

    qualifications = db.relationship("QualificationModel", back_populates="institute", lazy="dynamic")