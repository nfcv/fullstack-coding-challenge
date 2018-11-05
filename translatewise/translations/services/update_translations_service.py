from translatewise.translations.repositories.translation_repo import TranslationRepo
from translatewise.translations.models import Translation
from translatewise.translations.unbabel_api import UnbabelApi


class UpdateTranslationsService(object):

    def __init__(self, api: UnbabelApi, repository: TranslationRepo):
        self.api = api
        self.repository = repository

    def update_translations(self) -> [Translation]:
        translations = self.repository.find_untranslated()

        for t in translations:
            result = self.api.fetch_translation(uid=t.id)

            if not result:
                continue

            status = result["status"]
            if status == "translating":
                self.repository.update_status_pending(translation=t)
            elif status == "completed":
                translated_text = result["translatedText"]
                if translated_text:
                    self.repository.update_status_translated(
                        translation=t,
                        translated_text=translated_text
                    )

        return translations
