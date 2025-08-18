from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from schemas import ProjectPointSchema

from models import PointsModel

from db import db 

from sqlalchemy.exc import SQLAlchemyError

blp = Blueprint("points", __name__, description = "Operations on project points")

@blp.route("/points")
class PointsList(MethodView):
    @blp.arguments(ProjectPointSchema)
    @blp.response(201, ProjectPointSchema)
    def post(self, point_data):
        point = PointsModel(**point_data)

        try:
            db.session.add(point)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occured when adding a new project point")
        return point