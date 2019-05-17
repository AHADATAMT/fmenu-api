from flask import Blueprint

ControlPanel = Blueprint(
    'controlpanel',
    __name__,
    template_folder='templates',
    static_folder='static'
)

from . import views