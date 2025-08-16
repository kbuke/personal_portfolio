from db import db 

class TechModel(db.Model):
    __tablename__ = "tech"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    image = db.Column(db.String, nullable=False, unique=True)

    # set up a many-to-many relationship with projects
    projects = db.relationship("ProjectModel", back_populates = "tech", secondary = "project_tech")