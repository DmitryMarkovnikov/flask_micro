from app import app
from flask import render_template
from forms import LoginForm



@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Dmitry'}
    posts = [
        {
            "author": {"nickname": "James P."},
            "body": "What a rainy day!"
        },
        {
            "author": {"nickname": "Lily P."},
            "body": "Minsk is not the place I'm dreaming about =("
        },
        {
            "author": {"nickname": "Harry P."},
            "body": "Hello, mam, dad!"
        }

    ]
    return render_template("index.html", title="Home", user=user, posts=posts)


@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template("login.html", title="Sign In", form=form)