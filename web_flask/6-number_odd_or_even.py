#!/usr/bin/python3
"""Routes /number_odd_or_even/<int:n>."""
from flask import Flask, render_template
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


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """Displays n is a number."""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_n(n):
    """Displays number template."""
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even_n(n):
    """Displays n is even|odd."""
    return render_template("6-number_odd_or_even.html", n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
