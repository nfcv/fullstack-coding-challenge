from flask import Blueprint, render_template, redirect, url_for, request, current_app
from translatewise.translations.forms import TranslationForm
from translatewise.translations.interactors.translation_interactor import TranslationInteractor
from translatewise.translations.services.translation_service import TranslationService
from translatewise.translations.services.translation_queue_service import TranslationQueueService
from translatewise.translations.repositories.translation_repo import TranslationRepo


translations = Blueprint('translations', __name__)


@translations.route("/", methods=['GET', 'POST'])
def home():
    repo = TranslationRepo()
    queue = current_app.task_queue
    queue_service = TranslationQueueService(queue=queue)
    translation_service = TranslationService(repository=repo)

    interactor = TranslationInteractor(
        translation_service=translation_service,
        queue_service=queue_service
    )

    form = TranslationForm(request.form)
    if request.method == "POST":
        interactor.request_translation(form=form)
        return redirect(url_for("translations.home"))

    translations = interactor.get_translations()
    return render_template("index.html", translations=translations, form=form)
