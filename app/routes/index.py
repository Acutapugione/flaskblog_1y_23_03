from .. import app
from flask import render_template
from sqlalchemy import select
from db import Post, Session


@app.get("/")
def index():
    with Session.begin() as session:
        posts = [Post(**x) for x in session.scalars(select(Post)).all()]
    context = {
        "posts": posts
    }
    return render_template('index.html', **context)