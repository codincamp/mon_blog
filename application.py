#!/usr/bin/env python
from flask import render_template, send_from_directory, request

from settings import app

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/posts')
def posts():
    "Display all posts"
    return render_template('post_listing.html')

@app.route('/post/<slug>')
def post(slug):
    "Display only one post"
    return render_template('post_display.html')

@app.route('/add/post')
def add_post():
    "Add post"
    return render_template('add_post_form.html')


@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True)
