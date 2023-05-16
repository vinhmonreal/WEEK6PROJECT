from flask import Blueprint

bp = Blueprint('social', __name__, url_prefix='/social')

from app.blueprints.social import routes