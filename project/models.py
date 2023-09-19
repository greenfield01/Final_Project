from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    firstname = db.Column(db.String(1000))
    lastname = db.Column(db.String(1000))
    age = db.Column(db.String(100))
    picture = db.Column(db.String(1000))


class Ailment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ailment_name = db.Column(db.String(100))
    symptoms = db.Column(db.String(500))
    causes = db.Column(db.String(500))
    effects = db.Column(db.String(500))
    natural_treatments = db.Column(db.String(500))
    drugs = db.Column(db.String(500))
    diets = db.Column(db.String(500))
    exercise = db.Column(db.String(500))


