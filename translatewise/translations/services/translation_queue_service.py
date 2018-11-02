from translatewise.translations.models import Translation
from rq import Queue
from rq.job import Job


class TranslationQueueService(object):

    def __init__(self, queue: Queue):
        self.queue = queue

    def enqueue_post_translation(self, translation: Translation) -> Job:
        return self.queue.enqueue(
            'translatewise.translations.worker.post_translation',
            translation,
            result_ttl=60000
        )

    def enqueue_update_translations_status(self) -> Job:
        return self.queue.enqueue(
            'translatewise.translations.worker.update_translations_status',
            result_ttl=60000
        )
