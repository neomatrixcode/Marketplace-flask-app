from flask import Flask, request, redirect
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
from app.main.database import db
from app.main.ext import migration, ma
from app import main
from app.main.api import api
from flask_cors import CORS

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

