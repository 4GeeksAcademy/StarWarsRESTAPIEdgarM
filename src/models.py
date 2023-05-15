from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    favorites_people = db.relationship('People', backref='fan', lazy='dynamic')
    favorites_planets = db.relationship('Planet', backref='fan', lazy='dynamic')

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
