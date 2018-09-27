import os
from os.path import join, dirname
from dotenv import load_dotenv
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

APP_CONFIG = os.environ.get("APP_CONFIG")

app = Flask(__name__)
app.config.from_object(APP_CONFIG)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Translation

translations = [
    {
        'en_UK': 'Hello',
        'es_ES': 'Holla',
        'status': 'requested'
    },
    {
        'en_UK': 'How you doing?',
        'es_ES': 'Como estas?',
        'status': 'pending'
    },
    {
        'en_UK': 'How',
        'es_ES': 'Como',
        'status': 'translated'
    }
]

@app.route("/")
def index():
    return render_template("index.html", translations=translations)

if __name__ == '__main__':
    app.run()