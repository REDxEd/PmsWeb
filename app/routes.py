from app import app
from flask import render_template,url_for


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('test.html')

@app.route('/acompanhar')
def acompanhar():
    return render_template('acompanhar.html')

@app.route('/editar')
def editar():
    return render_template('editar.html')