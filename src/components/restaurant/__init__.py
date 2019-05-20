from flask import Blueprint

Restaurant_Blueprint = Blueprint(
    'restaurant',
    __name__,
)

from . import restaurant
from . import option
from . import category
from . import dish