from db import db 

class AboutModel(db.Model):
    __tablename__ = "intro"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False, unique=True)
    last_name = db.Column(db.String, nullable=False, unique=True)
    picture = db.Column(db.String, nullable=False)
    introduction = db.Column(db.String, nullable=False)
    cv = db.Column(db.String, nullable=False)

    qualifications = db.relationship("QualificationModel", back_populates="about", lazy="dynamic")