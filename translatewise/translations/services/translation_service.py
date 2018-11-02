from translatewise.translations.repositories.translation_repo import TranslationRepo
from translatewise.translations.models import Translation


class TranslationService(object):

    def __init__(self, repository: TranslationRepo):
        self.repository = repository

    def get_ordered_by_word_count(self) -> [Translation]:
        return self.repository.find_all_ordered_by_word_count()

    def add(self, translation: Translation):
        self.repository.create(translation=translation)
