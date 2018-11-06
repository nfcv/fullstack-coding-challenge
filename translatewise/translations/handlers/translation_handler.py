from translatewise.translations.models import Translation
from translatewise.translations.repositories.translation_repo import TranslationRepo
from translatewise.translations.services.create_translation_service import CreateTranslationService
from translatewise.translations.services.translation_queue_service import TranslationQueueService
from translatewise.translations.services.get_translations_service import GetTranslationsService
from translatewise.translations.forms import TranslationForm
from flask import flash
from rq import Queue


class TranslationHandler(object):

    def __init__(self, repository: TranslationRepo, queue: Queue):
        self.repository = repository
        self.queue = queue

    def request_translation(self, form: TranslationForm):
        if form.validate_on_submit():
            text = form.text.data
            translation = Translation(text=text)
            create_service = CreateTranslationService(repository=self.repository)
            create_service.create(translation)
            TranslationQueueService(self.queue).enqueue_post_translation(translation)
            flash(f'Translation added!', 'success')
            return

        error = form.errors['text'][0]
        flash(error, 'danger')
        return

    def get_translations_ordered_by_word_count(self) -> [Translation]:
        translations = GetTranslationsService(repository=self.repository).ordered_by_word_count()
        TranslationQueueService(self.queue).enqueue_update_translations_status()
        return translations
