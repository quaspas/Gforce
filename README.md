Gforce
======

Api Test

Development Environment Setup
-----------------------------

You will need the following:

* Python 3.4+

Start by creating a virtual environment

    > mkvirtualenv gforce --python=/usr/local/bin/python3
    (gforce) >

The `(gforce)` prefix indicates that a virtual environment called "gforce" is being used. Next, check that you have the correct version of Python:

    (gforce) > python --version
    Python 3.4.1
    (gforce) > pip --version
    pip 1.5.6 from /Users/..../site-packages (python 3.4)

Install the project requirements

    (gforce) > pip install -r requirements.txt

Create `localsettings.py` with the following

    API_SECRET_KEY = 'somesupersecretkey'
    API_CLIENT_KEY = 'somenotsosupersecretkey'
    WEBHOOKS_KEY = 'someotherkey'