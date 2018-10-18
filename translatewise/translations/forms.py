from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class TranslationForm(FlaskForm):
    text = StringField('Insert Text', validators=[DataRequired()])
    submit = SubmitField('Translate')
