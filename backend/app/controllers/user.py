from flask_restful import Resource
from flask import request
import json
from app import db
from app.models.user import User
from app.serializers.user import UserSchema
from app.main.auth_middleware import token_required_admin


class UserResource(Resource):
    @token_required_admin
    def get(self, id):
        result= {}
        user = User.get_by_id(id)
        if user.active == True:
            result = UserSchema().dump(user)
        return result

    @token_required_admin
    def put(self, id):
        data = json.loads(request.data)
        user_dict = UserSchema().loads(json.dumps(data))
        user = User.get_by_id(id)
        if("fullname" in user_dict):
            user.fullname = user_dict['fullname']
        if("email" in user_dict):
            user.email = user_dict['email']
        if("password" in user_dict):
            user.password = user_dict['password']
        if("rol" in user_dict):
            user.rol = user_dict['rol']
        user.save()
        result = UserSchema().dump(user)
        return result

    @token_required_admin
    def delete(self, id):
        user = User.get_by_id(id)
        user.active = 0;
        user.save()
        result = UserSchema().dump(user)
        return result


class UserListResource(Resource):
    @token_required_admin
    def get(self):
        users = User.simple_filter(active=True)
        result = UserSchema().dump(users, many=True)
        return result

    @token_required_admin
    def post(self):
        data = json.loads(request.data)
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

