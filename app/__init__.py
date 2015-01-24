from flask import Flask
from flask.ext.bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
bcrypt = Bcrypt(app)

db = SQLAlchemy(app)

from controllers import *

db.create_all()