from flask_restful import Resource
from app import db
import os
from flask import request
import json
import boto3
from app.models.product import Product
from app.models.records import Records
from app.serializers.product import ProductSchema
from app.main.auth_middleware import token_required
from app.main.auth_middleware import token_required_admin
from app.main.auth_middleware import get_token, get_current_user
from app.models.user import User

def send_plain_email(producto):
    ses_client = boto3.client("ses",
         region_name="us-east-1",
         aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
         aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
         )

    CHARSET = "UTF-8"

    users = User.simple_filter(rol=1)

    try:
        for user in users:
            response = ses_client.send_email(
                Destination={
                    "ToAddresses": [
                        str(user.email),
                    ],
                },
                Message={
                    "Body": {
                        "Text": {
                            "Charset": CHARSET,
                            "Data": "El producto "+str(producto)+" se ha modificado",
                        }
                    },
                    "Subject": {
                        "Charset": CHARSET,
                        "Data": "Notification Email",
                    },
                },
                Source=os.environ.get('EMAIL_SOURCE'),
            )
    except:
        print("Amazon SES sigue en modo Sandbox")

class ProductResource(Resource):
    @token_required
    def get(self, sku):
        current_user = get_current_user(get_token(request.headers))
        product = Product.get_by_id(sku)
        result={}
        if product.active == True:
            records = Records(id_user=current_user.id, id_products=product.sku)
            records.save()
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
        send_plain_email(ProductSchema().dumps(product))
        return result

    @token_required_admin
    def delete(self, sku):
        product = Product.get_by_id(sku)
        product.active = 0;
        product.save()
        result = ProductSchema().dump(product)
        send_plain_email(ProductSchema().dumps(product))
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
