from db import db 
from models import TechModel, ProjectTech, ProjectModel
from schemas import TechSchema

from flask.views import MethodView
from flask_smorest import Blueprint, abort

from sqlalchemy.exc import SQLAlchemyError, IntegrityError

blp = Blueprint("Tech", "tech", description="Operations on tech stac")

@blp.route("/tech")
class TechStack(MethodView):
    @blp.response(200, TechSchema(many=True))
    def get(self):
        return TechModel.query.all()

    @blp.arguments(TechSchema)
    @blp.response(201, TechSchema)
    def post(self, tech_data):
        tech = TechModel(**tech_data)

        try:
            db.session.add(tech)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            abort(400, message=f"Integrity error: {str(e.orig)}")
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message=f"Database error: {str(e)}")

        return tech

@blp.route("/tech/<string:tech_id>/project/<project_id>")
class LinkTechToProject(MethodView):
    @blp.response(201, TechSchema)
    def post(self, tech_id, project_id):
        tech = TechModel.query.get_or_404(tech_id)
        project = ProjectModel.query.get_or_404(project_id)

        tech.projects.append(project)

        try:
            db.session.add(tech)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occured when inserting the tech")
        return tech 