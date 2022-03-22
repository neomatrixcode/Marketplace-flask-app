from marshmallow import fields, INCLUDE
from app.main.ext import ma

class ProductSchema(ma.Schema):
    sku = fields.String(dump_only=True)
    name = fields.String()
    price = fields.Integer()
    mark = fields.String()
    quantity = fields.Integer()

    class Meta:
        unknown = INCLUDE