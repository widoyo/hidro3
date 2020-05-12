from flask import (Flask, Blueprint)
from flask_restful import (Api, Resource)

from .pos import PosList

bp = Blueprint('api', __name__, url_prefix='/api')

api = Api(bp)

@bp.route('/')
def index():
    return ''

api.add_resource(PosList, '/pos')
