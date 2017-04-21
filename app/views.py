from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Thomas'} # fake user
    posts = [ # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day on Newton!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': "I'm looking forward to Random Things being gone."
        }
    ]
    return render_template('index.html',
                            title='Catholicrafters',
                            user=user,
                            posts=posts)
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for MC_Username="%s", remember_me=%s' %
                (form.mc_username.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                            title='Sign In',
                            form=form)
