#!/usr/bin/env python3
"""Flask app with forced locale via URL parameter"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext

app = Flask(__name__)

class Config:
    """Configuration for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)
babel = Babel(app)

@babel.localeselector
def get_locale():
    """Select locale from URL parameter or request headers"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    """Render the index page with translations"""
    return render_template('4-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
