from translatewise.translations.services.get_all_translations_service import GetAllTranslationsService
from translatewise.translations.services.add_translation_service import AddTranslationService
from translatewise.translations.services.unbabel_api import UnbabelApi
from translatewise.translations.models import Translation

unbabel_api = UnbabelApi()


class TranslationInteractor(object):

    @classmethod
    def get_all_translations(cls) -> [Translation]:
        return GetAllTranslationsService().call()

    @classmethod
    def add_translation(cls, text: str) -> Translation:
        translation = AddTranslationService(text).call()
        unbabel_api.post_translation(translation.text,
                                     translation.id,
                                     translation.text_lang_code,
                                     translation.translated_lang_code)
        return translation
