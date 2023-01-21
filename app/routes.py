from app import app
from flask import render_template,url_for,flash,redirect
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    # solução temporária para validar o login enquanto não existe bd
    if form.validate_on_submit():
        flash('Login request for user: {}, remember_me: {}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/acompanhar')
def acompanhar():
    return render_template('acompanhar.html')

@app.route('/editar')
def editar():
    return render_template('editar.html')