import os
from flask import send_from_directory
from src import app
from . import QRcode_Blueprint
from src.models.image import QRCode
from config import UPLOAD_FOLDER


# @QRcode_Blueprint.route('/<id>')
# def show_qrcode(id):
#     print(id)
#     qrcode = QRCode.query.filter_by(id=1).first()
#     print(qrcode.name)
#     filename = qrcode.name+".svg"
#     # qrcode_url = os.path.join(UPLOAD_FOLDER, filename)
#     return send_from_directory(UPLOAD_FOLDER, filename)
