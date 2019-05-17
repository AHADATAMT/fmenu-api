from flask import Blueprint

Restaurant_Blueprint = Blueprint(
    'restaurant',
    __name__,
)

from . import views