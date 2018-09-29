from flask import Blueprint, render_template, flash
from translatewise import db
from translatewise.translations.forms import TranslationForm
from translatewise.translations.models import Translation

translations = Blueprint('translations', __name__)

data = [
    {
        'en_UK': 'Hello',
        'es_ES': 'Holla',
        'status': 'requested'
    },
    {
        'en_UK': 'How you doing?',
        'es_ES': 'Como estas?',
        'status': 'pending'
    },
    {
        'en_UK': 'How',
        'es_ES': 'Como',
        'status': 'translated'
    }
]


@translations.route("/", methods=['GET', 'POST'])
def index():
    form = TranslationForm()
    if form.validate_on_submit():
        translation = Translation(form.text.data)
        db.session.add(translation)
        db.session.commit()
        flash(f'Translation added!', 'success')
        
    return render_template("index.html", translations=data, form=form)