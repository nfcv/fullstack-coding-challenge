from translatewise.translations.models import Translation
from translatewise import db


class TranslationRepo(object):

    @classmethod
    def find_all(cls):
        return Translation.query.filter().all()

    @classmethod
    def find_by_id(cls, id: int):
        return Translation.query.get(id)

    @classmethod
    def create_translation(cls, translation: Translation) -> Translation:
        db.session.add(translation)
        db.session.commit()
        return translation
