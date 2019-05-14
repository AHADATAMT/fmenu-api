from src import db

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    showname = db.Column(db.String(100), unique=True, nullable=False)
    dishs = db.relationship('Dish', backref='dishs', lazy=True)