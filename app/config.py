import os

from flask import Flask

from app.api import api_1_0_blueprint


class FlaskConfig:
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__name__)),
                                 'uploads')


def create_app():
    app = Flask(__name__)
    app.config.from_object(FlaskConfig)
    app.register_blueprint(api_1_0_blueprint,  url_prefix='/api')
    return app
