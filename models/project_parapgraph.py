from db import db 

class ParagraphModel(db.Model):
    __tablename__ = "paragraphs"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable = True)
    text = db.Column(db.String, nullable = False)
    img_1 = db.Column(db.String, nullable = True, unique = False)
    img_2 = db.Column(db.String, nullable = True, unique = False)

    # set up relation with the project model; a paragraph belongs to one project, but a project can have multiple paragraphs
    project_id = db.Column(db.Integer, db.ForeignKey("projects.id"), unique = False, nullable = False)
    project = db.relationship("ProjectModel", back_populates="paragraph")