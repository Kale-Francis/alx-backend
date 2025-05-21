#!/usr/bin/env python3
"""Flask app with timezone selection"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext
import pytz

app = Flask(__name__)

class Config:
    """Configuration for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

@babel.localeselector
def get_locale():
    """Select locale with priority: URL parameter, user settings, request headers"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@babel.timezoneselector
def get_timezone():
    """Select timezone with priority: URL parameter, user settings, default"""
    timezone = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    if g.user and g.user['timezone']:
        try:
            pytz.timezone(g.user['timezone'])
            return g.user['timezone']
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    return 'UTC'

def get_user():
    """Return user dictionary or None"""
    user_id = request.args.get('login_as')
    if user_id and user_id.isdigit():
        return users.get(int(user_id))
    return None

@app.before_request
def before_request():
    """Set user as global before each request"""
    g.user = get_user()

@app.route('/')
def index():
    """Render the index page with translations and user info"""
    return render_template('7-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
