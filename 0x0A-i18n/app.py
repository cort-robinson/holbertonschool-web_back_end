#!/usr/bin/env python3
"""Basic flask app"""
from datetime import datetime
from typing import Optional

from flask import Flask, g, render_template, request
from flask_babel import Babel, format_datetime
from pytz import UnknownTimeZoneError, timezone

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """Babel config class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """Get locale"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    if g.user:
        user_locale = g.user.get('locale')
        if user_locale and user_locale in app.config['LANGUAGES']:
            return user_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """Get timezone"""
    timezone_str = request.args.get('timezone')
    if timezone_str:
        try:
            timezone(timezone_str)
            return timezone
        except UnknownTimeZoneError:
            pass
    if g.user:
        user_timezone = g.user.get('timezone')
        if user_timezone:
            try:
                timezone(user_timezone)
                return user_timezone
            except UnknownTimeZoneError:
                pass
    return app.config['BABEL_DEFAULT_TIMEZONE']


def get_user(login_as: int) -> Optional[dict]:
    """Get user"""
    if login_as:
        return users.get(login_as)


@app.before_request
def before_request():
    """Before requests"""
    user = request.args.get('login_as')
    if user:
        user = int(user)
    g.user = get_user(user)


@app.route('/')
def index() -> str:
    """Index route"""
    return render_template('index.html',
                           current_time=format_datetime(datetime.now()))


if __name__ == '__main__':
    app.run()
