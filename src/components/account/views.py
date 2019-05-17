from flask import request, jsonify
from flask_login import current_user, login_user
from src import db
from src.models.user import User
from . import Account
import json


@Account.route('/signup', methods=['POST'])
def signup():

    if request.method == 'POST':
        data = request.get_json()
        new_user = User(
            firstname=data["firstname"],
            lastname=data["lastname"],
            email=data["email"]
        )
        new_user.set_password(data["password"])
        print(new_user)
        db.session.add(new_user)
        db.session.commit()
    return jsonify({
        "msg": True,
        "user": new_user.id
    })


@Account.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        user_email = data['email']
        user_password = data['password']
        user = User.query.filter_by(email=user_email).first()
        if(user is not None and user.check_password(user_password)):
            print(user.firstname)
            login_user(user)

    return jsonify({
        "msg": True,
        "username": user.firstname
    })
