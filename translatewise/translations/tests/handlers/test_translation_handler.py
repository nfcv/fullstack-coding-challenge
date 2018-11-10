from translatewise.translations.handlers.translation_handler import TranslationHandler
from unittest.mock import MagicMock, Mock
from unittest import TestCase, mock


class TranslationHandlerTestCase(TestCase):

    def test_get_translations_ordered_by_word_count(self):
        handler = TranslationHandler(repository=Mock(), queue=Mock())
        handler.get_translations_service = Mock()

        handler.get_translations_ordered_by_word_count()

        handler.get_translations_service.ordered_by_word_count.assert_called_with()

    @mock.patch('translatewise.translations.handlers.translation_handler.flash')
    def test_request_translation_when_isValidForm(self, mocked_flask):
        handler = TranslationHandler(repository=Mock(), queue=Mock())
        handler.create_translation_service = Mock()
        handler.queue_translation_service = Mock()
        form = Mock()
        form.validate_on_submit = MagicMock(return_value=True)

        handler.request_translation(form=form)

        handler.create_translation_service.create.assert_called()
        handler.queue_translation_service.enqueue_post_translation.assert_called()
        mocked_flask.assert_called_with(f'Translation added!', 'success')

    @mock.patch('translatewise.translations.handlers.translation_handler.flash')
    def test_request_translation_when_isInvalidForm(self, mocked_flask):
        handler = TranslationHandler(repository=Mock(), queue=Mock())
        handler.create_translation_service = Mock()
        handler.queue_translation_service = Mock()
        form = Mock()
        form.validate_on_submit = MagicMock(return_value=False)
        form.errors = {"text": ["There is an error."]}

        handler.request_translation(form=form)

        assert not handler.create_translation_service.create.called
        assert not handler.queue_translation_service.enqueue_post_translation.called
        mocked_flask.assert_called_with("There is an error.", 'danger')
