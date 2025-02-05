#!/usr/bin/python3
""" a flask script that print line of text """

from flask import Flask, render_template
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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_test(text='is cool'):
    """display "Python " + the text variable if provided"""
    return 'Python ' + text.replace("_", " ")


@app.route('/number/<n>', strict_slashes=False)
def numb(n):
    """ Display an integer"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    """Display a html template"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def hmtl_var(n):
    """Display html variables"""
    if n % 2 == 0:
        nm_odd_or_even = 'even'
    else:
        nm_odd_or_even = 'odd'
    return render_template("6-number_odd_or_even.html", n=n, m=nm_odd_or_even)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
