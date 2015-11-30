from flask import Flask
import os

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from flask_cas import CAS
from flask_cas import logout

import logging
import sys

app = Flask(__name__)

# debugging
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

app.config.from_object('config')
cas = CAS(app)  

db = SQLAlchemy(app)

# create database
from models import Player
# db.drop_all()
# db.create_all()
# db.session.commit()

# initialize database
# from initplayers import initialize_db
# db.create_all()
# db.session.add(Player('Brian','brian.li@yale.edu',False,"You are a blessing on this earth."))
# db.session.add(Player('Ben','benjamin.bartolome@yale.edu',True))
# db.session.add(Player('Kevin','kevin.garcia@yale.edu',True,'Sucks to suck.'))
# db.session.add(Player('Aimee','aimee.sawyer@yale.edu'))
# db.session.commit()
# players = Player.query.all()
# print players

from app import views