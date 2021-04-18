Welcome to my URL Shortener made with Python, Flask, SQL, HTML, and CSS

This is a simple Flask app setup where a user can enter a long url
and the app will rerturn a shortened url. The app has different landing 
pages to display the infomation.

This program implements SQLAlchemny, Flask, random, datetime, and os to function.
Also, on the HTML side CSS classes and objects were used from bulma.io

Flask is used to create the micro web structure and useed to import SQLAlchemy
which is the driver for the programs SQL Database

URLSHORTENER-
            |
            |
            MyEnv----
                    |
                    bin-
                    include-
                    lib-
                    .env
                    .gitignore
                    pyenv.cfg
            README---
                    |
                    readme.md
                    Homepage.png
                    Stats.png
                    AddedLink.png
            url_shortener----
                            |
                            __pycache__-
                            bin-
                            include-
                            lib-
                            templates----
                                        |
                                        index.html
                                        link_added.html
                                        stats.html
                            __init__.py
                            .gitignote
                            auth.py
                            db.sqlite3
                            extension.py
                            models.py
                            pyeenv.cfg
                            routes.py
                            settings.py

To learn about each file, their tasks, and their contents follow the above file directory
to inspect the documented file.

To run this program you will need Flask to start a web app on a local or web IP.
Run the application with; FLASK_APP= url_shortener/__init__.py flask run

Thank You
Maanav Modi
Student of University of Arizona
Obtaining B.S. Computer Science

If you have any questions or comments please email me @ maanavm.2001@gmail.com