import os

from dotenv import load_dotenv
load_dotenv()

POSTGRES = {
    'user': os.getenv('PSQL_USER'),
    'pw': os.getenv('PSQL_PWD'),
    'db': os.getenv('PSQL_DB'),
    'host': os.getenv('PSQL_HOST'),
    'port': os.getenv('PSQL_PORT')
}


UPLOAD_FOLDER = os.path.basename('uploads')
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess-10794'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FACEBOOK_OAUTH_CLIENT_ID = os.environ.get('FACEBOOK_OAUTH_CLIENT_ID')
    FACEBOOK_OAUTH_CLIENT_SECRET = os.environ.get('FACEBOOK_OAUTH_CLIENT_SECRET')
    UPLOAD_FOLDER = UPLOAD_FOLDER