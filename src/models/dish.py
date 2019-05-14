from src import db
from sqlalchemy.sql import func


class Dish(db.Model):
    timestamp = db.Column(db.DateTime(timezone=True),
                          server_default=func.now())
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    showname = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    price = db.Column(db.Integer)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
