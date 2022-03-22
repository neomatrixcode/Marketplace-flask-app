from sqlalchemy import Integer, String, Boolean

from app.main.database import db, BaseModelMixin

class Product(db.Model, BaseModelMixin):
    """
    Product Model
    """
    __tablename__ = 'products'

    sku = db.Column(String(500), primary_key=True)
    name = db.Column(String(100), nullable=True)
    price = db.Column(Integer, nullable=True)
    mark = db.Column(String(50), nullable=True)
    quantity = db.Column(Integer, nullable=True)
    active = db.Column(Boolean, default=True)

    def __init__(self, sku, name, price, mark, quantity):
        self.sku = sku
        self.name = name
        self.price = price
        self.mark = mark
        self.quantity = quantity

    def __repr__(self):
        return "<Product(sku='%s', name='%s')>" % (self.sku, self.name)