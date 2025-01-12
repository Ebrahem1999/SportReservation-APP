from sqlalchemy import String
from svc.db import db


class User(db.Model):
    __tablename__ = 'users'

    uid = db.Column(db.UUID(as_uuid=True), unique=True, nullable=False, primary_key=True)
    username = db.Column(String(50), unique=True)
    password = db.Column(String(250))
    phonenum = db.Column(String(12), unique=True)
    user_type = db.Column(String(20), nullable=True)
    preference = db.Column(String, nullable=True)
    

    payments = db.relationship('Payments', back_populates='user')
    favorites = db.relationship('Favorites', back_populates='user')
    ratings = db.relationship('Ratings', back_populates='user')
    fields_managed = db.relationship('Field', back_populates='manager')
    

