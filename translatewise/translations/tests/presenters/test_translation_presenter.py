from translatewise.translations.models import Translation
from translatewise.translations.presenters.translation_presenter import TranslationPresenter
from unittest import TestCase


class TranslationPresenterTestCase(TestCase):

    def setUp(self):
        self.translation = Translation(text="Hello")
        self.translation.translated = "Hola"
        self.translation.status = "REQUESTED"

    def test_text(self):
        self.presenter = TranslationPresenter(self.translation)

        assert self.presenter.text == "Hello"

    def test_translated_text_isTranslatedNone(self):
        self.translation.translated = None
        self.presenter = TranslationPresenter(self.translation)

        assert self.presenter.translated_text == ""

    def test_status(self):
        self.translation.translated = None
        self.presenter = TranslationPresenter(self.translation)

        assert self.presenter.status == "Requested"
