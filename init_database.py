# -*- coding: utf-8 -*-
from app import db


def init_database():
    db.create_all()


def make_superuser(email, password):
    from app.models import User
    u = User()
    u.email = email
    u.set_password(password=password)
    u.nickname = u'관리자'
    u.is_admin = True
    db.session.add(u)
    db.session.commit()
