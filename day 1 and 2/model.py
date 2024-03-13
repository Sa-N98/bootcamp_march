from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy()

class users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable= False)
    username = db.Column(db.String)
    email =  db.Column(db.String, unique=True)
    password = db.Column(db.String)

class movies(db.Model):
     __tablename__ = "movies"
     id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable= False)
     title = db.Column(db.String)
     rating = db.Column(db.Integer)
     poster_url = db.Column(db.String)