from sqlalchemy import Integer, String, ForeignKey, Boolean, DateTime
import datetime
from app.main.database import db, BaseModelMixin

class Records(db.Model, BaseModelMixin):
    """
    Records Model
    """
    __tablename__ = 'records'

    id = db.Column(Integer, primary_key=True, autoincrement=True)
    id_user = db.Column(Integer, ForeignKey('users.id'), nullable = False)
    id_products = db.Column(String(500), ForeignKey('products.sku'), nullable = False)
    time = db.Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, id_user, id_products):
        self.id_user = id_user
        self.id_products = id_products

    def __repr__(self):
        return "<Records(id_user='%d', id_products='%s', id='%d')>" % (self.id_user, self.id_products,self.id)


