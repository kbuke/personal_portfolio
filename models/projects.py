from db import db
from datetime import date 

class ProjectModel(db.Model):
    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    title_img = db.Column(db.String)
    title_video = db.Column(db.String)
    start_date = db.Column(db.Date, nullable = False)
    end_date = db.Column(db.Date, nullable = True) # add an option to say currently working on it

    # add relations which will include:
        # where you did this project (one-to-many; one project belongs to one institute, but an institute can have many projects)
        # what tech stack you used (many-to-many; a project can use multiple tech, and tech can be used in multiple projects)
        # key points you want displayed on the home page (one-to-many; a point belongs to a project, but a project can have multiple points)
        # paragraphs you want to add when user looks for more detail (one-to-many; a paragraphy belongs to a project, but a project can have multiple paragraphs)
    # one-to-many; where project is the one
    institute_id = db.Column(db.Integer, db.ForeignKey("institutes.id"), unique = False, nullable = False)
    institute = db.relationship("InstituteModel", back_populates="projects")

    # many-to-many relationship with tech
    tech = db.relationship("TechModel", back_populates = "projects", secondary = "project_tech")

    paragraph = db.relationship("ParagraphModel", back_populates="project", lazy="dynamic")