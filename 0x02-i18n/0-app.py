#!/usr/bin/env python3
"""Welcome to Holberton"""


from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """ sends a GET /
    Return:
        Hello world
    """
    return render_template('index.html')


if __name__ == '__main__':
  app.run(host="0.0.0.0", port="5000")
