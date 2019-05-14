from src import db

class Option(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    showname = db.Column(db.String(100), unique=True, nullable=False)
    # restaurant_id = db.Column(db.String(), nullable=False)


class Option_meta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(80), unique=True, nullable=False)
    value = db.Column(db.String(100), unique=True, nullable=False)
    # option_id = db.Column(db.String(), nullable=False)