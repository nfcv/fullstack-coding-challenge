from translatewise.translations.services.get_all_translations_service import GetAllTranslationsService
from translatewise.translations.services.add_translation_service import AddTranslationService
from translatewise.translations.models import Translation
from translatewise.translations.forms import TranslationForm
from flask import current_app


class TranslationInteractor(object):

    @classmethod
    def submit(cls, form: TranslationForm) -> Translation or None:
        if form.validate_on_submit():
            text = form.text.data
            translation = AddTranslationService(text).call()
            current_app.task_queue.enqueue(
                'translatewise.translations.worker.post_translation',
                translation,
                result_ttl=60000
            )
            return translation

        return None

    @classmethod
    def translations(cls) -> [Translation]:
        translations = GetAllTranslationsService().call()
        current_app.task_queue.enqueue(
            'translatewise.translations.worker.update_translations_status',
            result_ttl=60000
        )
        return translations
