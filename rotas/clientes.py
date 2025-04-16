from flask import Blueprint, render_template, request, redirect, session, url_for
from bancos.models.clientes import Cliente
from time import sleep 

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

@clientes.route('/login', methods=["POST"])
def logar():
    erro = ''
    if request.method == 'POST':
        username = request.form['usuario'].capitalize()
        password = request.form['senha']
        try:
            usuario = Cliente.get(Cliente.usuario == username)
            if usuario.senha == password:
                session['usuario'] = username
                return redirect('/')
            else:
                erro = 'Senha incorreta.'
        except Cliente.DoesNotExist:
            erro = 'Usuário não encontrado.'
    return render_template('login.html', erro=erro)

@clientes.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect('/')

@clientes.route('/cadastro', methods=["GET"])
def cadastro():
    return render_template('cadastro.html', accept=None)

@clientes.route('/cadastro', methods=["POST"])
def cadastrar():

    nomeus = request.form['nome']
    emailus = request.form['email']
    usuarious = request.form['usuario'].capitalize()
    senhaus = request.form['senha']
    telefoneus = request.form['telefone']

    if Cliente.select().where(Cliente.usuario == usuarious).exists():
        texto = "Usuario já em uso"
    else:
        if Cliente.select().where(Cliente.email == emailus).exists():
            texto = "Email já cadastrado"
            if Cliente.select().where(Cliente.telefone == telefoneus).exists():
                texto = "Email e Telefone já cadastrados"
        else:
            if Cliente.select().where(Cliente.telefone == telefoneus).exists():
                texto = "Telefone já cadastrado"

    try:
        cliente = Cliente.create(nome=nomeus, usuario=usuarious, email=emailus, senha=senhaus, telefone=telefoneus)
    except ValueError as e:
        return render_template('cadastro.html', texto=str(e))
    except:
        return render_template('cadastro.html', texto=texto)
    else:
        return redirect(url_for('clientes.login'))

    
