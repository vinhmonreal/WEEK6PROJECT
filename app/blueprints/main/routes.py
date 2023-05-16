from flask import render_template

from . import bp 
from app import app

@bp.route('/')
@bp.route('/home')
def home():
    return render_template('home.jinja', title='Home')

@bp.route('/about')
def about():
    return render_template('about.jinja', title='About')
