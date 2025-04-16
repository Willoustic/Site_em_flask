from flask import Blueprint, render_template, request
from bancos.models.clientes import Cliente

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

@clientes.route('/cadastro', methods=["GET"])
def cadastro():
    return render_template('cadastro.html', accept=None)

@clientes.route('/cadastro', methods=["POST"])
def cadastrar():

    nomeus = request.form['nome']
    emailus = request.form['email']
    senhaus = request.form['senha']
    telefoneus = request.form['telefone']

    print(nomeus, emailus, senhaus, telefoneus)

    try:
        cliente = Cliente.create(nome=nomeus, email=emailus, senha=senhaus, telefone=telefoneus)
    except:
        return render_template('cadastro.html', accept=False)
    else:
        return render_template('cadastro.html', accept=True)
