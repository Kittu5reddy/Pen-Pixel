from flask import Flask
from app.views import main
from app.models import db,csrf
from flask_migrate import Migrate
from app.views import bcrypt,login_manager


def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']='your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///project.db"
    login_manager.init_app(app)
    bcrypt.init_app(app)
    db.init_app(app)
    migrate=Migrate(app,db)
    app.register_blueprint(main)
    csrf.init_app(app)
    return app

