#!/usr/bin/env python3
'''
    Get local decorator
'''
import babel
from flask import request
from flask_babel import Babel


@babel.localselector
def getlocale():
    return request.accept_languages.best_match(['en', 'es', 'de'])
