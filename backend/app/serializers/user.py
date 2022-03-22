from marshmallow import fields
from app.main.ext import ma

class UserSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    fullname = fields.String()
    username = fields.String()
    password = fields.String()
    email = fields.String()
    #rol = fields.Nested('RolSchema', many=True)

# class RolSchema(ma.Schema):
#     id = fields.Integer(dump_only=True)
#     rol = fields.String()