from translatewise.tests.base import BaseTestCase
from translatewise.translations.models import Translation


class ModelsTestCase(BaseTestCase):

    def test_init(self):
        model = Translation(text="Teste", text_lang_code="pt", translated_lang_code="en")
        assert model.text == "Teste"
        assert model.text_lang_code == "pt"
        assert model.translated_lang_code == "en"
        assert model.status == "REQUESTED"

    def test_init_default_args(self):
        model = Translation("Testing")

        assert model.text == "Testing"
        assert model.text_lang_code == "en"
        assert model.translated_lang_code == "es"
        assert model.status == "REQUESTED"
