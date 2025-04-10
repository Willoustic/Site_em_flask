from flask import Blueprint, render_template

clientes = Blueprint('clientes', __name__)

@clientes.route('/')
def inicial():
    return render_template('inicial.html')

@clientes.route('/contato')
def contato():
    return render_template('contato.html')

@clientes.route('/manuntençao')
def manun():
    return render_template('manun.html')

@clientes.route('/login')
def login():
    return render_template('login.html')

@clientes.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')
