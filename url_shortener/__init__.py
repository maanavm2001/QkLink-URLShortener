"""__init__.py
Author: Maanav Modi
This script is the initializer __init__.py to iniatilize the
Flask application which has the routes bluperint from routes.py
functions:
    * create_app(comfig_file): A function that takes in a settings config .py file
    that will then intialize the Flask app, and assign the html routes and functions
    from routes.py
"""
from flask import Flask 

from .extension import db
from .routes import short

# A function that takes in a settings config .py file
# that will then intialize the Flask app, and assign the html routes and functions
# from routes.py
#   config_file = settings config .py file
def create_app(config_file='settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    # initializes app
    db.init_app(app)

    # assigns blueprint of routes
    app.register_blueprint(short)

    return app