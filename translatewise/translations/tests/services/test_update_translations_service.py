from translatewise.translations.models import Translation
from translatewise.translations.services.update_translations_service import UpdateTranslationsService
from unittest.mock import MagicMock, Mock, call
from unittest import TestCase


class UpdateTranslationsServiceTestCase(TestCase):

    def setUp(self):
        self.translation_one = Translation("Test 1")
        self.translation_one.id = 1
        self.translation_two = Translation("Test 2")
        self.translation_two.id = 2
        self.translations = [self.translation_one, self.translation_two]

        self.repo = Mock()
        self.repo.find_untranslated = MagicMock(return_value=self.translations)

    def tearDown(self):
        self.repo = None
        self.translation_one = None
        self.translation_two = None
        self.translations = None

    def test_update_translations_calls_fetch_translation(self):
        self.api = Mock()
        self.api.fetch_translation = MagicMock(return_value={"status": "translating"})

        UpdateTranslationsService(self.api, self.repo).update_translations()

        calls = [call(uid=1), call(uid=2)]
        self.api.fetch_translation.assert_has_calls(calls)

    def test_update_translations_StatusIsPending(self):
        self.api = Mock()
        self.api.fetch_translation = MagicMock(return_value={"status": "translating"})

        UpdateTranslationsService(self.api, self.repo).update_translations()

        calls = [call(translation=self.translation_one), call(translation=self.translation_two)]
        self.repo.update_status_pending.assert_has_calls(calls)

    def test_update_translations_StatusIsCompleted(self):
        self.api = Mock()
        self.api.fetch_translation = MagicMock(return_value={"status": "completed", "translatedText": "worked"})

        UpdateTranslationsService(self.api, self.repo).update_translations()

        calls = [call(translation=self.translation_one, translated_text="worked"),
                 call(translation=self.translation_two, translated_text="worked")]
        self.repo.update_status_translated.assert_has_calls(calls)
