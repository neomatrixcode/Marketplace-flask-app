from sqlalchemy import Integer, String

from app.main.database import db, BaseModelMixin

class Rol(db.Model, BaseModelMixin):
    """
    Rol Model
    """
    __tablename__ = 'roles'

    id = db.Column(Integer, primary_key=True, autoincrement=True)
    rol = db.Column(String(100), nullable=False)

    def __init__(self, rol):
        self.rol = rol

    def __repr__(self):
        return "<Rol(rol='%s', username='%s')>" % (self.rol)
