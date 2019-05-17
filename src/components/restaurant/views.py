from flask import request, jsonify
from flask_login import current_user, login_required
from src import db
from . import Restaurant_Blueprint
from src.models.restaurant import Restaurant
from src.models.image import Image
from src.access_level import requires_access_level, ACCESS
from src.upload_img import fileUpload
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
import json


@Restaurant_Blueprint.route('/create', methods=['POST'])
@login_required
@requires_access_level(ACCESS['owner'])
def create():
    message = {
        "success": False,
    }
    if request.method == 'POST':

        form_data = json.loads(request.form.get('form'))

        new_restaurant = Restaurant(
            name=form_data["name"],
            hotline=form_data["hotline"],
            address=form_data["address"],
            description=form_data["description"],
            user_id=current_user.id
        )

        db.session.add(new_restaurant)

        try:
            file = request.files['file']
            db.session.commit()
            image_id = fileUpload(file)
            new_restaurant.image_id = image_id
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()

        message['success'] = True
        message['restaurant'] = new_restaurant.id

    return jsonify(message)


@Restaurant_Blueprint.route('/')
@login_required
@requires_access_level(ACCESS['owner'])
def show():
    message = {
        "success": False,
        "restaurants" : []
    }
    restaurants = Restaurant.query.all()
    if restaurants is not None:
        for restaurant in restaurants:
            message['restaurants'].append(restaurant.__dict__)
    print (message)
    return jsonify(message)
