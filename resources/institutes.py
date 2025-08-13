import uuid 
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from schemas import InstitutesSchema

from models import InstituteModel

from db import db

from sqlalchemy.exc import SQLAlchemyError

blp = Blueprint("institutes", __name__, description="Operations on institutes")

@blp.route("/institute")
class InstitutionList(MethodView):
    @blp.response(200, InstitutesSchema(many=True))
    def get(self):
        return InstituteModel.query.all()

    @blp.arguments(InstitutesSchema)
    @blp.response(201, InstitutesSchema)
    def post(self, institute_data):
        institute = InstituteModel(**institute_data)

        try:
            db.session.add(institute)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occured when inserting the institution.")
        return institute