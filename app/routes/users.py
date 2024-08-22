from flask import Blueprint, abort, request, render_template, redirect, url_for
from flask_login import login_required, current_user
from ..extensions import db

users = Blueprint('users', __name__)


@users.route('/user/create', methods=['GET', 'POST'])
def user_create():
    return render_template('users/create.html')
