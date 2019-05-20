from src import db


class Option(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    showname = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    option_metaes = db.relationship('Option_meta', backref='option_metaes', lazy=True)
    

class Option_meta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(80), nullable=False)
    value = db.Column(db.String(100), nullable=False)
    option_id = db.Column(db.Integer, db.ForeignKey('option.id'))
