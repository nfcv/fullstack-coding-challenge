from translatewise import create_app
from translatewise.translations.models import Translation, RequestStatus
from translatewise.translations.services.get_untranslated_translations_service import GetUntranslatedTranslationsService
from translatewise.translations.services.update_translation_status_service import UpdateTranslationStatusService
from translatewise.translations.services.unbabel_api import UnbabelApi
from rq import get_current_job

app = create_app()
app.app_context().push()

unbabel_api = UnbabelApi()

# TODO: Count words and order by words

def update_translations_status():
    job = get_current_job()
    print(f"Job id: {job.get_id()}")
    translations = GetUntranslatedTranslationsService().call()
    for t in translations:
        result = unbabel_api.fetch_translation(uid=t.id)
        print(result)
        if not result:
            continue
        if result["status"] == "translating":
            UpdateTranslationStatusService(translation=t, status=RequestStatus.PENDING).call()
        elif result["status"] == "completed":
            UpdateTranslationStatusService(translation=t, status=RequestStatus.TRANSLATED).call()


def post_translation(translation: Translation):
    try:
        result = unbabel_api.post_translation(
          translation.text,
          translation.id,
          translation.text_lang_code,
          translation.translated_lang_code
        )
        print(result)
        uid = result["uid"]
        print(f"UID: {uid}")
    except Exception as e:
        job = get_current_job()
        print(f"Exception:{e}")
        print(f"Job failed with ID: {job.get_id()}")
