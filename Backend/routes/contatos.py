from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from Backend.models.advogado import Advogado
from Backend.models.cliente import Cliente


rota2_bp = Blueprint("contatos", __name__)

@rota2_bp.route("/contatos")
def contatos():
    return render_template("contatos.html")