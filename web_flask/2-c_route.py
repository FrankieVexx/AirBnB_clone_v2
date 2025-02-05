#!/usr/bin/python3
""" a flask script that print line of text """

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """function that prnts 'Hello hbnb' """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def index():
    """ a function that returns hbnb """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """ display "c is fun """
    return 'C ' + text.replace("_", " ")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
