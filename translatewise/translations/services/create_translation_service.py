from translatewise.translations.repositories.translation_repo import TranslationRepo
from translatewise.translations.models import Translation


class CreateTranslationService(object):

    def __init__(self, repository: TranslationRepo):
        self.repository = repository

    def create(self, translation: Translation) -> Translation:
        return self.repository.create(translation=translation)
