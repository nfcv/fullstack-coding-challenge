from translatewise.translations.repositories.translation_repo import TranslationRepo
from translatewise.translations.models import Translation


class CreateTranslationService(object):

    def __init__(self, text, text_lang_code="en_UK", translated_lang_code="es_ES"):
        self.text = text
        self.original_lang_code = text_lang_code
        self.translating_lang_code = translated_lang_code

    def call(self):
        translation = Translation(self.text,
                                  self.original_lang_code,
                                  self.translating_lang_code)

        return TranslationRepo.create_translation(translation)
