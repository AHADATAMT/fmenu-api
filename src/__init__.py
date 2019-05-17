from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from dotenv import load_dotenv
from flask_cors import CORS
from flask_login import LoginManager, UserMixin, logout_user, login_required, current_user, login_user
import os
from flask_dance.contrib.facebook import make_facebook_blueprint, facebook
load_dotenv()


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config.from_object(Config)
login_manager = LoginManager()
login_manager.init_app(app)
CORS(app)
db = SQLAlchemy(app)

from src.models.helpertable import dish_option, order_dish
from src.models.order import Order
from src.models.option import Option, Option_meta
from src.models.dish import Dish
from src.models.category import Category
from src.models.restaurant import Restaurant
from src.models.user import User, Token
from src.models.image import Image, QRCode

migrate = Migrate(app, db)

from src.components.account import Account
app.register_blueprint(Account, url_prefix="/profile")

from src.oauth import facebook_blueprint 
app.register_blueprint(facebook_blueprint, url_prefix="/login")
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

from src.components.controlpanel import ControlPanel 
app.register_blueprint(ControlPanel, url_prefix="/controlpanel")

from src.components.restaurant import Restaurant_Blueprint 
app.register_blueprint(Restaurant_Blueprint, url_prefix="/restaurant")

@app.route("/facebook_login")
def facebook_login():
    if not current_user.is_authenticated:
        return redirect(url_for("facebook.login"))
    return redirect("http://localhost:3000/")

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@login_manager.request_loader
def load_user_from_request(request):
    # Login Using our Custom Header
    api_key = request.headers.get('Authorization')
    if api_key:
        api_key = api_key.replace('Token ', '', 1)
        token = Token.query.filter_by(uuid=api_key).first()
        if token:
            login_user(token.user)
            return token.user
    return None


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("http://localhost:3000/")

from . import upload_img