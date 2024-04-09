#!/usr/bin/env python3
"""making main file"""


from flask import Flask, render_template, request
from flask.ext.babel import Babel, gettext

# Create a configuration class
class Config:
  LANGUAGES = ["en", "fr"]  # Supported languages
  BABEL_DEFAULT_LOCALE = "en"  # Default locale (English)
  BABEL_DEFAULT_TIMEZONE = "UTC"  # Default timezone

# Initialize Flask app and Babel object
app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

@babel.localeselector
def get_locale():
  return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
  welcome_message = gettext('Welcome to Holberton')  # Mark for translation
  return render_template('2-index.html', welcome_message=welcome_message)

if __name__ == '__main__':
  app.run(debug=True)

