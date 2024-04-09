#!/usr/bin/env python3
"""get_locale function to use a user’s preferred"""


from flask import request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


SUPPORTED_LANGUAGES = ['en', 'fr']  # Your supported languages


@babel.localeselector
def get_locale():
    """Check if locale is specified in URL parameters"""
    if 'locale' in request.args:
        locale = request.args.get('locale')
        if locale in SUPPORTED_LANGUAGES:
            return locale

    if hasattr(g, 'user') and g.user and 'locale' in g.user:
        user_locale = g.user['locale']
        if user_locale in SUPPORTED_LANGUAGES:
            return user_locale

    return request.accept_languages.best_match(SUPPORTED_LANGUAGES)


@app.before_request
def before_request():
    user_id = request.args.get('login_as')
    if user_id:
        g.user = get_user(int(user_id))
    else:
        g.user = None
