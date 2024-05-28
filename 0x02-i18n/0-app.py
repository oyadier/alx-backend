#!/usr/bin/env python3
"""Flask Babel project"""


from flask import (Flask, render_template)

app = Flask(__name__)


@app.route("/")
def app_title():
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host='127.0.0.0', port=5000, debug=True)
