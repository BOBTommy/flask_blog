from flask import Flask
from flask import render_template
from flask import request
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


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
    return render_template('index.html',
                           title='Flask',
                           posts=posts,
                           user=user)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/login_process', methods=['POST'])
def login_process():
    if request.method == 'POST':
        return request.form['user_email']

app.run(debug=True)
