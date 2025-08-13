from marshmallow import Schema, fields

class AboutSchema(Schema):
    id = fields.Int(dump_only=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    picture = fields.Str(required=True)
    introduction = fields.Str(required=True)
    cv = fields.Str(required=True)

class PlainQualificationSchema(Schema):
    id = fields.Int(dump_only=True)
    qualification_title = fields.Str(required=True)
    qualifciation_img = fields.Str(required=True)
    qualification_date = fields.Str(required=True) 

class QualificationSchema(PlainQualificationSchema):
    about_id = fields.Int(required=True, load_only=True)
    about = fields.Nested(AboutSchema(), dump_only=True)