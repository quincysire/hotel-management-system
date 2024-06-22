# from dotenv import load_dotenv
# import redis
import os
from datetime import timedelta

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://hotels_90q7_user:A6RSArvCUh4OXcKWUGQJeZRyWJDvC8jz@dpg-cpreeq5umphs73c43jl0-a.oregon-postgres.render.com/hotels_90q7'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    # SECRET_KEY = os.environ['SECRET_KEY']


    # Additional JWT Configurations
    JWT_SECRET_KEY = os.urandom(32).hex()
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access']
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=72)


    # Email config
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ""
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True