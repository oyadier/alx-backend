#!/usr/bin/env python3
'''
    Get local decorator
'''

import babel
from babel import Babel
from flask import request
from flask import Flask, render_template


app = Flask(__name__)
babel = Babel(app=app)


class Config():
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAUL_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def home():
    '''
        A webpage with babel configuration
    '''
    return render_template('3-index.html')


@babel.localeselector
def get_locale() -> str:
    '''
        Getting local of a country
    '''
    return request.accept_languages.best_match(Config.LANGUAGES)
