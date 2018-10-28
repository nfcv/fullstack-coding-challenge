from translatewise import create_app
from translatewise.translations.models import Translation
from translatewise.translations.services.unbabel_api import UnbabelApi
from rq import get_current_job

app = create_app()
app.app_context().push()


def post_translation(translation: Translation):
    try:
        unbabel_api = UnbabelApi()
        result = unbabel_api.post_translation(
          translation.text,
          translation.id,
          translation.text_lang_code,
          translation.translated_lang_code
        )
        uid = result["uid"]
        print(f"UID: {uid}")
    except Exception as e:
        job = get_current_job()
        print(f"Job failed with ID: {job.get_id()}")
