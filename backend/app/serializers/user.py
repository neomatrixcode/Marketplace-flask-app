from marshmallow import fields, INCLUDE
from app.main.ext import ma

class UserSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    fullname = fields.String()
    username = fields.String()
    password = fields.String()
    email = fields.String()

    class Meta:
        unknown = INCLUDE