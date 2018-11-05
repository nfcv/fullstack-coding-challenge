from flask_testing import TestCase
from translatewise import create_app, db
from fakeredis import FakeRedis
from rq import Queue


class BaseTestCase(TestCase):
    def create_app(self):
        app = create_app("config.TestingConfig")
        app.redis = FakeRedis()
        app.task_queue = Queue("translatewise", connection=app.redis)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
