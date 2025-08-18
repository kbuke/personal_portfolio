from marshmallow import Schema, fields, validates_schema, ValidationError

class AboutSchema(Schema):
    id = fields.Int(dump_only=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    picture = fields.Str(required=True)
    introduction = fields.Str(required=True)
    cv = fields.Str(required=True)

class AboutUpdateSchema(Schema):
    first_name = fields.Str()
    last_name = fields.Str()
    picture = fields.Str()
    introduction = fields.Str()
    cv = fields.Str()

#---------------------------------- Plain Schemas ----------------------------------
class PlainQualificationSchema(Schema):
    id = fields.Int(dump_only=True)
    qualification_title = fields.Str(required=True)
    qualifciation_img = fields.Str(required=True)
    qualification_date = fields.Date(required=True, format="%Y-%m-%d")

class PlainInstituteSchema(Schema):
    id = fields.Int(dump_only=True)
    institute_name = fields.Str(required=True)
    institute_img = fields.Str(required=True)
    position = fields.Str(required=True)
    start_date = fields.Date(required=True, format="%Y-%m-%d")
    end_date = fields.Date(required=True, format="%Y-%m-%d")

    @validates_schema
    def validate_dates(self, data, **kwargs):
        start = data.get("start_date")
        end = data.get("end_date")
        
        if start and end and end <= start:
            raise ValidationError("End date must be after the start date", field_name="end_date")
        
class PlainProjectSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    title_img = fields.Str()
    title_video = fields.Str()
    start_date = fields.Date(required = True, format="%Y-%m-%d")
    end_date = fields.Date(allow_none=True, format="%Y-%m-%d")

    @validates_schema
    def validate_end_date(self, data, **kwargs):
        start = data.get("start_date")
        end = data.get("end_date")

        if end is not None and start and end <= start:
            raise ValidationError("End date must come after start date", field_name="end_date")

class PlainTechSchema(Schema):
    id = fields.Int(dump_only = True)
    name = fields.Str(required=True)
    image = fields.Str(required=True)

class PlainParagraphSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(allow_none=True)
    text = fields.Str(required=True)
    img_1 = fields.Str(allow_none=True)
    img_2 = fields.Str(allow_none=True)

class PlainProjectPointSchema(Schema):
    id = fields.Int(dump_only=True)
    point = fields.Str(required=True)

#---------------------------------- Specific Schemas ----------------------------------
class InstitutesSchema(PlainInstituteSchema):
    about_id = fields.Int(required=True, load_only=True)
    about = fields.Nested(AboutSchema(), dump_only=True)

class InstituteUpdateSchema(Schema):
    id = fields.Int()
    institute_name = fields.Str()
    institute_img = fields.Str()
    position = fields.Str()
    start_date = fields.Date()
    end_date = fields.Date()
    about_id = fields.Int()

class QualificationSchema(PlainQualificationSchema):
    about_id = fields.Int(required=True, load_only=True)
    about = fields.Nested(AboutSchema(), dump_only=True)

    institute_id = fields.Int(required=True, load_only=True)
    institute = fields.Nested(InstitutesSchema(), dump_only=True)

class QualificationUpdateSchema(Schema):
    qualification_title = fields.Str()
    qualifciation_img = fields.Str()
    qualification_date = fields.Date()
    about_id = fields.Int()
    institute_id = fields.Int()

class ProjectSchema(PlainProjectSchema):
    institute_id = fields.Int(required=True, load_only=True)
    institute = fields.Nested(InstitutesSchema(), dump_only=True)
    tech = fields.List(fields.Nested(PlainTechSchema()), dump_only=True)
    paragraph = fields.List(fields.Nested(PlainParagraphSchema()), dump_only = True)
    points = fields.List(fields.Nested(PlainProjectPointSchema()), dump_only = True)

class TechSchema(PlainTechSchema):
    projects = fields.List(fields.Nested(PlainProjectSchema()), dump_only = True)

class ParagraphSchema(PlainParagraphSchema):
    project_id = fields.Int(required=True, load_only=True)
    # project = fields.Nested(ProjectSchema(), dump_only=True)

class ParagraphUpdateSchema(Schema):
    title = fields.Str()
    text = fields.Str()
    img_1 = fields.Str()
    img_2 = fields.Str()
    project_id = fields.Int()

class ProjectPointSchema(PlainProjectPointSchema):
    project_id = fields.Int(required=True, load_only=True)

class ProjectPointUpdateSchema(Schema):
    point = fields.Str()
    project_id = fields.Int()