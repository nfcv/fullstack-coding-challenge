from translatewise.translations.repositories.translation_repo import TranslationRepo
from translatewise.translations.models import Translation


class AddTranslationService(object):

    def __init__(self, text: str, text_lang_code="en", translated_lang_code="es"):
        self.text = text
        self.original_lang_code = text_lang_code
        self.translating_lang_code = translated_lang_code

    def call(self) -> Translation:
        translation = Translation(self.text,
                                  self.original_lang_code,
                                  self.translating_lang_code)

        return TranslationRepo.create_translation(translation)
