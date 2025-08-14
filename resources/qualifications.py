import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from schemas import QualificationSchema

from models import QualificationModel

from db import db

from sqlalchemy.exc import SQLAlchemyError

blp = Blueprint("qualifications", __name__, description="Operations on qualifications")

@blp.route("/qualification/<string:qualification_id>")
class Qualification(MethodView):
    @blp.response(200, QualificationSchema)
    def get(self, qualification_id):
        qualification = QualificationModel.query.get_or_404(qualification_id)
        return qualification

@blp.route("/qualification")
class QualificationList(MethodView):
    @blp.response(200, QualificationSchema(many=True))
    def get(self):
        return QualificationModel.query.all()
    
    @blp.arguments(QualificationSchema)
    @blp.response(201, QualificationSchema)
    def post(self, qualification_data):
        qualification = QualificationModel(**qualification_data)

        try:
            db.session.add(qualification)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occured when inserting the qualification.")
        return qualification