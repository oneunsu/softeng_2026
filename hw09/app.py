from flask import Flask, render_template
from flask import request
import pandas as pd

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/blog_list")
def blog_list():
    df = pd.read_csv("hw09/blog_data.csv", encoding="cp949")
    posts = []
    posts = df.to_dict(orient="records")

    return render_template("blog_list.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about_me.html")


app.run(debug=True)
