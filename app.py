from flask import Flask
from flask_smorest import Api

from resources.about import blp as AboutBlueprint 
from resources.qualifications import blp as QualificationBlueprint
from resources.institutes import blp as InstituteBlueprint
from resources.project import blp as ProjectBlueprint
from resources.tech_stack import blp as TechBluePrint

from db import db
import os 

def create_app(db_url=None):
    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    with app.app_context():
        db.create_all()

    api = Api(app)

    api.register_blueprint(AboutBlueprint)
    api.register_blueprint(QualificationBlueprint)
    api.register_blueprint(InstituteBlueprint)
    api.register_blueprint(ProjectBlueprint)
    api.register_blueprint(TechBluePrint)

    return app
