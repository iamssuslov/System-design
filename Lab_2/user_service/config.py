import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    MONGODB_SETTINGS = os.environ.get(
        'MONGODB_SETTINGS') or {
                           'db': 'users_db',
                           'host': 'mongo-db',
                           'port': 27017
                       }
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get(
        'JWT_SECRET_KEY') or 'your_jwt_secret_key'
