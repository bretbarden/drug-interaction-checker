#  ( . ) refers to current package (../Website/)
# flask_login is module for Logins
from . import create_database
from flask_login import UserMixin
from sqlalchemy.sql import func
from . import db

class UserAccount(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)



class Medications(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    brand_name = db.Column(db.String, nullable=False)
    generic_name = db.Column(db.String, nullable=False)
    known_interactions = db.Column(db.String, nullable=False)
    



class Queries(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    medicationA = db.Column(db.String, nullable=False)
    medicationB = db.Column(db.String, nullable=True)


 