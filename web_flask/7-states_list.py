#!/usr/bin/python3
"""Lists all states in /states_list."""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def close(self):
    """Disposes of the current Session."""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def state_list():
    """Lists all states."""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
