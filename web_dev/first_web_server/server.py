from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    print("HELLO RUNNING")
    return render_template("./index.html")


@app.route('/blog')
def hello_blog():
    return 'Hello, World BLOG'
