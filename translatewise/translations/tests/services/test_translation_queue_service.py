from translatewise.translations.models import Translation
from translatewise.translations.services.translation_queue_service import TranslationQueueService
from unittest.mock import Mock
from unittest import TestCase


class TranslationQueueServiceTestCase(TestCase):

    def test_enqueue_post_translation(self):
        queue = Mock()
        translation = Translation("test")

        TranslationQueueService(queue=queue).enqueue_post_translation(translation)

        queue.enqueue.assert_called_with('translatewise.translations.worker.post_translation',
                                         translation,
                                         result_ttl=60000)

    def test_enqueue_update_translations_status(self):
        queue = Mock()

        TranslationQueueService(queue=queue).enqueue_update_translations_status()

        queue.enqueue.assert_called_with('translatewise.translations.worker.update_translations_status',
                                         result_ttl=60000)