from flask import Blueprint, render_template, redirect, url_for, request
from translatewise.translations.forms import TranslationForm
from translatewise.translations.interactors.translation_interactor import TranslationInteractor


translations = Blueprint('translations', __name__)


@translations.route("/", methods=['GET', 'POST'])
def home():
    form = TranslationForm(request.form)
    if request.method == "POST":
        TranslationInteractor.submit(form=form)
        return redirect(url_for("translations.home"))

    translations = TranslationInteractor.translations()
    return render_template("index.html", translations=translations, form=form)
