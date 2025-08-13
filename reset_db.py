from db import db
from app import create_app  # import the factory function

app = create_app()  # create the Flask app instance

with app.app_context():
    # ⚠️ This drops ALL tables — you’ll lose all data
    db.drop_all()
    db.create_all()
    print("Database reset complete.")
