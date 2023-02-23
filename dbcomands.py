# manipular bd direto (solução temporária)

from app import app, db
from app.models import *


app.app_context().push()
# u = User(username='Gomes', nip='11051957', super_user=1)
# db.session.add(u)
# db.session.commit()

pedidos = list(Pedido.query.filter(Pedido.solicitante!=None))




print(type(pedidos))
for p in pedidos:
    print(p.id, p.solicitante, p.setor)
