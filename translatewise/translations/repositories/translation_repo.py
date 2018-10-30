from translatewise.translations.models import Translation, RequestStatus
from translatewise import db


class TranslationRepo(object):

    @classmethod
    def find_all(cls) -> [Translation]:
        return Translation.query.filter().all()

    @classmethod
    def find_by_id(cls, id: int)-> Translation:
        return Translation.query.get(id)

    @classmethod
    def find_untranslated(cls) -> [Translation]:
        return Translation.query.filter(Translation.status != RequestStatus.TRANSLATED.value).all()

    @classmethod
    def update_status(cls, translation: Translation, status: RequestStatus) -> Translation:
        translation.status = status.value
        db.session.commit()
        return translation

    @classmethod
    def create(cls, translation: Translation) -> Translation:
        db.session.add(translation)
        db.session.commit()
        return translation
