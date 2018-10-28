from translatewise.translations.services.get_all_translations_service import GetAllTranslationsService
from translatewise.translations.services.add_translation_service import AddTranslationService
from translatewise.translations.models import Translation
from flask import current_app


class TranslationInteractor(object):

    @classmethod
    def get_all_translations(cls) -> [Translation]:
        return GetAllTranslationsService().call()

    @classmethod
    def add_translation(cls, text: str) -> Translation:
        translation = AddTranslationService(text).call()
        current_app.task_queue.enqueue(
            'translatewise.translations.worker.post_translation',
            translation,
            result_ttl=60000
        )
        return translation
