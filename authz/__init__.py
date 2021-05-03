from flask import Flask
from flask_restful import Api
from authz import resource
from authz.config import config

api = Api()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config) #Load configs from env variables
    api.init_app(app)
    return app
