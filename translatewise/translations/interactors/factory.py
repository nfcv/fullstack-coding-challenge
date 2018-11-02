from translatewise.translations.interactors.translation_interactor import TranslationInteractor
from translatewise.translations.repositories.translation_repo import TranslationRepo
from translatewise.translations.services.translation_queue_service import TranslationQueueService
from translatewise.translations.services.translation_service import TranslationService
from flask import current_app


class TranslationInteractorFactory(object):

    @classmethod
    def create(cls) -> TranslationInteractor:
        repo = TranslationRepo()
        queue = current_app.task_queue
        queue_service = TranslationQueueService(queue=queue)
        translation_service = TranslationService(repository=repo)

        interactor = TranslationInteractor(
            translation_service=translation_service,
            queue_service=queue_service
        )

        return interactor
