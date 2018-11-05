from translatewise import create_app
from translatewise.translations.models import Translation
from translatewise.translations.repositories.translation_repo import TranslationRepo
from translatewise.translations.services.update_translations_service import UpdateTranslationsService
from translatewise.translations.services.post_translation_service import PostTranslationService
from translatewise.translations.unbabel_api import UnbabelApi
from rq import get_current_job


app = create_app()
app.app_context().push()

unbabel_api = UnbabelApi()
repo = TranslationRepo()


def update_translations_status():
    job = get_current_job()
    print(f"Update Translations Job running with id: {job.get_id()}")
    try:
        service = UpdateTranslationsService(api=unbabel_api, repository=repo)
        translations = service.update_translations()
        print(f"Job success with ID: {job.get_id()}")
        print("result:", translations)
    except Exception as e:
        print(f"Job failed with ID: {job.get_id()}")
        print("Exception:", e)
    print("")
    return


def post_translation(translation: Translation):
    job = get_current_job()
    print(f"Post Translation Job running with id: {job.get_id()}")
    try:
        result = PostTranslationService(api=unbabel_api).post_translation(translation)
        print(f"Job success with ID: {job.get_id()}")
        print("result:", result)
    except Exception as e:
        print(f"Job failed with ID: {job.get_id()}")
        print("Exception:", e)
    print("")
    return
