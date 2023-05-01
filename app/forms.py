# Esse arquivo tem o objetivo de reunir Classes Python que representarão webforms

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FloatField,TextAreaField, IntegerField, SelectField
from wtforms.validators import DataRequired, ValidationError, EqualTo
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired()])
    password = PasswordField('Senha',validators=[DataRequired()])
    remember_me = BooleanField('Lembrar de mim')
    submit = SubmitField('sign')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    password2= PasswordField("Repetir senha", validators=[DataRequired(), EqualTo('password')])
    remember_me = BooleanField('Lembrar de mim')
    submit = SubmitField('Register')


    #******************************************referencia para modificação futura
    # def validate_username(self, username):
    #     user = User.query.filter_by(username=username.data).first()
    #     if user is not None:
    #         raise ValidationError('Please use a different username.')

    # def validate_email(self, email):
    #     user = User.query.filter_by(email=email.data).first()
    #     if user is not None:
    #         raise ValidationError('Please use a different email address.')

class ItemForm(FlaskForm):
    descricao_item = TextAreaField('Descrição', validators=[DataRequired()],render_kw={"rows":"1","placeholder":"Ex. Colchão solteiro D33 88x188cm"})
    quantidade = FloatField('Quantidade', validators=[DataRequired()])
    valor_unitario = FloatField('Preço aprox. (unidade)', validators=[DataRequired()])
    observacao = TextAreaField('Observação', validators=[DataRequired()],render_kw={"rows":"1"})
    submit = SubmitField('Add')

class PedidoForm(FlaskForm):
    descricao_pedido = StringField('Descrição', validators=[DataRequired()], render_kw={"placeholder":"Ex. Material de conforto para o dormitório da 2ªCIA"})
    tipo = SelectField('Tipo de pedido',validators=[DataRequired()],choices=['MATERIAL','SERVIÇO'])
    setor = StringField('Setor/Incubência', validators=[DataRequired()], render_kw={"placeholder": "Ex. 2ªCiaFuzNav"})
    solicitante = StringField('Solicitante', validators=[DataRequired()],render_kw={"placeholder": "Ex. 3ºSG-FN-QQ INFANTSON"})
    justificativa = TextAreaField('Justificativa', validators=[DataRequired()], render_kw={"placeholder": "Texto sucinto explicando o \"por que\" do pedido", 'rows':'6'})
    prioridade = SelectField('Prioridade', validators=[DataRequired()],choices=['MELHORIA','CONFORTO','EMERGÊNCIAL','OPORTUNIDADE'])
    submit = SubmitField('Enviar')
