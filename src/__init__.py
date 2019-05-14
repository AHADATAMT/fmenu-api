from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from dotenv import load_dotenv
from flask_cors import CORS
import os
load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

POSTGRES = {
    'user': os.getenv('PSQL_USER'),
    'pw': os.getenv('PSQL_PWD'),
    'db': os.getenv('PSQL_DB'),
    'host': os.getenv('PSQL_HOST'),
    'port': os.getenv('PSQL_PORT')
}

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:\
%(port)s/%(db)s' % POSTGRES
db = SQLAlchemy(app)

from src.models.user import User
from src.models.restaurant import Restaurant
from src.models.category import Category
from src.models.dish import Dish
from src.models.option import Option, Option_meta
from src.models.order import Order
from src.models.helpertable import dish_option, order_dish

migrate = Migrate(app, db)

from src.components.user import user
app.register_blueprint(user, url_prefix="/profile")
 