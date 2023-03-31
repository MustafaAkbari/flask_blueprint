from flask import render_template, Blueprint

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("index.html")

@main.route("/users/<name>")
def username(name):
    return render_template("userpage.html", name=name)
