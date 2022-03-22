from app.controllers.user import UserListResource, UserResource
from app.controllers.product import ProductListResource, ProductResource
from app.main.errors import errors
from flask_restful import Api

# Flask API Configuration
api = Api(
    catch_all_404s=True,
    errors=errors,
    prefix='/api'
)

api.add_resource(UserListResource, '/users')
api.add_resource(UserResource, '/users/<int:id>/')

api.add_resource(ProductListResource, '/products')
api.add_resource(ProductResource, '/products/<string:sku>/')
