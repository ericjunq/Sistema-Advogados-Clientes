from main import app
from flask import render_template

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/adv-cadastro")
def adv_cadastro():
    return render_template("adv-login.html")

@app.route("/cli-cadastro")
def cli_cadastro():
    return render_template("cli-login.html")
