from .. import app
from flask import render_template



@app.get("/post/<int:post_id>")
def post(post_id:int):
    context = {
        "posts": [{"id": 1, "title": "mama mila ramu"}]
    }
    return render_template('index.html', **context)