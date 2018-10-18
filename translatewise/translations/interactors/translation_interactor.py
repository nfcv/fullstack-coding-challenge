from translatewise.translations.services.get_all_translations_service import GetAllTranslationsService
from translatewise.translations.services.create_translation_service import CreateTranslationService
from translatewise.translations.models import Translation


class TranslationInteractor(object):

    @classmethod
    def get_all_translations(cls) -> [Translation]:
        return GetAllTranslationsService().call()

    @classmethod
    def add_translation(cls, text: str) -> Translation:
        return CreateTranslationService(text).call()
