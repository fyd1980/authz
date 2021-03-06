from flask import Flask
from flask_restful import Api
from authz import resource
from flask_sqlalchemy import SQLAlchemy
from authz.config import Config

db = SQLAlchemy()
api = Api()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config) #Load configs from env variables
    db.init_app(app)
    api.init_app(app)
    return app
