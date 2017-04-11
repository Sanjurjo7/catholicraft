from flask import render_template
from app import app

post1 = {"author":"sanjurjo", "post":"This is a fake post"}

@app.route('/')
@app.route('/index')
def index():
  user = {'nickname': 'schylus'} #fake user
  posts = [post1]
  return render_template('index.html',
                          title='Home',
                          user=user,
                          posts=posts)

