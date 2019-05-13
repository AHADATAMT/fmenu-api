from src import db
from flask import render_template
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import requests


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(), nullable=False)
    role = db.Column(db.Integer,default=0)
    # ticket = db.relationship('Ticket', backref='ticket', lazy=True)
    # order = db.relationship('Orders', backref='order', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # def send_password_reset_email(self, token):
    #     apikey = "b3f12503ed1b521baa50e37e523fcacb-7bce17e5-1288a4cc"
    #     domain_name = "sandboxd56ad08b71e043f0acf78d2d27412282.mailgun.org"
    #     # apikey = "get-this-from-mailgun"
    #     # domain_name = "get-this-from-mailgun"
    #     print(render_template('email.html', token=token))
    #     requests.post(
    #         "https://api.mailgun.net/v3/" + domain_name + "/messages",
    #         auth=("api", apikey),
    #         data={"from": "ticketbox.mt@" + domain_name,
    #               "to": [self.email],
    #               "subject": "Reset password",
    #               "html": render_template('email.html', token=token)})
