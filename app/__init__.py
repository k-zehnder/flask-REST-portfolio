from flask_restx import Api
from flask import Blueprint

from .main.controller.peak_controller import api as peak_ns
from .main.controller.review_controller import api as review_ns

blueprint = Blueprint('api', __name__)

api = Api(
    blueprint,
    title='FLASK REST API by Kevin Zehnder',
    version='1.0',
    description='Flask RESTPLUS Web Service'
)

api.add_namespace(peak_ns, path='/peaks')
api.add_namespace(review_ns)
