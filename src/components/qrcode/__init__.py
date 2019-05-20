from flask import Blueprint

QRcode_Blueprint = Blueprint(
    'qrcode',
    __name__,
)

from . import views
