from translatewise.translations.repositories.translation_repo import TranslationRepo
from translatewise.translations.models import RequestStatus
from translatewise.translations.models import Translation
from translatewise import db


class UpdateTranslationStatusService(object):

    def __init__(self, translation_id: int, status: RequestStatus):
        self.id = translation_id
        self.status = status

    def call(self) -> Translation:
        translation = TranslationRepo.find_by_id(self.id)
        translation.status = self.status.value
        db.session.commit()
        return translation
