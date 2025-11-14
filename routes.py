from main import app
from flask import render_template, request, redirect, url_for, flash, session
from models.advogado import Advogado
from models.cliente import Cliente

@app.route("/")
def homepage():
    return render_template("homepage.html")

# Login
@app.route("/adv-login", methods=['GET','POST'])
def adv_login():

    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')

        advogado = Advogado.buscar_por_email(email)

        if advogado and advogado.verifacar_senha(senha):

            session['advogado_id'] = advogado.id
            session['advogado_nome'] = advogado.nome
            session['user_type'] = 'advogado'
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('homepage')) 
        else:
            flash('Email ou senha incorretos!', 'error')
    return render_template("adv-login.html")


@app.route("/cli-login", methods=['GET', 'POST'])
def cli_login():

    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')

        cliente = Cliente.buscar_por_email(email)

        if cliente and cliente.verificar_senha(senha):
            
            session['advogado_id'] = cliente.id
            session['advogado_nome'] = cliente.nome
            session['user_type'] = 'advogado'
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('homepage')) 
        else:
            flash('Email ou senha incorretos!', 'error')
            
    return render_template("cli-login.html")

# Cadastro
@app.route("/adv-cadastro", methods=['GET', 'POST'])
def adv_cadastro():
    if request.method == 'POST':

        nome = request.form.get == ('nome')
        email = request.form.get == ('email')
        senha = request.form.get == ('senha')
        username = request.form.get == ('username')
        cpf = request.form.get ==('cpf')
        telefone = request.form.get == ('telefone')
        oab = request.form.get == ('oab')

        advogado = Advogado.cadastrar_advogado_web(
            nome, email, senha, username, cpf, telefone, oab
        )

        if advogado:
            flash('Cadastro realizado com sucesso! Faça login.', 'success')
            return redirect(url_for('adv_login'))
        else:
            flash('Erro ao cadastrar. Email, CPF, Username ou OAB já cadastrados.', 'error')
    
    return render_template("adv-cadastro.html")

@app.route("/cli-cadastro", methods=('GET', 'POST'))
def cli_cadastro():

    if request.method == 'POST':
         
          nome = request.form.get == ('nome')
          email = request.form.get == ('email')
          senha = request.form.get == ('senha')
          username = request.form.get == ('username')
          cpf = request.form.get == ('cpf')
          telefone = request.form.get == ('telefone')

          cliente = Cliente.cadastrar_cliente_web(
              nome, email, senha, username, cpf, telefone
          )

          if cliente:
              flash('Cadastro realizado com sucesso! Faça login.', 'success')
              return redirect(url_for('cli_login'))
          else:
              flash('Erro ao cadastrar. Email, CPF ou Username já cadastrados.', 'error')
              

    return render_template("cli-cadastro.html")
