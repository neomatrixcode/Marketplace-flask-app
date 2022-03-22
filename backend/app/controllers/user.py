from flask_restful import Resource
from flask import request
import json
from app import db
from app.models.user import User
from app.serializers.user import UserSchema

class UserResource(Resource):
    def get(self, id):
        user = User.get_by_id(id)
        result= {}
        if user.active == True:
            result = UserSchema().dump(user)
        return result

    def delete(self, id):
        pass


class UserListResource(Resource):

    def get(self):
        users = User.simple_filter(active=True)
        result = UserSchema().dump(users, many=True)
        return result

    def post(self):
        data = json.loads(request.data)
        print(data)
        print(json.dumps(data))
        user_dict = UserSchema().loads(json.dumps(data))
        user = User(
            fullname=user_dict['fullname'],
            username=user_dict['username'],
            password=user_dict['password'],
            email=user_dict['email'],
            rol=user_dict['rol']
            )
        user.save()
        resp = UserSchema().dump(user)
        return resp, 201

