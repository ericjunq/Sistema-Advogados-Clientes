from flask import Flask
from Backend.routes.routes import rota1_bp
from Backend.routes.contatos import rota2_bp
from Backend.database import banco
import sys, os

# Caminho absoluto até a pasta Frontend
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FRONTEND_DIR = os.path.join(BASE_DIR, "Frontend")

app = Flask(
    __name__,
    static_folder=os.path.join(FRONTEND_DIR, "static"),
    template_folder=os.path.join(FRONTEND_DIR, "templates")
)

# Registrar blueprint SEM url_prefix
app.register_blueprint(rota1_bp)
app.register_blueprint(rota2_bp)

if __name__ == "__main__":
    app.run(debug=True)