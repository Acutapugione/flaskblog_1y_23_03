from .. import app
from flask import render_template



@app.get("/about")
def about():
    context = {
        "posts": [{"id": 1, "title": "mama mila ramu"}]
    }
    return render_template('index.html', **context)