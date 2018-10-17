from translatewise.translations.models import Translation
from translatewise import db

class TranslationRepo(object):

    @classmethod
    def find_all(cls):
        return Translation.query.filter().all()

    @classmethod
    def create_translation(cls, translation):
        db.session.add(translation)
        db.session.commit()
        return translation
