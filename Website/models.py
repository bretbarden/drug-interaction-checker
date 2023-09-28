#  ( . ) refers to current package (../Website/)
# flask_login is module for Logins
from . import create_database
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
from . import db

class User(db.Model, UserMixin, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

     # Set up relationships
    queries = db.relationship('Query', back_populates = 'user')
    # Associations
    medications = association_proxy('queries', 'medication')
    # Serialize Rules
    serialize_rules = ('-queries.user',)



class Medication(db.Model, UserMixin, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    brand_name = db.Column(db.String, nullable=False)
    generic_name = db.Column(db.String, nullable=False)
    known_interactions = db.Column(db.String, nullable=False)

    # Set up relationships
    queries = db.relationship('Query', back_populates = 'medication')
    # Associations
    users = association_proxy('queries', 'user')

    # Serialize Rules
    serialize_rules = ('-queries.medication',)

    



class Query(db.Model, UserMixin, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    medicationA = db.Column(db.String, nullable=False)
    medicationB = db.Column(db.String, nullable=True)

    interactionA = db.Column(db.String, nullable=False)
    interactionB = db.Column(db.String, nullable=True)

    # Foreign Keys
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    medication_id = db.Column(db.Integer, db.ForeignKey('medication.id'))
    # Set up relationships
    user = db.relationship("User", back_populates = 'queries')
    medication = db.relationship("Medication", back_populates = 'queries')
    # Serialize Rules
    serialize_rules = ('-user.queries', '-medication.queries')


 