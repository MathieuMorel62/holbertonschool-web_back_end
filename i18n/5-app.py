#!/usr/bin/env python3
""" Basic Babel setup """

from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"}
}


class Config:
    """ Config class """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


def get_user():
    """ Get user """
    user_id = request.args.get('login_as', None)
    if user_id:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """ Before request """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """ Get locale """
    user = getattr(g, 'user', None)
    if user:
        locale = user.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


# babel.init_app(app, locale_selector=get_locale)


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """ Index """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
