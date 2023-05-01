from app import app, db
from flask import render_template,url_for,flash,redirect, request
from app.forms import LoginForm, RegistrationForm, PedidoForm, ItemForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Pedido, Item
from werkzeug.urls import url_parse # redirecione para a página "next"


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()

    if form.validate_on_submit():
        user=User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Usuário ou senha inválidos')
            return redirect(url_for('login'))
        
        login_user(user, remember=form.remember_me.data)
        next_page= request.args.get('next')
        
        if not next_page or url_parse(next_page).netloc !='':
            next_page=url_for('index')
        return redirect(next_page)

    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/solicitar', methods=['GET', 'POST',])
def solicitar():

    
    form_pedido=PedidoForm()
    form_item= ItemForm()
    
    pedido = Pedido()
    
    if request.method=='GET':

        db.session.add(pedido)
        db.session.commit()

        pedido_id = pedido.id


    if request.method=='POST':
        
        pedido = Pedido.query.get(int(request.args.get('pedido_id')))
        pedido.descricao_pedido = request.form.get('descricao_pedido')
        pedido.tipo = request.form.get('tipo')
        pedido.setor = request.form.get('setor')
        pedido.solicitante = request.form.get('solicitante')
        pedido.justificativa = request.form.get('justificativa')
        pedido.prioridade = request.form.get('prioridade')
        pedido.validate = True

        db.session.add(pedido)
        db.session.commit()


        return redirect(url_for('index'))
    
    return render_template('solicitar.html',form_pedido=form_pedido,form_item=form_item, pedido_id=pedido_id)



@app.route('/add_item', methods=['POST'])
def add_item():
    print('IN ADD_ITEM')
    if request.method=='POST':
        
        item = Item(
            pedido_id = int(request.args.get('pedido_id')),
            descricao_item =request.form.get('descricao_item'),
            quantidade = float(request.form.get('quantidade')),
            valor_unitario = float(str(request.form.get('valor_unitario').replace(',','.'))),
            observacao = request.form.get('observacao'))
        
        db.session.add(item)
        db.session.commit()
        print('pedido_id = {}'.format(item.pedido_id))
        print('descricao_item = {}'.format(item.descricao_item))
        print('quantidade = {}'.format(item.quantidade))
        print('valor_unitario = {}'.format(item.valor_unitario))
        return('',204)


@app.route('/acompanhar')
def acompanhar():
    
    
    pedidos = list(Pedido.query.filter(Pedido.solicitante!=None))

    return render_template('acompanhar.html',pedidos=pedidos)

@app.route('/pedido')
def pedido():
    
    id = request.args.get('id')
    pedido = Pedido.query.filter_by(id=id).first()
    
    itens = Item.query.filter_by(pedido_id=id).all()
    
    print(type(itens))
    for i in itens:
        print(i.id)
        print(i.descricao_item)
        print(i)
        print(i)
        print(i)
        print(i)
    return render_template('pedido.html',pedido=pedido, itens=itens)

#===========================================================================================================




@app.route('/test', methods=['GET', 'POST'])
def test():

    return render_template('test.html')


@app.route('/editar')
@login_required
def editar():
    return render_template('editar.html')

@app.route('/register')
@login_required
def register():

    form=RegistrationForm()
    return render_template('register.html', form =form)