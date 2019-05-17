from src import db
from sqlalchemy.sql import func


class Image(db.Model):
    timestamp = db.Column(db.DateTime(timezone=True),
                          server_default=func.now())
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    restaurants = db.relationship(
        'Restaurant', backref='restaurant_photo', lazy=True)


class QRCode(db.Model):

    __tablename__ = 'qrcode'
    timestamp = db.Column(db.DateTime(timezone=True),
                          server_default=func.now())
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    restaurants = db.relationship(
        'Restaurant', backref='restaurant_qrcode', lazy=True)
