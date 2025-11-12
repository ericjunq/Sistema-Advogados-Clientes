from main import app
from flask import render_template

@app.route("/")
def homepage():
    return render_template("homepage.html")

# Login
@app.route("/adv-login", methods=['GET','POST'])
def adv_login():
    return render_template("adv-login.html")

@app.route("/cli-login", methods=['GET', 'POST'])
def cli_login():
    return render_template("cli-login.html")

# Cadastro
@app.route("/adv-cadastro")
def adv_cadastro():
    return render_template("adv-cadastro.html")

@app.route("/cli-cadastro")
def cli_cadastro():
    return render_template("cli-cadastro.html")
