from flask import Blueprint, render_template, redirect, url_for, flash, request
from translatewise.translations.forms import TranslationForm
from translatewise.translations.interactors.translation_interactor import TranslationInteractor


translations = Blueprint('translations', __name__)


@translations.route("/", methods=['GET', 'POST'])
def home():
    data = TranslationInteractor.get_all_translations()

    form = TranslationForm(request.form)
    if form.validate_on_submit():
        text = form.text.data
        TranslationInteractor.add_translation(text)
        flash(f'Translation added!', 'success')
        return redirect(url_for("translations.home"))

    return render_template("index.html", translations=data, form=form)
