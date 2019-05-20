from src import db

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    showname = db.Column(db.String(100), unique=True, nullable=False)
    # restaurant_id = db.Column(db.Integer,db.ForeignKey('restaurant.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    status=db.Column(db.Integer,default=1)
    dishs = db.relationship('Dish', backref='category', lazy=True)
