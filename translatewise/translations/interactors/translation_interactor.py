from translatewise.translations.models import Translation
from translatewise.translations.forms import TranslationForm
from translatewise.translations.services.translation_service import TranslationService
from translatewise.translations.services.translation_queue_service import TranslationQueueService
from flask import flash


class TranslationInteractor(object):

    def __init__(self, translation_service: TranslationService, queue_service: TranslationQueueService):
        self.translation_service = translation_service
        self.queue = queue_service

    def request_translation(self, form: TranslationForm) -> Translation or None:
        if form.validate_on_submit():
            text = form.text.data
            translation = Translation(text=text)
            self.translation_service.add(translation)
            self.queue.enqueue_post_translation(translation)
            flash(f'Translation added!', 'success')
            return translation

        error = form.errors['text'][0]
        flash(error, 'danger')
        return None

    def get_translations(self) -> [Translation]:
        translations = self.translation_service.get_ordered_by_word_count()
        self.queue.enqueue_update_translations_status()
        return translations
