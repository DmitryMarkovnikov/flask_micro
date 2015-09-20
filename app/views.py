from app import app
from flask import render_template, flash, redirect, request
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


@app.route('/login', methods=['GET', 'POST'])
def login():
    # You have to initialize the form instance with values from the request:
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        flash('Login submitted with OpenID: "{0}" and'
              ' with remember_me: "{1}"'.format(form.open_id.data,
                                                form.remember_me.data))
        return redirect("/index")
    return render_template("login.html", title="Sign In", form=form,
                           providers=app.config['OPENID_PROVIDERS'])
