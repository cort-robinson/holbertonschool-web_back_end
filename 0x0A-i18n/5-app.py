#!/usr/bin/env python3
"""Basic flask app"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Optional

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Babel config class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """Get locale"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user(login_as: str) -> Optional[dict]:
    """Get user"""
    if login_as:
        return users.get(login_as)


@app.before_request
def before_request():
    """Before requests"""
    user = get_user(request.args.get('login_as'))
    if user:
        g.user = user


@app.route('/')
def index() -> str:
    """Index route"""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
