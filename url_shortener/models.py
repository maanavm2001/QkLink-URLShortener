"""models.py
Author: Maanav Modi
This script is the Link class. This is the class
object to be stored within the database. This is the driver
for the short link generation. It holds link informations such 
as (id, original_url, short_url, visits, etc.)
"""
import string
from datetime import datetime
from random import choices

from .extension import db 

class Link(db.Model):
    # information variables
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(512))
    short_url = db.Column(db.String(3), unique=True)
    visits = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.now)

    # initializer takes args from super class
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # sets short url
        self.short_url = self.generate_short_link()

    # generates short url max length of 6
    def generate_short_link(self):
        characters = string.digits + string.ascii_letters
        short_url = ''.join(choices(characters, k=6))

        # checks to see if link is in database
        link = self.query.filter_by(short_url=short_url).first()

        # if so, reemake the combination
        if link:
            return self.generate_short_link()
        
        return short_url