from src import db
from sqlalchemy.sql import func


class Image(db.Model):
    timestamp = db.Column(db.DateTime(timezone=True),
                          server_default=func.now())
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String, unique=True)
    restaurants = db.relationship(
        'Restaurant', backref='img', lazy=True)
    dishs = db.relationship(
        'Dish', backref='img', lazy=True)


class QRCode(db.Model):

    __tablename__ = 'qrcode'
    timestamp = db.Column(db.DateTime(timezone=True),
                          server_default=func.now())
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String, unique=True)
