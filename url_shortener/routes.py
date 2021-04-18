"""routes.py
Author: Maanav Modi
This script is the routes handler/assigner in the flask application.
It creates a Flask Blueprint which allows it to set up the routes
to other pages and render HTML pages. This script also handles the database
(adding, removing, visits counter, etc.) and routing to a 404 page.
"""
from flask import Blueprint, render_template, request, redirect

from .extension import db
from .models import Link
from .auth import requires_auth

# initalizes the Blueprint
short = Blueprint('short', __name__)

# Redirects to original link from an enter of short link
@short.route('/<short_url>')
def redirect_to_url(short_url):
    # Finds link
    link = Link.query.filter_by(short_url=short_url).first_or_404()

    # Increase visits
    link.visits = link.visits + 1
    db.session.commit()

    # Goes to original url
    return redirect(link.original_url) 

# Displays home page
@short.route('/')
def index():
    return render_template('index.html') 

# Recieves and adds origiinal link to db
# Redirects to page containing new link
@short.route('/add_link', methods=['POST'])
def add_link():
    # Gets user input from page
    original_url = request.form['original_url']
    # Creats a new Link object
    link = Link(original_url=original_url)
    # adds to db
    db.session.add(link)
    db.session.commit()

    # Redirects to link_added page containing new links
    return render_template('link_added.html', 
        new_link=link.short_url, original_url=link.original_url)

# stats page showing database statistics
@short.route('/stats')
@requires_auth
def stats():
    # gets all link objects
    links = Link.query.all()

    # Redirects to stats page with given all links in the database
    return render_template('stats.html', links = links)

#404 page
@short.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1>", 404