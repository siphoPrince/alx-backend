from flask import Flask, render_template
from flask.ext.babel import Babel,gettext

# Create a configuration class
class Config:
  LANGUAGES = ["en", "fr"]  # Supported languages
  BABEL_DEFAULT_LOCALE = "en"  # Default locale (English)
  BABEL_DEFAULT_TIMEZONE = "UTC"  # Default timezone

# Initialize Flask app and Babel object
app = Flask(__name__)
app.config.from_object(Config)  # Use Config class for configuration
babel = Babel(app)

@app.route('/')
def index():
  welcome_message = gettext('Welcome to Holberton')  # Mark for translation
  return render_template('index.html', welcome_message=welcome_message)

if __name__ == '__main__':
  app.run(debug=True)

