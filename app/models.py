# toda a estrutura do DATABASE deve ser implementado aqui
# sempre que alguma modificação for feita aqui, os comandos abaixo precisam ser realizados para atualizar o bd:
#*********************{[(   flask db migrate -m "{commit}"   )]}*********************
#*********************{[(          flask db upgrade          )]}*********************
from datetime import datetime
from app import db
    #flask db init

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    super_user = db.Column(db.Integer)
    username = db.Column(db.String(64), unique=True)
    nip = db.Column(db.String(8), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self) -> str:
        return '<User {} {}>'.format(self.nip, self.username)

class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    solicitante = db.Column(db.String(64))
    setor = db.Column(db.String(30))
    descricao = db.Column(db.String(400))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    estado = db.Column(db.String(60), default='Aguardando aprovação')

    def __repr__(self) -> str:
        return '<Pedido {} {} {}>'.format(self.id, self.descricao, self.estado)
