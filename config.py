import os

from dotenv import load_dotenv
if os.path.isfile('.env'):
    load_dotenv('.env', override=True)


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    UNBABEL_API_USERNAME = os.environ['UNBABEL_API_USERNAME']
    UNBABEL_API_KEY = os.environ['UNBABEL_API_KEY']
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SECRET_KEY = 'super-secret'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
