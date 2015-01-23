from init_database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import DateTime
from sqlalchemy import Text
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    nickname = Column(String(64), index=True, unique=True)
    email = Column(String(120), index=True, unique=True)
    posts = relationship('Post', backref='author', lazy='dynamic')
    password = Column(String(256))

    def __repr__(self):
        return '%r' % self.nickname

    def set_password(self, password):
        from app import bcrypt
        self.password = bcrypt.generate_password_hash(password=password)

    def check_password_hash(self, password):
        from app import bcrypt
        if bcrypt.check_password_hash(pw_hash=self.password,
                                      password=password):
            return True
        else:
            return False


class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    title = Column(String(64), index=True)
    body = Column(Text)
    writer = Column(String(64))
    timestamp = Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id'))

    def __repr__(self):
        return "<%r's Post>" % self.id
