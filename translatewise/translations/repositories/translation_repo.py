from translatewise.translations.models import Translation


class TranslationRepo(object):

    @classmethod
    def find_all(cls):
        return Translation.query.filter().all()
