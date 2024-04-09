!#/usr/bin/env python3
""" mock a database user table. """


from flask import Flask, render_template, g, request
from flask_babel import Babel, _
import pytz


app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user(user_id):
    """get user"""
    return users.get(user_id)


@app.before_request
def before_request():
    """before"""
    user_id = request.args.get('login_as')
    if user_id:
        g.user = get_user(int(user_id))
    else:
        g.user = None

@app.route('/')
def index():
    return render_template('5-index.html')

if __name__ == '__main__':
    app.run(debug=True)
