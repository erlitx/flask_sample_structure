from flask import render_template, current_app, session
# Import the Blueprint object from main/__init__.py
from . import main, errors
from ..models import User
from .. import db
from flask_login import login_required, current_user

#main = Blueprint('main', __name__)

@main.route('/')
@login_required
def index():

    return render_template('index.html')

@main.route('/2')
def index2():
    return render_template('index.html')

@main.route('/3')
def index3():
    return 'Hello3'