import os
from translatewise import create_app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

APP_CONFIG = os.environ.get("APP_CONFIG")

app = create_app()
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
