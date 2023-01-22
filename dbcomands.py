# manipular bd direto (solução temporária)

from app import app, db
from app.models import *


app.app_context().push()
# u = User(username='Gomes', nip='11051957', super_user=1)
# db.session.add(u)
# db.session.commit()

users = User.query.all()
for u in users:
    print (u.id, u.username, u.nip)