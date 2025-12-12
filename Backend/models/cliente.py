from Backend.database.banco import db
from werkzeug.security import generate_password_hash, check_password_hash


class Cliente:
    def __init__(
        self, id=None, nome=None, email=None, senha=None,
        username=None, cpf=None, telefone=None,
        foto_perfil=None, bio=None, data_criacao=None,
        status=1, tipo_conta="cliente"
    ):

        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.username = username
        self.cpf = cpf
        self.telefone = telefone
        self.foto_perfil = foto_perfil
        self.bio = bio
        self.data_criacao = data_criacao or datetime.now()
        self.status = status
        self.tipo_conta = tipo_conta

    @classmethod
    def from_dict(cls, data):
        return cls(
            nome=data.get("nome"),
            email=data.get("email"),
            senha=data.get("senha"),
            username=data.get("username"),
            cpf=data.get("cpf"),
            telefone=data.get("telefone"),
            foto_perfil=data.get("foto_perfil"),
            bio=data.get("bio"),
            data_criacao=data.get("data_criacao"),
            status=data.get("status", 1),
            tipo_conta="cliente"
        )

    @classmethod
    def from_row(cls, row):
        return cls(
            id=row["id"],
            nome=row["nome"],
            email=row["email"],
            senha=row["senha"],
            username=row["username"],
            cpf=row["cpf"],
            telefone=row["telefone"],
            foto_perfil=row["foto_perfil"],
            bio=row["bio"],
            data_criacao=row["data_criacao"],
            status=row["status"],
            tipo_conta="cliente"
        )

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "username": self.username,
            "cpf": self.cpf,
            "telefone": self.telefone,
            "foto_perfil": self.foto_perfil,
            "bio": self.bio,
            "data_criacao": self.data_criacao,
            "tipo_conta": self.tipo_conta,
            "status": self.status
        }
