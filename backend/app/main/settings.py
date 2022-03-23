# -*- coding: utf-8 -*-
import os


class Config:

    # project root directory
    BASE_DIR = os.path.join(os.pardir, os.path.dirname(__file__))
    SECRET_KEY = os.environ.get("SECRET_KEY","89y7h7666t687")

    # Flask Configuration
    # --------------------------------------------------------------------
    DEBUG = False
    TESTING = False
    PORT = 80

    # sqlalchemy database main
    # --------------------------------------------------------------------
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL','mysql://root:root@192.168.1.67:3306/db')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    PROPAGATE_EXCEPTIONS = True
    ERROR_404_HELP = True

    # SMTP server main
    # --------------------------------------------------------------------
    REGION_NAME= os.environ.get('REGION_NAME',"us-east-1")
    AWS_ACCESS_KEY_ID=os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY=os.environ.get('AWS_SECRET_ACCESS_KEY')
    EMAIL_SOURCE=os.environ.get('EMAIL_SOURCE')


class DevelopmentConfig(Config):

    ENV = os.environ.get("FLASK_ENV", "development")
    DEBUG = True
    ASSETS_DEBUG = True


class TestingConfig(Config):

    ENV = os.environ.get("FLASK_ENV", "testing")
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):

    ENV = os.environ.get("FLASK_ENV", "production")
    DEBUG = False
    USE_RELOADER = False


settings = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
}