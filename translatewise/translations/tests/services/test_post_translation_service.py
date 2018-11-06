from translatewise.translations.models import Translation
from translatewise.translations.services.post_translation_service import PostTranslationService
from translatewise.translations.unbabel_api import UnbabelApi
from unittest.mock import MagicMock
from unittest import TestCase


class PostTranslationServiceTestCase(TestCase):

    def test_post_translation_calls_external_service(self):
        api = UnbabelApi()
        api.post_translation = MagicMock(return_value="")

        translation = Translation("test")

        PostTranslationService(api=api).post_translation(translation)

        api.post_translation.assert_called_with(text=translation.text,
                                                source_language=translation.text_lang_code,
                                                target_language=translation.translated_lang_code,
                                                uid=translation.id)
