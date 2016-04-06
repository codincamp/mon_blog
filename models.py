#!/usr/bin/env python

from settings import db, app
from datetime import datetime
from slugify import slugify

import flask.ext.login as flask_login
login_manager = flask_login.LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

class User(db.Model, flask_login.UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(60))
    last_name = db.Column(db.String(60))
    password = db.Column(db.String(60))
    email = db.Column(db.String(120), unique=True)

    posts = db.relationship("Post", backref='author')

    def __init__(self, first_name, last_name, password, email):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email

    def __repr__(self):
        return "User : %s %s %s %s" % (self.first_name, self.last_name, self.email, self.password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    slug = db.Column(db.String(60), unique=True)
    body = db.Column(db.Text)
    creation_date = db.Column(db.DateTime, default=datetime.now())
    id_author = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, title, body, author):
        self.title = title
        self.slug = slugify(title)
        self.body = body
        self.id_author = author.id

# db.drop_all()
# db.create_all()
# author = User("Alban", "Tiberghien", "plop", "alban@plop.fr")
# db.session.add(author)
# db.session.commit()
#
# for i in range(20):
#     post = Post("Post #%s" % i, "Bonjour le monde", author)
#     db.session.add(post)
#     db.session.commit()
