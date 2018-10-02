import unittest
from flask_testing import TestCase
from translatewise import create_app, db


class BaseTestCase(TestCase):
    def create_app(self):
        return create_app("config.TestingConfig")

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


if __name__ == '__main__':
    unittest.main()
