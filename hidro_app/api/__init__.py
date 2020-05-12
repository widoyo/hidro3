from flask import (Flask, Blueprint)
from flask_restful import (Api)

from .pos import PosList

bp = Blueprint('api', __name__, url_prefix='/api')

api = Api(bp)


api.add_resource(PosList, '/pos')
