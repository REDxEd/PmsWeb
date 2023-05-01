# manipular bd direto (solução temporária)

from app import app, db
from app.models import *


app.app_context().push()
# u = User(username='Gomes', nip='11051957', super_user=1)
# db.session.add(u)



pedidos = Pedido.query.all()
itens = Item.query.all()

for i in itens:
    db.session.delete(i)
    
for p in pedidos:
    db.session.delete(p)


db.session.commit()


