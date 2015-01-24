#DEBUGING
DEBUG = True

#SQLALCHEMY
import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

#SECRETKEY
SECRET_KEY = '\xa9~\xd8\\\xe0\x90}N^\xab\xd9]\xa6.\xc2\x0f8U\xcd\x8d,\xa5JY'