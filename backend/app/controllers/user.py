from flask_restful import Resource
from app import db
from app.models.user import User


class User(Resource):
    def get(self, id):
        pass

    def put(self, id):
        pass

    def patch(self, id):
        pass

    def delete(self, id):
        pass


class UserList(Resource):

    def get(self):
        return User.query.all()
#return User.read_all()#
    def post(self):
        pass


