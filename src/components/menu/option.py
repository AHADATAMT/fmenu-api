from flask import request, jsonify
from flask_login import current_user, login_required
from src import db
from . import Restaurant_Blueprint
from src.access_level import requires_access_level, ACCESS
from src.models.option import Option, Option_meta
import json


@Restaurant_Blueprint.route('/create_option', methods=['POST'])
@requires_access_level(ACCESS['owner'])
@login_required
def createOption():
    message = {
        "success": False,
    }
    if request.method == 'POST':
        form_data = json.loads(request.form.get('form'))
        options_data = json.loads(request.form.get('options'))

        new_option = Option(
            name=form_data["name"],
            showname=form_data["showname"],
            user_id=current_user.id,
        )

        db.session.add(new_option)
        db.session.commit()
        for option in options_data:
            print(list(option.values()))
            option_value = list(option.values())
            new_option_meta = Option_meta(
                key=option_value[0], value=option_value[1], option_id=new_option.id)
            db.session.add(new_option_meta)

        db.session.commit()
        message['success'] = True
        message['options'] = new_option.id

    return jsonify(message)


@Restaurant_Blueprint.route('/options')
@login_required
@requires_access_level(ACCESS['owner'])
def get_all_options_by_user():
    message = {
        "success": False,
        "options": []
    }
    options = Option.query.filter_by(user_id=current_user.id)
    if options is not None:
        for option in options:
            res = {
                "id": option.id,
                "name": option.name,
                "showname": option.showname,
                "option_metaes": []
            }
            for option_meta in option.option_metaes:
                res["option_metaes"].append(
                    {"option": option_meta.key, "value": option_meta.value})

            message["options"].append(res)
            message["success"] = True

    return jsonify(message)


@Restaurant_Blueprint.route('delete/option/<option_id>', methods=['POST'])
@requires_access_level(ACCESS['owner'])
@login_required
def deleteoption(option_id):
    message = {
        "success": False,
    }
    target = Option.query.filter_by(id=option_id).first()
    db.session.delete(target)
    db.session.commit()
    message['success'] = True

    return jsonify(message)
