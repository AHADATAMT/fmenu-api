from flask import request, jsonify
from flask_login import current_user, login_required
from src import db
from . import Restaurant_Blueprint
from src.models.restaurant import Restaurant
from src.models.category import Category
from src.models.image import Image
from src.access_level import requires_access_level, ACCESS
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
        # update or create new
        print(form_data)
        new_restaurant = Restaurant(
            name=form_data["name"],
            hotline=form_data["hotline"],
            address=form_data["address"],
            description=form_data["description"],
            user_id=current_user.id
        )

        db.session.add(new_restaurant)

        try:

            db.session.commit()
            img = Image(url=form_data["img_logo_url"])
            db.session.add(img)
            db.session.commit()
            new_restaurant.image_id = img.id
            db.session.commit()

        except SQLAlchemyError as e:
            db.session.rollback()

        message['success'] = True
        message['restaurant'] = new_restaurant.id

    return jsonify(message)


@Restaurant_Blueprint.route('/')
@login_required
@requires_access_level(ACCESS['owner'])
def get_all_restaurants_by_user():
    message = {
        "success": False,
        "restaurants": []
    }
    restaurants = Restaurant.query.filter_by(user_id=current_user.id)
    if restaurants is not None:
        for restaurant in restaurants:
            res = {
                "id": restaurant.id,
                "name": restaurant.name,
                "hotline": restaurant.hotline,
                "address": restaurant.address,
                "description": restaurant.description,
                "image_id": restaurant.image_id
            }
            message["restaurants"].append(res)
            message["success"] = True

    return jsonify(message)


@Restaurant_Blueprint.route('/<restaurant_id>')
def get_restaurant_by_user(restaurant_id):
    message = {
        "success": False,
        "restaurant": [],
        "menu": [],
    }
    restaurant = Restaurant.query.filter_by(id=restaurant_id).first()
    if restaurant is not None:
        res = {
            "id": restaurant.id,
            "name": restaurant.name,
            "hotline": restaurant.hotline,
            "address": restaurant.address,
            "description": restaurant.description,
            "image_url": restaurant.img.url
        }
        
        for dish in restaurant.dishs:
            dish_obj = {
                "id": dish.id,
                "name": dish.name,
                "showname": dish.showname,
                "description": dish.description,
                "price": dish.price,
                "img_url": dish.img.url,
                "selection": [],
                "category": dish.category.showname,
            }

            for option_group in dish.selection:
                opt_meta = [(option_meta.key,option_meta.value) for option_meta in option_group.option_metaes]
                opt = {
                    "option_group_name":option_group.showname,
                    "opt_meta": opt_meta
                }
                dish_obj['selection'].append(opt)
            message["menu"].append(dish_obj)

        message["restaurant"].append(res)
        message["success"] = True

    return jsonify(message)


@Restaurant_Blueprint.route('/update/<id>', methods=['POST'])
@login_required
@requires_access_level(ACCESS['owner'])
def update(id):
    message = {
        "success": False,
    }
    if request.method == 'POST':

        form_data = json.loads(request.form.get('form'))
        # update or create new
        restaurant = Restaurant.query.filter_by(id=id).first()
        restaurant.name = form_data["name"]
        restaurant.hotline = form_data["hotline"]
        restaurant.address = form_data["address"]
        restaurant.description = form_data["description"]

        img = Image(name=form_data["img_logo_url"])
        db.session.add(img)
        db.session.commit()
        restaurant.image_id = img.id
        db.session.commit()
        message["success"] = True

    return


@Restaurant_Blueprint.route('delete/<restaurant_id>', methods=['POST'])
@requires_access_level(ACCESS['owner'])
@login_required
def deleteRestaurant(restaurant_id):
    message = {
        "success": False,
    }
    target = Restaurant.query.filter_by(id=restaurant_id).first()
    db.session.delete(target)
    db.session.commit()
    message['success'] = True

    return jsonify(message)
