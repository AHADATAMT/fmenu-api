import os
from src import db
import qrcode, pickle
import qrcode.image.svg
from config import UPLOAD_FOLDER
from src.models.image import QRCode


# def generate_qrcode(restaurant_id):
#     method = ''
#     restaurant_id = str(restaurant_id)
#     qrcode_name = restaurant_id+"_restaurant"
#     content_res_url = "http://localhost:3000/restaurant/"+restaurant_id
#     if method == 'basic':
#         # Simple factory, just a set of rects.
#         factory = qrcode.image.svg.SvgImage
#     elif method == 'fragment':
#         # Fragment factory (also just a set of rects)
#         factory = qrcode.image.svg.SvgFragmentImage
#     else:
#         # Combined path factory, fixes white space that may occur when zooming
#         factory = qrcode.image.svg.SvgPathImage
#     path = os.path.join(UPLOAD_FOLDER, qrcode_name+'.svg')
#     qrcode.make(content_res_url, image_factory=factory).save(path)
#     new_qr_code = QRCode(name=qrcode_name)
#     db.session.add(new_qr_code)
#     db.session.commit()
#     return new_qr_code.id
#     # img = qrcode.make('Some data here', image_factory=factory)
#     # img.save("qrcode.svg", UPLOAD_FOLDER)
