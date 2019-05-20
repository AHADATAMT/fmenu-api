from flask import render_template
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.sql import func
from src import db
import requests
from flask_dance.consumer.storage.sqla import OAuthConsumerMixin

ACCESS = {
    'guest' : 0,
    'customer': 1,
    'owner': 2
}

class User(UserMixin, db.Model):
    timestamp = db.Column(db.DateTime(timezone=True),
                          server_default=func.now())
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80))
    fb_username = db.Column(db.String(80))
    gg_username = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String())
    access = db.Column(db.Integer, default=0)
    orders = db.relationship('Order', backref='orders', lazy=True)
    restaurants = db.relationship(
        'Restaurant', backref='owner', lazy=True)
    categories = db.relationship(
        'Category', backref='admin', lazy=True)
    

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def send_password_reset_email(self, token):
        
        apikey = "get-this-from-mailgun"
        domain_name = "get-this-from-mailgun"
        print(render_template('email.html', token=token))
        requests.post(
            "https://api.mailgun.net/v3/" + domain_name + "/messages",
            auth=("api", apikey),
            data={"from": "ticketbox.mt@" + domain_name,
                  "to": [self.email],
                  "subject": "Reset password",
                  "html": render_template('email.html', token=token)})

    def is_owner(self):
        return self.access == ACCESS['owner']

    def allowed(self, access_level):
        return self.access >= access_level

class OAuth(OAuthConsumerMixin, db.Model):
    provider_user_id = db.Column(db.String(256), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    user = db.relationship(User)


class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    user = db.relationship(User)

