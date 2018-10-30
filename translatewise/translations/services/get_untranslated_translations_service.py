from translatewise.translations.repositories.translation_repo import TranslationRepo


class GetUntranslatedTranslationsService(object):

    def call(self):
        return TranslationRepo.find_untranslated()
