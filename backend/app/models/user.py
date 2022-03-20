from sqlalchemy import Integer, String, ForeignKey

from app import db

class User(db.Model):
    """
    User Model
    """
    __tablename__ = 'users'

    id = db.Column(Integer, primary_key=True)
    fullname = db.Column(String(100), nullable=False)
    username = db.Column(String(20), nullable=False, unique=True)
    password = db.Column(String(50), nullable=False)
    email = db.Column(String(100), nullable=False, unique=True)
    rol = db.Column(Integer, ForeignKey('roles.id'), nullable = False)

    def __init__(self, fullname, username, password, email, rol):
        self.fullname = fullname
        self.username = username
        self.password = password
        self.email = email
        self.rol = rol

    def __repr__(self):
        return "<User(fullname='%s', username='%s')>" % (self.fullname, self.username)


