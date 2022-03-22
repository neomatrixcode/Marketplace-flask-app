from flask_restful import Resource
from app import db
from flask import request
import json
from app.models.product import Product
from app.serializers.product import ProductSchema

class ProductResource(Resource):
    def get(self, sku):
        product = Product.get_by_id(sku)
        result={}
        if product.active == True:
            result = ProductSchema().dump(product)
        return result

    def post(self, id):
        return "", 201

    def delete(self, id):
        pass


class ProductListResource(Resource):

    def get(self):
        products = Product.simple_filter(active=True)
        result = ProductSchema().dump(products, many=True)
        return result

    def post(self):
        data = json.loads(request.data)
        print(data)
        product_dict = ProductSchema().loads(json.dumps(data))
        print(product_dict)
        product = Product(
            sku = product_dict['sku'],
            name = product_dict['name'],
            price = product_dict['price'],
            mark = product_dict['mark'],
            quantity = product_dict['quantity']
            )
        product.save()
        resp = ProductSchema().dump(product)
        return resp, 201
