# config.py
import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'b299860c3dc7b3d9a319e97a68cd0c2c')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
