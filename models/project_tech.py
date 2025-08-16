from db import db 

class ProjectTech(db.Model):
    __tablename__ = "project_tech"

    id = db.Column(db.Integer, primary_key = True)

    # Set up relations between the project and the tech
    project_id = db.Column(db.Integer, db.ForeignKey("projects.id"))
    tech_id = db.Column(db.Integer, db.ForeignKey("tech.id"))