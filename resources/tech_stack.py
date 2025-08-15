from db import db 
from models import TechModel, ProjectTech, ProjectModel
from schemas import TechSchema

from flask.views import MethodView
from flask_smorest import Blueprint, abort

from sqlalchemy.exc import SQLAlchemyError

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
        except SQLAlchemyError:
            abort(500, message="An error occured when inserting this tech")
        return tech 