import os
import sqlalchemy

# uncomment the line below for postgres database url from environment variable
# postgres_local_base = os.environ['DATABASE_URL']

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False


class DevelopmentConfig(Config):
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base
    DEBUG = True
    engine = sqlalchemy.create_engine('mysql://root:''@localhost')
    # engine.execute("DROP DATABASE IF EXISTS eidola")
    engine.execute("CREATE DATABASE IF NOT EXISTS eidola")
    engine.execute("USE eidola") 
    SQLALCHEMY_DATABASE_URI = 'mysql://root:''@localhost/eidola'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    engine = sqlalchemy.create_engine('mysql://root:''@localhost')
    # engine.execute("DROP DATABASE IF EXISTS eidola")
    engine.execute("CREATE DATABASE IF NOT EXISTS eidola")
    engine.execute("USE eidola") 
    SQLALCHEMY_DATABASE_URI = 'mysql://root:''@localhost/eidola'
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    engine = sqlalchemy.create_engine('mysql://root:''@localhost')
    # engine.execute("DROP DATABASE IF EXISTS eidola")
    engine.execute("CREATE DATABASE IF NOT EXISTS eidola")
    engine.execute("USE eidola") 
    SQLALCHEMY_DATABASE_URI = 'mysql://root:''@localhost/eidola'
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
