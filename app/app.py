# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import redirect
from flask import url_for
from datetime import timedelta
from init_database import db_session
from flask.ext.bcrypt import Bcrypt


app = Flask(__name__)
app.config.from_object('config')
bcrypt = Bcrypt(app)


@app.before_request
def make_session_timeout():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5)


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Tommy'}
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day!'
        },
        {
            'author': {'nickname': 'Tony'},
            'body': 'Worst day!'
        }
    ]
    menu_item = [u'글보기', u'글쓰기']
    return render_template('index.html',
                           title='Flask',
                           posts=posts,
                           user=user,
                           menu_item=menu_item)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/login_process', methods=['POST'])
def login_process():
    if request.method == 'POST':
        from models import User
        user_email = request.form['user_email']
        user_password = request.form['user_password']
        u = User.query.filter_by(email=user_email).first()
        if not u is None:
            if u.check_password_hash(password=user_password):
                session['user_name'] = user_email
                session['user_nickname'] = u.nickname
                session['logged_in'] = True
        return redirect(url_for('index'))


@app.route('/join')
def join():
    return render_template('join.html')


@app.route('/join_process', methods=['POST'])
def join_process():
    if request.method == 'POST':
        from models import User
        new_user = User()
        new_user.email = request.form['user_email']
        new_user.nickname = request.form['user_nickname']
        new_user.set_password(request.form['user_password'])
        db_session.add(new_user)
        db_session.commit()
        return redirect(url_for('index'))


@app.route('/logout')
def logout():
    session['logged_in'] = False
    session.pop('user_name', None)
    session.pop('user_nickname', None)
    return redirect(url_for('index'))

app.secret_key = '\xa9~\xd8\\\xe0\x90}N^\xab\xd9]\xa6.\xc2\x0f8U\xcd\x8d,\xa5JY'

# When this application package is imported, this will block automatically
# starting app
if __name__ == '__main__':
    app.run(debug=True)
