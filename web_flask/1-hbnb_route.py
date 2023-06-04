#!/usr/bin/python3
"""Write a script that starts a Flask web application."""

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Function "hello" is defined but its implementation is missing."""
    return 'Hello HBNB!'


@app.route("/", Strict_slashes=False)
def hello_hbnb():
    """Function 'hello_hbnb()' is defined but has no code inside it."""
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)