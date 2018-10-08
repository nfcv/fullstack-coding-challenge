from flask import Blueprint, render_template, redirect, url_for, flash
from translatewise import db
from translatewise.translations.forms import TranslationForm
from translatewise.translations.models import Translation
from translatewise.translations.interactors.translation_interactor import TranslationInteractor
from translatewise.translations.services.get_all_translations_service import GetAllTranslationsService


translations = Blueprint('translations', __name__)


@translations.route("/", methods=['GET', 'POST'])
def index():
    data = TranslationInteractor.get_all_translations()

    form = TranslationForm()
    if form.validate_on_submit():
        translation = Translation(form.text.data)
        db.session.add(translation)
        db.session.commit()
        flash(f'Translation added!', 'success')
        return redirect(url_for("translations.index"))

    return render_template("index.html", translations=data, form=form)
