from flask import Flask, request, redirect
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
from app import main

app = Flask(__name__)
# adding configuration for using a sqlite database
app.config.from_object(main.settings['default'])


# Creating an SQLAlchemy instance
db = SQLAlchemy(app)

from app import models
# Settings for migrations
migrate = Migrate(app, db)


# function to render index page
@app.route('/')
def index():
    return "jajojojojoja"