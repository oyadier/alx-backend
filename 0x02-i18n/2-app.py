#!/usr/bin/env python3
'''
    Get local decorator
'''

import babel
from babel import Babel
from flask import request
from flask import Flask, render_template

class Config():
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAUL_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app=app)


@app.route('/')
def home():
    '''
        A webpage with babel configuration
    '''
    return render_template('2-index.html')

@babel.localeselector
def get_locale():
    '''
        Getting local of a country
    '''
    return request.accept_languages.best_match(Config.LANGUAGES)
