from translatewise.translations.models import Translation
from translatewise.translations.repositories.translation_repo import TranslationRepo
from translatewise.translations.services.get_translations_service import GetTranslationsService
from unittest.mock import MagicMock
from unittest import TestCase


class GetTranslationServiceTestCase(TestCase):

    def test_translations_ordered_by_word_count(self):
        expected = [Translation("test"), Translation("Other"), Translation("test2")]
        repo = TranslationRepo()
        repo.find_all_ordered_by_word_count = MagicMock(return_value=expected)

        service = GetTranslationsService(repository=repo)

        assert service.ordered_by_word_count() == expected
