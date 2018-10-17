from translatewise.translations.services.get_all_translations_service import GetAllTranslationsService
from translatewise.translations.services.create_translation_service import CreateTranslationService


class TranslationInteractor(object):

    @classmethod
    def get_all_translations(cls):
        return GetAllTranslationsService().call()

    @classmethod
    def add_translation(cls, text):
        return CreateTranslationService(text).call()
