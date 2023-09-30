#  ( . ) refers to current package (../Website/)
# flask_login is module for Logins
from . import create_database
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime
from . import db




#  ( . ) refers to current package (../Website/)
# flask_login is module for Logins
from . import create_database
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime
from . import db




class User(db.Model, UserMixin, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

     # Set up relationships
    queries = db.relationship('Query', back_populates = 'user')
    # Associations
    notes = association_proxy('queries', 'note')
    # Serialize Rules
    serialize_rules = ('-queries.user',)

def get_current_date():
    return datetime.utcnow().strftime('%Y-%m-%d')

class Note(db.Model, UserMixin, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    datesubmit = db.Column(db.String, nullable=False, default=get_current_date)
    text = db.Column(db.String(600), nullable=False)


    # Set up relationships
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    query_id = db.Column(db.Integer, db.ForeignKey('query.id'))


    queryRX = db.relationship('Query', back_populates = 'notes')
    # Associations
    users = association_proxy('queries', 'user')

    # Serialize Rules
    serialize_rules = ('-queryRX.notes',)

    



class Query(db.Model, UserMixin, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    medicationA = db.Column(db.String, nullable=False)
    medicationB = db.Column(db.String, nullable=True)

    interactionA = db.Column(db.String, nullable=False)
    interactionB = db.Column(db.String, nullable=True)

    # Foreign Keys
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # Set up relationships
    user = db.relationship("User", back_populates = 'queries')
    notes = db.relationship("Note", back_populates = 'queryRX')
    # Serialize Rules
    serialize_rules = ('-user.queries', '-note.queries')


 
























# class User(db.Model, UserMixin, SerializerMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(150), unique=True)
#     username = db.Column(db.String, nullable=False)
#     password = db.Column(db.String, nullable=False)

#      # Set up relationships
#     queries = db.relationship('Query', back_populates = 'user')
#     # Associations
#     notes = association_proxy('queries', 'note')
#     # Serialize Rules
#     serialize_rules = ('-queries.user',)

# def get_current_date():
#     return datetime.utcnow().strftime('%Y-%m-%d')


# class Note(db.Model, UserMixin, SerializerMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     datesubmit = db.Column(db.String, nullable=False, default=get_current_date())
#     text = db.Column(db.String(600), nullable=False)

#     # Foreign Keys
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     query_id = db.Column(db.Integer, db.ForeignKey('query.id'))

#     user = db.relationship("User", back_populates="note")
#     query = db.relationship("Query", back_populates="note")
#     #



#     # Set up relationships
#     queries = db.relationship('Query', back_populates = 'note')
#     # Associations
#     users = association_proxy('queries', 'user')

#     # Serialize Rules
#     serialize_rules = ('-queries.note',)

    



# class Query(db.Model, UserMixin, SerializerMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     medicationA = db.Column(db.String, nullable=False)
#     medicationB = db.Column(db.String, nullable=True)

#     interactionA = db.Column(db.String, nullable=False)
#     interactionB = db.Column(db.String, nullable=True)

#     # Foreign Keys
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


#     # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     # note_id = db.Column(db.Integer, db.ForeignKey('note.id'))
#     # Set up relationships
#     user = db.relationship("User", back_populates = 'queries')
#     note = db.relationship("Note", back_populates = 'queries')
#     # Serialize Rules
#     serialize_rules = ('-user.queries', '-note.queries')


 