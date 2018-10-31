from translatewise.translations.repositories.translation_repo import TranslationRepo


class GetAllTranslationsService(object):

    def call(self):
        return TranslationRepo.find_all_ordered_by_word_count()
