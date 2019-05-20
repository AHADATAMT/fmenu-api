from flask import request, jsonify
from flask_login import current_user, login_required
from src import db
from . import Restaurant_Blueprint
from src.models.image import Image
from src.models.dish import Dish
from src.models.option import Option
from src.access_level import requires_access_level, ACCESS
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
import json


@Restaurant_Blueprint.route('/create_dish', methods=['POST'])
@requires_access_level(ACCESS['owner'])
@login_required
def createDish():
    message = {
        "success": False,
    }
    if request.method == 'POST':

        form_data = json.loads(request.form.get('form'))
        # update or create new
        print(form_data["optionsSeleted"])
        new_dish = Dish(
            name=form_data["name"],
            showname=form_data["showname"],
            description=form_data["description"],
            price=form_data["price"],
            category_id=form_data["category"],
            restaurant_id=form_data["restaurant_id"]
        )
        # add category id and restaurant id
        db.session.add(new_dish)
        for option_id in form_data["optionsSeleted"]:
            optionObj = Option.query.filter_by(id=option_id).first()
            new_dish.selection.append(optionObj)
        try:

            db.session.commit()
            img = Image(url=form_data["img_logo_url"])
            db.session.add(img)
            db.session.commit()
            new_dish.image_id = img.id
            db.session.commit()

            db.session.commit()

        except SQLAlchemyError as e:
            db.session.rollback()

        message['success'] = True
        message['restaurant'] = new_dish.id

    return jsonify(message)


@Restaurant_Blueprint.route('delete_dish/<dish_id>', methods=['POST'])
@requires_access_level(ACCESS['owner'])
@login_required
def deleteDish(dish_id):
    message = {
        "success": False,
    }
    target = Dish.query.filter_by(id=dish_id).first()
    if target.selection is not None:
        target.selection.clear()
    db.session.delete(target)
    db.session.commit()
    print(Dish.query.all())
    message['success'] = True

    return jsonify(message)
