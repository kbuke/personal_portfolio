import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort 

from schemas import AboutSchema
from models import AboutModel

from db import db

from sqlalchemy.exc import SQLAlchemyError, IntegrityError

blp = Blueprint("intro", __name__, description="Operations on my information.")

@blp.route("/about/<string:about_id>")
class About(MethodView):
    @blp.response(200, AboutSchema)
    def get(self, about_id):
        about = AboutModel.query.get_or_404(about_id)
        return about 

@blp.route("/about")
class AboutList(MethodView):
    @blp.response(200, AboutSchema(many=True))
    def get(self):
        return AboutModel.query.all()
    
    @blp.arguments(AboutSchema)
    @blp.response(201, AboutSchema)
    def post(self, about_data):
        about = AboutModel(**about_data)

        try:
            db.session.add(about)
            db.session.commit()
        except IntegrityError:
            abort(400, message="A user with that name already exists")
        except SQLAlchemyError:
            abort(500, message="An error occured when inserting the user")
        return about 