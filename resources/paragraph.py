from flask import request 
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from schemas import ParagraphSchema

from models import ParagraphModel

from db import db

from sqlalchemy.exc import SQLAlchemyError

blp = Blueprint("paragraphs", __name__, description = "Operations on project paragraphs")

@blp.route("/paragraphs")
class ParagraphList(MethodView):
    @blp.response(200, ParagraphSchema(many=True))
    def get(self):
        return ParagraphModel.query.all()

    @blp.arguments(ParagraphSchema)
    @blp.response(201, ParagraphSchema)
    def post(self, paragraph_data):
        paragraph = ParagraphModel(**paragraph_data)

        try: 
            db.session.add(paragraph)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occured when adding a new paragrapgh")
        return paragraph