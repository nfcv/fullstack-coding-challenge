from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from translatewise.utils.validators import Unique
from translatewise.translations.models import Translation


class TranslationForm(FlaskForm):
    text = StringField(
        'Insert Text', 
        validators=[
            DataRequired(), 
            Unique(Translation, Translation.text, message="Translation already added!")
        ]
    )
    submit = SubmitField('Translate')
