from app import db


class Base(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key= True)


class User(Base):
    __tablename__ = "user"
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    password = db.Column(db.String(256))
    is_admin = db.Column(db.Boolean)

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
    title = db.Column(db.String(64), index=True)
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return "<%r's Post>" % self.id
