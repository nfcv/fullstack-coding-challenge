from translatewise.translations.models import Translation


class TranslationListViewModel(object):

    def __init__(self, translation: Translation):
        self.text = translation.text
        self.translated_text = translation.translated
        self.status = translation.status.capitalize()
