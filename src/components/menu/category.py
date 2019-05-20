from flask import request, jsonify
from flask_login import current_user, login_required
from src import db
from . import Restaurant_Blueprint
from src.models.category import Category
from src.access_level import requires_access_level, ACCESS
import json


@Restaurant_Blueprint.route('/create_category', methods=['POST'])
@requires_access_level(ACCESS['owner'])
@login_required
def createCategory():
    message = {
        "success": False,
    }
    if request.method == 'POST':

        form_data = json.loads(request.form.get('form'))
        # update or create new

        new_category = Category(
            name=form_data["name"],
            showname=form_data["showname"],
            user_id=current_user.id,
        )
        # add category id and restaurant id
        db.session.add(new_category)

        db.session.commit()
        message['success'] = True
        message['category'] = new_category.id

    return jsonify(message)


@Restaurant_Blueprint.route('/categories')
@login_required
@requires_access_level(ACCESS['owner'])
def get_all_categories_by_user():
    message = {
        "success": False,
        "categories": []
    }
    # categories = Category.query.filter_by(user_id=current_user.id)
    categories = current_user.categories
    print(categories)
    if categories is not None:
        for category in categories:
            print(category.name)
            res = {
                "id": category.id,
                "name": category.name,
                "showname": category.showname,
            }
            message["categories"].append(res)
            message["success"] = True

    return jsonify(message)


@Restaurant_Blueprint.route('delete/category/<category_id>', methods=['POST'])
@requires_access_level(ACCESS['owner'])
@login_required
def deleteCategory(category_id):
    message = {
        "success": False,
    }
    target = Category.query.filter_by(id=category_id).first()
    db.session.delete(target)
    db.session.commit()
    message['success'] = True

    return jsonify(message)
