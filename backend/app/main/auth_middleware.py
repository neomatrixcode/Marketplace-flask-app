from functools import wraps
import jwt
from flask import request, abort
from flask import current_app
from app.models.user import User


def get_token(headers):
    token = None
    if "Authorization" in headers:
        token = request.headers["Authorization"].split(" ")[1]
    return token

def get_current_user(token):
    current_user = None
    try:
        data=jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
        current_user=User.get_by_id(data["user_id"])
    except Exception as e:
         raise Exception("Something went wrong")
    return current_user

def token_required_admin(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = get_token(request.headers)
        if not token:
            return {
            "message": "Authentication Token is missing!",
            "data": None,
            "error": "Unauthorized"
            }, 401
        current_user = get_current_user(token)
        if current_user is None:
            return {
            "message": "Invalid Authentication token!",
            "data": None,
            "error": "Unauthorized"
            }, 401
        if not current_user.active:
            abort(403)
        if current_user.rol !=1:
            abort(403)
        return f(*args, **kwargs)
    return decorated

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = get_token(request.headers)
        if not token:
            return {
            "message": "Authentication Token is missing!",
            "data": None,
            "error": "Unauthorized"
            }, 401
        current_user = get_current_user(token)
        if current_user is None:
            return {
            "message": "Invalid Authentication token!",
            "data": None,
            "error": "Unauthorized"
            }, 401
        if not current_user.active:
            abort(403)
        return f(*args, **kwargs)
    return decorated