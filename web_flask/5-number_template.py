#!/usr/bin/python3

"""Script that starts a Flask web application."""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """The function "hello" returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """The function "hbnb" returns HBNB."""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """The function "display_c" returns text."""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text='is cool'):
    """The function "display_python" returns text."""
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """The function "display_number" returns integer number."""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_template(n):
    """
    The function "display_template"
    display a HTML page only if n is an integer.
    """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)