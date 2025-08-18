from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from schemas import ProjectPointSchema, ProjectPointUpdateSchema

from models import PointsModel

from db import db 

from sqlalchemy.exc import SQLAlchemyError

blp = Blueprint("points", __name__, description = "Operations on project points")

@blp.route("/points/<string:point_id>")
class Point(MethodView):
    def delete(self, point_id):
        point = PointsModel.query.get_or_404(point_id)
        db.session.delete(point)
        db.session.commit()
        return {"message": "Point deleted"}

    @blp.arguments(ProjectPointUpdateSchema)
    @blp.response(200, ProjectPointSchema)
    def put(self, point_data, point_id):
        point = PointsModel.query.get(point_id)
        if point:
            point.point = point_data["point"]
            point.project_id = point_data["project_id"]
        else:
            point = PointsModel(id=point_id, **point_data)
        db.session.add(point)
        db.session.commit()
        return point


@blp.route("/points")
class PointsList(MethodView):
    @blp.response(200, ProjectPointSchema(many=True))
    def get(self):
        return PointsModel.query.all()

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