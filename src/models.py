from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#serialize all the classes

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), index=True, unique=True)
    favorites_people = db.relationship('People', backref='fan', lazy='dynamic')
    favorites_planets = db.relationship('Planet', backref='fan', lazy='dynamic')

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), index=True, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), index=True, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
