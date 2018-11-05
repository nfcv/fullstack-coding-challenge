from translatewise.tests.base import BaseTestCase
from translatewise import db
from translatewise.translations.models import Translation
from translatewise.translations.repositories.translation_repo import TranslationRepo


class RepositoriesTestCase(BaseTestCase):

    def setUp(self):
        super.setup()
        self.repo = TranslationRepo()  # system under test

    def test_find_all(self):
        translation_one = Translation("Test 1")
        translation_two = Translation("Test 2")
        db.session.add(translation_one)
        db.session.add(translation_two)

        all = self.repo.find_all()
        expected_translations = [translation_one, translation_two]

        assert all == expected_translations
        assert len(all) == 2
