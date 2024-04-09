#!/usr/bin/env python3
"""l implement a way to force a particular locale """


from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


SUPPORTED_LANGUAGES = ['en', 'fr']


@babel.localeselector
def get_locale():
    """main local"""
    if 'locale' in request.args:
        locale = request.args.get('locale')

        if locale in SUPPORTED_LANGUAGES:
            return locale

    return request.accept_languages.best_match(SUPPORTED_LANGUAGES)


@app.route('/')
def index():
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
