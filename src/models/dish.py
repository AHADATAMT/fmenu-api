from src import db
from sqlalchemy.sql import func
from src.models.helpertable import dish_option

class Dish(db.Model):
    timestamp = db.Column(db.DateTime(timezone=True),
                          server_default=func.now())
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    showname = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(300))
    price = db.Column(db.Integer)
    status=db.Column(db.Integer,default=1)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    image_id = db.Column(db.Integer,db.ForeignKey('image.id'))
    selection = db.relationship("Option",
                    secondary=dish_option,
                    lazy='subquery',
                    backref=db.backref('options',lazy=True) )