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