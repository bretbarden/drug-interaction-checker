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
    app.config["SQLALCHEMY_DATABSE_URI"] = f"sqlite:///{MEDS_REF_DATABASE}"
    db.init_app


    from .views import views
    from .auth import auth


    app.register_blueprint(views, url_prefix="/home")
    app.register_blueprint(auth, url_prefix="/")

    from .models import UserAccount, Medications, Queries

    with app.app_context():
        db.create_all()

    # create_database(app)


    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_member(id):
        return Member.query.get(int(id))

    return app

def create_database(app):
    if not path.exists("website/" + BIKE_SHARE_DB):
        db.create_all(app=app)
        print("")













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
