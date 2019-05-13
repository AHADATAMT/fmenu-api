from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from dotenv import load_dotenv
import os
load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config.from_object(Config)

POSTGRES = {
    'user': os.getenv('PSQL_USER'),
    'pw': os.getenv('PSQL_PWD'),
    'db': os.getenv('PSQL_DB'),
    'host': os.getenv('PSQL_HOST'),
    'port': os.getenv('PSQL_PORT')
}

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, "database.db")
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:\
%(port)s/%(db)s' % POSTGRES
db = SQLAlchemy(app)

from src.models.user import User

migrate = Migrate(app, db)
# from src.components.events.views import events_blueprint
# app.register_blueprint(events_blueprint, url_prefix="/events")

# from src.components.home.views import events_blueprint
# app.register_blueprint(events_blueprint, url_prefix="/")

from src.components.user import user
app.register_blueprint(user, url_prefix="/profile")
 