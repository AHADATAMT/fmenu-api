from src import app
from flask import render_template, redirect, url_for


# @app.route('/')
# def index():
#     return (redirect(url_for("facebook.login")))


if __name__ == '__main__':
    app.run(dedug=True)
