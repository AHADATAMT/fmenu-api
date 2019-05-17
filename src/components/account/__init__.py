from flask import Blueprint

Account = Blueprint(
    'account',
    __name__,
    template_folder='templates',
    static_folder='static'
)

from . import views