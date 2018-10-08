from translatewise.translations.services.get_all_translations_service import GetAllTranslationsService


class TranslationInteractor(object):

    @classmethod
    def get_all_translations(cls):
        return GetAllTranslationsService().call()
