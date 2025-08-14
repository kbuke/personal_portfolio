import uuid 
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from schemas import InstitutesSchema, InstituteUpdateSchema

from models import InstituteModel

from db import db

from sqlalchemy.exc import SQLAlchemyError

blp = Blueprint("institutes", __name__, description="Operations on institutes")

@blp.route("/institute/<string:institute_id>")
class Institute(MethodView):
    @blp.response(200, InstitutesSchema)
    def get(self, institute_id):
        institute = InstituteModel.query.get_or_404(institute_id)
        return institute
    
    @blp.arguments(InstituteUpdateSchema)
    @blp.response(200, InstitutesSchema)
    def put(self, institute_data, institute_id):
        institute = InstituteModel.query.get(institute_id)
        if institute:
            institute.institute_name = institute_data["institute_name"]
            institute.institute_img = institute_data["institute_img"]
            institute.position = institute_data["position"]
            institute.start_date = institute_data["start_date"]
            institute.end_date = institute_data["end_date"]
            institute.about_id = institute_data["about_id"]
        else:
            institute = InstituteModel(id=institute_id, **institute_data)
        db.session.add(institute)
        db.session.commit()
        return institute


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