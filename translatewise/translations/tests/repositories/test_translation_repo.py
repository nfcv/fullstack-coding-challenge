from translatewise.tests.base import BaseTestCase
from translatewise import db
from translatewise.translations.models import Translation, RequestStatus
from translatewise.translations.repositories.translation_repo import TranslationRepo


class RepositoriesTestCase(BaseTestCase):

    def test_find_all(self):
        translation_one = Translation("Test 1")
        translation_two = Translation("Test 2")

        db.session.add(translation_one)
        db.session.add(translation_two)
        db.session.commit()

        all = TranslationRepo().find_all()
        expected_translations = [translation_one, translation_two]

        assert all == expected_translations
        assert len(all) == 2

    def test_find_all_ordered_by_word_count(self):
        translation_one = Translation("Test 1")
        translation_one.word_count = 3
        translation_two = Translation("Test 2")
        translation_two.word_count = 2
        translation_three = Translation("Test 3")
        translation_three.word_count = 1

        db.session.add(translation_one)
        db.session.add(translation_two)
        db.session.add(translation_three)
        db.session.commit()

        all_ordered_by_word_count = TranslationRepo().find_all_ordered_by_word_count()
        expected_translations = [translation_three, translation_two, translation_one]

        assert all_ordered_by_word_count == expected_translations

    def test_find_by_id(self):
        expected = Translation("test")
        expected.id = 3

        db.session.add(expected)
        db.session.commit()

        translation = TranslationRepo().find_by_id(3)

        assert expected == translation

    def test_find_untranslated(self):
        translated_one = Translation("test 1")
        translated_one.status = RequestStatus.TRANSLATED.value
        translated_two = Translation("Test 2")
        translated_two.status = RequestStatus.TRANSLATED.value
        not_translated = Translation("Test 3")

        db.session.add(translated_one)
        db.session.add(translated_two)
        db.session.add(not_translated)
        db.session.commit()

        expected = [not_translated]
        untranslated = TranslationRepo().find_untranslated()

        assert untranslated == expected

    def test_create(self):
        new_translation = Translation("new")

        TranslationRepo().create(new_translation)

        assert new_translation == Translation.query.filter().first()

    def test_update_status_to_pending(self):
        translation = Translation("test")

        TranslationRepo().update_status_pending(translation)

        assert translation.status == RequestStatus.PENDING.value

    def test_update_status_to_translated(self):
        translation = Translation("test")

        TranslationRepo().update_status_translated(translation, "it works")

        assert translation.status == RequestStatus.TRANSLATED.value
        assert translation.translated == "it works"
