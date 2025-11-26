from Backend.database.banco import db
from werkzeug.security import generate_password_hash, check_password_hash

class Advogado(db.Model):
    __tablename__ = "advogados"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)
    username = db.Column(db.String(120), unique=True, nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    oab = db.Column(db.String(20), unique=True, nullable=False)

    def verificar_senha(self, senha_digitada):
        return check_password_hash(self.senha, senha_digitada)

    @staticmethod
    def buscar_por_email(email):
        return Advogado.query.filter_by(email=email).first()
