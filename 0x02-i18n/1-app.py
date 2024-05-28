#!/usr/bin/env python3
'''
    Basic Babe setup
'''
from flask_babel import Babel
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
    return render_template('1-index.html')
