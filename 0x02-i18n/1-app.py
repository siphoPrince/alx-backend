#!/usr/bin/env python3
""" Store it in a module-level variable named babel"""


from flask import Flask, render_template
from flask.ext.babel import Babel,gettext


class Config:
    """main class"""
  LANGUAGES = ["en", "fr"]
  BABEL_DEFAULT_LOCALE = "en"
  BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
  welcome_message = gettext('Welcome to Holberton')
  return render_template('index.html', welcome_message=welcome_message)


if __name__ == '__main__':
  app.run(debug=True)

