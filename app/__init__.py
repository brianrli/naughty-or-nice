from flask import Flask
import os

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.cas import CAS
from flask.ext.cas import logout
import logging
import sys

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

app.config.from_object('config')
cas = CAS(app)  

db = SQLAlchemy(app)

# create database
from models import Player
# db.drop_all()
# db.create_all()
db.session.commit()

# initialize database
# from initplayers import initialize_db
# initialize_db()
# players = Player.query.all()
# print players

from app import views