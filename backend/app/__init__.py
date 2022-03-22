from flask import Flask, request, redirect
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
from app.main.database import db
from app.models.user import User
from app.main.ext import migration, ma
from app import main
from app.main.api import api
from flask_cors import CORS
import json
import jwt

app = Flask(__name__)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# adding configuration for using a sqlite database
app.config.from_object(main.settings['default'])


# # Database ORM Initialization
db.init_app(app)

# # Database Migrations Initialization
migration.init_app(app, db)

# # Flask API Initialization
api.init_app(app)

#
ma.init_app(app)




@app.route("/users/login", methods=["POST"])
def login():
	try:
		data = json.loads(request.data)
		if not data:
			return {
			"message": "Please provide user details",
			"data": None,
			"error": "Bad request"
			}, 400

		user = User.filter_one(email=data["email"])
		if user.active==True:
			if user.password == data["password"]:
				try:# token should expire after 24 hrs
					token = jwt.encode(
						{"user_id": user.id},
						app.config["SECRET_KEY"],
						algorithm="HS256"
						)
					return {
					"message": "Successfully fetched auth token",
					"data": token
					}
				except Exception as e:
					return {
					"error": "Something went wrong",
					"message": str(e)
					}, 500
		return {
		"message": "Error fetching auth token!, invalid user, email or password",
		"data": None,
		"error": "Unauthorized"
		}, 404
	except Exception as e:
		return {
		"message": "Something went wrong!",
		"error": str(e),
		"data": None
		}, 500


