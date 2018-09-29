from flask import render_template, url_for, redirect, flash
from translatewise import app
from translatewise import db
from translatewise.forms import TranslationForm
from translatewise.models import Translation

translations = [
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

@app.route("/", methods=['GET', 'POST'])
def index():
    form = TranslationForm()
    if form.validate_on_submit():
        translation = Translation(form.text.data)
        db.session.add(translation)
        db.session.commit()
        flash(f'Translation added!', 'success')
        
    return render_template("index.html", translations=translations, form=form)