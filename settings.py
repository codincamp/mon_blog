#!/usr/bin/env python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "plop42"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
