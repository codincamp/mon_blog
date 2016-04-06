#!/usr/bin/env python
from flask import render_template, send_from_directory, request, redirect, url_for
from flask_login import login_user, login_required, logout_user
from settings import app, db
from models import Post, User


@app.route('/signup', methods=['GET', 'POST'])
def signup():
  if request.method == 'GET':
      return render_template('signup.html')
  else:
      new_user = User(request.form["first_name"],
      request.form["last_name"],
      request.form["password"],
      request.form["email"])
      db.session.add(new_user)
      db.session.commit()
      login_user(new_user)
      return redirect(url_for("homepage"))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form["email"]
        password = request.form["password"]
        try:
            user = User.query.filter_by(email=email, password=password).first()
            login_user(user)
            return redirect(url_for('homepage'))
        except:
            pass
    return render_template('login.html')

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('homepage'))

@app.route('/')
def homepage():
    users = User.query.all()
    latest_posts = Post.query.order_by(Post.creation_date.desc()).limit(3)
    scored_posts = Post.query.limit(3).all()
    commented_posts = Post.query.limit(3).all()
    return render_template('homepage.html',
                            users=users,
                            latest_posts=latest_posts,
                            scored_posts=scored_posts,
                            commented_posts=commented_posts)

@app.route('/posts')
def posts():
    "Display all posts"
    posts = Post.query.all()
    return render_template('post_listing.html',
                            posts=posts)

@app.route('/post/<slug>')
def post(slug):
    "Display only one post"
    post = Post.query.filter_by(slug=slug).first()
    return render_template('post_display.html',
                            post=post)

@app.route('/add/post', methods=["POST", "GET"])
@login_required
def add_post():
    if request.method == "GET":
        return render_template('add_post_form.html')
    else:
        author = User.query.all()[0]
        title = request.form["title"]
        body = request.form["body"]
        post = Post(title, body, author)
        db.session.add(post)
        db.session.commit()

        return redirect(url_for("posts"))


@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True)
