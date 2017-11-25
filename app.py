from flask import (Flask, render_template, request,
                   make_response, url_for, redirect)

app = Flask("__name__")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/save", methods=["POST"])
def save():
    return "Saved"


app.run(debug=True)