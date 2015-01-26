# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import config

engine = create_engine(config.SQLALCHEMY_DATABASE_URI,
                       convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    from models import User,Post
    Base.metadata.create_all(bind=engine)


def make_superuser(email, password):
    from models import User
    from app import db
    u = User()
    u.email = email
    u.password = u.set_password(password=password)
    u.nickname = u'관리자'
    u.is_admin = True
    db.session.add(u)
    db.session.commit()
