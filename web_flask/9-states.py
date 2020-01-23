#!/usr/bin/python3
"""Displays State and Cities in /states/<id>."""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def close(self):
    """Disposes of the current Session."""
    storage.close()


@app.route('/states', strict_slashes=False)
def state():
    """Lists all states."""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """Displays a State by id."""
    key = "State.{}".format(id)
    state = storage.all()[key] if key in storage.all() else None
    return render_template('9-states.html', state=state)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
