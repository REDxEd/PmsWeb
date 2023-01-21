# Esse arquivo tem o objetivo de reunir Classes Python que representarão webforms

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired()])
    password = PasswordField('Senha',validators=[DataRequired()])
    remember_me = BooleanField('Lembrar de mim')
    submit = SubmitField('sign')