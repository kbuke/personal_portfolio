import uuid 
from flask import request 
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from schemas import ProjectSchema

from models import ProjectModel

from db import db 

from sqlalchemy.exc import SQLAlchemyError

blp = Blueprint("projects", __name__, description = "Operations on projects")

@blp.route("/project")
class ProjectList(MethodView):
    @blp.response(200, ProjectSchema(many=True))
    def get(self):
        return ProjectModel.query.all()

    @blp.arguments(ProjectSchema)
    @blp.response(200, ProjectSchema)
    def post(self, project_data):
        project = ProjectModel(**project_data)

        try:
            db.session.add(project)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occured when inserting the project.")
        return project