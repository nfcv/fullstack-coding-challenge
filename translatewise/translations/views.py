from flask import Blueprint, render_template, redirect, url_for, request, current_app
from translatewise.translations.forms import TranslationForm
from translatewise.translations.handlers.translation_handler import TranslationHandler
from translatewise.translations.repositories.translation_repo import TranslationRepo
from translatewise.translations.presenters.translation_presenter import TranslationPresenter

translations = Blueprint('translations', __name__)


@translations.route("/", methods=['GET', 'POST'])
def home():
    handler = TranslationHandler(repository=TranslationRepo(), queue=current_app.task_queue)

    form = TranslationForm(request.form)
    if request.method == "POST":
        handler.request_translation(form=form)
        return redirect(url_for("translations.home"))

    translations = handler.get_translations_ordered_by_word_count()
    translation_presenters = list(map(lambda t: TranslationPresenter(t), translations))
    return render_template("index.html", translations=translation_presenters, form=form)
