#!/usr/bin/env python3
'''
    Get local decorator
'''

import babel
from flask import request


@babel.localeselector
def get_locale():
    '''
        Getting local of a country
    '''
    return request.accept_languages.best_match(['en', 'es', 'de'])
