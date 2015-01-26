from flask import Flask
from flask.ext.bcrypt import Bcrypt
from flask_migrate import Manager
from flask_migrate import Migrate
from flask_migrate import MigrateCommand
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# Importing configuration from config file
app.config.from_object('config')
# For Password Scramble
bcrypt = Bcrypt(app)
# Create Manager instance for using Database Migration
manager = Manager(app)
# Database using SQLAlchemy
db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

from controllers import *