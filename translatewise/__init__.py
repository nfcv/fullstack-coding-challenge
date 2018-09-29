import os
from os.path import join, dirname
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

APP_CONFIG = os.environ.get("APP_CONFIG")

app = Flask(__name__)
app.config.from_object(APP_CONFIG)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from translatewise import routes