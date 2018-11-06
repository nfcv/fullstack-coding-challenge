import os
import unittest
import coverage

from translatewise import create_app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

APP_CONFIG = os.environ.get("APP_CONFIG")

app = create_app(APP_CONFIG)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Runs tests without coverage."""
    tests = unittest.TestLoader().discover('.')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.command
def cov():
    """Runs tests with coverage."""
    cov = coverage.coverage(branch=True, include='translatewise/*')
    cov.start()
    tests = unittest.TestLoader().discover('.')
    unittest.TextTestRunner(verbosity=2).run(tests)
    cov.stop()
    cov.save()
    print("Test Coverage: ")
    cov.report()
    basedir = os.path.abspath(os.path.dirname(__file__))
    covdir = os.path.join(basedir, 'htmlcov')
    cov.html_report(directory=covdir)
    cov.erase()


if __name__ == '__main__':
    manager.run()
