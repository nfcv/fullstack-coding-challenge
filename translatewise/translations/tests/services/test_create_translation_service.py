from translatewise.translations.models import Translation
from translatewise.translations.repositories.translation_repo import TranslationRepo
from translatewise.translations.services.create_translation_service import CreateTranslationService
from unittest.mock import MagicMock
from unittest import TestCase


class CreateTranslationServiceTestCase(TestCase):

    def test_create(self):
        translation = Translation("test")
        repo = TranslationRepo()
        repo.create = MagicMock(return_value=translation)

        service = CreateTranslationService(repository=repo)

        assert service.create(translation) == translation
