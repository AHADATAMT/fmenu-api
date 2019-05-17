import os
from flask import Flask, render_template, request
from . import app, db
from werkzeug.utils import secure_filename
from config import UPLOAD_FOLDER, ALLOWED_EXTENSIONS
from src.models.image import Image
from datetime import datetime


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def fileUpload(imgFile):
    dt = datetime.now()
    dt.microsecond
    target = os.path.join(UPLOAD_FOLDER)
    if not os.path.isdir(target):
        os.mkdir(target)
    file = imgFile
    filename = secure_filename(str(dt.microsecond) + "_" + file.filename)
    destination = "/".join([target, filename])
    file.save(destination)
    img = Image(name=filename)
    db.session.add(img)
    db.session.commit()
    return img.id
