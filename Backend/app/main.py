from flask import Flask
from Backend.routes.routes import rota1_bp
from Backend.routes.contatos import rota2_bp
from Backend.database.banco import db
import os

# Caminho absoluto até a pasta Frontend
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FRONTEND_DIR = os.path.join(BASE_DIR, "Frontend")

app = Flask(
    __name__,
    static_folder=os.path.join(FRONTEND_DIR, "static"),
    template_folder=os.path.join(FRONTEND_DIR, "templates")
)

# CONFIGURAÇÃO DO BANCO DE DADOS (exemplo com SQLite)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///meubanco.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Inicializar DB
db.init_app(app)

# Importar modelos depois de inicializar o app para EVITAR import circular
from Backend.models.cliente import Cliente

with app.app_context():
    db.create_all()

# Registrar blueprints
app.register_blueprint(rota1_bp)
app.register_blueprint(rota2_bp)

if __name__ == "__main__":
    app.run(debug=True)
