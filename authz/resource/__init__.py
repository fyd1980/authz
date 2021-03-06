from authz import api
from authz.resource.user import UserResource

api.add_resource(
    UserResource,
    "/users",
    methods=["GET", "POST"]
)

api.add_resource(
    UserResource,
    "/users/<user_id>",
    methods=["GET", "PATCH", "DELETE"]
)
