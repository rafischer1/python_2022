from flask import Flask
from flask import render_template, url_for
app = Flask(__name__)


@app.route('/')
def hello_world():
    url_for('static', filename='main.70a66962.js')
    return render_template("./index.html")


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)
