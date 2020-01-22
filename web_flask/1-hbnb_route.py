#!/usr/bin/python3
"""Routes /hbnb."""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def default():
    """Displays 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB'."""
    return "HBNB"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
