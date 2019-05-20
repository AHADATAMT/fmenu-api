from src import db
from sqlalchemy.sql import func

class Restaurant(db.Model):
    timestamp = db.Column(db.DateTime(timezone=True), server_default=func.now())
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    hotline = db.Column(db.String(100), unique=True, nullable=False)
    address = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(),default=0)
    qrcode = db.Column(db.String(),default=0)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    image_id = db.Column(db.Integer,db.ForeignKey('image.id'))
    # categories = db.relationship('Category', backref='categories', lazy=True)
    dishs = db.relationship('Dish', backref='menu', lazy=True)
    status=db.Column(db.Integer,default=1)


