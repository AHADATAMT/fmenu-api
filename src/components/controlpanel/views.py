from flask import render_template, flash, redirect, url_for
from flask_login import login_required, logout_user, current_user, login_user
from src import db
from src.models.user import User, ACCESS
from . import ControlPanel
from src.access_level import requires_access_level
import json

@ControlPanel.route('/')
@requires_access_level(ACCESS['owner'])
def profile():
    user = User.query.filter_by(email=current_user.email).first()
    if not user.is_owner():
        return redirect("http://localhost:3000/")
    
    return ("True")