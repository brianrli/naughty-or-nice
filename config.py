import os

# Whoosh does not work on Heroku
WHOOSH_ENABLED = os.environ.get('HEROKU') is None

WTF_CSRF_ENABLED = True

# CAS
CAS_SERVER = 'https://secure.its.yale.edu'
CAS_LOGIN_ROUTE = '/cas/login'
CAS_AFTER_LOGIN = 'index'
SECRET_KEY = 'mysecretkey'

# DATABASE
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
# SQLALCHEMY_DATABASE_REPO = os.path.join(basedir,'db_repository')