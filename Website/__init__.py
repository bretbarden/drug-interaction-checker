from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


# create database
db = SQLAlchemy()
MEDS_REF_DATABASE = "database.db"


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "catdogcatdog"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{MEDS_REF_DATABASE}"
    db.init_app(app)


    from .views import views
    from .auth import auth


    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User, Medication, Query

    with app.app_context():
        db.create_all()

   

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_member(id):
        return User.query.get(int(id))
    
    return app

def create_database(app):
    if not path.exists("Website/" + MEDS_REF_DATABASE):
        db.create_all(app=app)
        print("Databse created")













#     with app.app_context():
#         db.create_all


# from models import UserAccount, Medications,  Queries

# # configure login stuff fromLLoginManager
# login_manager = LoginManager()
# login_manager.login_view = "auth.login"
# login_manager.init_app(app)

# @login_manager.user_loader
# def load_member(id): 
#     return .query.get(int(id))
    
# return app

# def create_database(app):
#     if not path exists("Website/" + MEDS_REF_DATABASE):
#         db.create_all(app=app)
#     print("MEDS REF DATABASE CREATED")
