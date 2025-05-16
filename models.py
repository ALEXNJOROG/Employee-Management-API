from flask_sqlalchemy import SQLAlchemy
import uuid
from datetime import date

db = SQLAlchemy()

class Employee(db.Model):
    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    fullName = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    position = db.Column(db.String, nullable=False)
    salary = db.Column(db.Float, nullable=False)
    dateOfJoining = db.Column(db.Date, nullable=False)
