from datetime import datetime
from . import main
from ..models import User
from .. import db
from flask import render_template, flash, redirect, session, request, url_for
from flask_login import login_user, logout_user, current_user, login_required

@main.route('/')
@main.route('/index')
def index():
    user = {'nickname': 'Jason'}  # fake user
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'John'}, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': {'nickname': 'Susan'}, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts,
                           logged=session.get('username'),
                           current_time=datetime.utcnow())


@main.route('/user/<name>')
def user(name):
    return render_template('user.html', name = name)

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session['username'] = form.username.data
        flash('Login requested for User ID="%s", remember_me=%s' %
              (form.username.data, str(form.remember_me.data)))
        return redirect(url_for('.index'))
    return render_template('login.html', 
                           title='Sign In',
                           form=form)