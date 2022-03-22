from flask_restful import Resource
from app import db
from flask import request
import json
from app.models.product import Product
from app.serializers.product import ProductSchema
from app.main.auth_middleware import token_required
from app.main.auth_middleware import token_required_admin

class ProductResource(Resource):
    @token_required
    def get(self, sku):
        product = Product.get_by_id(sku)
        result={}
        if product.active == True:
            result = ProductSchema().dump(product)
        return result

    @token_required_admin
    def put(self, sku):
        data = json.loads(request.data)
        product_dict = ProductSchema().loads(json.dumps(data))
        product = Product.get_by_id(sku)
        if("name" in product_dict):
            product.name = product_dict['name']
        if("price" in product_dict):
            product.price = product_dict['price']
        if("mark" in product_dict):
            product.mark = product_dict['mark']
        if("quantity" in product_dict):
            product.quantity = product_dict['quantity']
        product.save()
        result = ProductSchema().dump(product)
        return result

    @token_required_admin
    def delete(self, sku):
        product = Product.get_by_id(sku)
        product.active = 0;
        product.save()
        result = ProductSchema().dump(product)
        return result

class ProductListResource(Resource):

    @token_required_admin
    def get(self):
        products = Product.simple_filter(active=True)
        result = ProductSchema().dump(products, many=True)
        return result

    @token_required_admin
    def post(self):
        data = json.loads(request.data)
        product_dict = ProductSchema().loads(json.dumps(data))
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
