from translatewise.translations.models import Translation
from translatewise.translations.repositories.translation_repo import TranslationRepo
from translatewise.translations.services.create_translation_service import CreateTranslationService
from translatewise.translations.services.translation_queue_service import QueueTranslationService
from translatewise.translations.services.get_translations_service import GetTranslationsService
from translatewise.translations.forms import TranslationForm
from flask import flash
from rq import Queue


class TranslationHandler(object):

    def __init__(self, repository: TranslationRepo, queue: Queue):
        self.create_translation_service = CreateTranslationService(repository)
        self.queue_translation_service = QueueTranslationService(queue)
        self.get_translations_service = GetTranslationsService(repository)

    def request_translation(self, form: TranslationForm):
        if form.validate_on_submit():
            text = form.text.data
            translation = Translation(text=text)
            self.create_translation_service.create(translation)
            self.queue_translation_service.enqueue_post_translation(translation)
            flash(f'Translation added!', 'success')
            return

        error = form.errors['text'][0]
        flash(error, 'danger')
        return

    def get_translations_ordered_by_word_count(self) -> [Translation]:
        translations = self.get_translations_service.ordered_by_word_count()
        self.queue_translation_service.enqueue_update_translations_status()
        return translations
