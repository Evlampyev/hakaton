from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, RadioField
from wtforms.validators import DataRequired

"""Разобраться с полями"""
class AddProposalForm(FlaskForm):
    full_name = StringField('Введите ФИО', validators=[DataRequired(message="Поле 'адрес' не может быть пустым")])
    job = StringField('Введите вашу должность', validators=[DataRequired(message="Поле 'адрес' не может быть пустым")])
    place_of_work = StringField('Введите место работы', validators=[DataRequired(message="Поле 'адрес' не может быть пустым")])
    topic = StringField('Введите тему работы', validators=[DataRequired(message="Поле 'адрес' не может быть пустым")])
    header = StringField('Введите тему работы', validators=[DataRequired(message="Поле 'адрес' не может быть пустым")])
    annotation = StringField('Введите аннотацию по конкурсной работе', validators=[DataRequired(message="Поле 'адрес' не может быть пустым")])
    type = RadioField('Выберите тип заявки', choices=[('text','Печатное издание'),('video','Видеоматериал')])
    file = StringField('Введите ссылку на файл в облачном хранилище', validators=[DataRequired(message="Поле 'адрес' не может быть пустым")])
    submit = SubmitField('Добавить сообщение')
