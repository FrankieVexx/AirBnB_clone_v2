#!/usr/bin/python3
""" a flask script that print line of text """

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """function that prnts 'Hello hbnb' """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
