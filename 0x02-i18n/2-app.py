#!/usr/bin/env python3

from flask import Flask, render_template
from flask_babel import Babel

babel = Babel(__name__)

class Config:
    LANGUAGES = ["en", "fr"]

app = Flask(__name__, config=Config)
babel.init_app(app, locae_selector=get_locale)

@app.route("/")
def index():
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)
