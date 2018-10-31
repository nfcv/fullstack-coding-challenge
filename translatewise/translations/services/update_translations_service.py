from translatewise.translations.repositories.translation_repo import TranslationRepo
from translatewise.translations.models import Translation
from translatewise.translations.services.unbabel_api import UnbabelApi
from translatewise import db


class UpdateTranslationsService(object):

    def __init__(self, api=UnbabelApi()):
        self.api = api

    def call(self) -> [Translation]:
        translations = TranslationRepo.find_untranslated()

        for t in translations:
            result = self.api.fetch_translation(uid=t.id)
            print(result)

            if not result:
                continue

            status = result["status"]
            if status == "translating":
                TranslationRepo.update_status_pending(translation=t)
            elif status == "completed":
                translated_text = result["translatedText"]
                if translated_text:
                    TranslationRepo.update_status_translated(
                        translation=t,
                        translated_text=translated_text
                    )

        if translations:
            db.session.commit()

        return translations
