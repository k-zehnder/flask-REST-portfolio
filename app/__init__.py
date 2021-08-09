from flask_restx import Api
from flask import Blueprint

from .main.controller.peak_controller import api as peak_ns

blueprint = Blueprint('api', __name__)

api = Api(
    blueprint,
    title='FLASK RESTPLUS(RESTX) API by Kevin Zehnder',
    version='1.0',
    description='Flask RESTPLUS Web Service'
)

api.add_namespace(peak_ns, path='/peak')
