from translatewise.translations.models import Translation


class TranslationPresenter(object):

    def __init__(self, translation: Translation):
        self._translation = translation

    @property
    def text(self):
        return self._translation.text

    @property
    def translated_text(self):
        if not self._translation.translated:
            return ""

        return self._translation.translated

    @property
    def status(self):
        return self._translation.status.capitalize()
