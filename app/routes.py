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
    db.session.add(pedido)
    db.session.commit()

    pedido_id = pedido.id

    if request.method=='POST':
        
        print ('validate_ON!')
        pedido=Pedido(
            descricao_pedido = request.form.get('descricao_pedido'),
            tipo = request.form.get('tipo'),
            setor = request.form.get('setor'),
            solicitante = request.form.get('solicitante'),
            justificativa = request.form.get('justificativa'),
            prioridade = request.form.get('prioridade'),
            validate = True
        )
        db.session.add(pedido)
        db.session.commit()
        return redirect(url_for('index'))



    return render_template('solicitar.html',form_pedido=form_pedido,form_item=form_item, pedido_id=pedido_id)



@app.route('/add_item', methods=['POST', 'GET'])
def add_item():
    print('IN ADD_ITEM')
    if request.method=='POST':
        item = Item(
            pedido_id = request.args.get('pedido_id'),
            descricao_item =request.form.get('descricao_item'),
            quantidade = float(request.form.get('quantidade')),
            valor_unitario = float(str(request.form.get('valor_unitario').replace(',','.'))),
        )
        db.session.add(item)

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

    return render_template('pedido.html')

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