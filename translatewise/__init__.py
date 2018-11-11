from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig
from redis import Redis
from rq import Queue
import rq_dashboard
from apscheduler.schedulers.background import BackgroundScheduler
import atexit
import os


db = SQLAlchemy()


def update_translations_job(app):
    from translatewise.translations.services.translation_queue_service import QueueTranslationService
    queue_service = QueueTranslationService(queue=app.task_queue)
    queue_service.enqueue_update_translations_status()


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

    if not app.debug or os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
        scheduler = BackgroundScheduler()
        scheduler.add_job(func=update_translations_job, args=[app], trigger="interval", seconds=60)
        scheduler.start()
        atexit.register(lambda: scheduler.shutdown())

    return app
