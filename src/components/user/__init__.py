from flask import Blueprint
from src import db

user = Blueprint(
    'user',
    __name__,
    template_folder='templates',
    static_folder='static'
)

from . import views