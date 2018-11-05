from translatewise.translations.models import Translation
from translatewise.translations.unbabel_api import UnbabelApi


class PostTranslationService(object):

    def __init__(self, api: UnbabelApi):
        self.api = api

    def post_translation(self, translation: Translation):
        return self.api.post_translation(
            text=translation.text,
            uid=translation.id,
            source_language=translation.text_lang_code,
            target_language=translation.translated_lang_code
        )
