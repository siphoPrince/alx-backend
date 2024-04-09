#!/usr/bin/env python3
""" Store it in a module-level variable named babel"""


from flask import Flask
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


babel = Babel(app)
app.config.from_object(Config)
