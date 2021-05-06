from flask import request

from authz import db
from authz.model import User

class UserController:

    def create_user():
        data = request.get_json()
        return {
            "username": data["username"],
            "password": data["password"]
        }

    def get_users():
        pass

    def get_user(user_id):
        pass

    def update_user(user_id):
        pass

    def delete_user(user_id):
        pass


