from flask_restful import Resource
from authz.controller import UserController

class UserResource(Resource):
    def get(self, user_id=None):
        if user_id is None:
            return UserController.get_users()
        else:
            return UserController.get_user()

    def post(self):
        UserController.create_user()

    def patch(self, user_id):
        UserController.update_user()

    def delete(self, user_id):
        UserController.delete_user()
