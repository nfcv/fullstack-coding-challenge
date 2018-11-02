from flask import Blueprint, render_template, redirect, url_for, request
from translatewise.translations.forms import TranslationForm
from translatewise.translations.interactors.factory import TranslationInteractorFactory


translations = Blueprint('translations', __name__)


@translations.route("/", methods=['GET', 'POST'])
def home():
    interactor = TranslationInteractorFactory.create()

    form = TranslationForm(request.form)
    if request.method == "POST":
        interactor.request_translation(form=form)
        return redirect(url_for("translations.home"))

    translations = interactor.get_translations()
    return render_template("index.html", translations=translations, form=form)
