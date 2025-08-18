from flask import request 
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from schemas import ParagraphSchema, ParagraphUpdateSchema

from models import ParagraphModel

from db import db

from sqlalchemy.exc import SQLAlchemyError

blp = Blueprint("paragraphs", __name__, description = "Operations on project paragraphs")

@blp.route("/paragraphs/<string:paragraph_id>")
class Paragraph(MethodView):
    def delete(self, paragraph_id):
        paragraph = ParagraphModel.query.get_or_404(paragraph_id)
        db.session.delete(paragraph)
        db.session.commit()
        return {"message": "Paragraph deleted"}
    
    @blp.arguments(ParagraphUpdateSchema)
    @blp.response(200, ParagraphSchema)
    def put(self, paragraph_data, paragraph_id):
        paragraph = ParagraphModel.query.get_or_404(paragraph_id)
        if paragraph:
            paragraph.title = paragraph_data["title"]
            paragraph.text = paragraph_data["text"]
            paragraph.img_1 = paragraph_data["img_1"]
            paragraph.img_2 = paragraph_data["img_2"]
            paragraph.project_id = paragraph_data["project_id"]
        else:
            paragraph = ParagraphModel(id=paragraph_id, **paragraph_data)
        db.session.add(paragraph)
        db.session.commit()
        return paragraph

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