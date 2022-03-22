from flask_restful import Resource
from app import db
from app.models.product import Product
from app.serializers.product import ProductSchema

class ProductResource(Resource):
    def get(self, sku):
        product = Product.get_by_id(sku)
        result = ProductSchema().dumps(product)
        return result

    def post(self, id):
        pass

    def delete(self, id):
        pass


class ProductListResource(Resource):

    def get(self):
        products = Product.get_all()
        result = ProductSchema().dumps(products, many=True)
        return result
