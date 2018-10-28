from translatewise import create_app
from translatewise.translations.models import Translation
from translatewise.translations.services.unbabel_api import UnbabelApi

app = create_app()
app.app_context().push()


def post_translation(translation: Translation):
    unbabel_api = UnbabelApi()
    result = unbabel_api.post_translation(
      translation.text,
      translation.id,
      translation.text_lang_code,
      translation.translated_lang_code
    )
    uid = result["uid"]
    print(f"UID: {uid}")
