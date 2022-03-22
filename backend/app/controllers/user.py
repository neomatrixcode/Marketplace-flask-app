from flask_restful import Resource
from app import db
from app.models.user import User
from app.serializers.user import UserSchema

class UserResource(Resource):
    def get(self, id):
        user = User.get_by_id(id)
        result = UserSchema().dumps(user)
        return result

    def post(self, id):
        pass

    def delete(self, id):
        pass


class UserListResource(Resource):

    def get(self):
        users = User.get_all()
        result = UserSchema().dumps(users, many=True)
        return result

