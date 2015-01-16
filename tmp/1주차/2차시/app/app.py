from flask import Flask
from flask import render_template

app = Flask(__name__)


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

app.run(debug=True)
