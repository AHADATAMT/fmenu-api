import os
from flask import Flask, render_template, request
from . import app, db
from werkzeug.utils import secure_filename
from config import UPLOAD_FOLDER, ALLOWED_EXTENSIONS
from src.models.image import Image
from datetime import datetime
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# def fileUpload(imgFile):
#     dt = datetime.now()
#     dt.microsecond
#     target = os.path.join(UPLOAD_FOLDER)
#     if not os.path.isdir(target):
#         os.mkdir(target)
#     file = imgFile
#     filename = secure_filename(str(dt.microsecond) + "_" + file.filename)
#     destination = "/".join([target, filename])
#     file.save(destination)
#     img = Image(name=filename)
#     db.session.add(img)
#     db.session.commit()
#     return img.id


# TODO: HANDLE IMAGE STORAGE
# @app.route("/uploadimg_cloudinary", method=['POST'])
# def uploadImg_Cloudinary():
#     upload_result = None
#     thumbnail_url1 = None
#     thumbnail_url2 = None
#     if request.method == 'POST':
#         file_to_upload = request.files['file']
#         if file_to_upload:
#             upload_result = upload(file_to_upload)
#             thumbnail_url1, options = cloudinary_url(upload_result['public_id'], format="jpg", crop="fill", width=100,
#                                                      height=100)
#             thumbnail_url2, options = cloudinary_url(upload_result['public_id'], format="jpg", crop="fill", width=200,
#                                                      height=100, radius=20, effect="sepia")
#     return render_template('upload_form.html', upload_result=upload_result, thumbnail_url1=thumbnail_url1,
#                            thumbnail_url2=thumbnail_url2)
