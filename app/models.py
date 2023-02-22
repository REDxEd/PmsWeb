# toda a estrutura do DATABASE deve ser implementado aqui
# sempre que alguma modificação for feita aqui, os comandos abaixo precisam ser realizados para atualizar o bd:
#*********************{[(   flask db migrate -m "{commit}"   )]}*********************
#*********************{[(          flask db upgrade          )]}*********************
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import db # $  flask db init
from flask_login import UserMixin
from app import login

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    super_user = db.Column(db.Boolean)
    username = db.Column(db.String(64), unique=True)
    nip = db.Column(db.String(8), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    Atualizacoes = db.relationship('AtualizacaoPedido', backref='user', lazy='dynamic')

    def set_password(self,password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,password)->bool:
        return check_password_hash(self.password_hash, password)

    def __repr__(self) -> str:
        return '<User {} {}>'.format(self.nip, self.username)
    

class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    validate = db.Column(db.Boolean, default=False)
    
    # fields editable by all users
    descricao_pedido = db.Column(db.String(400))
    tipo = db.Column(db.String(30))
    setor = db.Column(db.String(30))
    solicitante = db.Column(db.String(64))
    justificativa = db.Column(db.String(500))
    prioridade = db.Column(db.String(30))

    # fields editable by only logged users
    aprovado = db.Column(db.Boolean)
    estado = db.Column(db.String(60), default='Aguardando aprovação')

    # ForengKeys
    itens = db.relationship('Item', backref='pedido', lazy='dynamic')
    solemps = db.relationship('Solemp', backref='pedido', lazy='dynamic')
    Atualizacoes = db.relationship('AtualizacaoPedido', backref='pedido', lazy='dynamic')

    def __repr__(self) -> str:
        return '<Pedido {} {} {}>'.format(self.id, self.solicitacao, self.estado)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedido.id'))

    # fields editable by all users
    descricao_item = db.Column(db.String(200))
    quantidade = db.Column(db.Float)
    valor_unitario = db.Column(db.Float)
    observacao = db.Column(db.String(500))

    # fields editable by only logged users
    numero_pregao = db.Column(db.String)
    item_pregao = db.Column(db.Integer)







class Solemp(db.Model):
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedido.id'))
    numero_solemp = db.Column(db.Integer, index=True, primary_key=True)

class AtualizacaoPedido(db.Model):
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedido.id'),primary_key=True)
    user_nip = db.Column(db.String, db.ForeignKey('user.nip'),primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow,primary_key=True)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))