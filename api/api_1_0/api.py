from flask_restful import Api
from flask import Blueprint

from .resources import HelloWorld, UploadCsv

api_1_0_blueprint = Blueprint('api_1_0', __name__)
api_1_0 = Api(api_1_0_blueprint)

api_1_0.add_resource(HelloWorld, '/')
api_1_0.add_resource(UploadCsv, '/upload')
