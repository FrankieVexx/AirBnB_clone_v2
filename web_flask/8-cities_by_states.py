#!/usr/bin/python3

"""This module contains the app instance for the AirBnB Web"""

from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def clean_up_session(exception=None):
    """eliminates current Session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    """enumerate all states"""
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
