from flask import Flask

from api.api_1_0.api import api_1_0, api_1_0_blueprint


def create_app():
    app = Flask(__name__)
    app.register_blueprint(api_1_0_blueprint,  url_prefix='/api/v1.0')
    return app
