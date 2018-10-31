from translatewise.translations.services.unbabel_api import UnbabelApi
from translatewise.translations.models import Translation


class PostTranslationService(object):

    def __init__(self, translation: Translation, api=UnbabelApi()):
        self.api = api
        self.translation = translation

    def call(self):
        return self.api.post_translation(
            self.translation.text,
            self.translation.id,
            self.translation.text_lang_code,
            self.translation.translated_lang_code
        )
