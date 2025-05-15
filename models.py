from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4
from datetime import datetime

db = SQLAlchemy()

def generate_uuid():
    return str(uuid4())

class Employee(db.Model):
    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    fullName = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    position = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.Float, nullable=False)
    dateOfJoining = db.Column(db.Date, nullable=False)
