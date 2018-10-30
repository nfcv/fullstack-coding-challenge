from translatewise.translations.repositories.translation_repo import TranslationRepo
from translatewise.translations.models import RequestStatus
from translatewise.translations.models import Translation


class UpdateTranslationStatusService(object):

    def __init__(self, translation: Translation, status: RequestStatus):
        self.translation = translation
        self.status = status

    def call(self) -> Translation:
        return TranslationRepo.update_status(translation=self.translation, status=self.status)
