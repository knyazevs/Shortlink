from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, DateField
from wtforms.validators import DataRequired
from wtforms_validators import ActiveUrl


class LinkForm(FlaskForm):
    url = StringField("Ссылка для сокращения",
                      validators=[DataRequired(), ActiveUrl(message="Введите действительный URL")])
    name = StringField("Название ссылки", render_kw={"placeholder": "Название ссылки"},
                       validators=[validators.optional()])
    author = StringField("Имя автора", render_kw={"placeholder": "Имя автора"},
                         validators=[validators.optional()])
    deadline = DateField("Время конца жизни ссылки",
                         render_kw={"placeholder": "Время конца жизни ссылки"},
                         validators=[validators.optional()])

    submit = SubmitField('Сократить')
