from translatewise import create_app
from translatewise.translations.models import Translation
from translatewise.translations.repositories.translation_repo import TranslationRepo
from translatewise.translations.services.translation_jobs_service import TranslationJobsService
from translatewise.translations.unbabel_api import UnbabelApi
from rq import get_current_job


app = create_app()
app.app_context().push()

unbabel_api = UnbabelApi()
repo = TranslationRepo()
jobs = TranslationJobsService(api=unbabel_api, repository=repo)


def update_translations_status():
    job = get_current_job()
    print(f"Update Translations Job running with id: {job.get_id()}")
    try:
        translations = jobs.update_translations()
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
        result = jobs.post_translation(translation)
        print(f"Job success with ID: {job.get_id()}")
        print("result:", result)
    except Exception as e:
        print(f"Job failed with ID: {job.get_id()}")
        print("Exception:", e)
    print("")
    return
