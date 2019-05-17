from flask import Flask, redirect, url_for
from flask_login import  current_user
from functools import wraps
from src.models.user import User


ACCESS = {
    'guest' : 0,
    'customer': 1,
    'owner': 2
}


def requires_access_level(access_level):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.email:
                return redirect(url_for('facebook.login'))

            user = User.query.filter_by(email=current_user.email).first()
            if not user.allowed(access_level):
                return ("You do not have access to that page. Sorry!")
            return f(*args, **kwargs)
        return decorated_function
    return decorator
