import json

from flask import (Flask, render_template, request,
                   make_response, url_for, redirect, flash)

from options import DEFAULTS

app = Flask("__name__")
# secret key needed because of flash module needs a session which can't work without secret key
app.secret_key = b"+*\x02X\xf5LH\x9a\x1c\x1dm|s\xbd\xf8j'\xec\xc7;M&\xd7\xbe"


def get_saved_data():
    try:
        data = json.loads(request.cookies.get("character"))
    except TypeError:
        data = {}
    return data

@app.route("/")
def index():
    data = get_saved_data()
    return render_template("index.html", saves=data)

@app.route("/builder")
def builder():
    data = get_saved_data()
    return render_template("builder.html", saves=data, options=DEFAULTS)


@app.route("/save", methods=["POST"])
def save():
    flash("You made it! Proud of you")
    # what we redirected is turned to response object
    response = make_response(redirect(url_for("builder")))
    # the response is set to cookie with "character". it could be any word.
    # json.dumps is to dump strings.|| request.form is ImmutableMultiDict, key value is gotten by .items()

    # logic for updating the cookies created in the form
    # we first get saved cookies
    data = get_saved_data()
    # we update based on new submissions
    data.update(dict(request.form.items()))
    # set the new cookies
    response.set_cookie("character", json.dumps(data))
    return response


app.run(debug=True)