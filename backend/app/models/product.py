from sqlalchemy import Integer, String

from app import db

class Product(db.Model):
    """
    Product Model
    """
    __tablename__ = 'products'

    sku = db.Column(String(500), primary_key=True)
    name = db.Column(String(100), nullable=False)
    price = db.Column(String(20), nullable=False, unique=True)
    mark = db.Column(String(50), nullable=False)
    quantity = db.Column(Integer, nullable=False, unique=True)

    def __init__(self, sku, name, price, mark, quantity):
        self.sku = sku
        self.name = name
        self.price = price
        self.mark = mark
        self.quantity = quantity

    def __repr__(self):
        return "<Product(sku='%s', name='%s')>" % (self.sku, self.name)