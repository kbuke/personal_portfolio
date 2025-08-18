from db import db 

class PointsModel(db.Model):
    __tablename__ = "points"

    id = db.Column(db.Integer, primary_key = True)
    point = db.Column(db.String, nullable = False, unique = True)

    # set up relation with projects 
    project_id = db.Column(db.Integer, db.ForeignKey("projects.id"))
    project = db.relationship("ProjectModel", back_populates="points")
