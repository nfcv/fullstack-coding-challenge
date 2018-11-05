from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig
from redis import Redis
from rq import Queue
import rq_dashboard

db = SQLAlchemy()


def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(rq_dashboard.default_settings)
    app.config.from_object(config_class)
    app.register_blueprint(rq_dashboard.blueprint, url_prefix="/rq")
    app.redis = Redis.from_url(app.config['REDIS_URL'])
    app.task_queue = Queue('translatewise', connection=app.redis)

    db.init_app(app)

    from translatewise.translations.views import translations
    app.register_blueprint(translations)

    return app
