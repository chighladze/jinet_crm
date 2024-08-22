from flask import Blueprint, abort, request, render_template, redirect, url_for
from flask_login import login_required, current_user
from ..extensions import db

login = Blueprint('login', __name__)


@login.route('/login', methods=['GET', 'POST'])
def user_create():
    return render_template('main/login.html')
