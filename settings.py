#!/usr/bin/env python
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:plop@localhost/blog'
