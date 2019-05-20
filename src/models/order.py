from src import db
from sqlalchemy.sql import func


class Order(db.Model):
    timestamp = db.Column(db.DateTime(timezone=True),
                          server_default=func.now())
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    status = db.Column(db.Integer, default=0) # payment or not yet


class Order_detail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dish_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    quota = db.Column(db.Integer)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
