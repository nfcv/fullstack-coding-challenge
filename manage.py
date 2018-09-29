import os
from os.path import join, dirname
from dotenv import load_dotenv
from translatewise import create_app
from flask_script import Manager

APP_CONFIG = os.environ.get("APP_CONFIG")

app = create_app()

manager = Manager(app)

if __name__ == '__main__':
    manager.run()