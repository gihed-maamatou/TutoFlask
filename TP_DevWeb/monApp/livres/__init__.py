from flask import Blueprint
livres_bp = Blueprint('livres', __name__, template_folder='templates')
from . import routes