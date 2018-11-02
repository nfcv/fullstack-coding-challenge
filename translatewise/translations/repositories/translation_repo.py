from translatewise.translations.models import Translation, RequestStatus
from translatewise import db


class TranslationRepo(object):

    def find_all(self) -> [Translation]:
        return Translation.query.filter().all()

    def find_all_ordered_by_word_count(self) -> [Translation]:
        return Translation.query.filter().order_by(Translation.word_count).all()

    def find_by_id(self, id: int)-> Translation:
        return Translation.query.get(id)

    def find_untranslated(self) -> [Translation]:
        return Translation.query.filter(Translation.status != RequestStatus.TRANSLATED.value).all()

    def update_status_pending(self, translation: Translation):
        translation.status = RequestStatus.PENDING.value
        db.session.commit()
        return translation

    def update_status_translated(self, translation: Translation, translated_text: str) -> Translation:
        translation.status = RequestStatus.TRANSLATED.value
        translation.translated = translated_text
        translation.word_count = len(translated_text)
        db.session.commit()
        return translation

    def create(self, translation: Translation) -> Translation:
        db.session.add(translation)
        db.session.commit()
        return translation
