from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms_validators import ActiveUrl


class LinkForm(FlaskForm):
    url = StringField("Ссылка для сокращения",
                      validators=[DataRequired(), ActiveUrl(message="Введите действительный URL")])
    submit = SubmitField('Сократить')
