from translatewise.translations.models import Translation, RequestStatus
from translatewise import db


class TranslationRepo(object):

    @classmethod
    def find_all_ordered_by_word_count(cls) -> [Translation]:
        return Translation.query.filter().order_by(Translation.word_count).all()

    @classmethod
    def find_by_id(cls, id: int)-> Translation:
        return Translation.query.get(id)

    @classmethod
    def find_untranslated(cls) -> [Translation]:
        return Translation.query.filter(Translation.status != RequestStatus.TRANSLATED.value).all()

    @classmethod
    def update_status_pending(cls, translation: Translation):
        translation.status = RequestStatus.PENDING.value
        return translation

    @classmethod
    def update_status_translated(cls, translation: Translation, translated_text: str) -> Translation:
        translation.status = RequestStatus.TRANSLATED.value
        translation.translated = translated_text
        translation.word_count = len(translated_text)
        return translation

    @classmethod
    def create(cls, translation: Translation) -> Translation:
        db.session.add(translation)
        db.session.commit()
        return translation
