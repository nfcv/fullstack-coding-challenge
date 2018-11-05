from flask_testing import TestCase
from translatewise import create_app, db
import fakeredis


class BaseTestCase(TestCase):
    def create_app(self):
        app = create_app("config.TestingConfig")
        app.redis = fakeredis.FakeRedis()
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
