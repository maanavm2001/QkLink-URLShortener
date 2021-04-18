"""settings.py
Author: Maanav Modi
This script is the settings fot the flask app intialized in __init__.py
Keeps track of Database access and system username and password
"""
import os 

SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
SQLALCHEMY_TRACK_MODIFICATIONS = False

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'password'