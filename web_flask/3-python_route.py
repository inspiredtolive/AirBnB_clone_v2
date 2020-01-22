#!/usr/bin/python3
"""Routes /python/(<text>)."""
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


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Displays C followed by the text."""
    return "C {}".format(text.replace("_", " "))


@app.route('/python/', defaults={"text": "is cool"})
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Displays Python followed by the text."""
    return "Python {}".format(text.replace("_", " "))

if __name__ == "__main__":
    app.run(host="0.0.0.0")
