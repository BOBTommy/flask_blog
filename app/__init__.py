from flask import Flask
from flask.ext.bcrypt import Bcrypt

app = Flask(__name__)
app.config.from_object('config')
bcrypt = Bcrypt(app)

from controllers import *