from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class User(db.Model):
    full_name=db.Column(db.String(120),nullable=False)
    username=db.Column(db.String(120),nullable=False)
    email=db.Column(db.String(120),primary_key=True)
    password=db.Column(db.String(120),nullable=False)