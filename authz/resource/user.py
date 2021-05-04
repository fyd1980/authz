from flask_restful import Resource

USERS = [
    {
        "id": "89877878",
        "username": "admin"
    },
    {
        "id": "89877858",
        "username": "test"
    },
    {
        "id": "89577878",
        "username": "farid"
    },
]


class UserResource(Resource):
    def get(self, user_id=None):
        if user_id is None:
            return USERS
        else:
            return USERS[int(user_id)]

    def post(self):
        pass

    def patch(self, user_id):
        pass

    def delete(self, user_id):
        pass
